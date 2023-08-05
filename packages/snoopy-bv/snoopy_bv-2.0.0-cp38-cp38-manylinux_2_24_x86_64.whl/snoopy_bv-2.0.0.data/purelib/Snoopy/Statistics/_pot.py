import numpy as np
from scipy import stats
from scipy.interpolate import InterpolatedUnivariateSpline
from matplotlib import pyplot as plt
from Snoopy import logger
from Snoopy import Statistics as st


def rolling_declustering( se , window=None, window_int=None ) : 
    """Return declustered events
   
    Parameters
    ----------
    se : pd.Series
        Time series (time is index)
    window : float, optional
        window used to decluster the data. The default is None.
    window_int : int, optional
        window used to decluster the data, in number of time step. The default is None.

    Returns
    -------
    pd.Series
        The declustered sample
    """
  
    if window_int is not None : 
        _se = se.reset_index(drop=True)
        se_tmp = _se.rolling( window = window_int, min_periods=1, center=True, axis=0, closed = 'neither' ).max()   
        se_tmp = se_tmp.loc[ se_tmp == _se ]
        se_tmp.loc[ np.concatenate( [[True], np.diff(se_tmp.index) > window_int / 2 ]) ]
        se_tmp.index = se.index[se_tmp.index.values]
    else :
        se_tmp = se.rolling( window = window, min_periods=1, center=True, axis=0, closed = 'neither' ).max()   
        se_tmp = se_tmp.loc[ se_tmp == se ]
        se_tmp = se_tmp.loc[ np.concatenate( [[True], np.diff(se_tmp.index) > window / 2] ) ]
    return se_tmp



class POT():

    def __init__(self, sample, duration, threshold, variant = (0.,0.) ):
        """Peak over Threshold method to calcualte return values. 
        
        Uses only empirical quantiles, for generalized pareto fit, see POT_GPD class. 

        Parameters
        ----------
        sample : np.ndarray
            Sample of independant observation
        duration : float
            Duration corresponding to the sample
        threshold : float
            Threshold
        """
        
        self.sample = sample
        
        self.duration = duration
        
        self.threshold = threshold
        
        self.extremes = np.sort( sample[sample >= threshold] )
        self.exceedances = self.extremes - self.threshold
        
        self.f = len(self.extremes) / self.duration
        
        #Which variant for the empirical quantile calculation
        self._variant = variant
        
        #Interpolator, not always needed ==> lazy evaluated
        self._x_to_rp_empirical = None
        self._rp_to_x_empirical = None
        
        
    def x_to_rp_empirical(self, x):
        """Return period from return value, using interpolation between data.

        Parameters
        ----------
        x : float
            Return value

        Returns
        -------
        float
            Return period
        """
        if self._x_to_rp_empirical is None : 
            self._build_interp_x_to_rp()
        return self._x_to_rp_empirical(x)
    
    def rp_to_x_empirical(self, x):
        """Return value from return period

        Parameters
        ----------
        rp : float
            return period

        Returns
        -------
        float
            return value
        """
        if self._rp_to_x_empirical is None : 
            self._build_interp_rp_to_x()
        return self._rp_to_x_empirical(x)    
            

    def _build_interp_rp_to_x(self):
        # Build interpolator
        logger.debug("Build return level interpolator")
        self._rp_to_x_empirical = InterpolatedUnivariateSpline( self.empirical_rp() , self.extremes, ext = "raise", k = 1 )

    def _build_interp_x_to_rp(self):
        # Build interpolator
        logger.debug("Build return level interpolator")
        self._x_to_rp = InterpolatedUnivariateSpline( self.extremes , self.empirical_rp(), ext = "raise", k = 1)


    @classmethod
    def FromTimeSeries( cls, se, duration, threshold = None, threshold_q = None, window = None , window_int = None, **kwargs ):
        """Create POT analysis using time series as input
        
        Parameters
        ----------
        se : pd.Series
            The time signal.
        duration : float
            Duration associated to the time-series.
        threshold : float
            Threshold.
        treshold_q : float
                Threshold.
        window : float, optional
            window used to decluster the data. The default is None.
        window_int : int, optional
            window used to decluster the data, in number of time step. The default is None.
        **kwargs : TYPE
            DESCRIPTION.

        Returns
        -------
        The POT analysis class
        """
        sample = rolling_declustering( se, window = window, window_int = window_int )
        
        if threshold_q is not None :
            threshold = np.quantile( sample, threshold_q, method = "weibull") # Weibull corresponds to "i / (n+1)" method
        return cls( sample.values, duration, threshold = threshold, **kwargs )
    
        
    def empirical_rp( self  ):
        """Return empirlcal return period of events above threshold (sorted).

        Parameters
        ----------
        variant : (float,float) or str, optional
            DESCRIPTION. The default is (0.0, 0.0), which corresponds to i/(n+1)

        Returns
        -------
        np.ndarray
            Return period of events above threshold (sorted).
        """
        return 1 / ( self.f * st.probN( len(self.extremes), variant = self._variant ) )


    def plot_rp_data(self, ax = None, variant = (0.0 , 0.0), marker = "+", linestyle = ""):
        """
        

        Parameters
        ----------
        ax : TYPE, optional
            DESCRIPTION. The default is None.
        variant : TYPE, optional
            DESCRIPTION. The default is (0.0 , 0.0).
        marker : TYPE, optional
            DESCRIPTION. The default is "+".
        linestyle : TYPE, optional
            DESCRIPTION. The default is "".

        Returns
        -------
        ax : TYPE
            DESCRIPTION.

        """
        
        if ax is None :
            fig, ax = plt.subplots()

        ax.plot( self.empirical_rp(),  self.extremes, marker = marker , linestyle=linestyle)
        ax.set_xscale("log")
        return ax
        
                 


class POT_GPD( POT ):
    
    def __init__(self, sample, duration , threshold , fit_kwargs = {} ):
        """Peak over threshold, extremes are fitted with Generalize Pareto Distribution
        
        Parameters
        ----------
        sample : np.ndarray
            Sample of independant observation
        duration : float
            Duration corresponding to the sample
        threshold : float
            Threshold
        fit_kwargs : any
            Argument pass to scipy.rv_continous.fit method
        """
        POT.__init__(self , sample, duration , threshold)
        self._gpd = None
        self.fit_kwargs = {}

    
    def _fit(self):
        self._gpd = stats.genpareto(*stats.genpareto.fit( self.exceedances, floc=0 ))
        
        
    @property
    def gpd(self):
        if self._gpd is None:
            self._fit( **self.fit_kwargs )
        return self._gpd

    
    def x_to_rp( self, x ) :
        """Calculate return period from return value

        Parameters
        ----------
        x : float or np.ndarray
            Return value

        Returns
        -------
        float or np.ndarray
            return period
        """
        return  1 /  (self.f * ( self.gpd.sf( x - self.threshold  ))  )
        
    def rp_to_x(self , rp):
        """Provide return value at RP
        
        Parameters
        ----------
        rp : float or array
            Return period.

        Returns
        -------
        float or np.ndarray
             Return value
        """
        return self.threshold + self.gpd.ppf( 1. - ( 1 / (rp * self.f ) ))
    
    
    def plot_rp_fit(self, rp_range=None, ax=None):
        """Plot return value against return period.
        
        Parameters
        ----------
        rp_range : np.ndarray or None, optional
            Range of RP to plot. The default is None.
        ax : plt.Axis, optional
            The figure. The default is None.

        Returns
        -------
        plt.Axis, optional
            The figure
        """
        
        if ax is None :
            fig, ax= plt.subplots()
            
        if rp_range is None : 
            _x = self.empirical_rp()
            rp_range = np.logspace(  np.log10( np.min( _x ) ) , np.log10(np.max( _x ))*1.5   , 200 )
        
        ax.plot( rp_range , self.rp_to_x( rp_range ) )
        ax.set_xscale("log")
        ax.set( xlabel = "Return period" )
        return ax


if __name__ == "__main__" : 

    import pandas as pd
    from Snoopy.TimeDomain import TEST_DIR
    
    data = pd.read_csv( f"{TEST_DIR}/hs.csv", index_col = 0 , parse_dates = True ).hs
    
    duration = len(data) / 2922
    
    data_decluster = rolling_declustering( data, window = pd.offsets.Day(2) )
    
    data_decluster2 = rolling_declustering( data, window_int = 16 )
    
    pot = POT_GPD.FromTimeSeries( se = data, duration=duration, threshold = np.quantile(data_decluster, 0.9), window_int=16 )
      
    fig, ax = plt.subplots()
    pot.plot_rp_data(ax=ax)
    pot.plot_rp_fit(ax=ax)
    
    pot.rp_to_x_empirical( 10 )
    pot.rp_to_x( 10 )

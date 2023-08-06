
import pandas as pd

def Describe(data):

    """
    Add more descriptive to default describe() of Pandas:
    - mad: mean absolute deviation
    - variance: variance
    - sem: standard error of the mean
    - sum: sum
    - skewness: skewness
    - kurtosis: kurtosis

    Constructor method.
        Parameters
        ----------
        data: data in NumPy array or Panadas DataFrame
    
        Return
        ---------- 
        stats: the descriptive statistics
    """
    
    data = pd.DataFrame(data)
    describe = data.describe()
    #median = data.median(skipna=True,numeric_only=True,)# it is 50%
    mad = data.mad(skipna=True) # mean absolute deviation
    var = data.var(skipna=True,numeric_only=True)
    sem = data.sem(numeric_only=True, skipna=True) #standard error of the mean
    sum = data.sum(numeric_only=True, skipna=True)
    skew = data.skew(skipna=True,numeric_only=True)
    kurt = data.kurt(skipna=True,numeric_only=True)
    
    # display in pandas dataframe and transpose it
    #median = pd.DataFrame({'median':median}).T
    mad_df = pd.DataFrame({'mad':mad}).T
    var_df = pd.DataFrame({'variance':var}).T
    sem_df = pd.DataFrame({'sem':sem}).T
    sum_df = pd.DataFrame({'sum':sum}).T
    skew_df = pd.DataFrame({'skewness':skew}).T
    kurt_df = pd.DataFrame({'kurtosis':kurt}).T
    
    stats = pd.concat([describe[0:2],mad_df,var_df,sem_df,describe[2:],sum_df,skew_df,kurt_df])
                             
    return stats
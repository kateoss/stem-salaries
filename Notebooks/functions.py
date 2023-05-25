
def replace_with_other(df, col_name, threshold):
    
    """
    The function replaces values in selected columns based on the value counts, and a defined threshold.
    Args:
       df(pandas.DataFrame): the df containing a selected column
       col_name(sts): the name of a selected column
       threshold(int): a number selected under which the values in col_name will change to "other"
    Returns:
       pandas.DataFrame: the updated df with replaced values
    """
    
    values_count = df[col_name].value_counts()
    low_values_count = values_count[values_count < threshold].index
    df.loc[df[col_name].isin(low_values_count), col_name] = "other"
    return df
def train_models(models, X_train, y_train):
    
    """
    This function trains a list of provided models.
    Args:
       models: a list of models with default or selected parameters
       X_train: train set with independent variables
       y_train: predicted variable from the train set
    Returns:
       trained models
    """
    for model in models:
        model.fit(X_train, y_train)
    return models



def error_metrics_calculations(y_true, y_pred):

    """
    This function given a model predicted and real values calculates error metrics.
    Args:
       y_true: actual y values in a test set
       y_pred: predicted by model y values
    Returns:
       pandas.DataFrame: the dataframe with error metrics name and values
    """
        
    error_metrics = {"MAE": mean_absolute_error(y_true, y_pred), 'MSE': mean_squared_error(y_true, y_pred), 
                     'RMSE': np.sqrt(mean_squared_error(y_true, y_pred)), 'MAPE': np.mean(np.abs((y_true - y_pred) / y_true)) * 100,
                     'R2': r2_score(y_true, y_pred)}
    df = pd.DataFrame(list(error_metrics.items()), columns=['Error_metric', 'Value'])
    return df

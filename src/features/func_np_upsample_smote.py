def func_np_upsample_smote(X_train, y_train):
    """function to upsample imbalanced training data
    Keyword arguments: X_train, y_train (output from train_test_split); Return: X_resampled, y_resampled
    """
    from imblearn.over_sampling import SMOTE
    X_resampled, y_resampled = SMOTE().fit_resample(X_train, y_train)
    print(X_train.shape)
    print(y_train.shape)
    print(X_resampled.shape)
    print(y_resampled.shape)
    return X_resampled, y_resampled

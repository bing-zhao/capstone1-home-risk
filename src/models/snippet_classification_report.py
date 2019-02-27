from sklearn.metrics import classification_report

print('training set')
cr = classification_report(y_train, y_pred_train, output_dict=True)
cr_df = pd.DataFrame(cr)
display(cr_df)

print('test set')
cr = classification_report(y_test, y_pred_test, output_dict=True)
cr_df = pd.DataFrame(cr)
display(cr_df)

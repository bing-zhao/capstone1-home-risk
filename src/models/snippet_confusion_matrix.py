from sklearn.metrics import confusion_matrix
unique_label = np.unique(y_test)
cm = confusion_matrix(y_train, y_pred_train, labels=unique_label)
print('training set')
print(pd.DataFrame(cm,
                   index=['true:{:}'.format(x) for x in unique_label],
                   columns=['pred:{:}'.format(x) for x in unique_label]))

cm = confusion_matrix(y_test, y_pred_test, labels=unique_label)
print('test set')
print(pd.DataFrame(cm,
                   index=['true:{:}'.format(x) for x in unique_label],
                   columns=['pred:{:}'.format(x) for x in unique_label]))

%%time
from tpot import TPOTClassifier
tpot = TPOTClassifier(generations=5, population_size=20, cv=5, scoring='roc_auc', random_state=42, verbosity=2)
tpot.fit(X_train, y_train)
print(tpot.score(X_test, y_test))
tpot.export('tpot_pipeline.py')

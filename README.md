# Classification-Practice
A place for me to apply classification modelling techniques to data.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/RJBraith/Classification-Practice/HEAD)

---
## Titanic Dataset
An exercise on an already well documented dataset so I can measure my process compared to others and see where my bad habits / areas of strength lie.

The data I downloaded came fragmented into 3 csv files, so I created a merge script and used the merged csv as my dataframe in the notebook.

There were around 200 missing age values in the dataframe so I scaled my data then used KNN imputation to approximate them, unscaling afterwards.

I tested 5 classification methods each with their own gridsearch to try and find the most appropriate algorithm to classify passenger survival.
    1. Logistic Regression
    2. Support Vector Machine Classifier
    3. K-Nearest-Neighbor Classifier
    4. Random Forest Classifier
    5. Gradient Boosting Classifier

Each algorithm was placed in it's own pipeline, scaled and fit accordingly and then was scored using balanced accuracy. A grid search was then performed to try and further improve upon the default settings of the algorithms

The results show that all of the models are close but if I had to choose a top 3, KNN would be my number 1, followed by logit and random forest.
This is because these three models achieve high balanced accuracy in their individual fittings as well as in the cross validation test. They also achieve low misclassification, the lowest I achieved was 60 passengers misclassified.
That being said, all of the models perform quite well it is just these three are the better performing of the group.

If I were to do this again, I would perform the train test split earlier, as I suspect I have some data leakage due to the imputation of Age.
missing ages were imputed using the whole dataset which means that imputed ages in the test set were influenced by the data in the test set.

---
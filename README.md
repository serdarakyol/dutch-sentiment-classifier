# Dutch sentiment classification
This repository provides classification model on FastAPI. Trained BERT, Random Forest, KNeighborsClassifier, Complement Naive Bayes classifier, Gaussian Naive Bayes, Logistic Regression and SVM. Outputs under train_notebooks folder.

# Results
Model | Accuracy | Precision | recall | f1-score | bias | variance
--- | --- | --- | --- | --- | --- | ---
BERT | 0.79 | 0.80 | 0.79 | 0.79
SVM | 0.67 | 0.67 | 0.67 | 0.67 | 0.26 | 0.15
Logistic Regression | 0.68 | 0.68 | 0.68 | 0.67 | 0.27 | 0.13
Gaussian Naive Bayes | 0.59 | 0.61 | 0.59 | 0.59 | 0.39 | 0.18
Complement Naive Bayes | 0.65 | 0.66 | 0.65 | 0.66 | 0.31 | 0.08
KNeighborsClassifier | 0.53 | 0.56 | 0.53 | 0.52 | 0.34 | 0.23
Random Forest | 0.66 | 0.66 | 0.66 | 0.65 | 0.24 | 0.15

# Model Selection
After evaluated all models, Complement Naive Bayes classifier have been choosen. The reason is model is light. Has lower bias and variance. Accuracy, precision, recall and f1-score lower than BERT but cost much cheaper than BERT

# USAGE
First go to dutch-sentiment-classifier directory and create an image with below code
```
$ sudo docker image build -t sentiment-classifier .
```

Then run docker
```
$ sudo docker run sentiment-classifier -pd 1234:1234
```
Go to http://0.0.0.0:1234/docs and click to Authorize and write "serdarakyol55@outlook.com" in value text box. Now everything is ready. Let's start to try Complement Naive Bayes Classifier with FastAPI!

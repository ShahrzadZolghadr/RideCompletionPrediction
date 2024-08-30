# RideCompletionPrediction
The task is to predict the ride canselation via provided features. The dataset is so imbalanced and this is the most important challenge of the problem.

# Solution Steps
1. Convert numerical features to categical mappings
2. Using chi2 and mutual information to consider and determine valuable features among the dataset
3. Consider different classic classifier which seems more robust to imbalanced data
   ### Decision Tree
   ### Random Forest
   ### GradientBoosting
More analysis and details are available in the colab notebook added to the project, evaluation metrics are also available in the notebooks outputs for all experiments.
In this problem like anomaly detection problems the 1 class is so important. Acoording to f1 metric the best fitted method on the selected features has been chosen to build the service.

# Notes and Furthur suggestions
* Normalising features can be added to the solution 
* Timestamp features could be used as another categorical data using intervals and can be considered in the future
* using the 'comment' feature in addition to the 'income' column as a text feature and use tfidf + naive bayes or any other text classification approach is a suggestion which may leads to apprppriate results
* BERT finetuning and treet categorical features as text sequence can be used due to transformers more robustness to the dataset imbalancement
* Oversampling can be also considered

# Reproduce the service
Image building command:
  docker build -t canselpred .
  
Container running command:
docker run -d -p 8005:8005 --name canselpred canselpred

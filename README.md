# RideCompletionPrediction
The task is to predict the ride canselation via provided features. The dataset is so imbalanced and this is the most important challenge of the problem.

# Solution Steps
1. Convert numerical features to categical mappings
2. Using chi2 and mutual information to consider and determine valuable features among the dataset
3. Consider different classic classifier which seems more robust to imbalanced data
   ### Decision Tree
   ### Random Forest
   ### GradientBoosting
more analysis and details are available in the colab notebook added to the project, evaluation metrics are also available in the notebooks outputs for all experiments.

# Reproduce the service
Image building command:
  docker build -t canselpred .
  
Container running command:
docker run -d -p 8005:8005 --name canselpred canselpred

#### SER594: Machine Learning Evaluation
#### TODO Hazardous Asteroid Prediction
#### TODO Mayank Mathur
#### TODO November 21, 2022
 
## Evaluation Metrics
### Metric 1
**Name:** Accuracy
 
**Choice Justification:** Accuracy is one of the most common accuracy metrics used and for obvious reasons. It tells us of all the testing data what percentage of the data was correctly classified.
 
 
### Metric 2
**Name:** F1 score
 
**Choice Justification:** F1 Score is a good way to understand the models capabilty to predict outputs correctly. In case of Hazardous asteroid prediction, we need a model that has low false negative scores as that could be potentially catastrophic. Therefore f1 score which keeps false negatives in calculation is a good metric to keep.
 
## Alternative Models
### Alternative models for KNN
**Construction:** Multiple KNN models were trained starting from k=3 all the way to K=20 with an interval of 2. That means only odd K values were selected between 3 and 20. Odd K values usually tend to have better accuracy as there is no chance of a tie happening while voting for class.
 
**Evaluation:** F1 score was used to select the final model. The highest average F1 score came for k=3 as 0.34 which is still very low(1 is perfect 0 is worst case).
 
### Alternative models for Random Forest
**Construction:** Multiple Random Forest models were trained by altering the number of estimators used. Starting with 10 estimators, multiple of 10 were used till 100 estimators.
 
**Evaluation:** F1 score was used to select the final model. The highest average F1 score came for n=40 as 0.991 which is the highest of all models trained.
 
### Alternative models for Gradient Boosting
**Construction:** Multiple Gradient Boosting models were trained by altering the learning rate used. Learning rates used are 0.001,0.01,0.05,0.1 and 0.15.
 
**Evaluation:** F1 score was used to select the final model. The highest average F1 score came for Lr=0.01 as 0.983 which is the second best of all models trained.
 
## Visualization
### Visual KNN_Plot
**Analysis:** There are 2 subplots, 1st is K vs F1 Score and 2nd is K vs accuracy score. As it can be seen from the plot, k=3 offers the best f1 score but not the highest accuracy. This is probably because as we increase K we end up overfitting the data. This can be seen as F1 score overall goes down as K increases.
 
 
### Visual RF_Plot
**Analysis:** There are 2 subplots, 1st is Number of estimators n vs F1 Score and 2nd is n vs accuracy score. As it can be seen from the plot, n=40 offers the best f1 score. It seems that accuracy and F1 score change proprtionally as n increases.
 
 
### Visual GB_Plot
**Analysis:** There are 2 subplots, 1st is learning rate lr vs F1 Score and 2nd is lr vs accuracy score. As it can be seen from the plot both F1 and accuracy pretty much flatten for all Lr. This means we can reach global minima using any Lr, only time to train will change as Lr changes.
 
 
## Best Model
 
**Model:** Best model selected is the Random Forest model with 40 estimators. This model has the highest F1 score and one of the highest accuracy of all models trained.


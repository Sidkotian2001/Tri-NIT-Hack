## Optimal Crop Prediction System

### Introduction
Optimal crop prediction is a crucial aspect of modern agriculture. Farmers need to make informed decisions about the crops they want to grow, 
taking into account factors such as soil composition, rainfall, temperature, and return on investment. This information not only helps them 
save money on fertilizers but also helps avoid the dangerous practice of growing the same crops repeatedly on the same patch of land, which 
can deplete the soil of its natural resources.

### About the System
This system uses a Random Forest classifier to predict the best crop to grow in a particular location based on soil composition, rainfall, temperature, 
and return on investment. The temperature and rainfall are found from an average of the past 5 years, while the yield price is found from a script.

### About the accuracy
Our model predicts a crop at 98.5+ % and a confusion matrix is being plotted in the ipynb file. Along with that various data cleaning and experimentation
has been done to predict the future weather and the yield price.


## How the model works
How it Works
The model reads in a pre-existing dataset of labeled crops and their associated data, including soil composition (nitrogen, phosphorus, and potassium levels), temperature, rainfall, and pH levels. This data is then split into training and testing sets, with 80% used for training and 20% used for testing.

The Random Forest classifier algorithm is then trained on the training data, using the nitrogen, phosphorus, potassium, temperature, pH, and rainfall levels as input features and the label of the crop as the target output. The model is then used to make predictions on the testing data, and the accuracy of the predictions is evaluated using a confusion matrix and an accuracy score.

Finally, the trained model can be used to make predictions on new data by passing in soil composition, temperature, and rainfall information as input.

## Flask Api hosted on Render
https://fasal.onrender.com/predict - Post 

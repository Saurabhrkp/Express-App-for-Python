# importing Joblib
import joblib

# Getting file path
filename = 'C:/Users/saura/Documents/express-python-app/python/models/pima-indians-diabetes.data.sav'

# load the model from disk
loaded_model = joblib.load(filename)

# Predicting
print(loaded_model.predict([[8, 99, 84, 0, 0, 35.4, 0.388, 50]]))

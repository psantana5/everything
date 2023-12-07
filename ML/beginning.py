# Import the required libraries
import numpy as np
from sklearn.linear_model import LinearRegression

# Create the training data
X_train = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
y_train = np.array([2, 3, 3, 4])

# Create the linear regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions
X_test = np.array([[3, 5], [5, 2]])
predictions = model.predict(X_test)

# Print the predictions
print(predictions)
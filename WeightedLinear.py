import pandas as pd
import numpy as np
from scipy.stats import norm
from scipy.signal import gaussian
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import explained_variance_score

def gaussian_smoothings(data, feature_name, window_size, std):
  # Generate Gaussian weights
  weights = gaussian(window_size, std=std)
  weights /= np.sum(weights)  # Normalize weights

  # Apply weights using vectorized multiplication
  smoothed_data = np.convolve(data[feature_name], weights, mode='same')
  return smoothed_data


# Load data
df = pd.read_csv('wr_timestamp.csv', index_col='Timestamps', parse_dates=True)
features = ['Bytes_Sent (TCP)', 'Bytes_Sent (UDP)', 'Bytes_Sent (Other)',
            'Bytes_Received (TCP)', 'Bytes_Received (UDP)', 'Bytes_Received (Other)',
            'Packets_Sent (TCP)', 'Packets_Sent (UDP)', 'Packets_Sent (Other)',
            'Packets_Received (TCP)', 'Packets_Received (UDP)', 'Packets_Received (Other)']


def model_evaluation(df, target):
  print('Evaluating the model for:', target)
  print('-' * 50)

  # Define weight function 
  def weights_function(timestamp):
    weights = np.ones(len(timestamp))  # Equal weights (modify for custom weights)
    return weights

  # Handle missing values before splitting (consider alternative methods if needed)
  df.dropna(inplace=True)

  # Split data with smoothing
  smoothed_data = df[features].apply(lambda x: gaussian_smoothings(df.copy(), x.name, 3, 1))
  X_train, X_test, y_train, y_test = train_test_split(smoothed_data, df[target], test_size=0.2, random_state=42)

  # Calculate weights based on training data size
  weights = weights_function(X_train.index)

  # Create and fit weighted linear regression model
  model = LinearRegression()
  model.fit(X_train, y_train, sample_weight=weights)

  # Make predictions
  y_pred = model.predict(X_test)

  # Calculate evaluation metrics
  mse = mean_squared_error(y_test, y_pred)
  mae = mean_absolute_error(y_test, y_pred)
  r2 = r2_score(y_test, y_pred)
  explained_variance = explained_variance_score(y_test, y_pred)

  print(f"Mean Squared Error: {mse}")
  print(f"Mean Absolute Error: {mae}")
  print(f"R-squared: {r2}")
  print(f"Explained Variance Score: {explained_variance}")
  print('-' * 50)

  print('Using the trained model to make predictions on new data......')
  y_pred = model.predict(X_test)
  print(y_pred)


for each_feature in features:
  model_evaluation(df, each_feature)
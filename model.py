import tensorflow as tf
from tensorflow import keras
from sklearn.metrics import mean_absolute_error

# Define and compile the model
model = keras.Sequential([
    keras.layers.Input(shape=(X_train_scaled.shape[1],)),
    keras.layers.Dense(512, activation='relu'),
    keras.layers.Dense(216, activation='relu'),
    keras.layers.Dense(1, activation='linear')
])
model.compile(optimizer='adam', loss='mean_absolute_error')

# Train the model
model.fit(X_train_scaled, y_train, epochs=4, batch_size=64, validation_data=(X_test_scaled, y_test), verbose=2)

# Function to predict score
def predict_score(venue, batting_team, bowling_team, striker, bowler):
    input_data = pd.DataFrame({
        'venue': [venue],
        'bat_team': [batting_team],
        'bowl_team': [bowling_team],
        'batsman': [striker],
        'bowler': [bowler]
    })
    for column, encoder in label_encoders.items():
        input_data[column] = encoder.transform(input_data[column])
    input_data_scaled = scaler.transform(input_data)
    predicted_score = model.predict(input_data_scaled)[0][0]
    print(f'Predicted Score: {int(predicted_score)}')

# Function to check the accuracy of the model
def check_accuracy():
    y_pred = model.predict(X_test_scaled)
    mae = mean_absolute_error(y_test, y_pred)
    print(f'Mean Absolute Error on Test Set: {mae}')

# Check accuracy
check_accuracy()

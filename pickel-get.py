import pandas as pd
import numpy as np
from pymongo import MongoClient
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
import pickle
from sklearn.metrics import mean_squared_error, mean_absolute_error

# Replace <password> with your actual MongoDB Atlas password
uri = "mongodb+srv://chethankeshavmurthy:okchethan123@cluster0.jvsptl5.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# Access the 'Cluster0' database
db = client['Cluster0']

# Access the 'menstrual_data' collection
menstrual_data = db['menstrual_data']

# Define your ANN model with the desired number of epochs
max_epochs = 25  # You can change this number
ann = MLPRegressor(hidden_layer_sizes=(50, 50), max_iter=max_epochs, random_state=42, warm_start=True)

# Print progress
print("Loading data from MongoDB...")

# Load the dataset from MongoDB
data = list(menstrual_data.find())
df = pd.DataFrame(data)

# Check if data is available
if len(df) == 0:
    print("No data found in MongoDB.")
else:
    # Print a table with only names
    names = df['username']
    print(names.to_string(index=False))

    # Extract features from 'health_stats'
    health_stats = df['health_stats'].apply(pd.Series)  # Extract the subfields within 'health_stats'

    # Define the features you want to use
    selected_features = [
        'weight',
        'height',
        'heart_rate',
        'body_temperature',
        'sleep_duration_hours',
        'stress_level',
        'exercise_minutes',
        'water_intake_ml',
        'caloric_intake_kcal'
    ]

    X = health_stats[selected_features]

    # Check if data is available for features
    if not X.empty:
        # Convert the 'last_period_date' column to datetime and calculate days from the min date
        df['last_period_date'] = pd.to_datetime(df['last_period_date'])
        df['last_period_date_days'] = (df['last_period_date'] - df['last_period_date'].min()).dt.days

        y = df['last_period_date_days']

        # Check if target variable data is available
        if not y.empty:
            # Standardize the features
            scaler = StandardScaler()
            X_scaled = scaler.fit_transform(X)

            # Split the data into training and testing sets
            X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

            # Check if there is data available for training
            if X_train.shape[0] > 0:
                # Train the ANN model with multiple epochs
                print(f"Training the ANN model for {max_epochs} epochs...")
                for epoch in range(max_epochs):
                    ann.fit(X_train, y_train)
                    y_pred = ann.predict(X_test)
                    mse = mean_squared_error(y_test, y_pred)
                    mae = mean_absolute_error(y_test, y_pred)
                    print(f"Epoch {epoch + 1}/{max_epochs}:")
                    print(f"Mean Squared Error: {mse:.2f} (Lower is better)")
                    print(f"Mean Absolute Error: {mae:.2f} (Lower is better)")
                    print("--------------------------")

                print("Training completed.")

                # Save the trained model to a pickle file
                with open('ann_model.pkl', 'wb') as model_file:
                    pickle.dump(ann, model_file)

                # Predict upcoming period dates
                predicted_days = ann.predict(X_scaled)
                predicted_dates = df['last_period_date'].min() + pd.to_timedelta(predicted_days, unit='D')

                # Update the 'predicted_date' field in the MongoDB database
                for i, row in df.iterrows():
                    menstrual_data.update_one({'_id': row['_id']}, {'$set': {'predicted_date': predicted_dates[i]}})

                # Extract the 'last_period_date' and 'predicted_date' columns
                actual_dates = df['last_period_date']
                predicted_dates = predicted_dates

                # Calculate the difference in days between predicted and actual dates
                date_difference = (predicted_dates - actual_dates).dt.days

                # Create a new DataFrame to hold actual and predicted dates
                date_df = pd.DataFrame({'Actual Dates': actual_dates, 'Predicted Dates': predicted_dates,
                                        'Date Difference (Days)': date_difference})

                # Display the table of actual and predicted dates
                print(date_df.to_string(index=False))

                # Generate a histogram to visualize the date difference
                plt.hist(date_difference, bins=20, color='lightblue', edgecolor='black')
                plt.title('Difference between Predicted and Actual Dates')
                plt.xlabel('Date Difference (Days)')
                plt.ylabel('Frequency')
                plt.grid(True)
                plt.show()

            else:
                print("Insufficient data for training.")
        else:
            print("No data found for the target variable.")
    else:
        print("No data found for features.")


from pymongo import MongoClient

# Replace <password> with your actual MongoDB Atlas password
uri = "mongodb+srv://chethankeshavmurthy:okchethan123@cluster0.jvsptl5.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# Access the 'Cluster0' database
db = client['Cluster0']

# Access the 'menstrual_data' collection
menstrual_data = db['menstrual_data']

# Delete all existing documents in the collection
menstrual_data.delete_many({})

# Define data for 15 girls
girls_data = [
    {
        'username': 'Alice',
        'password': 'password1',
        'last_period_date': '2023-11-05',
        'health_stats': {
            'weight': 52.2,
            'height': 169,
            'blood_pressure': '113/70',
            'heart_rate': 71,
            'body_temperature': 36.4,
            'sleep_duration_hours': 9,
            'stress_level': 1,
            'exercise_minutes': 21,
            'water_intake_ml': 1061,
            'caloric_intake_kcal': 1556,
        }
    },
    {
        'username': 'Alisha',
        'password': 'password2',
        'last_period_date': '2023-11-05',
        'health_stats': {
            'weight': 52.2,
            'height': 169,
            'blood_pressure': '113/70',
            'heart_rate': 71,
            'body_temperature': 36.4,
            'sleep_duration_hours': 9,
            'stress_level': 1,
            'exercise_minutes': 21,
            'water_intake_ml': 1061,
            'caloric_intake_kcal': 1556,
        }
    },
    {
        'username': 'Emily',
        'password': 'password3',
        'last_period_date': '2023-11-10',
        'health_stats': {
            'weight': 50.0,
            'height': 165,
            'blood_pressure': '120/80',
            'heart_rate': 75,
            'body_temperature': 36.5,
            'sleep_duration_hours': 8,
            'stress_level': 2,
            'exercise_minutes': 30,
            'water_intake_ml': 1200,
            'caloric_intake_kcal': 1600,
        }
    },
    {
        'username': 'Olivia',
        'password': 'password4',
        'last_period_date': '2023-11-08',
        'health_stats': {
            'weight': 48.5,
            'height': 160,
            'blood_pressure': '110/70',
            'heart_rate': 72,
            'body_temperature': 36.3,
            'sleep_duration_hours': 7,
            'stress_level': 3,
            'exercise_minutes': 40,
            'water_intake_ml': 1300,
            'caloric_intake_kcal': 1450,
        }
    },
    {
        'username': 'Sophia',
        'password': 'password5',
        'last_period_date': '2023-11-12',
        'health_stats': {
            'weight': 54.0,
            'height': 170,
            'blood_pressure': '125/75',
            'heart_rate': 70,
            'body_temperature': 36.8,
            'sleep_duration_hours': 8,
            'stress_level': 2,
            'exercise_minutes': 35,
            'water_intake_ml': 1400,
            'caloric_intake_kcal': 1700,
        }
    },
    {
        'username': 'Ava',
        'password': 'password6',
        'last_period_date': '2023-11-09',
        'health_stats': {
            'weight': 51.5,
            'height': 167,
            'blood_pressure': '115/75',
            'heart_rate': 68,
            'body_temperature': 36.6,
            'sleep_duration_hours': 7,
            'stress_level': 4,
            'exercise_minutes': 45,
            'water_intake_ml': 1100,
            'caloric_intake_kcal': 1550,
        }
    },
    {
        'username': 'Mia',
        'password': 'password7',
        'last_period_date': '2023-11-15',
        'health_stats': {
            'weight': 49.8,
            'height': 163,
            'blood_pressure': '112/72',
            'heart_rate': 70,
            'body_temperature': 36.4,
            'sleep_duration_hours': 7,
            'stress_level': 3,
            'exercise_minutes': 50,
            'water_intake_ml': 1250,
            'caloric_intake_kcal': 1600,
        }
    },
    {
        'username': 'Charlotte',
        'password': 'password8',
        'last_period_date': '2023-11-11',
        'health_stats': {
            'weight': 52.5,
            'height': 168,
            'blood_pressure': '118/78',
            'heart_rate': 73,
            'body_temperature': 36.7,
            'sleep_duration_hours': 8,
            'stress_level': 2,
            'exercise_minutes': 55,
            'water_intake_ml': 1350,
            'caloric_intake_kcal': 1650,
        }
    },
    {
        'username': 'Amelia',
        'password': 'password9',
        'last_period_date': '2023-11-14',
        'health_stats': {
            'weight': 49.2,
            'height': 162,
            'blood_pressure': '110/68',
            'heart_rate': 68,
            'body_temperature': 36.3,
            'sleep_duration_hours': 7,
            'stress_level': 3,
            'exercise_minutes': 60,
            'water_intake_ml': 1400,
            'caloric_intake_kcal': 1550,
        }
    },
    {
        'username': 'Ella',
        'password': 'password10',
        'last_period_date': '2023-11-13',
        'health_stats': {
            'weight': 50.5,
            'height': 165,
            'blood_pressure': '115/75',
            'heart_rate': 72,
            'body_temperature': 36.5,
            'sleep_duration_hours': 8,
            'stress_level': 2,
            'exercise_minutes': 50,
            'water_intake_ml': 1300,
            'caloric_intake_kcal': 1600,
        }
    },
    {
        'username': 'Lily',
        'password': 'password11',
        'last_period_date': '2023-11-16',
        'health_stats': {
            'weight': 48.5,
            'height': 160,
            'blood_pressure': '112/72',
            'heart_rate': 70,
            'body_temperature': 36.4,
            'sleep_duration_hours': 7,
            'stress_level': 3,
            'exercise_minutes': 45,
            'water_intake_ml': 1250,
            'caloric_intake_kcal': 1550,
        }
    },
    {
        'username': 'Grace',
        'password': 'password12',
        'last_period_date': '2023-11-17',
        'health_stats': {
            'weight': 52.0,
            'height': 170,
            'blood_pressure': '120/80',
            'heart_rate': 75,
            'body_temperature': 36.6,
            'sleep_duration_hours': 8,
            'stress_level': 2,
            'exercise_minutes': 40,
            'water_intake_ml': 1200,
            'caloric_intake_kcal': 1500,
        }
    },
    {
        'username': 'Chloe',
        'password': 'password13',
        'last_period_date': '2023-11-19',
        'health_stats': {
            'weight': 49.8,
            'height': 167,
            'blood_pressure': '118/78',
            'heart_rate': 73,
            'body_temperature': 36.7,
            'sleep_duration_hours': 7,
            'stress_level': 3,
            'exercise_minutes': 35,
            'water_intake_ml': 1300,
            'caloric_intake_kcal': 1550,
        }
    },
    {
        'username': 'Sofia',
        'password': 'password14',
        'last_period_date': '2023-11-20',
        'health_stats': {
            'weight': 53.0,
            'height': 168,
            'blood_pressure': '125/75',
            'heart_rate': 68,
            'body_temperature': 36.8,
            'sleep_duration_hours': 8,
            'stress_level': 2,
            'exercise_minutes': 30,
            'water_intake_ml': 1400,
            'caloric_intake_kcal': 1600,
        }
    },
    {
        'username': 'Harper',
        'password': 'password15',
        'last_period_date': '2023-11-18',
        'health_stats': {
            'weight': 51.5,
            'height': 163,
            'blood_pressure': '115/75',
            'heart_rate': 70,
            'body_temperature': 36.6,
            'sleep_duration_hours': 7,
            'stress_level': 4,
            'exercise_minutes': 45,
            'water_intake_ml': 1100,
            'caloric_intake_kcal': 1550,
        }
    },
    {
        'username': 'Evelyn',
        'password': 'password16',
        'last_period_date': '2023-11-21',
        'health_stats': {
            'weight': 54.5,
            'height': 169,
            'blood_pressure': '130/80',
            'heart_rate': 72,
            'body_temperature': 36.5,
            'sleep_duration_hours': 8,
            'stress_level': 3,
            'exercise_minutes': 40,
            'water_intake_ml': 1300,
            'caloric_intake_kcal': 1500,
        }
    },
    {
        'username': 'Zoe',
        'password': 'password17',
        'last_period_date': '2023-11-23',
        'health_stats': {
            'weight': 52.2,
            'height': 170,
            'blood_pressure': '120/75',
            'heart_rate': 75,
            'body_temperature': 36.7,
            'sleep_duration_hours': 7,
            'stress_level': 2,
            'exercise_minutes': 35,
            'water_intake_ml': 1400,
            'caloric_intake_kcal': 1600,
        }
    },
    {
        'username': 'Nora',
        'password': 'password18',
        'last_period_date': '2023-11-22',
        'health_stats': {
            'weight': 50.8,
            'height': 168,
            'blood_pressure': '118/76',
            'heart_rate': 73,
            'body_temperature': 36.8,
            'sleep_duration_hours': 8,
            'stress_level': 2,
            'exercise_minutes': 30,
            'water_intake_ml': 1200,
            'caloric_intake_kcal': 1550,
        }
    },
    {
        'username': 'Lillian',
        'password': 'password19',
        'last_period_date': '2023-11-25',
        'health_stats': {
            'weight': 48.9,
            'height': 165,
            'blood_pressure': '112/72',
            'heart_rate': 70,
            'body_temperature': 36.6,
            'sleep_duration_hours': 7,
            'stress_level': 3,
            'exercise_minutes': 45,
            'water_intake_ml': 1250,
            'caloric_intake_kcal': 1550,
        }
    },
    {
        'username': 'Lucy',
        'password': 'password20',
        'last_period_date': '2023-11-24',
        'health_stats': {
            'weight': 52.0,
            'height': 167,
            'blood_pressure': '115/74',
            'heart_rate': 72,
            'body_temperature': 36.5,
            'sleep_duration_hours': 8,
            'stress_level': 2,
            'exercise_minutes': 40,
            'water_intake_ml': 1300,
            'caloric_intake_kcal': 1600,
        }
    }
]

# Insert the data for 15 girls into the collection
result = menstrual_data.insert_many(girls_data)

print(f"Inserted {len(result.inserted_ids)} documents")

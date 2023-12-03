from pymongo import MongoClient

# Replace <password> with your actual MongoDB Atlas password
uri = "mongodb+srv://chethankeshavmurthy:okchethan123@cluster0.jvsptl5.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# Access the 'Cluster0' database
db = client['Cluster0']

# Access the 'menstrual_data' collection
menstrual_data = db['menstrual_data']

# Remove the 'r2_score' field from all documents where it is set to NaN
filter_criteria = {'r2_score': {'$exists': True, '$type': 10}}  # Type 10 represents NaN
update_query = {'$unset': {'r2_score': 1}}

result = menstrual_data.update_many(filter_criteria, update_query)

print(f"Removed {result.modified_count} documents with NaN r2_score.")

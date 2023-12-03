from flask import Flask, render_template, request
from pymongo import MongoClient
from flask import Flask, render_template, request, redirect, url_for
from transformers import pipeline

text_generation_pipe = pipeline("text-generation", model="Israr-dawar/psychology_chatbot")

app = Flask(__name__)

# Replace <password> with your actual MongoDB Atlas password
uri = "mongodb+srv://chethankeshavmurthy:okchethan123@cluster0.jvsptl5.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# Access the 'Cluster0' database
db = client['Cluster0']

# Access the 'menstrual_data' collection
menstrual_data = db['menstrual_data']




@app.route('/')
def index():
    return render_template('index.html')  # Replace with your index page content

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        last_period_date = request.form['last_period_date']
        weight = float(request.form['weight'])
        height = int(request.form['height'])
        blood_pressure = request.form['blood_pressure']
        heart_rate = int(request.form['heart_rate'])
        body_temperature = float(request.form['body_temperature'])
        sleep_duration_hours = float(request.form['sleep_duration_hours'])
        stress_level = int(request.form['stress_level'])
        exercise_minutes = int(request.form['exercise_minutes'])
        water_intake_ml = float(request.form['water_intake_ml'])
        caloric_intake_kcal = int(request.form['caloric_intake_kcal'])

        user_data = {
            'username': username,
            'password': password,
            'last_period_date': last_period_date,
            'health_stats': {
                'weight': weight,
                'height': height,
                'blood_pressure': blood_pressure,
                'heart_rate': heart_rate,
                'body_temperature': body_temperature,
                'sleep_duration_hours': sleep_duration_hours,
                'stress_level': stress_level,
                'exercise_minutes': exercise_minutes,
                'water_intake_ml': water_intake_ml,
                'caloric_intake_kcal': caloric_intake_kcal
            }
        }

        # Store user data in MongoDB
        menstrual_data.insert_one(user_data)  # Change 'collection' to 'menstrual_data'
        print(f"User data inserted into MongoDB: {user_data}")

        # Redirect to the login page
        print("Redirecting to login page")
        return redirect(url_for('loginL'))

    print("Rendering signup form")
    return render_template('signup.html')  # Render the sign-up form



@app.route('/login-LOAD')
def loginL():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Check if the username and password match an existing user in the database
    user_data = menstrual_data.find_one({'username': username, 'password': password})

    if user_data:
        # If login is successful, redirect to the dashboard and send user data
        return render_template('dashboard.html', user_data=user_data)
    else:
        return "Login failed. Please try again."


@app.route('/visualize')
def visualize():
    # Get the data from MongoDB
    data = menstrual_data.find()

    # Get the dark mode preference from the query string (if set)
    dark_mode = request.args.get('dark_mode', default='light')

    return render_template('visualize.html', data=data, dark_mode=dark_mode)


@app.route('/chat', methods=['POST'])
def chat():
    # Get the user's message from the request
    user_message = request.get_json()["userMessage"]

    # Define a positive message about women's mental health
    positive_message = "It's important to prioritize and care for your mental health. Taking time for self-care, seeking support, and staying connected with loved ones can have a positive impact on women's mental health."

    # Generate a chatbot response based on the user's message
    chatbot_response = chatbot_pipeline(user_message)

    # Combine the chatbot's response with the positive message
    full_response = f"{positive_message}\nChatbot: {chatbot_response}"

    # Return the combined response as JSON
    return jsonify({"chatbotResponse": full_response})


@app.route('/run_script')
def run_script():
    output = subprocess.check_output(['python', 'pickel-get.py'], universal_newlines=True)
    return output

@app.route('/download_model')
def download_model():
    return send_file('ann_model.pkl', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)

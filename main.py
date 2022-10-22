from flask import Flask
import better_weather_code

app = Flask(__name__)

@app.route("/")
def home():
    return "Here",200
    
if __name__ == "__main__":
    app.run(debug=True)
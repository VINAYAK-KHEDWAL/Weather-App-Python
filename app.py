from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    weather = None
    if request.method == "POST":
        city = request.form.get("city")
        api_key = " "  # Add Your Api_key
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        data = requests.get(url).json()
        print(data)  # Debugging present to view response
        if data.get("main"):
            weather = {
                "city": city,
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"]  # Fix for list index
            }
        else:
            weather = {"error": data.get("message", "Error fetching data")}
    return render_template("index.html", weather=weather)

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "( Ali DEVOPS ENGINEER Intern at Blue Stone  Dockerized with CICD pipeline with jenkins  Application new updated Today code Pushed"

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=5000)  
    

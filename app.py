# app.py
from flask import Flask, render_template, request
from chatbot import chatbot_response

app = Flask(__name__)
app = Flask(__name__, template_folder='templates')

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_text = request.args.get('msg')
    return chatbot_response(user_text)

if __name__ == "__main__":
    app.run(debug=True)

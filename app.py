from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return "kya haal hai"
if __name__=='__main__':
    app.run(debug=True)
    
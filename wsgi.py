from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello From Python Demo with Red Hat OpenShift!"

@app.route("/test")
def test():
    return "Testing"

if __name__ == "__main__":
    application.run()

from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello From Red Hat OpenShift!"

if __name__ == "__main__":
    application.run()

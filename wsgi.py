from flask import Flask
# import requests

application = Flask(__name__)

@application.route("/")
def hello():
  return "Hello From Python Demo with Red Hat OpenShift!"

@app.route("/test")
def test():
  return "Testing"

@app.route("/geturldata")
def geturldata():
  # url_req = requests.get("https://data.gov.sg/api/action/datastore_search?resource_id=f9dbfc75-a2dc-42af-9f50-425e4107ae84&limit=10")
  # json_data = url_req.json()
  json_data = "String variable"
  return json_data

if __name__ == "__main__":
    application.run()

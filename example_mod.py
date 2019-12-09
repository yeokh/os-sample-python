from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello World, from Flask Web Framework!<br><a href='./shutdown'>Shutdown</a>"

@app.route("/test")
def test():
  return "Testing"

@app.route("/geturldata")
def geturldata():
  url_req = requests.get("https://data.gov.sg/api/action/datastore_search?resource_id=f9dbfc75-a2dc-42af-9f50-425e4107ae84&limit=10")
  json_data = url_req.json()
  return json_data

if __name__ == "__main__":
  print("Running Flask app")
  app.run()
  

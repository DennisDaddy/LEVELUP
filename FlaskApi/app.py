from flask import Flask
import requests
from requests.auth import HTTPBasicAuth
import time
import base64


app = Flask(__name__)

@app.route('/mpesa/api', methods= ['POST'])
def api_message():
	data = request.data
	print(data)
	return "already run"

timestamp = str(time.strftime("%Y%m%d%H%M%S"))

password = 

consumer_key = ""
consumer_secret = ""
api_URL = ""

r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key,consumer_secret))

print(r.text)


access_token = "{}".format(r.text)
api_url = ""

headers = { }

request = {
      "BusinessShortCode": "601754",
      "Password": "{}".format(password),
      "Timestamp": "{}".format(timestamp),
      "TransactionType": "CustomerPayBillOnline",
      "Amount": "100",
      "PartyA": "254799989486",
      "PartyB": "601754",
      "PhoneNumber": "254799989486",
      "CallBackURL": "https://dennis.ml/callback.html",
      "AccountReference": "account",
      "TransactionDesc": "test"
}

response = requests.post(api_url, json = request, headers=headers)

print(response.text)



if __name__ == '__main__':
		app.run(debug=True)	
from flask import Flask
import requests
from requests.auth import HTTPBasicAuth
import time
import base64
import json
app = Flask(__name__)

@app.route('/mpesa', methods=['POST'])
def api_message():
	pass

response1 = requests.get("https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials",auth=('3glGFjDvn6RZz9qyo02iA5HXKsImulew','MCxBBj6cdIpGYfbq')).text
res=json.loads(response1)
access_token = res['access_token']
api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"



amount = int(input('Enter Amount: '))
phone = input("Enter Phone Number(708XXX): ")

headers = { "Authorization": "Bearer "+access_token}

request = {
      "BusinessShortCode": "174379",
      "Password": "MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMTgwNzAzMTA0ODAw",
      "Timestamp": "20180703104800",
      "TransactionType": "CustomerPayBillOnline",
      "Amount": amount,
      "PartyA": "254"+phone,
      "PartyB": "174379",
      "PhoneNumber": "254706480612",
      "CallBackURL": "http://mpesa-requestbin.herokuapp.com/1i6fj7k1",
      "AccountReference": "Dennis Account ",
      "TransactionDesc": "blue"
    }


response = requests.post(api_url, json = request, headers=headers)

print (response.text)	

if __name__ == '__main__':
	app.run(debug=True)
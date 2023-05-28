from flask import Flask, request, render_template, redirect, url_for, flash, make_response, jsonify
import requests, time, random
import time
import threading
import os.path
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

#take p20t and csrf token from binance
p20t = "Bla Bla Bla"
Csrftoken = "Bla Bla Bla"

file_exists = os.path.exists("Claimed.txt")
if not file_exists:
  with open("Claimed.txt","w",newline='') as fi:pass

def claim(code):
    gift_url = "https://www.binance.com:443/bapi/pay/v1/private/binance-pay/gift-box/code/grabV2"
    gift_cookies = {"userPreferredCurrency": "USD_USD",
                    "source": "referral", "campaign": "www.binance.com",
                    "logined": "y", "isAccountsLoggedIn": "y",
                    "p20t": p20t}

    gift_headers = {"Sec-Ch-Ua": "\"Google Chrome\";v=\"112\", \"Chromium\";v=\"112\", \"Not=A?Brand\";v=\"24\"",
                     "Csrftoken": Csrftoken,
                     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 uacq", "Content-Type": "application/json", "Lang": "en", "Clienttype": "web", "Sec-Ch-Ua-Platform": "\"macOS\"", "Accept": "*/*", "Origin": "https://www.binance.com", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://www.binance.com/en/my/wallet/account/payment/cryptobox", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9,my;q=0.8"}
    gift_json={"channel": "DEFAULT", "grabCode": code}
    r1 = requests.post(gift_url, headers=gift_headers, cookies=gift_cookies, json=gift_json)
    r1jsn = r1.json()

    if r1jsn.get("message") == None:
      if r1jsn.get("success") == True:
        amt = r1jsn.get("data")['grabAmountStr']
        currency = r1jsn.get("data")['currency']
        print(f"Successfully Claimed {amt} {currency}.")
    else:
      print(f"Message : {r1jsn.get('message')}")


app = Flask('app')
@app.route('/', methods=['GET'])
def my_form_post():
    print()
    code = request.args.get('code')#.form['code']
    print(f"Code : {code}")
    with open("Claimed.txt","r") as r:
        rr = r.readline()
        if rr == code:
            print("Already Done.")
            return "Success",200#jsonify({"status":300}) 
    claim(code)
    with open("Claimed.txt","w",newline='') as fi:
        fi.writelines(code)
        
    return "Success",200#jsonify({"status":200})
app.run(host='0.0.0.0', port=80,debug=False)

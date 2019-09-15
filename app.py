import os
from os.path import join, dirname
import requests
from flask import Flask, request, render_template
import json
from loan import *

app = Flask(__name__)

BASE_URL = "https://api.freshbooks.com"

CLIENT_SECRET='c511a1c9f546b3e5a9c665b2b00dd70c0239d92f19146268abc3f4e52bef5619'
CLIENT_ID='45fbe62aa0fd2ba9cc48a07ec3ee74b5e11b66164a6e5dd249a2a9c79854eeb4'
REDIRECT_URL='https://localhost:5000/auth'
access_token = ""

@app.route('/auth')
def test_authentication():
    auth_code = request.args.get('code')
    auth_data = {
        "grant_type": "authorization_code",
        "client_secret": CLIENT_SECRET,
        "code": auth_code,
        "client_id": CLIENT_ID,
        "redirect_uri": REDIRECT_URL
    }
    auth_request = requests.post(BASE_URL + "/auth/oauth/token", json = auth_data)
    access_token_dict = json.loads(auth_request.text)
    refresh_token = access_token_dict["refresh_token"]
    access_token = access_token_dict["access_token"]

    _cache_access_token(access_token)
    _cache_refresh_token(refresh_token)
    headers = {"Authorization":"Bearer " + access_token_dict["access_token"]}
    identity_request = requests.get(BASE_URL + "/auth/api/v1/users/me", headers=headers)
    identity_dict = json.loads(identity_request.text)
    profile_dict = identity_dict["response"]["profile"]
    return refresh_token

@app.route('/operations.html')
def operations():
    #loan = Loan(get_account_id(), _get_access_token())
    return render_template('operations.html')

def _cache_access_token(access_token):
    with open("access_token", "w") as fh:
        fh.write(access_token)

def _cache_refresh_token(refresh_token):
    with open("refresh_token", "w") as fh:
        fh.write(refresh_token)

def _get_refresh_token():
    with open("refresh_token") as fh:
        return fh.read()

def _get_access_token():
    with open("access_token") as fh:
        return fh.read()

def refresh_access_token():
    auth_data = {
        "grant_type": "refresh_token",
        "client_secret": CLIENT_SECRET,
        "refresh_token": _get_refresh_token(),
        "client_id": CLIENT_ID,
    }
    auth_request = requests.post(BASE_URL + "/auth/oauth/token", json = auth_data)
    access_token_dict = json.loads(auth_request.text)
    refresh_token = access_token_dict["refresh_token"]
    access_token = access_token_dict["access_token"]

    _cache_access_token(access_token)
    _cache_refresh_token(refresh_token)

def get_data(url, data, headers):
    access_token = _get_access_token()
    headers = {'Authorization': 'Bearer '+access_token, 'Api-Version': 'alpha', 'Content-Type': 'application/json'}
    res = requests.get(url, data=data, headers=headers)
    if res == "<Response [404]>":
        refresh_access_token()
        get_data(url, data, headers)
    return res


# @app.route('/test')
def get_account_id():
    access_token = _get_access_token()
    url = "https://api.freshbooks.com/auth/api/v1/users/me"
    headers = {'Authorization': 'Bearer '+_get_access_token(), 'Api-Version': 'alpha', 'Content-Type': 'application/json'}
    res = get_data(url, data=None, headers=headers)
    response = json.loads(res.text)
    res_dict = response['response']
    return res_dict['roles'][0]['accountid']

if __name__ == '__main__':
    app.run()
    # loan = Loan(get_account_id(), _get_access_token())
    # print(loan.get_income_total())
    # print(loan.get_expense_total())
    # print(loan.get_average_order_value())
    # print(loan.get_profit())
    # print(loan.get_sales_on_account())
    # print(loan.get_profit_analysis())
    # print(loan.get_cash())
    # print(loan.get_biggest_exp())
    # print(loan.get_client_dict())

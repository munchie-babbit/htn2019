import requests
import json
from app import *

class Loan():

    invoice_dict = []
    otherIncome_dict = []

    def __init__(self, accountid, access_token):
        self.url = "https://api.freshbooks.com/accounting/account/"+str(accountid)+"/invoices/invoices"
        self.headers = {'Authorization': 'Bearer '+access_token, 'Api-Version': 'alpha', 'Content-Type': 'application/json'}
        self.res = get_data(self.url, data=None, headers=self.headers)
        res = requests.get(self.url, data=None, headers=self.headers)
        response = json.loads(res.text)
        self.invoice_dict = response['response']

        self.url = "https://api.freshbooks.com/accounting/account/"+str(accountid)+"/other_incomes/other_incomes"
        self.headers = {'Authorization': 'Bearer '+access_token, 'Api-Version': 'alpha', 'Content-Type': 'application/json'}
        self.res = requests.get(self.url, data=None, headers=self.headers)
        res = requests.get(self.url, data=None, headers=self.headers)
        response = json.loads(res.text)
        self.otherIncome_dict = response['response']




    def getInvoiceTotal(self):
        invoices = self.invoice_dict['result']['invoices']
        invoiceTotal = 0.0
        for invoice in invoices:
            invoiceTotal += float(invoice['amount']['amount'])
        return invoiceTotal

    def getOtherIncomeTotal(self):
        others = self.otherIncome_dict['result']['other_income']
        otherTotal = 0.0
        for other in others:
            otherTotal += other['amount']['amount']
        return otherTotal

    def getIncomeTotal(self):
        return self.getInvoiceTotal() + self.getOtherIncomeTotal()

    def average_order_value(self):
        invoice_count = self.invoice_dict.length();
        invoice_total = self.getInvoiceTotal()
        return invoice_total / invoice_count

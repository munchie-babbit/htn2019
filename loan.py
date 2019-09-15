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
        self.res = get_data(self.url, data=None, headers=self.headers)
        res = requests.get(self.url, data=None, headers=self.headers)
        response = json.loads(res.text)
        self.otherIncome_dict = response['response']

        self.url = "https://api.freshbooks.com/accounting/account/"+str(accountid)+"/expenses/expenses"
        self.headers = {'Authorization': 'Bearer '+access_token, 'Api-Version': 'alpha', 'Content-Type': 'application/json'}
        self.res = get_data(self.url, data=None, headers=self.headers)
        res = requests.get(self.url, data=None, headers=self.headers)
        response = json.loads(res.text)
        self.expense_dict = response['response']

        self.url = "https://api.freshbooks.com/accounting/account/"+str(accountid)+"/users/clients"
        self.headers = {'Authorization': 'Bearer '+access_token, 'Api-Version': 'alpha', 'Content-Type': 'application/json'}
        self.res = get_data(self.url, data=None, headers=self.headers)
        res = requests.get(self.url, data=None, headers=self.headers)
        response = json.loads(res.text)
        self.client_dict = response['response']
        print(self.client_dict)

    def get_invoice_total(self):
        invoices = self.invoice_dict['result']['invoices']
        invoiceTotal = 0.0
        for invoice in invoices:
            invoiceTotal += float(invoice['amount']['amount'])
        return invoiceTotal

    def get_other_income_total(self):
        others = self.otherIncome_dict['result']['other_income']
        otherTotal = 0.0
        for other in others:
            otherTotal += float(other['amount']['amount'])
        return otherTotal

    def get_expense_total(self):
        expenses = self.expense_dict['result']['expenses']
        expenseTotal = 0.0
        for expense in expenses:
            expenseTotal += float(expense['amount']['amount'])
        return expenseTotal

    def get_income_total(self):
        return self.get_invoice_total() + self.get_other_income_total()

    def get_average_order_value(self):
        invoice_count = len(self.invoice_dict['result']['invoices'])
        invoice_total = self.get_invoice_total()
        return invoice_total / invoice_count

    def get_profit(self):
        return self.get_income_total() - self.get_expense_total()

    def get_sales_on_account(self):
        if self.get_other_income_total() > 0: return self.get_invoice_total() / self.get_other_income_total()
        else: return -1

    def get_profit_analysis(self):
        return self.get_profit() / self.get_expense_total()

    def get_cash(self):
        return self.get_profit() - self.get_expense_total()

    def get_biggest_exp(self):
        expenses = self.expense_dict['result']['expenses']
        maxExpense = 0.0
        for expense in expenses:
            if maxExpense < float(expense['amount']['amount']): maxExpense = float(expense['amount']['amount'])
        return maxExpense

    # def get_client_dict(self):
    #     print("In get client")
    #     clients = self.client_dict['result']['clients']
    #     client_invoice_dict = []
    #     for client in clients:
    #         client_invoice_dict[client['id']] += client
    #     print(client_invoice_dict)
    #     self.client_dict['']
    #
    # def get_client_sum(self, clientid, accountid):
    #     print("in sum")
    #     return 0
    #
    # def get_biggest_client(self, accountid):
    #     clients = self.client_dict['result']['clients']
    #     if len(clients) <= 0: return ''
    #     highRoller = ''
    #     jackpot = 0.0
    #     for client in clients:
    #         self.get_client(client['id'], accountid)





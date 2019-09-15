import requests
import json
import datetime as DT
from datetime import datetime
from app import *

class Loan():

    invoice_dict = []
    otherIncome_dict = []
    accountid = get_account_id()

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

    def get_invoice_total(self):
        invoices = self.invoice_dict['result']['invoices']
        invoiceTotal = 0.0
        for invoice in invoices:
            invoiceTotal += float(invoice['amount']['amount'])
        return round(invoiceTotal, 2)

    def get_other_income_total(self):
        others = self.otherIncome_dict['result']['other_income']
        otherTotal = 0.0
        for other in others:
            otherTotal += float(other['amount']['amount'])
        return round(otherTotal, 2)

    def get_expense_total(self):
        expenses = self.expense_dict['result']['expenses']
        expenseTotal = 0.0
        for expense in expenses:
            expenseTotal += float(expense['amount']['amount'])
        return round(expenseTotal, 2)

    def get_income_total(self):
        return self.get_invoice_total() + self.get_other_income_total()

    def get_average_order_value(self):
        invoice_count = len(self.invoice_dict['result']['invoices'])
        invoice_total = self.get_invoice_total()
        return round(invoice_total / invoice_count, 2)

    def get_profit(self):
        return round(self.get_income_total() - self.get_expense_total(),)

    def get_sales_on_account(self):
        if self.get_other_income_total() > 0: return round(self.get_invoice_total() / self.get_other_income_total(), 2)
        else: return -1

    def get_profit_analysis(self):
        if self.get_expense_total() == 0: return 0
        else: return round(self.get_profit() / self.get_expense_total(), 2)

    def get_cash(self):
        return round(self.get_profit() - self.get_expense_total(), 2)

    def get_biggest_exp(self):
        expenses = self.expense_dict['result']['expenses']
        maxExpense = 0.0
        for expense in expenses:
            if maxExpense < float(expense['amount']['amount']): maxExpense = float(expense['amount']['amount'])
        return round(maxExpense, 2)

    def get_biggest_buyer(self):
        buyers = self.invoice_dict['result']['invoices']
        maxPurchase = 0.0
        maxBuyer = ''
        for buyer in buyers:
            if maxPurchase < float(buyer['amount']['amount']):
                maxPurchase = float(buyer['amount']['amount'])
                maxBuyer = buyer['fname'] + " " + buyer['lname']
        return maxBuyer

    def get_date(self):
        return DT.datetime.today().strftime('%Y-%m-%d')

    def last_week(self):
        today = DT.datetime.today()
        return (today - DT.timedelta(days=7)).strftime('%Y-%m-%d')

    def get_date_difference(self, date):
        d1 = datetime.strptime(self.last_week(), "%Y-%m-%d")
        d2 = datetime.strptime(date, "%Y-%m-%d")
        delta = d2 - d1
        return delta.days - 1

    def get_invoice_total_today(self):
        invoices = self.invoice_dict['result']['invoices']
        invoiceTotal = 0.0
        for invoice in invoices:
            if invoice['date_paid'] == str(self.get_date()): invoiceTotal += float(invoice['amount']['amount'])
        return round(invoiceTotal, 2)

    def get_other_income_total_today(self):
        incomes = self.otherIncome_dict['result']['other_income']
        otherIncomeTotal = 0.0
        for income in incomes:
            if income['date'] == str(self.get_date()): otherIncomeTotal += float(income['amount']['amount'])
        return round(otherIncomeTotal, 2)

    def get_total_today(self):
        return round(self.get_invoice_total_today() + self.get_other_income_total_today(), 2)

    def get_expenses_today(self):
        expenses = self.expense_dict['result']['expenses']
        expenseTotal = 0.0
        for expense in expenses:
            if expense['date'] == str(self.get_date()): expenseTotal += float(expense['amount']['amount'])
        return round(expenseTotal, 2)

    def get_profit_today(self):
        return round(self.get_total_today() - self.get_expenses_today(), 2)

    def get_profit_analysis_today(self):
        if self.get_expenses_today() == 0: return 0
        else: return round(self.get_profit_today() / self.get_expenses_today(), 2)

    def get_week_invoices(self):
        invoices = self.invoice_dict['result']['invoices']
        invoiceTotals = [0]*7
        for invoice in invoices:
            date_diff = self.get_date_difference(invoice['create_date'])
            if date_diff >= 0: invoiceTotals[date_diff] += float(invoice['amount']['amount'])
        return invoiceTotals

    def get_week_other_income(self):
        others = self.otherIncome_dict['result']['other_income']
        otherTotals = [0]*7
        for other in others:
            date_diff = self.get_date_difference(other['date'])
            if date_diff >= 0: otherTotals[date_diff] += float(other['amount']['amount'])
        return otherTotals

    def get_week_expenses(self):
        expenses = self.expense_dict['result']['expenses']
        expenseTotal = [0]*7
        for expense in expenses:
            date_diff = self.get_date_difference(expense['date'])
            if date_diff >= 0: expenseTotal[date_diff] += float(expense['amount']['amount'])
        return expenseTotal

    def get_week_revenue(self):
        invoice = self.get_week_invoices()
        other = self.get_week_other_income()
        revenue = [0]*7
        for i in range(0,7): revenue[i] = invoice[i] + other[i]
        print(revenue)
        return revenue

    def get_week_profit(self):
        revenue = self.get_week_revenue()
        expenses = self.get_week_expenses()
        profit = [0]*7
        for i in range(0,7): profit[i] = revenue[i] - expenses[i]
        print(profit)
        return profit



    # def get_client_dict(self):
    #     print("In get client")
    #     clients = self.client_dict['result']['clients']
    #     client_invoice_dict = {}
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
    #
    #



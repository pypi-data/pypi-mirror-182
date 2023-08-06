from datetime import datetime as dtime

class MonthError(Exception):

    def __int__(self):
        print("Error")

class Search(object):

    def __init__(self, df):
        self.statement = df
        
    def check_empty(self, df):
        if(df.empty == True):
            print("No records found")
            return None
        else:
            return df 
    
    def search_date(self, date):
        try:
            matched_date = self.statement.loc[self.statement['date'] == dtime.strptime(date, "%d/%m/%Y")]
        except ValueError:
            print("Input the date in correct format")
        except Exception as Ex:
            print(Ex)
        else:
            return self.check_empty(matched_date)

    def search_range(self, start_date, end_date):
        if(dtime.strptime(start_date, "%d/%m/%Y") <= dtime.strptime(end_date, "%d/%m/%Y")):
            # filter by date range
            matched_date = self.statement[(self.statement['date'].dt.strftime("%d/%m/%Y") >= start_date) & (self.statement['date'].dt.strftime("%d/%m/%Y") <= end_date)]
            # check if any transaction occured during that period
            return self.check_empty(matched_date)
        else:
            print("Starting date is bigger than ending date!")
            return None

    def search_month(self, month):
        try:
            if month > 12 or month < 1:
                raise MonthError
        except MonthError:
            print("Please enter a number between 1-12")
        else:
            # filter by date range
            matched_month = self.statement[self.statement['date'].dt.strftime("%m") == str(month)]
            # check if any transaction occured during that period
            return self.check_empty(matched_month)


    def search_year(self, year):
        # filter by date range
        matched_year = self.statement[self.statement['date'].dt.strftime("%Y") == year]
        # check if any transaction occured during that period
        return self.check_empty(matched_year)

    def search_category(self, cname):
        # filter by category
        matched_cat = self.statement.loc[self.statement['category'] == cname]
        # return matched_cat
        return self.check_empty(matched_cat)

    def search_category_range(self, cname, start_date, end_date):
        filtered_statement = self.search_range(start_date, end_date)
        # check filtered_statement valid or not
        if(filtered_statement is None):
            return None
        else:
            matched_cat = filtered_statement.loc[filtered_statement["category"] == cname]
            return self.check_empty(matched_cat)    

    def search_amount(self, amount):
        matched_amt = self.statement.loc[self.statement['amount'] == amount]
        # return matched_amt
        return self.check_empty(matched_amt)

    def search_amount_range(self, amount, start_date, end_date):
        filtered_statement = self.search_range(start_date, end_date)
        # check filtered_statement valid or not
        if(filtered_statement is None):
            return None
        else:
            
            matched_amt = filtered_statement.loc[filtered_statement['amount'] == amount]
            return self.check_empty(matched_amt)


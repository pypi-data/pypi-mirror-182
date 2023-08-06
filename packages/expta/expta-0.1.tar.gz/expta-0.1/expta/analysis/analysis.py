from analysis.search import Search

class Analysis(Search):

    def __init__(self, df, start_date, end_date):
        super().__init__(df)
        self.start_date = start_date
        self.end_date = end_date

    def total_expense(self, df):
        return df['amount'].sum()
    
    def income_expense_ratio_range(self, income):
        filtered_statement = Search.search_range(self, self.start_date, self.end_date)
        exp_amount = self.total_expense(filtered_statement)
        if income >= exp_amount:
            ratio = (exp_amount/income)*100
            return ratio
        else:
            return None

    def category_percentage(self):
        filtered_statement = Search.search_range(self, self.start_date, self.end_date)
        category_percentage = filtered_statement.groupby(["category"], dropna=False).sum()
        category_percentage["percentage"] = 100 * (category_percentage['amount']/self.total_expense(category_percentage))
        return category_percentage

    def category_average(self):
        filtered_statement = Search.search_range(self, self.start_date, self.end_date)
        category_average = filtered_statement.groupby(["category"], dropna=False).sum()
        category_average['average'] = filtered_statement.groupby('category', dropna=False).mean()
        return category_average

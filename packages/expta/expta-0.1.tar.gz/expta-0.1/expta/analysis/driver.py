
# to use subpackage individually, 
# you need to provide the dataframe
import pandas as pd # import to initialize dataframe

from analysis.search import Search as s #from subpackage.module import class
from analysis.analysis import Analysis as a

# providing dataframe and formatting properly
# this step is done in `data` subpackage
statement = pd.read_csv("filename") # filename is td credit card statement csv file
statement['date'] = pd.to_datetime(statement['date']) # formatting date

# using the package

# search module
p = s(statement) # creating a search object with the dataframe
p.search_year("2022") # searching for all 2022 expenses

# analysis module
j = a.Analysis(statement, "02/11/2022", "26/11/2022") # creating an analysis object, with the dataframe, and start and end dates
j.income_expense_ratio_range(1000) # argument is income

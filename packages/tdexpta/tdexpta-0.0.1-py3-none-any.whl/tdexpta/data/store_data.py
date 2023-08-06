import pandas as pd
from datetime import datetime
import tdexpta.data.categorize_data as cd
from numpy import nan 

catlist = cd.catlist

colnames = ["date", "shop_name", "amount", "category"]
#createnewdf = None

"""def __init__(self, maindf = newdf, colnames = colnames):
    self.maindf = maindf
    self.colnames = colnames"""

"""def convert_to_df(self):
    return self.maindf"""

def add_csv(filename, df = None):
    if df is None:
        df = pd.DataFrame(columns=colnames)
    try: 
    #filename = input("Enter csv file name to add: ")
        #print("File to add is: " + filename)
        userdf = pd.read_csv(filename, header=None, usecols=[0, 1, 2])
        userdf['category'] = ''
        userdf.columns = colnames
        userdf = userdf.dropna()
        userdf["date"] = pd.to_datetime(userdf["date"])
        #df = df.append(userdf)
        df = pd.concat([df, userdf], ignore_index=True)
    except Exception as e:
        print(e) 
        return None
    return df

def add_expenses(user_date, user_shopname, user_amount, user_category,  df = None, catlist=catlist):
    """ adds expense to a dataframe

    Parameters:
    user_date: date of transaction format MM/DD/YYYY
    user_shopname: the transaction name
    user_amount: amount of transaction, numeric
    user_category: key of category list dictionary (catlist)
    df: dataframe to append to. If not specified, default is a new empty dataframe
    catlist: dictionary of categories in format index:name, default is catlist

    Returns:
    Dataframe with new row appended to it
    """
    if df is None:
        df = pd.DataFrame(columns=colnames)
    try:
        date_format = "%d/%m/%Y"
        user_date = datetime.strptime(user_date, date_format)
        user_shopname = user_shopname.upper()
        user_amount = float(user_amount)
        user_category = cd.catlist.get(int(user_category))
        #print(f'Confirm input (y/n): Date: {user_date}, Transaction name: {user_shopname}, Amount: {user_amount}, Category: {user_category}')
        newrow = [user_date, user_shopname, user_amount, user_category]
        #confirm = input("Confirm input (y/n): ")
        ## confirm = "y"
        #if confirm == "y":
        df.loc[len(df)] = newrow
            #print(self.maindf)
        #else:
            #print("input cancelled")
    #except ValueError:
        #print("input cancelled; Please input a numeric value for amount")
    except Exception as e:
        print(e)
        return None
    return df
        


# def show_expenses(self, start = 0, end = None):
#     if end == None:
#         end = len(self.maindf)
#     if len(self.maindf) != 0:
#         return self.maindf.loc[start:end]
#     #else:
#         #print("No data yet")

def export_expenses(df, newfilename):
    #filename = input("Name the exported file: ")
    export_data = df.to_csv(newfilename)
    return export_data

def delete_expenses(df, whichrow):
    #try:
        #whichrow = int(input("Which row number you would like to delete: "))
        #confirm = input(f'Confirm delete row {whichrow} (y/n): ')
        #if confirm == "y":
    df = df.drop(whichrow)
    df = df.reset_index(drop=True)
        #else:
            #print("deletion cancelled")#
    #except Exception as e:
        #print(e)
    return df








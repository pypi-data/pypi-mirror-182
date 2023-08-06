# importing the moduels of this package

import store_data as sd
import categorize_data as cd

filename = "statement.csv"

# creting a object
base_df = sd.Expenses()

# add the csv file
base_df.add_csv(filename) 

# show all expenses
df = base_df.show_expenses()

# categorize all the expenses

# define categories in a dictionary
catlist = {1:"groceries", 2:"dining out", 3:"household", 4:"clothing", 5:"misc"}
# define an empty dictionary - so you don't have to categorize the same expense again
dict_cat_shop = {}
#call the funciton
cd.categorize_all(df, catlist, catlist)
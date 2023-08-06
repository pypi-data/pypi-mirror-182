# Expense-Tracker-and-Analysis

[![Release][release-shield]][release-url]
[![Forks][forks-shield]][forks-url]
[![Downloads][downloads-shield]][downloads-url]
[![Stargazers][stars-shield]][stars-url]
[![MIT License][license-shield]][license-url]

<!-- MARKDOWN LINKS & IMAGES -->
[release-shield]: https://img.shields.io/github/v/release/sahaavi/Expense-Tracker-and-Analysis.svg?style=flat-square
[release-url]: https://github.com/sahaavi/Expense-Tracker-and-Analysis/releases
[forks-shield]: https://img.shields.io/github/forks/sahaavi/Expense-Tracker-and-Analysis.svg?style=flat-square
[forks-url]: https://github.com/sahaavi/Expense-Tracker-and-Analysis/network/members
[downloads-shield]: https://img.shields.io/github/downloads/sahaavi/Expense-Tracker-and-Analysis/total.svg?style=flat-square
[downloads-url]: https://github.com/sahaavi/Expense-Tracker-and-Analysis
[stars-shield]: https://img.shields.io/github/stars/sahaavi/Expense-Tracker-and-Analysis.svg?style=flat-square
[stars-url]: https://github.com/sahaavi/Expense-Tracker-and-Analysis/stargazers
[license-shield]: https://img.shields.io/github/license/sahaavi/Expense-Tracker-and-Analysis.svg?style=flat-square
[license-url]: https://github.com/sahaavi/Expense-Tracker-and-Analysis/blob/master/LICENSE

[![Build Status](https://app.travis-ci.com/sahaavi/Expense-Tracker-and-Analysis.svg?branch=main)](https://app.travis-ci.com/sahaavi/Expense-Tracker-and-Analysis)


- Package pypi link: [exptatd]

[exptatd]: https://pypi.org/project/exptatd/

# Package: ExpenseTrackerAndAnalysis 

This package is best used via the run.py file as an application. It will help users who want to get some insights into their spending habits from their credit card statements. This package will help them add expenses, categorize them, and aggregate them in different ways. To see how to run individual subpackages, inspect the driver.py. There is a sample csv file available. 

## Sub-Package: data

### Module1: store_data

- add_csv: Adds a csv file [only td bank credit card statement in csv format is supported] to the dataframe. Arguments: filename
- add_expenses: add individual expense to dataframe. Arguments: category list [default], user_date, user_shopname, user_amount, user_category
- show_expenses: prints out all the expenses so the user can see it. Arguments: Default arguments are row index start = 0 and row index end = length of dataframe
- export_expenses: export the expenses into a new csv file. Arguments: newfilename
- delete_expenses: deletes a specific expense according to which row index. Argument: whichrow

### Module2: categorize_data

- categorize_all: iterates over every item in the datafram that doesn't already have a category, prompting user to choose a category. Arguments: df, catlist(default), dict_cat_shop(default)
- categorize_item: Categorize a specific expense according to name or row index, prompts user. Arguments: df, catlist, dict_cat_shop
- update_category: Update a category name, prompts user. Arguments: df, catlist, dict_cat_shop
- add_category: Add a category, prompts user. Arguments: catlist

## Sub-Package: analysis

### Module1: search

- search_date: shows transactions from a user inputed day/month/year
- search_category: shows transactions from user input category
- search_amount: shows transactions from user input range of spending amount

### Module2: analysis

- total_expense: returns the total expenses. Arguments: df
- income_expense_ratio: shows the user the ratio of their spending vs their income. Arguments: income
- category_percentage: shows the percentage of every category in total expenses. No arguments
- category_average: outputs the monthly averages of every category over a specified range of months. No arguments.


from tdexpta.data import store_data as sd
from tdexpta.data import categorize_data as cd
from tdexpta.analysis.search import Search as s
from tdexpta.analysis.analysis import Analysis as a

def main():
    #catlist = {1:"groceries", 2:"dining out", 3:"household", 4:"clothing", 5:"misc"}
    #dict_cat_shop = {}
    n = 1
    input0 = None
    while n == 1:
        print("1: add csv file")
        print("2: add individual expense")
        input0 = input("Choose option: ")
        if input0 == "1":
            filename = input("Enter csv file name to add: ")
            base_df = sd.add_csv(filename)
            if 'base_df' in locals():
                n += 1
        elif input0 == "2":
            user_date = input("Enter the date (MM/DD/YYYY): ")
            user_shopname = input("Enter the transaction name: ").upper()
            user_amount = float(input("Enter the amount: "))
            print(cd.catlist)
            user_category = cd.catlist.get(int(input("Enter a category: ")))
            base_df = sd.add_expenses(user_date, user_shopname, user_amount, user_category, base_df, cd.catlist)
            if 'base_df' in locals():
                n += 1
        else:
            print("Input a valid choice (1-2)")
        

    while True:
        print("1. Import/Export the data or add expenses.")
        print("2. Categorize the data")
        print("3. Search")
        print("4. Analysis")
        print("Type exit to exit")

        user_input = input("Choose an option: ")

        if user_input == "1":
            input1 = None
            while input1 != "0":
                print("1: add csv file")
                print("2: add individual expense")
                print("3: show expenses")
                print("4: delete expense")
                print("5: export expenses to csv")
                print("0: back")
                input1 = input("Choose an option: ")

                if input1 == "1":
                    filename = input("Enter csv file name to add: ")
                    base_df = sd.add_csv(filename, base_df)

                elif input1 == "2":
                    user_date = input("Enter the date (DD/MM/YYYY): ")
                    user_shopname = input("Enter the transaction name: ").upper()
                    user_amount = float(input("Enter the amount: "))
                    print(cd.catlist)
                    user_category = input("Enter a category: ")
                    base_df = sd.add_expenses(user_date, user_shopname, user_amount, user_category, base_df, cd.catlist)

                elif input1 == "3":
                    print(base_df)

                elif input1 == "4":
                    print(base_df)
                    whichrow = int(input("Which row number you would like to delete: "))
                    base_df = sd.delete_expenses(base_df, whichrow)
                
                elif input1 == "5":
                    newfilename = input("Name the exported file: ")
                    sd.export_expenses(base_df, newfilename)
                
                elif input1 == "0":
                    break

                else:
                    print("Input a valid choice (0-5)")

        if user_input == "2":
            
            input2 = None
            while input2 != "0":
                print("1: categorize all uncategorized expenses")
                print("2: categorize specific expense")
                print("3: update a category name")
                print("4: add a category")
                print("5: show expenses")
                print("0: back")
                input2 = input("Choose an option: ")
                if input2 == "1":
                    cd.categorize_all(base_df, cd.catlist, cd.dict_cat_shop)
                
                elif input2 == "2":
                    #user_shop_name = input('What transaction name would you like to categorize? ').upper()
                    #cd.categorize_item(base_df, user_shop_name, cd.catlist, cd.dict_cat_shop)
                    cd.categorize_item(base_df, cd.catlist, cd.dict_cat_shop)
                elif input2 == "3":
                    print(cd.catlist)
                    try:
                        user_cat = int(input('Which category would you like to rename? (input number) '))
                        user_newcat = input('What do you want to rename it as? ')
                        cd.update_category(base_df, user_cat, user_newcat, cd.catlist, cd.dict_cat_shop)
                    except ValueError:
                        print("Please input a valid number")

                elif input2 == "4":
                    print(cd.catlist)
                    try:
                        new_cat = input('Name of new category: ')
                        cd.add_category(new_cat, cd.catlist)
                    except Exception as e:
                        print(e)

                elif input2 == "5":
                    print(base_df)

                elif input2 == "0":
                    break

                else:
                    print("Input a valid choice (0-5)")
                    
        elif user_input == "3":
            p = s(base_df)
            while True:
                print("1. Search a specific day's transactions")
                print("2. Search transactions from a range of days")
                print("3. Search a month's transactions")
                print("4. Search a year's transactions")
                print("5. Search category")
                print("6. Search category from a range of days")
                print("7. Search amount")
                print("8. Search amount from a range of days")
                print("0. Back to main")
                user_input_s = input("Choose an option: ")
                if user_input_s == "1":
                    date = input("Enter the date (dd/mm/yyyy): ")
                    print(p.search_date(date))
                elif user_input_s == "2":
                    start_date = input("Enter start date (dd/mm/yyyy): ")
                    end_date = input("Enter end date (dd/mm/yyyy): ")
                    print(p.search_range(start_date, end_date))
                elif user_input_s == "3":
                    try:
                        month = int(input("Enter month's number (8 -> Aug): "))
                    except ValueError:
                        print("Please use valid number")
                    except:
                        print(sys.exc_info()[0],"occured.")
                    else:
                        print(p.search_month(month))
                elif user_input_s == "4":
                    year = input("Enter year (yyyy): ")
                    print(p.search_year(year))
                elif user_input_s == "5":
                    print(cd.catlist)
                    cname = cd.catlist.get(int(input("Enter a category: ")))
                    print(p.search_category(cname))
                elif user_input_s == "6":
                    print(cd.catlist)
                    cname = cd.catlist.get(int(input("Enter a category: ")))
                    start_date = input("Enter start date (dd/mm/yyyy): ")
                    end_date = input("Enter end date (dd/mm/yyyy): ")
                    print(p.search_category_range(cname, start_date, end_date))
                elif user_input_s == "7":
                    amount = float(input("Enter the amount: "))
                    print(p.search_amount(amount))
                elif user_input_s == "8":
                    amount = float(input("Enter the amount: "))
                    start_date = input("Enter start date (dd/mm/yyyy): ")
                    end_date = input("Enter end date (dd/mm/yyyy): ")
                    print(p.search_amount_range(amount, start_date, end_date))
                elif user_input_s == "0":
                    break
                else:
                    print("Input a valid choice (0-8)")

        elif user_input == "4":
            start_date = input("Enter start date (dd/mm/yyyy): ")
            end_date = input("Enter end date (dd/mm/yyyy): ")
            j = a(base_df, start_date, end_date)
            while True:
                print("1. Income Expense Ratio from a range of days")
                print("2. Category Percentage")
                print("3. Category Average")
                print("0. Back to main")
                user_input_s = input("Choose an option: ")

                if user_input_s == "1":
                    income = float(input("Enter the income: "))
                    print(j.income_expense_ratio_range(income))
                elif user_input_s == "2":
                    print(j.category_percentage())
                elif user_input_s == "3":
                    print(j.category_average())
                elif user_input_s == "0":
                    break
                else:
                    print("Input a valid choice (0-3)")

        elif user_input == "exit":
            break

if __name__ == '__main__':
    main()

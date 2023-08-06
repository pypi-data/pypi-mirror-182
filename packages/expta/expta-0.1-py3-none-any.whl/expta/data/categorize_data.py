import pandas as pd

catlist = {1:"groceries", 2:"dining out", 3:"household", 4:"clothing", 5:"misc"}
dict_cat_shop = {}


def categorize_all(df, catlist = catlist, dict_cat_shop = dict_cat_shop):
    print(catlist)
    for index, row in df.iterrows():
        if len(df.loc[index, 'category']) == 0:
            if df.loc[index, 'shop_name'] in dict_cat_shop:
                df.loc[index, 'category'] = dict_cat_shop.get(df.loc[index, 'shop_name'])
            else:
                print(row['date'], row['shop_name'], row['amount'], row['category'])
                i = int(input("Enter the category: ", ))
                df.loc[index, 'category'] = catlist.get(i)
                dict_cat_shop[df.loc[index, 'shop_name']] = catlist.get(i)

def categorize_item(df, catlist = catlist, dict_cat_shop = dict_cat_shop):
    try:
        name_or_row = input('Would you like to categorize a specific transaction name or a specific row (t/r): ')
        if name_or_row == 't':
            # update the category in the dataframe
            # update dict_cat_shop shop_name : new category
            user_shop_name = input('What transaction name would you like to categorize? ').upper()
            if df['shop_name'].str.contains(user_shop_name).any():
                print('We have a match')
                df_contains = df[df['shop_name'].str.contains(user_shop_name)]
                print(df_contains)
                confirm = input("Confirm selection for categorizing (y/n): ")
                if confirm == 'y':
                    print(catlist)
                    i = int(input("Enter the category: ", ))
                    print(f'Updating the category to {catlist.get(i)}')
                    for index, row in df_contains.iterrows():
                        df.loc[index, 'category'] = catlist.get(i) # index is same as main dataframe
                        dict_cat_shop[df.loc[index, 'shop_name']] = catlist.get(i) # in case that str.contains shows items with diff names
                else:
                    print("Categorizing cancelled")
            else:
                print('No match')
        elif name_or_row == 'r':
            # update the category in the dataframe
            # does not update the dictionary shop_name
            user_show = input("Would you like to see the dataframe (y/n): ")
            if user_show == 'y':
                print(df)
            user_row = int(input("Which row would you like to categorize (input number): "))
            print(df.loc[[user_row]])
            confirm = input("Confirm selection for categorizing (y/n): ")
            if confirm == 'y':
                print(catlist)
                i = int(input("Enter the category: ", ))
                print(f'Updating the category of line {user_row} to {catlist.get(i)}')
                df.loc[user_row, 'category'] = catlist.get(i)
            else:
                print("Categorizing cancelled")
        else:
            print('Please input t (transaction name) or r (row number). Edit cancelled.')
    except Exception as e:
                print(e)

def update_category(df, user_cat, user_newcat, catlist = catlist, dict_cat_shop = dict_cat_shop):
    """ Renames a category

    Parameters:
    df: dataframe where changes will apply
    user_cat: index indicating which category to rename, refers to key in catlist
    user_newcat: new name for category
    catlist: (default catlist) dictionary of categories in format index:name
    dict_cat_shop: (default dict_cat_shop) dictionary in format shop_name:category
    """
    try:
        #print(catlist)
        #user_cat = int(input('Which category would you like to rename? (input number) '))
        #user_cat = int(user_cat)
        #user_newcat = input('What do you want to rename it as? ')
        #print(f'Renaming {catlist.get(user_cat)} as {user_newcat}')
        #confirm = input("Confirm renaming (y/n): ")
        #if confirm == 'y':
        _shop_name = {i for i in dict_cat_shop if dict_cat_shop[i]==catlist[user_cat]} # get keys that are affected
        # this gives a set of all keys ie shop_names that have that category
        for shop in _shop_name:
            dict_cat_shop[shop] = user_newcat # rename for affected keys
        for index, row in df.iterrows(): # rename in dataframe
            if df.loc[index, 'category'] == catlist[user_cat]:
                df.loc[index, 'category'] = user_newcat
        catlist[user_cat] = user_newcat # renames in list
        #else:
            #print("Cancelling renaming")
    except Exception as e:
        print(e)

def add_category(new_cat, catlist = catlist):
    #print(catlist)
    #new_cat = input('Name of new category: ')
    if not isinstance(new_cat, str):
        print("error: input a string name")
    elif new_cat in catlist.values():
        print(new_cat, "is already a category")
    else:
        catlist[len(catlist)+1] = new_cat

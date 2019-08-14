#%%
import pandas as pd 
import numpy as np 
import os

#%%
file_location = os.path.join('routes_and_structures_excel','ECO00032-01-V9_Summary_Rpt.xlsx')
df = pd.read_excel(file_location, skiprows=1)


#%%
df.rename(columns={'Unnamed: 3':'Child Item Decr'}, inplace=True)
df = df.where(~df.isnull().all(axis=1), df.fillna('BREAK'))
df

#%%
item_dict = {}
item_count = 0
for index, row in df.iterrows():
    
    change_tag_list = ['New Parts', 'Revised Parts', 'Obsolete Parts', 'Technical Publications Parts']
    if row['Item #'] in change_tag_list:
        pass
    elif row['Item #'] == 'BREAK':
        print()
        print('New Item Start', index)
        
        item_count += 1
        print()
        
    else:
        items = {col:row[col] for col in df.columns}
        item_dict[item_count] = items

    print(item_dict)
        # rs = [{col: row[col]} for col in df.columns]
        # print(len(rs))
        # print(rs)


#%%

df.to_dict('index')

#%%
df = pd.DataFrame([{'c1':10, 'c2':100}, {'c1':11,'c2':110}, {'c1':'BREAK','c2':'BREAK'}, 
                    {'c1':12,'c2':120}, {'c1':'BREAK','c2':'BREAK'}, {'c1':10, 'c2':100}])
df
#%%
count_index = 0
def make_value_lists(df, count_index):

    
    df_indexed = df.iloc[count_index:,:]

    for index, row in df_indexed.iterrows():
        if count_index >= 214:
            break

        if row['Item #'] == 'BREAK':
            print('New Item Start', index)
            count_index = index + 1
            print(count_index)
            make_value_lists(df, count_index)
        else:
            rs = [{col: row[col]} for col in df.columns]
            # print(len(rs))
            print(rs)

make_value_lists(df, count_index)

#%%
print(df.shape[0])

#%%

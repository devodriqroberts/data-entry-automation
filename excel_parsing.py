#%%
import pandas as pd 
import numpy as np 

#%%
file_location = r'\\txt.textron.com\tsv\Projects\Current Projects\100066 Misc-Advanced Concepts\Text_File_Processing_Scripts\sap_auto_part_entry_erin_amerson_move_this\xml_parsing\routes_and_structures_excel\ECO00032-01-V9_Summary_Rpt.xlsx'
df = pd.read_excel(file_location, skiprows=1)


#%%
df.rename(columns={'Unnamed: 3':'Child Item Decr'}, inplace=True)
df = df.where(~df.isnull().all(axis=1), df.fillna('BREAK'))
df

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

#%%
import pandas as pd 
import numpy as np
import xml.etree.ElementTree as et 
import os 
import pprint
from xml_preprocessing import Preprocess_xml

#%%
DATA_LOCATION = r'/Users/devodriqroberts/Desktop/Software-Development/python/xml_parsing/xml_sample_entry'
# DATA_LOCATION = r'\\txt.textron.com\tsv\Projects\Current Projects\100066 Misc-Advanced Concepts\Text_File_Processing_Scripts\sap_auto_part_entry_erin_amerson_move_this' 
FILE = 'xml_sample_entry.xml'
FILE2 = 'xml_sample_entry2.xml'
FILE3 = 'xml_sample_entry3.xml'

xml_txt_file = r'/Users/devodriqroberts/Desktop/Software-Development/python/xml_parsing/xml_txt/ECO00032-01_A_V9.txt'

# xml_file = os.path.join(os.path.join(DATA_LOCATION, FILE3))
clean_xml = Preprocess_xml().return_processed_xml(xml_txt_path=xml_txt_file)

# file = xml_file.readlines()
# file = [line.replace('&','&amp;') for line in xml_file]

# xtree = et.parse(xml_file)
# xroot = xtree.getroot()

xroot = et.fromstring(clean_xml)


#%%
def base(item, i):
    '''
    Return base nested dictionary of item attributes, plant and bom items
    with keys: 'bom' (nested dict), 'comments', 'is_srv_only', 'is_tc_only', 'item_id',
    'name', 'plant' (nested dict), 'rev_id', and 'uid'.

    Ex:
        {'bom': {},
        'comments': '',
        'is_srv_only': 'false',
        'is_tc_only': 'false',
        'item_id': '20271G12',
        'name': 'HOLE PLUG,1.187"',
        'plant': {},
        'rev_id': 'A',
        'uid': 'zLFASW1pVdWWHBAAAAAAAAAAAAA'}
    '''

    # Initialize Item, BOM Item, and Plant Item dictionaries as empty dict.
    item_dict = {}
    child_dict_bom = {}
    plant_dict = {}

    # Add Item attributes to Item dictionary.
    item_dict = item.attrib

    # Loop through Item object to find any children (BOM). Add to child dict.
    for j, child_item in enumerate(item.findall('ItemChild')):

        # Add child attributes to child bom dict with incremental key 'j'.
        child_dict_bom[j] = child_item.attrib

    # Add child dict to Item dict with key 'bom'.
    item_dict['bom'] = child_dict_bom

    # Loop through Item object to find any plant objects. Add to plant dict.
    for k, plant in enumerate(item.findall('Plant')):

        # Add Plant attributes to plant dictionary.
        plant_dict_items = plant.attrib

        # Add additional Plant information to plant dictionary.
        plant_dict_items['plant_setup'] = plant.find('PlantSetup').text
        plant_dict_items['proc_type'] = plant.find('ProcType').text
        plant_dict_items['item_category'] = plant.find('ItemCategory').text
        plant_dict_items['item_sequence'] = plant.find('ItemSequence').text
        plant_dict_items['line_sequence'] = plant.find('LineSequence').text
        plant_dict_items['unit_of_measure'] = plant.find('UOM').text 
        plant_dict_items['commodity'] = plant.find('Commodity').text

        # Add plant attributes dict to plant dict with incremental key 'k'.
        plant_dict[k] = plant_dict_items

    # Add plant dict to Item dict with key 'plant'.
    item_dict['plant'] = plant_dict
        
    # Return Item Dictionary    
    return item_dict


def parse_change_tag(change_tag, item_dict):
    # Loops through items under change tags.
    for item in xroot.findall(change_tag):

        # Loops to find all 'ItemRev' (item tags) and enumerates.
        for i, item_rev in enumerate(item.findall('ItemRev')):
            
            # Adds item base attributes dict to obs_items dict 
            # with enumerated key 'i.
            item_dict[i] = base(item_rev, i)
        return item_dict



#%%
def parse_xml_routes_structure():
    
    # Loops through xml tree for change type tags.
    for change_type in xroot:

        # Condition if change tags are 'Add' (new items).
        if change_type.tag == 'Add':

            # Initialize empty dictionary for new items.
            add_items = {}
            add_items = parse_change_tag(change_type.tag, add_items)

            # Loops through items under change tags.
            # for item in xroot.findall(change_type.tag):

            #     # Loops to find all 'ItemRev' (item tags) and enumerates.
            #     for i, item_rev in enumerate(item.findall('ItemRev')):

            #         # Adds item base attributes dict to add_items dict 
            #         # with enumerated key 'i.
            #         add_items[i] = base(item_rev, i)


        # Condition if change tags are 'Change' (revised items).
        if change_type.tag == 'Change':
    
            # Initialize empty dictionary for revised items.
            change_items = {}
            # change_items = parse_change_tag(change_type.tag, change_items)
            
            # Loops through items under change tags.
            for item in xroot.findall(change_type.tag):

                # Loops to find all 'ItemRev' (item tags) and enumerates.
                for i, item_rev in enumerate(item.findall('ItemRev')):

                    # Initialize empty dictionary for revised child items.
                    rev_change_child_items = {}

                    # Adds item base attributes dict to add_items dict 
                    # with enumerated key 'i.
                    change_items[i]= base(item_rev, i)
                    

                    # Loop to find all tags of Revised Item bom.
                    for k, rev_child in enumerate(item_rev.findall('ItemRevChild')):
                        
                        # Initialized empyt dict for items removed in items revision.
                        rem_change_child_items = {}

                        # Loop to find all tags of removed items of revised item.
                        for m, rem_child in enumerate(rev_child.findall('ItemRevRem')):

                            # Adding enumerated removed items to removed items dictionary.
                            rem_change_child_items[m] = rem_child.attrib

                            # Adding removed items dictionary to revised item dictionary with key 'rem'.
                            rev_child.attrib['rem'] = rem_change_child_items

                        # Adding enumerated revised items to revised items dictionary.
                        rev_change_child_items[k] = rev_child.attrib

                        # Add revised item child item dict to change_items dict with key 'rev'.
                        change_items[i]['rev'] = rev_change_child_items

        
        # Condition if change tags are 'Obsolete'.
        if change_type.tag == 'Obsolete':

            # Initialize empty dictionary for obsolete items.
            obs_items = {}
            obs_items = parse_change_tag(change_type.tag, obs_items)

            # # Loops through items under change tags.
            # for item in xroot.findall(change_type.tag):

            #     # Loops to find all 'ItemRev' (item tags) and enumerates.
            #     for i, item_rev in enumerate(item.findall('ItemRev')):
                    
            #         # Adds item base attributes dict to obs_items dict 
            #         # with enumerated key 'i.
            #         obs_items[i] = base(item_rev, i)

            



    r_and_s = {}
    r_and_s['Add'] = add_items
    r_and_s['Change'] = change_items
    r_and_s['Obsolete'] = obs_items

    return r_and_s
    # return add_items, change_items

#%%
pprint.pprint(parse_xml_routes_structure()['Add'])


#%%


# import re

# xml_txt_path = r'/Users/devodriqroberts/Desktop/Software-Development/python/xml_parsing/xml_txt/ECO00032-01_A_V9.txt'

# def search_space_ampersand(string):
#     amp = re.sub(r'\s*[&]\s*|(<=\w*)[&](?=\w*)', ' &amp; ', string)
#     if amp:
#         return amp #string.replace(amp.group(0), ' &amp; ')

#     return string

# def search_dash(string):
#     dash = re.sub(r'-<', '<', string)
#     if dash:
#         return dash #string.replace(dash.group(0), '<')

#     return string


# def search_nested_quote(string):
#     route = re.search(r'(?<=[,])ROUTE 1(?=[\s\",])', string)
#     if not route:

#         frac_regex = r'(?<=\/\d)\"(?=[\s\",])'
#         dec_regex = r'(?<=\.\d\d)\"(?=[\s\",])|(?<=\.\d)\"(?=[\s\",])'
#         inch_regex = r'(?<=\s\d\d)\"(?=[\s\",])'
#         name_sub_string_regex = r'(?<=name=)(\".*?\")(?=\sitem_id)'

#         sub = re.search(name_sub_string_regex, string)
#         quot = ''
#         if sub:
#             fixed_content = re.sub(f'{frac_regex}|{dec_regex}|{inch_regex}', '&quot;', sub.group(0))

#             quot = re.sub(name_sub_string_regex, fixed_content, string)

        
#         if quot:
#             return quot #string.replace(quot.group(0), '&quot;')
        
#     return string 


# clean_xml = ''
# with open(xml_txt_path, 'r') as xml:
#     for line in xml.readlines():
#         line = search_dash(line)
#         line = search_space_ampersand(line)
#         line = search_nested_quote(line)
#         clean_xml += line
        
# print(clean_xml)

#%%

x = et.fromstring(clean_xml)
print(x.iter())

#%%
content = '<ItemRevChild uid="SNCAAe9qVdWWHBAAAAAAAAAAAAA" rev_id="E" name="TRIM, VINYL - 6.25"" item_id="32372G6" qty="1" action="Added"/>'
# content = re.sub(r'\s*[&]\s*|(<=\w*)[&](?=\w*)', ' &amp; ', content)
# content = re.sub(r"^[^*$<,>?!\"]",'quot', content)

# content = re.sub(r'(?<=\s\d\d)\"(?=[\s\",])', 'quot', content)
# content = re.sub(r'(?<=\/\d)\"(?=[\s\",])', 'quot', content)
# content = re.sub(r'(?<=\.\d\d)\"(?=[\s\",])', 'quot', content)

# content = re.search(r'(?<=[,])ROUTE 1(?=[\s\",])', content)

# sub = re.search(r'(?<=name=)(\".*?\")(?=\sitem_id)', content)
# fixed_content = re.sub(r'(?<=\.\d\d)\"(?=[\s\",])', 'quot', sub.group(0))

# content = re.sub(r'(?<=name=)(\".*?\")(?=\sitem_id)', fixed_content,content)
# print(sub)

# print(content)
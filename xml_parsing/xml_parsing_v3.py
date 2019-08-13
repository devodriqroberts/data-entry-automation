#%%
import pandas as pd 
import numpy as np
import xml.etree.ElementTree as et 
import os 
import pprint
from glob import glob
from xml_preprocessing import Preprocess_xml

#%%
## USED FOR NON-ITERATIVE TESTS *************************

# DATA_LOCATION = r'/Users/devodriqroberts/Desktop/Software-Development/python/xml_parsing/xml'
# DATA_LOCATION = r'\\txt.textron.com\tsv\Projects\Current Projects\100066 Misc-Advanced Concepts\Text_File_Processing_Scripts\sap_auto_part_entry_erin_amerson_move_this' 
# FILE = 'xml_sample_entry.xml'
# FILE2 = 'xml_sample_entry2.xml'
# FILE3 = 'xml_sample_entry3.xml'

# xml_file = os.path.join(os.path.join(DATA_LOCATION, FILE3))

# xtree = et.parse(xml_file)
# xroot = xtree.getroot()

## USED FOR NON-ITERATIVE TESTS *************************

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
    for child_item in item.findall('ItemChild'):
        
        if ('type', 'Chart') in child_item.attrib.items():
            item_dict['chart'] = child_item.attrib

    # Loop through Item object to find any children (BOM). Add to child dict.
    for j, child_item in enumerate(item.findall('ItemRevChild')):

        # Initialized empyt dict for items removed in items revision.
        rem_change_child_items = {}

        # Loop to find all tags of removed items of revised item.
        for m, rem_child in enumerate(child_item.findall('ItemRevRem')):

            # Adding enumerated removed items to removed items dictionary.
            rem_change_child_items[m] = rem_child.attrib

            # Adding removed items dictionary to revised item dictionary with key 'rem'.
            child_item.attrib['rem'] = rem_change_child_items

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


def parse_change_tag(change_tag, item_dict, root):
    # Loops through items under change tags.
    for item in root.findall(change_tag):

        # Loops to find all 'ItemRev' (item tags) and enumerates.
        for i, item_rev in enumerate(item.findall('ItemRev')):
            
            # Adds item base attributes dict to obs_items dict 
            # with enumerated key 'i.
            item_dict[i] = base(item_rev, i)
        return item_dict



#%%
def parse_xml_routes_structure(root):
    
    # Loops through xml tree for change type tags.
    for change_type in root:

        # Condition if change tags are 'Add' (new items).
        if change_type.tag == 'Add':

            # Initialize empty dictionary for new items.
            add_items = {}
            add_items = parse_change_tag(change_type.tag, add_items, root)

        # Condition if change tags are 'Change' (revised items).
        if change_type.tag == 'Change':
    
            # Initialize empty dictionary for revised items.
            change_items = {}
            # change_items = parse_change_tag(change_type.tag, change_items)
            
            # Loops through items under change tags.
            for item in root.findall(change_type.tag):

                # Loops to find all 'ItemRev' (item tags) and enumerates.
                for i, item_rev in enumerate(item.findall('ItemRev')):

                    # Initialize empty dictionary for revised child items.
                    # rev_change_child_items = {}

                    # Adds item base attributes dict to add_items dict 
                    # with enumerated key 'i.
                    change_items[i]= base(item_rev, i)
                    
        
        # Condition if change tags are 'Obsolete'.
        if change_type.tag == 'Obsolete':

            # Initialize empty dictionary for obsolete items.
            obs_items = {}
            obs_items = parse_change_tag(change_type.tag, obs_items, root)


    r_and_s = {}
    r_and_s['Add'] = add_items
    r_and_s['Change'] = change_items
    r_and_s['Obsolete'] = obs_items

    return r_and_s

#%%

def loop_xml_files(folder_path):
    processor = Preprocess_xml()

    if 'xml' in folder_path:
        file_path = os.path.join(folder_path, '*.xml')
        for xml_file in glob(file_path):
            
            xtree = et.parse(file_path)
            xroot = xtree.getroot()
            
            # TODO: Automation SAP script

            pprint.pprint(parse_xml_routes_structure(xroot))
            print()
            print('#'*10)
            print()


    if 'txt' in folder_path:
        file_path = os.path.join(folder_path, '*.txt')
        for xml_file in glob(file_path):
            
            xroot = et.fromstring(processor.return_processed_xml(xml_file))
            
            # TODO: Automation SAP script

            print(len(parse_xml_routes_structure(xroot)['Add']))
            for i in range(len(parse_xml_routes_structure(xroot)['Add'])):

                print(parse_xml_routes_structure(xroot)['Add'][i].keys())

            pprint.pprint(parse_xml_routes_structure(xroot)['Add'])
            print()
            print('#'*10)
            print()

    
    if 'excel' in folder_path:
        file_path = os.path.join(folder_path, '*.xlsx').strip()
        for xml_file in glob(file_path):
            
            xtree = et.parse(file_path)
            xroot = xtree.getroot()
            
            # TODO: Automation SAP script

            # print(type(parse_xml_routes_structure(xroot)))
            pprint.pprint(parse_xml_routes_structure(xroot))
            print()
            print('#'*10)
            print()

#%%
# path = '/Users/devodriqroberts/Desktop/Software-Development/python/xml_parsing/xml_txt/*.txt'
folder_path = 'routes_and_structures_xml'
loop_xml_files(folder_path)


#%%
# xmlstr = et.tostring(xroot, encoding='utf8', method='xml')
# print(xmlstr)

# xml_from_str = et.fromstring(xmlstr)
# print(xml_from_str)
# print(xroot)

    
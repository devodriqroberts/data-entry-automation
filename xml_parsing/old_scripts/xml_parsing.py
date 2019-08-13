#%%
import pandas as pd 
import numpy as np
import xml.etree.ElementTree as et 
import os 

#%%
DATA_LOCATION = r'/Users/devodriqroberts/Desktop/Software-Development/python/xml_parsing/xml_sample_entry'
FILE = 'xml_sample_entry.xml'

xtree = et.parse(os.path.join(DATA_LOCATION, FILE))
xroot = xtree.getroot()

#%%
print(xroot.tag)
# ChangeSum

#%%
print(xroot.attrib)

'''
{}
'''
#%%
for child in xroot:
    print(child.tag, child.attrib)
    print()
    '''
    >> 
        Add {}
        Change {}
        Obsolete {}
        Techpub {}
        Error {}
    '''
    if child.tag == 'Add':
        for subChild in child:
            print(subChild.tag, subChild.attrib)
            print()

            for subSubChild in subChild:
                print(subSubChild.tag, subSubChild.attrib)
                print()

                for subSubSubChild in subSubChild:
                    print(subSubSubChild.tag, subSubSubChild.attrib)
                    print()

#%%
tag_list = [element.tag for element in xroot.iter()]
tag_list

#%%
for plant in xroot.iter('Plant'):
    print(plant.attrib)


# #%%
# items = {}
# item = {}
# for child in xroot:
#     print(child.tag, child.attrib)
#     print()
#     '''
#     >> 
#         Add {}
#         Change {}
#         Obsolete {}
#         Techpub {}
#         Error {}
#     '''
#     if child.attrib == {}:
        
#         print(len(list(xroot[0])))
#         if child.tag == 'Add':
            
#             # print(list(element.tag for element in child.iter()))
#             '''
#             ['Add', 'ItemRev', 'Plant', 'PlantSetup', 'ProcType', 
#             'ItemCategory', 'ItemSequence', 'LineSequence', 'UOM', 
#             'Commodity', 'ItemChild', 'ItemRev', 'Plant', 'PlantSetup', 
#             'ProcType', 'ItemCategory', 'ItemSequence', 'LineSequence', 
#             'UOM', 'Commodity', 'ItemChild']
#             '''
#             # print(child.attrib.get('ItemRev'))

#             for i, subChild1 in enumerate(child):
#                 # print(subChild1.tag, subChild1.attrib)
#                 # print(len(subChild1.attrib))
#                 # item_rev_dict = subChild1.attrib
#                 print(i)
#                 if subChild1.tag in tag_list:
#                     item[subChild1.tag] = subChild1.attrib

#                     for subChild2 in subChild1:
#                         item[subChild2.tag] = subChild2.attrib


                # print()
                

                # '''
                # ItemRev {'uid': 'DuJAiCMLVdWWHBAAAAAAAAAAAAA', 
                #         'rev_id': 'A', 
                #         'name': 'BRKT,TUBE,BG', 
                #         'item_id': '10002738', 
                #         'is_tc_only': 'false', 
                #         'is_srv_only': 'false', 
                #         'comments': ''}

                # ItemRev {'uid': 'EdMAiCMLVdWWHBAAAAAAAAAAAAA', 
                #         'rev_id': 'A', 
                #         'name': 'PLATE,FRAME,FRNT,CNPY', 
                #         'item_id': '10002763', 
                #         'is_tc_only': 'false', 
                #         'is_srv_only': 'false', 
                #         'comments': ''}

                # '''
                
                # for subChild2 in subChild1:
                #     print(subChild2.tag, subChild2.attrib)
                #     plant_dict = subChild2.attrib
                #     # print(subChild2.attrib.get('ItemChild'))
                #     print()
                #     item_revs.append(plant_dict)
                #     '''
                #     ItemRev {'uid': 'DuJAiCMLVdWWHBAAAAAAAAAAAAA', 
                #             'rev_id': 'A', 
                #             'name': 'BRKT,TUBE,BG', 
                #             'item_id': '10002738', 
                #             'is_tc_only': 'false', 
                #             'is_srv_only': 'false', 
                #             'comments': ''}

                #         #
                #         Plant {'isService': 'false', 
                #                 'isObs': 'false', 
                #                 'id': '6000'}

                #         ItemChild {'uid': 'SGJAxhMtVdWWHBAAAAAAAAAAAAA', 
                #                     'name': 'BN-SHEET STEEL,HSLA,A1011,7GA', 
                #                     'item_id': '649272', 
                #                     'comments': 'Materials/Finish', 
                #                     'type': 'Material'}

                #     ItemRev {'uid': 'EdMAiCMLVdWWHBAAAAAAAAAAAAA', 
                #             'rev_id': 'A', 
                #             'name': 'PLATE,FRAME,FRNT,CNPY', 
                #             'item_id': '10002763', 
                #             'is_tc_only': 'false', 
                #             'is_srv_only': 'false', 
                #             'comments': ''}

                #         Plant {'isService': 'false', 
                #                 'isObs': 'false', 
                #                 'id': '6000'}

                #         ItemChild {'uid': 'AFABs2cwVdWWHBAAAAAAAAAAAAA', 
                #                     'name': 'SHEET STEEL 7 GA. H.R.S. BN', 
                #                     'item_id': '10875GXX', 
                #                     'comments': 'Materials/Finish', 
                #                     'type': 'Material'}
                #     '''

                #     for subChild3 in subChild2:
                #         print(subChild3.tag, subChild3.attrib)
                #         # print(subChild3.attrib.get('ItemChild'))
                #         print()

                #         # for subChild4 in subChild3:
                #         #     print(subChild3.tag, subChild3.attrib)
                #         #     print()

#%%
# print(item)

#%%
item = {}
items = {}
for child in xroot:
    if child.tag == 'Add':
        # print(list(enumerate(child.iter('ItemRev').tag)))
        
        for i, element in enumerate(child.iter('ItemRev')):
        # for element in child.iter('ItemRev'):
            # print(element.tag, element.attrib)
            tag = f'{element.tag}{i}'
            item[tag] = element.attrib
            print()

            # for i, element in enumerate(child.iter('Plant')):
            for element in child.iter('Plant'):
                # print(element.tag, element.attrib)
                tag = f'{element.tag}{i}'
                item[tag] = element.attrib
                
                print()

                text_list = ['PlantSetup','ProcType','ItemCategory','ItemSequence',
                            'LineSequence','UOM','Commodity',]
                for ele in text_list:
                    for element in child.iter(ele):
                        # print(element.tag, element.attrib)
                        tag = f'{element.tag}{i}'
                        item[tag] = element.text
                        print()

            items[i] = item
                            

        

        
print(items)

#%%
child_item= {}
items = {}
for item in xroot.findall('Add'):
    for i, item_rev in enumerate(item.findall('ItemRev')):
        child_item= {}

        uid = item_rev.get('uid')
        rev_id = item_rev.get('rev_id')
        name = item_rev.get('name')
        item_id = item_rev.get('item_id')
        is_tc_only = item_rev.get('is_tc_only') 
        is_srv_only = item_rev.get('is_srv_only') 
        comments = item_rev.get('comments')

        for j, child in enumerate(item_rev.findall('ItemChild')):
            child_item[j] = child.attrib

        for plant in item_rev.findall('Plant'):
            isService = plant.get('isService')
            isObs = plant.get('isObs')
            plant_id = plant.get('id')
            plant_setup = plant.find('PlantSetup').text
            proc_type = plant.find('ProcType').text
            item_category = plant.find('ItemCategory').text
            item_sequence = plant.find('ItemSequence').text
            line_sequence = plant.find('LineSequence').text
            unit_of_measure = plant.find('UOM').text 
            commodity = plant.find('Commodity').text

            # for plant_info in plant.findall('Plant'):
            #     isService = plant.get('isService')
            #     isObs = plant.get('isObs')
            #     plant_id = plant.get('id')


        items[i] = {'uid':uid, 'rev_id':rev_id, 'name':name, 'item_id':item_id,
                    'is_tc_only':is_tc_only, 'is_srv_only':is_srv_only, 'comments':comments,
                    'isService':isService, 'isObs':isObs, 'plant_id':plant_id, 'plant_setup':plant_setup,
                    'proc_type':proc_type, 'item_sequence':item_sequence, 'line_sequence':line_sequence,
                    'unit_of_measure':unit_of_measure, 'commodity':commodity, 'bom':child_item}

print(items)
                

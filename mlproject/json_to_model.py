from enum import Enum
import json
from multiprocessing.sharedctypes import Value
from tkinter import W

with open('product/products.json', 'r') as f:
  data = json.load(f)
  
  

    

# Test input JSON object - one class
json_str =  r'''[{
        "clabjectNo":"5",
        "clabject_label":"ComputerDeluxe_ComputerModel_ProductType",
        "name":"ComputerDeluxe",
        "potency":"1",
        "subclassOf": null,
        "instanceOf":"ComputerModel",
        "attributes" : [
            {
                "attributeID":"501",
                "att_name":"name",
                "data_type": "string",
                "potency":"0",
                "value": "PC deluxe"
            },
            {
                "attributeID":"502",
                "att_name":"processor",
                "data_type":"STRING",
                "potency":"0",
                "value": "4.5 GHz"
            },
            {
                "attributeID":"403",
                "att_name":"price",
                "data_type":"Double",
                "potency":"1",
                "value": null
            }
        ]
 }]'''

# read JSON string and convert to native python object      
native_python_obj = json.loads(json_str)
print(native_python_obj) 
             
# ML Model output string

'''
Reads the attributes of the Clabject and returns a model string
Helper function for 
'''
def get_attributes(clabject):
      attribute_str = ''
      for attribute in clabject['attributes']:
            attribute_str = attribute_str + attribute['att_name'] 
            if attribute['data_type'].casefold() == 'string'.casefold() :
                  attribute_str = attribute_str + ' = models.CharField(max_length=255)'+ '\n\t' 
            elif attribute['data_type'].casefold() == 'int'.casefold() or attribute['data_type'].casefold() == 'integer'.casefold():
                  attribute_str = attribute_str + ' = models.IntegerField()' + '\n\t'
            elif attribute['data_type'].casefold() == 'double'.casefold():
                   attribute_str = attribute_str + ' = models.DecimalField(decimal_places=2)' + '\n\t'
            else:
                  attribute_str + '\n'   
                     
      return attribute_str + '\n'     
    
    
# build an ORM string
def create_orm_string(clabject):
    orm_model_str = ''
    for  clabject_name in clabject:
        orm_model_str = orm_model_str + 'class ' + clabject_name['name'] + '(models.Model):' + '\n\t' + get_attributes(clabject_name) 
    return orm_model_str



f_write = open('model_temp.py', 'w')
new_model = create_orm_string(data)
print(new_model)
f_write.write(new_model)
    




'''
class ComputerDeluxe(models.Model):
      name = models.ForeignKey(MLClass, on_delete=models.CASCADE)
    processor = models.CharField(max_length=255)
    price = models.CharField(max_length=50)


'''

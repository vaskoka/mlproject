from enum import Enum
import json


with open('product/products.json', 'r') as f:
  data = json.load(f)

# Test input JSON object - one class
json_str =  r''' {
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
 }'''

# read JSON string and convert to native python object      
native_python_obj = json.loads(json_str)
# print(native_python_obj) 

class Clabject:
       
    def __init__(self,name):
        self.name = name
        
    def get_name(self):
        return self.name
    
    def set_name(self,name):
        if name != None:
           print("I alrady have a name")
        else:
            self.name = name
            
    def set_attribute(self, attribute):
        attributes_list = []
        Attribute.attribute = attribute
        attributes_list.append(attribute)
        
                   
            

  
    
    


# ML Model output string

'''
Reads the attributes of the Clabject and returns a model string
'''
def get_attributes(native_python_obj):
      attribute_str = ''
      for attribute in native_python_obj['attributes']:
            attribute_str = attribute_str + attribute['att_name'] 
            
            if attribute['data_type'].casefold() == 'string'.casefold() :
                  attribute_str = attribute_str + ' = models.CharField(max_length=255)'+ '\n\t' 
            elif attribute['data_type'].casefold() == 'int'.casefold():
                  attribute_str = attribute_str + 'models.DecimalField(..., max_digits=5, decimal_places=2)' + '\n\t'
                  
            elif attribute['data_type'].casefold() == 'double'.casefold():
                   attribute_str = attribute_str + 'models.DecimalField(..., max_digits=5, decimal_places=2)' + '\n\t'
                  
            else:
                  attribute_str + '\n\t'      
      return attribute_str     


# build an ORM string
orm_model_str = 'class ' + native_python_obj['name'] + '(models.Model):' + '\n\t' + get_attributes(native_python_obj) 

print(orm_model_str)


      



'''     
for clabject in data:
      print (clabject, ":", data[clabject])
      for key in clabject:
            print(len(key))
      if len(key) == 1:
              
            print (key, ":", clabject[key])
'''

'''
class ComputerDeluxe(models.Model):
      name = models.ForeignKey(MLClass, on_delete=models.CASCADE)
    processor = models.CharField(max_length=255)
    price = models.CharField(max_length=50)


'''

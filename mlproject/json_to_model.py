import json

# read JSON string and convert to native python object      
with open('product/products.json', 'r') as f:
  data = json.load(f)
      

'''
Reads the attributes of the Clabject and returns a model string
Helper function for 
'''
def get_attributes(clabject):
      attribute_str = ''
      for attribute in clabject['attributes']:
            attribute_str = attribute_str + attribute['att_name'] 
            # String data type
            if attribute['data_type'].casefold() == 'string'.casefold() :
                  attribute_str = attribute_str + ' = models.CharField(max_length=255'+ add_default_value(attribute['value'])+')'+ '\n\t' 
            # Int data type
            elif attribute['data_type'].casefold() == 'int'.casefold() or attribute['data_type'].casefold() == 'integer'.casefold():
                  attribute_str = attribute_str + ' = models.IntegerField('+ add_default_value(attribute['value'])+')' + '\n\t'
            #Double data type
            elif attribute['data_type'].casefold() == 'double'.casefold():
                   attribute_str = attribute_str + ' = models.DecimalField(decimal_places=2, max_digits=9'+ add_default_value(attribute['value'])+')' + '\n\t'
            else:
                  attribute_str + '\n'   
                     
      return attribute_str + '\n'     
'''
Helper function for the the get_attributes class,
takes a value attribute key, checks the value and return String 
'''
def add_default_value(key):
    if key == None:
        return ''
    else : 
        return ',default="' + key +'"'
    
    
'''
    Helper function for create_orm_string,
    implements inheritance to the model.

'''
def implement_inheritance(key):
    if key['subclassOf'] == None and key['instanceOf'] == None:
        return 'models.Model'
    else:
        if key['subclassOf'] == None:
            return key['instanceOf']
        else:
            return key['subclassOf']
    
    

    
# build an ORM string
def create_orm_string(clabject_dict):
    orm_model_str = 'from django.db import models \n\n'
    for  key in clabject_dict:
        orm_model_str = orm_model_str + 'class ' + key['name'] + '('+ implement_inheritance(key) + '):' + '\n\t' + get_attributes(key) 
        if key['potency'] == '0' or int(key['potency']) > 1:
            print (int(key['potency']))
            orm_model_str = orm_model_str + '\tclass Meta(): \n\t\tabstract = True\n\n'
    return orm_model_str


# Write to a file
f_write = open('model_temp.py', 'w')
new_orm = create_orm_string(data)
print(new_orm)
f_write.write(new_orm)
f_write.close
    




'''
class ComputerDeluxe(models.Model):
    name = models.ForeignKey(MLClass, on_delete=models.CASCADE)
    processor = models.CharField(max_length=255)
    price = models.CharField(max_length=50)


'''

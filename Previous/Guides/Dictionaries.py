thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964, "year": 2020}  # "year": 1964 is overwritten (Duplicate values)
print(len(thisdict))   # 3                                                    Note that the values can be of any data type. 
print(type(thisdict))  # <class 'dict'>        #Functions used in other arrays can also usually be used.
                                               #e.g. for n in thisdict

#Accessing the items:
print(thisdict["brand"])        # "Ford"       #Items accessed seperately. Note that the reverse cannot be done
          #OR#
print(thisdict.get("model"))    # "Mustang"

for key in thisdict.keys():        #Do not need to be placed in a list
    print(key)
for value in thisdict.values():    #thisdict = {key1: value1, key2: value2, ...}
    print(value)
for item in thisdict.items():      #Output is in tuple data type, e.g. ('year', 2020)
    print(item)

#Changing the contents
thisdict["colour"] = "red"         #Duplicate keys (not items) cause the respective values to be overwritten.
          #OR#                     #Unexisting items are added.

thisdict.update({"colour":"red"})  #More than one set can be placed. 
del thisdict["year"]   #Only keys to be entered

dict2=thisdict.copy()  #Self-explanatory(?)

#Note: Dictionaries can also be stored in other dictionaries. This is called a nested dictionary.
myfamily = {"child1" : {"name" : "Emil","year" : 2004},"child2" : {"name" : "Tobias","year" : 2007},"child3" : {"name" : "Linus","year" : 2011}}
#          [           (                             )            (                               )            (                              )]
print(myfamily["child2"]["name"])
#More information on nested dictionaries here: [3]
"""
Glossary
‾‾‾‾‾‾‾‾
┌────────────────────────────────────────────────────────────────────────────────────────────────────┐
│Dictionary:       A list/collection of data in key:value pairs that are ordered (as of Python 3.7), │
│                  changeable and does not allow duplicates.                                         │
└────────────────────────────────────────────────────────────────────────────────────────────────────┘  
"""

"""
Acknowledgements
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
1)https://www.w3schools.com/python/python_dictionaries.asp
2)https://www.learnpython.org/en/Dictionaries
3)https://www.programiz.com/python-programming/nested-dictionary
""" 


#from StringIO import StringIO
from lxml import etree
import os
from os.path import join, dirname, abspath

def computations():
    global data_dict
    dir = os.listdir(join(dirname(dirname(abspath(__file__))), os.getcwd())) #GET THE LIST OF ALL XML FILES PRESENT IN THE DIRECTORY
    data_dict = {} #CREATE A DATA DICTIONARY TO STORE UNIQUE DATA

    for doc_name in dir:
        if('.xml' in doc_name): #WHILE TAKING UP ONLY XML FILES DO NOT TAKE UP ANY OTHER FILE OR ELSE XML OBJECT CANNOT BE PARSED
            data_dict[doc_name] = {} #CREATE A SEPARATE DICTIONARY FOR EACH AND EVERY XML DOCUMENT WE TAKE IN TO READ
            doc = etree.parse(doc_name) #PARSE THE DOCUMENT INTO AN XML OBJECT
            root = doc.getroot() #GET THE ROOT OF THE CURRENT XML
            for nodes in root: #ITERATE THROUGH ALL THE SUB NODES IN THE ROOT NODE
                if (nodes.tag != 'AccessRoles'): #IF THE TAG DOES NOT MATCH THE TAG OF THE NODE YOU ARE SEARCHING THEN BYPASS
                    continue
                else:
                    access_roles=nodes
                for accessrole in access_roles : #ONCE YOU GET YOUR NODE ITERATE WITHIN IT'S CHILDREN NODES
                    for allow in accessrole: #TO UNDERSTAND THIS, SEE THE HEIRARCHY OF THE XMLS
                        ad_group = allow.get('name') #GET THE NAME PROPERTY OF THE NODE
                        if(ad_group and '.app.' in ad_group.lower()): #CHECK IF THE NAME IS NOT EMPTY AND DATA MATCHES OUR CRITERIA
                            data_dict[doc_name][ad_group.upper()] = ad_group.upper()

def display():
    for data in data_dict.keys():
        print("****************************************************************")
        print("****************************************************************")
        print("data for environment :" + data)
        for ad in data_dict[data]:
            print(ad)
        print("****************************************************************")
        print("****************************************************************")


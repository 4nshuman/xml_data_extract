#from StringIO import StringIO
from lxml import etree
import os
from os.path import join, dirname, abspath

def clean_string(node_str):
    start_i = len('<author>')
    last_i = node_str.find('</author>')
    return node_str[start_i:last_i]

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
                if (nodes.tag != 'books_hardcopy'): #IF THE TAG DOES NOT MATCH THE TAG OF THE NODE YOU ARE SEARCHING THEN BYPASS
                    continue
                else:
                    hard_copy_books=nodes
                for book in hard_copy_books : #ONCE YOU GET YOUR NODE ITERATE WITHIN IT'S CHILDREN NODES
                    book_id = book.get('id')
                    for element in book: #TO UNDERSTAND THIS, SEE THE HEIRARCHY OF THE XMLS
                        if(element.tag=='author'):
                            author = clean_string(etree.tostring(element))
                            data_dict[doc_name][book_id] = author

def display():
    for data in data_dict.keys():
        print("****************************************************************")
        print("****************************************************************")
        print("Data for file :" + data)
        for ad in data_dict[data]:
            print(ad + " : " +data_dict[data][ad])
        print("****************************************************************")
        print("****************************************************************")


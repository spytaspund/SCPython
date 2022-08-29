from TxColorLib import *
from time import sleep as delay
import codecs

path = ""
text = ""

scptext = '''

   _____  _____   _____  
  / ____|/ ____| |  __ \ 
 | (___ | |      | |__) |
  \___ \| |      |  ___/ 
  ____) | |____ _| |_    
 |_____(_)_____(_)_(_)   Secure, Contain, Python.
                         
                         
'''

def clearDisplay():
    print('\n' * 500)

def openObject():
    path = "ObjectsDB\scp" + scpnum + ".txt"
    text = find(codecs.open(path, "r", "utf_8_sig").read())
    print(text)
    input()

print(scptext)
print("Welcome to S.C.P. foundation! Input a number of an object what you need to view.")
scpnum = input()
clearDisplay()
openObject()

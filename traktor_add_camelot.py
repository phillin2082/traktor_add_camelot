# %%
import argparse
#import xml.etree.ElementTree as et
from lxml import etree
from shutil import copy2
from time import strftime
from sys import exit
from readline import parse_and_bind
parse_and_bind("control-v: paste")

# %%
parser = argparse.ArgumentParser(description='Script to add keys')
parser.add_argument('-f', '--file', help='full path of collection.nml file', required=False)
args = vars(parser.parse_args())

if (args['file'] is not None):
    nml_fullpath = args['file']
else:        
    nml_fullpath = input("Enter full path to collection.nml file: ")

#nml_fullpath = '/data/allscripts-git/python/projects/dev/traktor_add_camelot_package/collection.nml'
#nml_fullpath = r'E:\scripts2-git\python\projects\dev\traktor_add_camelot_package\collection.nml'

def camelot_wheel():
    camelot_wheel = [
        {'traktor_key': 0, 'camelot_key': '08B'},
        {'traktor_key': 1, 'camelot_key': '03B'},
        {'traktor_key': 2, 'camelot_key': '10B'},
        {'traktor_key': 3, 'camelot_key': '05B'},
        {'traktor_key': 4, 'camelot_key': '12B'},
        {'traktor_key': 5, 'camelot_key': '07B'},
        {'traktor_key': 6, 'camelot_key': '02B'},
        {'traktor_key': 7, 'camelot_key': '09B'},
        {'traktor_key': 8, 'camelot_key': '04B'},
        {'traktor_key': 9, 'camelot_key': '11B'},
        {'traktor_key': 10, 'camelot_key': '06B'},
        {'traktor_key': 11, 'camelot_key': '01B'},
        {'traktor_key': 12, 'camelot_key': '05A'},
        {'traktor_key': 13, 'camelot_key': '12A'},
        {'traktor_key': 14, 'camelot_key': '07A'},
        {'traktor_key': 15, 'camelot_key': '02A'},
        {'traktor_key': 16, 'camelot_key': '09A'},
        {'traktor_key': 17, 'camelot_key': '04A'},
        {'traktor_key': 18, 'camelot_key': '11A'},
        {'traktor_key': 19, 'camelot_key': '06A'},
        {'traktor_key': 20, 'camelot_key': '01A'},
        {'traktor_key': 21, 'camelot_key': '08A'},
        {'traktor_key': 22, 'camelot_key': '03A'},
        {'traktor_key': 23, 'camelot_key': '10A'},
    ]
    return (camelot_wheel)


"""
def _nml(nml):    
    timestr = strftime("%Y%m%d-%H%M%S")
    src = nml
    dst = nml + timestr
    copy2(src, dst)    
    print("File is backed up to " + dst)
"""


def copy_nml(nml):
    """Input is full path to file. Backs up file appending timestamp"""
    timestr = strftime("-%Y%m%d-%H%M%S")
    src = nml
    dst = nml + timestr
    copy2(src, dst)    
    return dst

try:
    datafile = copy_nml(nml_fullpath)
except FileNotFoundError:
    print("The file collection.nml was not found")
    exit(1)
except:
    print("An error occurred when reading or writing the file. Check file or permissions")
    exit(1)

tree = etree.parse(datafile, etree.XMLParser(recover=True))
root = tree.getroot()
camelot_wheel = camelot_wheel()
#backup_nml(nml_fullpath)

print("Running...")
entries = list(root.iter('ENTRY'))


for entry in entries:
    #print(entry.tag, entry.attrib)
    try:
        print("Entering key for: " + entry.attrib['TITLE'])
    except:
        pass
    filename = ''
    traktor_key = ''
    key = ''
    if entry.find('LOCATION') is not None:
        filename = entry.find('LOCATION').attrib['FILE']
    if entry.find('MUSICAL_KEY') is not None:
        traktor_key = entry.find('MUSICAL_KEY').attrib['VALUE']
    if entry.find('INFO') is not None:
        if 'KEY' in entry.find('INFO').attrib:
            key = entry.find('INFO').attrib['KEY']
    if (traktor_key):       
        #print(filename)
        #print(traktor_key, key)       
        for camelot_spoke in camelot_wheel:
            if int(traktor_key) == int(camelot_spoke['traktor_key']):
                entry.find('INFO').attrib['KEY'] = camelot_spoke['camelot_key']
                #print(camelot_spoke['traktor_key'], camelot_spoke['camelot_key'])
       
tree.write(datafile)      
print("-------------------")
print("Success!")
print("-------------------")
input("Press Enter to close out this window.")

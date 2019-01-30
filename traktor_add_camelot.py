#import xml.etree.ElementTree as et
from lxml import etree
from shutil import copy2
from time import strftime
#from data import CamelotWheel

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


def backup_nml(nml):
    """Input is full path to file. Backs up file appending timestamp"""
    timestr = strftime("%Y%m%d-%H%M%S")
    src = nml
    dst = nml + timestr
    copy2(src,dst)    
    print("File is backed up to " + dst)

#nml_fullpath = input("Fullpath of collection.nml file\n")

nml_fullpath = '/data/allscripts-git/python/projects/dev/traktor_add_camelot_package/collection.nml'

datafile = nml_fullpath
tree = etree.parse(datafile, etree.XMLParser(recover=True))
root = tree.getroot()
camelot_wheel = camelot_wheel()
backup_nml(nml_fullpath)

print("Writing...")
entries = list(root.iter('ENTRY'))
for entry in entries:
    print(entry.tag, entry.attrib)
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
                print(camelot_spoke['traktor_key'], camelot_spoke['camelot_key'])
       
tree.write(datafile)      
print("Success!")
input("Press Enter to close out this window.")

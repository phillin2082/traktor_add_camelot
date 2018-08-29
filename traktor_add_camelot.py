import xml.etree.ElementTree as et
from shutil import copy2
from time import strftime
from data import CamelotWheel

#for development, comment out at build
#import sys
#cur_dir = r'E:\scripts2-git\python\projects\dev\traktor_add_camelot_package'
#sys.path.append(cur_dir)

nml_fullpath = input("Fullpath of collection.nml file\n")

def backup_nml(nml):
    """Input fullpath to file"""
    timestr = strftime("%Y%m%d-%H%M%S")
    src = nml
    dst = nml + timestr
    copy2(src,dst)    
    print("File is backed up to " + dst)
#%%
#datafile = '/data/allscripts-git/python/projects/dev/traktor-add-camelot/collection-mod.nml'
#datafile = r'E:\scripts2-git\python\projects\dev\traktor_add_camelot_package\collection-mod2.nml'
datafile = nml_fullpath
tree = et.parse(datafile)
root = tree.getroot()
camelot_wheel = CamelotWheel.camelot_wheel()
backup_nml(nml_fullpath)

#%%
print("Writing...")
entries = list(root.iter('ENTRY'))
for entry in entries:
    #print(entry.tag, entry.attrib)
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
print("Success!")
input("Press Enter to close out this window.")


#%%
#mndr feed me diamonds, 11a, 18
#entries[0].find('LOCATION').attrib['FILE']
#entries[0].find('INFO').attrib['KEY']
#entries[0].find('MUSICAL_KEY').attrib['VALUE'] = '19'

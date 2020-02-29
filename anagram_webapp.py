'''
from nltk.corpus import words
word_list = words.words()
print len(word_list)
'''

'''
import urllib.request, json, random
with urllib.request.urlopen("https://www.randomlists.com/data/words.json") as url:
    word_dict = json.loads(url.read().decode())['data']
    
rand_value = random.randrange(1, len(word_dict))
print(word_dict[rand_value])
'''

import os
folder_name = "temp_folder"
try:
    filename = os.listdir(folder_name)[0]
except IndexError:
    print('File not found')
print(filename)
path = folder_name+'/'+filename
filesize = os.path.getsize(folder_name+'/'+filename)
if filesize == 0:
    os.remove(path)


from multiprocessing.sharedctypes import Value
import os
import xml.etree.cElementTree as ET
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from googletrans import Translator
translator = Translator()
import subprocess as sb
from sys import stderr
os.system('cls')
from bs4 import BeautifulSoup
os.chdir('en')
os.chdir('text')


def ls():
    output = sb.check_output(['dir', '/b'], stderr = sb.STDOUT, shell=True)
    output = str(output).replace("\\r","")
    output = str(output).split('\\n')
    output[0] = output[0][2:]
    del output[len(output)-1]
    return output

file_count = 0
say = 0
checked_folders = []
checked_files = []
work = True
first_0 = True
first_1 = True
while True:
    output = ls()
    if len(output) == 0:
        os.chdir('..')
        say = 0
        output = ls()

    i = output[say]
    

    for folder in checked_folders:
        if i == folder:
            if len(output) == say + 1:
                os.chdir('..')
                say = 0
                output = ls()
                i = output[say]
            else:
                say += 1
                i = output[say]
            

    if i.find('.stringtable') != -1:
        

        if i == 'z_end_script.stringtable':
            break

        work = True
        for file in checked_files:
            if file == i:
                work = False
                break

        if work == True:
            file_count += 1
            print('\n[' + str(file_count) + '] ' + i)

            file = open(i,'r',encoding = 'utf-8')
            file_data = file.read()

            soup_data = BeautifulSoup(file_data, "xml")
            
            text = soup_data.find_all('DefaultText') 

        
            for orj in text:
                if orj.text != "":
                    tr = translator.translate(orj.text , src = 'en', dest='tr')
                    file_data = file_data.replace(orj.text, str(tr.text))

            print(file_data)
        
            file.close()

            file = open(i,'w',encoding = 'utf-8')
            file.write(file_data)
            file.close()

            checked_files.append(i)
        
        if len(output) == say + 1:
            os.chdir('..')
            say = 0

        else:
            say += 1
    
    else:
        os.chdir(i)
        if i == 'px2_companions':
            checked_folders.remove("poi")

        elif i == '04_defiance_bay_brackenbury' and first_0 == True:
            checked_files.remove('02_bs_crucible_knight_palace.stringtable')
            first_0 = False 

        elif i == '13_twin_elms_elms_reach' and first_1 == True:
            checked_files.remove('13_cv_glanfathan_elms_locals_01.stringtable')
            first_1 = False 

        elif i == 'game':
            checked_files.clear()
            checked_folders.clear()
            checked_folders.append('conversations')
            

        say = 0
        checked_folders.append(i)

        current_folder = i
        


print('\n\nToplam : ' + str(file_count))

"""
file = open('.\\conversations\\00_dyrwood\\00_bs_celby.stringtable','r',encoding = 'utf-8')

for text in file.readlines():
    if text.find('<DefaultText>') != -1:
        text = text.strip()
        text = text.replace('<DefaultText>','')
        text = text.replace('</DefaultText>','')
        text = text.replace('"','')
        if len(text) != 0:
            print(text)
            tr = translator.translate(text , src = 'en', dest='tr')
            tr_text = str(tr.text)
            print(tr_text)

file.close()
"""
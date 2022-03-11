# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 23:03:26 2021

@author: prawny331
"""

from PIL import Image
import os

#directory structure is simple yet inflexible
#have some parent directory (here, \\textures\\)
#have directory of PNG textures as pointed to in item_old, can be extracted from your .minecraft folder
#something like this
#%APPDATA%\Roaming\.minecraft\libraries\net\minecraft\client\<version>
#can open the .jar in winrar or any other unzipper
#in the .jar navigate to \assets\minecraft\textures\item and take everything
#purely extracting this will leave you with all the clock textures, compass textures and bows and stuff, will need to be removed manually

target_dir = 'OneDrive- Personal\\OneDrive\\textures\\item_old'
output_dir = 'compacteditems' #needs to be some directory in the parent directory
#WARNING: this will overwrite any existing texture and .properties files in this output directory without asking you


os.chdir('C:\\' + str(target_dir)) 

src = Image.open('../srcknot.png') #frame image, in this case the raw frame from knot's civpack
em = Image.open('../base_e.png') #emissive background
#both files in the parent directory

item_list = os.listdir() #get list of all files in the item_old directory

for i in range(0,len(item_list)): #loop through all files

    #opening images 
    im_item = Image.open(str(item_list[i])).convert('RGBA')
    new1 = Image.alpha_composite(src,im_item) #merge em
    new1.save('../' + str(output_dir) + '/compacted_' + str(item_list[i]))
    em.save('../' + str(output_dir) + '/compacted_' + item_list[i].split('.')[0]+ '_e.png')

    #now .properties file contents
    f = open('../' + str(output_dir) + '/' + str(item_list[i].split('.')[0]) + '.properties','w')
    f.write('type=item\n')
    f.write('matchItems=' + str(item_list[i].split('.')[0])+ '\n')
    f.write('texture=compacted/compacted_' + str(item_list[i].split('.')[0])+ '\n')
    f.write('nbt.display.Lore.*=Compacted Item'+ '\n') #change if lore in game is different
    f.close()


#blocks
#more complicated
#two schools of thought here - either render models as 2d using some mod and then apply like a texture as above
#school two is to keep it in the form of a model

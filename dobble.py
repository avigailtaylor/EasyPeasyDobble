#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 23 22:02:50 2025

@author: avigailt
"""
import random
from PIL import Image

cds=[0,1,3,10,14,26]

vocabpics = ["input_pngs/vocab"+str(x+1)+"_pic.png" for x in range(31)]

for i in range(31):
    
    incremented_cds_pics = [vocabpics[(x+i)%31] for x in cds]
    random.shuffle(incremented_cds_pics)
   
    dobble_card = Image.open("dobble_card_outline.png")
    
    # first, picture side
    
    img = Image.open(incremented_cds_pics[0])
    dobble_card.paste(img.rotate(180).resize((170,170)), (400, 400))
    
    img = Image.open(incremented_cds_pics[1])
    dobble_card.paste(img.resize((250, 250)), (300, 120))
    
    img = Image.open(incremented_cds_pics[2])
    dobble_card.paste(img.resize((320, 320)), (600, 250))
    
    img = Image.open(incremented_cds_pics[3])
    dobble_card.paste(img.resize((190, 190)), (250, 680))
    
    img = Image.open(incremented_cds_pics[4])
    dobble_card.paste(img.resize((300, 300)), (75, 380))
    
    img = Image.open(incremented_cds_pics[5])
    dobble_card.paste(img.resize((230, 230)), (575, 650))
    
    dobble_card.save("output_dobble_cards/dobble_card_"+str(i)+".png") 

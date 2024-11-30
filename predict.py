# Import libraries
import pandas as pd
import random
import matplotlib.pyplot as plt
import cv2
import os
from PIL import Image

# Prepare
data_dir = 'D:\\Python\\Tarot_Project\\data\\cards'
data = pd.read_json('D:\\Python\\Tarot_Project\\data\\tarot-images.json')['cards']
data = pd.json_normalize(data)

# Helper function to get a random card element
def get_random_element(card_data, key):
    return card_data[key][random.choice(range(len(card_data[key])))]

# Function to display a single tarot card
def tarot_one_card(name_char, age, rand_num):
    roll = len(name_char.strip()) + age + rand_num
    for i in range(roll):
        index = random.randint(0, 77)  # Random index from 0 to 77    
    
    # Get card details
    card = data.iloc[index]
    name = card['name']
    fortune = get_random_element(card, 'fortune_telling')
    keyword = get_random_element(card, 'keywords')
    light_mean = get_random_element(card, 'meanings.light')
    shadow_mean = get_random_element(card, 'meanings.shadow')
    file = card['img']
    image = Image.open(os.path.join(data_dir, file))
    # Return
    return name, fortune, keyword, light_mean, shadow_mean, image
# Function for a 3-card spread
def tarot_three_card(name_char, age, rand_num):
    roll = len(name_char.strip()) + age + rand_num
    for i in range(roll):
        index = random.sample(range(22), 3)  # Get 3 random Major Arcana cards
        
    # Prepare data for Major Arcana cards
    major_arcana = data[data['arcana'] == 'Major Arcana'][['name', 'fortune_telling', 'img']]
    
    # Get details for each card
    fortune, name, file = [], [], []
    for idx in index:
        card = major_arcana.iloc[idx]
        fortune.append(get_random_element(card, 'fortune_telling'))
        name.append(card['name'])
        file.append(card['img'])
    
    # Display images and results
    times = ['Past', 'Present', 'Future']
    images = [Image.open(os.path.join(data_dir, f)) for f in file]
    
    return times, fortune, name, images

# Function for a Celtic Cross spread (example template)
def tarot_celtic_cross(name_char, age, rand_num):   
    roll = len(name_char.strip()) + age + rand_num
    for i in range(roll):
        index = random.sample(range(78), k=10)
    
    positions = ['Present', 'Challenge', 'Past', 'Future', 'Above', 'Below','Advice', 'External Influences', 'Hopes and Fears', 'Outcome']
    result = {}
    # Lặp qua các vị trí và lấy thông tin từ các lá bài đã rút
    for i, pos in enumerate(positions):
        ind = index[i]
        card = data.iloc[ind]
        
        result[pos] = {
            'name': card['name'],
            'fortune': get_random_element(card,'fortune_telling'),
            'suit': card['suit'],
            'keywords':  get_random_element(card,'keywords'),
            'meanings_light':get_random_element(card,'meanings.light'),
            'meanings_shadow':get_random_element(card,'meanings.shadow'),
            'img': Image.open(os.path.join(data_dir,card['img']))
        }
    
    return result

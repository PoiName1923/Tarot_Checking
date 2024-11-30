# Import library
import pandas as pd
import random
import matplotlib.pyplot as plt
import cv2
import os
# Prepare
data_dir = 'D:\\Python\\Tarot_Project\\data\\cards'
files = os.listdir(data_dir)
data = pd.read_json('D:\\Python\\Tarot_Project\\data\\tarot-images.json')
data = data['cards']
data = pd.json_normalize(data)
# Predict
def tarot_predict():
    index = random.sample(range(78),k = 3)
    fortune = []
    name = []
    file = []
    for i in range(3):
        fortune += [data.loc[index[i],'fortune_telling'][0]]
        name += [data.loc[index[i],'name']]
        file += [data.loc[index[i],'img']]

    times = ['Past','Present','Future']
    f, ax = plt.subplots(1,3,figsize=(16,8))
    print()
    for i in range(3):
        img = cv2.imread(os.path.join(data_dir,file[i]))
        ax[i].imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
        ax[i].set_xticks([])
        ax[i].set_yticks([])
        ax[i].set_title(name[i])
        print(f'Your \033[1m{times[i]}\033[0m is \033[1m{name[i]}.\033[0m \033[1m{fortune[i]}.\033[0m')


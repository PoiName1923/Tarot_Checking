import streamlit as st
from predict import tarot_three_card,tarot_one_card,tarot_celtic_cross


st.title("TAROT FREE HERE")

name_c = st.text_input("Enter your name: ")
age_c = st.number_input("Enter your age:", min_value=1, max_value=120, value=2)
rand_num = st.number_input("Enter random number: ", value = 3)

if name_c and age_c >0 :
    if st.button("Three Cards Telling"):
        times, fortune, name, images = tarot_three_card(name_c, age_c, rand_num)
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.image(images[0], caption=name[0], use_container_width=True)
            st.write(f'Your {times[0]} is {name[0]}.')
            st.write(f'Fortune {fortune[0]}.')
        with col2:
            st.image(images[1], caption=name[1], use_container_width=True)
            st.write(f'Your {times[1]} is {name[1]}.')
            st.write(f'Fortune {fortune[1]}.')
        with col3:
            st.image(images[2], caption=name[2], use_container_width=True)
            st.write(f'Your {times[2]} is {name[2]}.')
            st.write(f'Fortune {fortune[2]}.')
    if st.button("One Cards Telling"):
        name, fortune, keyword, light_mean, shadow_mean, image = tarot_one_card(name_c, age_c, rand_num)
        
        st.image(image, caption=name, use_container_width=True)
        st.write(f'Name: {name}')
        st.write(f'Fortune: {fortune}')
        st.write(f'Keywords: {keyword}')
        st.write(f'Light Meaning: {light_mean}')
        st.write(f'Shadow Meaning: {shadow_mean}')
        
    if st.button("Celtic Cross Telling"):
        result = tarot_celtic_cross(name_c, age_c, rand_num)
        
        cols1 = st.columns(5)
        for i, (pos,card) in enumerate(result.items()):
            if i < 5:
                with cols1[i]:
                    st.image(card['img'], caption=card['name'], use_container_width=True)
                    st.write(f'Position: {pos}')
                    st.write(f'Name: {card['name']}')
                    st.write(f'Fortune: {card['fortune']}')
                    st.write(f'Suit: {card['suit']}')
                    st.write(f'Keywords: {card['keywords']}')
                    st.write(f'Light Meaning: {card['meanings_light']}')
                    st.write(f'Shadow Meaning: {card['meanings_shadow']}')
        cols2 = st.columns(5)
        for i, (pos,card) in enumerate(result.items()):
            if i >= 5:
                with cols2[i-5]:
                    st.image(card['img'], caption=card['name'], use_container_width=True)
                    st.write(f'Position: {pos}')
                    st.write(f'Name: {card['name']}')
                    st.write(f'Fortune: {card['fortune']}')
                    st.write(f'Suit: {card['suit']}')
                    st.write(f'Keywords: {card['keywords']}')
                    st.write(f'Light Meaning: {card['meanings_light']}')
                    st.write(f'Shadow Meaning: {card['meanings_shadow']}')
#!/usr/bin/env python
# coding: utf-8

# In[16]:


import streamlit as st 
import numpy as np 
import pandas as pd
import re



# In[42]:


data= pd.read_csv("ott.csv")
data["Genres"].fillna("Any", inplace = True) 
data["Language"].fillna("Check yourself", inplace = True) 
data["Netflix"].replace({0: "NO", 1: "Yes",1.01:"Yes"}, inplace=True)
data["Hulu"].replace({0: "NO", 1: "Yes"}, inplace=True)
data["Prime Video"].replace({0: "NO", 1: "Yes"}, inplace=True)
data["Disney+"].replace({0: "NO", 1: "Yes"}, inplace=True)



genres_unclean = dict(data['Genres'].value_counts())
count_genres = dict()
for g,count in genres_unclean.items():
    curr_g = g.split(",")
    for xg in curr_g:
        if xg in count_genres.keys():
            count_genres[xg] = count_genres.get(xg)+1
        else:
            count_genres[xg] = 1
count_genres_df = pd.DataFrame(count_genres.items(), columns=['Genre', 'Count'])

languages_dict = dict(data['Language'].value_counts())
languages_count = dict()
for lang,count in languages_dict.items():
    curr_lang = lang.split(",")
    for i in curr_lang:
        if i in languages_count.keys():
            languages_count[i] = languages_count.get(i) + 1
        else:
            languages_count[i] = 1
lang_count_df = pd.DataFrame(languages_count.items(), columns=['Language', 'Count'])

st.title('OTT Picker')

st.write("""
# Explore different ott platforms
""")

genre_name = st.sidebar.selectbox(
    'Select Genre',
    (count_genres_df.Genre)
   
)

st.write(f"## {genre_name} ")

language_name = st.sidebar.selectbox(
    'Select language',
    (lang_count_df.Language)
)

data.drop(['ID','Type','Country','Language'], axis=1, inplace = True)
movie_name=st.write(data[data['Genres'].str.contains(genre_name)])
data['Genres']=data['Genres'].str.replace(',',' ')


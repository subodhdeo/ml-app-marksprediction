# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 09:46:49 2022

@author: Subodh Deolekar
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt



# to cache the data and use it later

@st.cache
def load_data():
    dataset = pd.read_csv('student_scores.csv')
    return dataset

def plot_hrs_scores():
    ds = load_data()
    fig = plt.figure(figsize = (10, 5))
    #ds.plot(x='Hours', y='Scores', style='*')
    plt.scatter('Hours','Scores', data=ds)
    plt.title('Hours vs Percentage')
    plt.xlabel('Hours Studied')
    plt.ylabel('Percentage Score')
    st.pyplot(fig)


def show_explore_page():
    st.title("Explore Student study hours data")
    
    st.write(""" ### Student study hours vs marks obtained """)
    plot_hrs_scores()
             

# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 09:45:32 2022

@author: Subodh Deolekar
"""

import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page

page = st.sidebar.selectbox("Explore or Predict", ("Explore", "Predict"))

if page == "Explore":
    show_explore_page()
else:
    show_predict_page()
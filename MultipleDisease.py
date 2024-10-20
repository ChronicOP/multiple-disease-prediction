#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 00:17:39 2024

@author: prathameshpatil
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

diabeties_model=pickle.load(open('/Users/prathameshpatil/Desktop/Multiple disease Predicting System/SAVED MODELS/diabetes_model.sav','rb'))

heart_model=pickle.load(open('/Users/prathameshpatil/Desktop/Multiple disease Predicting System/SAVED MODELS/heart_disease_model.sav','rb'))

parkinson__model=pickle.load(open('/Users/prathameshpatil/Desktop/Multiple disease Predicting System/SAVED MODELS/parkinsons_model.sav','rb'))


with st.sidebar:
    
    selected=option_menu('Multiple Disease Prediction System',
                         ['Diabetes Prediction',
                          'Heart Disease Prediction',
                          'Parkinson Prediuction'],
                         default_index=0)
    


if (selected = 'Diabetes Prediction'):
# page title
    st. title( 'Diabetes Prediction using ML')
    
    
if (selected == 'Heart Disease Prediction'):
# page title
    st.title( 'Heart Disease Prediction using ML')
    
    
if (selected == 'Parkinson Prediction'):
# page title
    st. title( 'Parkinson Prediction using ML ')
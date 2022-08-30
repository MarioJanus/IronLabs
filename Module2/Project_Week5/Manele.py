#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 19:32:42 2022

@author: manele
"""
import streamlit as st
import pandas as pd
import numpy as np 


salary=pd.read_csv(r"/Users/manele/Downloads/salarynew.csv")

st.title("Our project")
st.write("This project aims at giving different insights regarding various Data Science jobs.")

year_to_filter = st.slider('year', 2020, 2022, 2021)
filtered_data = salary[salary['work_year'] == year_to_filter]

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(salary)
    

st.bar_chart(data=salary, x='job_title', y='salary_in_usd', width=0, height=0, use_container_width=True)


options = st.radio(
     "What do you want to see?",
     ('Raw Data', 'Bar plot', 'Graph'))

if options == 'Raw Data':
     st.write(salary)
elif options == 'Bar plot':
    st.bar_chart(data=salary, x='job_title', y='salary_in_usd', width=0, height=0, use_container_width=True)
else:
    st.write('Nothing to see here')


#Code for map:
import geocoder
import requests
with requests.Session() as session:
    for address in salary["employee_residence"]:
        coo = geocoder.osm(address, session=session)
        if coo:
            salary.loc[salary["employee_residence"] == address, "Long"] = round(coo.osm["x"], 2)
            salary.loc[salary["employee_residence"] == address, "Lat"] = round(coo.osm["y"], 2)
salary.rename(columns={"Lat": "lat", "Long": "lon"}, inplace = True)
salary.info()
salary['lat']=pd.to_numeric(salary['lat']) 
salary['lon']=pd.to_numeric(salary['lon'])
salary['lat']=salary['lat'].astype('float64')  
salary['lon']=salary['lon'].astype('float64') 
salary.dropna(subset=['lon', 'lat'], inplace = True)
st.map(data=salary, zoom=None, use_container_width=True)
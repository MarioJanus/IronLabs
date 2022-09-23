#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 19:32:42 2022

@author: manele
"""
import streamlit as st
import pandas as pd
import numpy as np 
import plotly.express as px
import plotly.figure_factory as ff



salary=pd.read_csv(r"/Users/manele/Downloads/salarynew.csv")

st.title("Data Scientist jobs")
st.write("This project aims at giving different insights regarding various Data Science jobs.")

options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])

st.write('You selected:', options)

year_to_filter = st.slider('year', 2020, 2022, 2021)
filtered_data = salary[salary['work_year'] == year_to_filter]

emp = salary.pivot_table(index =['work_year'], values=["remote_ratio"], aggfunc="sum")
d = emp.reset_index()

#bar chart jobs:
df1= salary.groupby('job_title', as_index=False)['salary_in_usd'].mean()
df1.sort_values("salary_in_usd", axis = 0, ascending = False, inplace = True)


#bar chat of salary by job and raw data:

if st.checkbox('Raw data : '):
    st.subheader('Raw data')
    st.write(salary)
elif st.checkbox('Average salaries : '):
    st.write(x = st.bar_chart(data=df1, x='job_title', y='salary_in_usd', width=0, height=0, use_container_width=True)
)


st.subheader('Remote work ratio by year :')
  

#remot work:
st.area_chart(data=d, x='work_year', y='remote_ratio', width=0, height=0, use_container_width=True)

st.subheader('Average salary by country :')

#bar chart countries
df2 = salary.groupby('employee_residence', as_index=False)['salary_in_usd'].mean()
df2.sort_values("salary_in_usd", axis = 0, ascending = False, inplace = True)
df2 = df2.head(10)
df2

st.bar_chart(data=df2, x='employee_residence', y='salary_in_usd', width=0, height=0, use_container_width=True)




    



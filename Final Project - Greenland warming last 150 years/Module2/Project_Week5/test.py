# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 09:50:29 2022

@author: Mario
"""
import plotly.figure_factory as ff
import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import regex
import country_converter as coco
import warnings
warnings.filterwarnings("ignore")

salary=pd.read_csv(r"C:\Users\Mario\Documents\Labs\Module2\Project_Week5\ds_salaries.csv")
salary.head(3)
salary.drop(["Unnamed: 0"], axis=1, inplace=True)


standard_names_empl = coco.convert(salary['employee_residence'], to='name')
salary['employee_residence'] = standard_names_empl
standard_names_comp = coco.convert(salary['company_location'], to='name')
salary['company_location'] = standard_names_comp
salary['experience_level'] = salary['experience_level'].replace({'EN':'Entry-Level', 'MI':'Mid-Level', 'SE':'Senior-Level', 'EX':'Executive-Level/Director'})
salary['company_size'] = salary['company_size'].replace({'S':'Small (<50)', 'M':'Medium (50-250)', 'L':'Large (250+)'})
salary['employment_type'] = salary['employment_type'].replace({'FT':'Full-time', 'PT':'Part-time', 'CT':'Contract', 'FL':'Freelance'})

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




options_job = salary['job_title'].unique().tolist()

selected_options = st.sidebar.multiselect('Number of jobs?',options_job, default=salary.groupby(["job_title"]).agg({"job_title":"count"}))
num_jobs = salary[salary["job_title"].isin(selected_options)]
st.dataframe(num_jobs.groupby(["job_title"]).agg({"job_title":"count"}).rename(columns={'job_title': 'Number of jobs'}))

options_emp_typ = salary['employment_type'].unique().tolist()
selected_options = st.sidebar.multiselect('Number of employment types?',options_emp_typ)
num_typ = salary[salary['employment_type'].isin(selected_options)]
st.dataframe(num_typ.groupby(["employment_type"]).agg({"employment_type":"count"}).rename(columns={'employment_type': 'Number of employement types'}))

#############################

#locations = salary['employee_residence'].sort_values().unique().tolist()
#sidebar = st.sidebar
#select_loc = sidebar.selectbox("Select Country",locations)
test = salary[salary['employee_residence']==select_loc]
st.dataframe(test.groupby(["employment_type"]).agg({"employment_type":"count"}))
             
x=salary.groupby([salary['employee_residence']==select_loc,"job_title"]).agg({'job_title':'count'})
x.dropna()
x


#x.plot(kind='pie', subplots=True)
#explode = (0.05, 0.05, 0.1,0.1)
#fig = plt.figure(figsize = (8, 8))
#plt.pie(list(x),labels=labels, explode=explode)
#plt.show()
#st.pyplot(x.bool())
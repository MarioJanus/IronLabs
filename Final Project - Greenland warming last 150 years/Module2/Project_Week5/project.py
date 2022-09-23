import plotly.express as px
import plotly.graph_objects as go
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
st.bar_chart(data=filtered_data, x='job_title', y='salary_in_usd', width=0, height=0, use_container_width=True)

#if filtered_data==2020:
#   st.bar_chart(data=salary[salary['work_year']==2020, x='job_title', y='salary_in_usd', width=0, height=0, use_container_width=True)
#elif filtered_data==2021:
#    st.bar_chart(data=salary[salary['work_year']==2021, x='job_title', y='salary_in_usd', width=0, height=0, use_container_width=True)
#elif filtered_data==2022:
#    st.bar_chart(data=salary[salary['work_year']==2022, x='job_title', y='salary_in_usd', width=0, height=0, use_container_width=True)    

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

selected_options = st.sidebar.multiselect('Number of jobs?',options_job)
num_jobs = salary[salary["job_title"].isin(selected_options)]
st.dataframe(num_jobs.groupby(["job_title"]).agg({"job_title":"count"}).rename(columns={'job_title': 'Number of jobs'}))

########

options_emp_typ = salary['employment_type'].unique().tolist()
selected_options = st.multiselect('Number of employment types?',options_emp_typ, default=salary["employment_type"].unique())
num_typ = salary[salary['employment_type'].isin(selected_options)]
st.dataframe(num_typ.groupby(["employment_type"]).agg({"employment_type":"count"}).rename(columns={'employment_type': 'Number of employement types'}))

########

locations = salary['employee_residence'].unique().tolist()
sidebar = st.sidebar
select_loc = st.selectbox("Select Country for jobs",locations)
sel_country=salary[salary['employee_residence']==select_loc]        
x=st.dataframe(sel_country.groupby(['employee_residence','job_title'])['job_title'].count())

#=st.dataframe(sel_country.groupby(['employee_residence',"job_title"]).agg(Number_of_jobs=('job_title', 'count')))
print(x)
#######

locations = salary['company_location'].unique().tolist()
sidebar = st.sidebar
select_loc = st.selectbox("Select Country for jobs",locations)
sel_country=salary[salary['company_location']==select_loc]        
#y=sel_country.groupby(['company_location',"company_size"]).agg(Size_of_Companies=('company_size', 'count'))


y_pie=sel_country.groupby(['employee_residence','job_title'])['job_title'].count()

#x=sel_country.groupby(['company_location',"company_size"]).agg(Size_of_Companies=('company_size', 'count'))
#pie_chart=px.pie(x, values='job_title', names='job_title')
#st.write(pie_chart)
#a=st.plotly_chart(pie_chart)
#st.write(a)

df2 = salary.groupby('employee_residence', as_index=False)['salary_in_usd'].mean()
df2.sort_values('salary_in_usd', axis = 0, ascending = False, inplace = True)
df2 = df2.head(10)
df2
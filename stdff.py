#https://discuss.streamlit.io/t/new-component-dynamic-multi-select-filters/49595/28
#https://dynamic-filters-demo.streamlit.app/Dates_Example
#https://github.com/arsentievalex/streamlit-dynamic-filters?tab=readme-ov-file
import plotly.express as px
import streamlit as st
import numpy as np
import pandas as pd
from streamlit_dynamic_filters import DynamicFilters

data = {
    'region': ['North America', 'North America', 'Europe', 'Oceania',
               'North America', 'North America', 'Europe', 'Oceania',
               'North America', 'North America', 'Europe', 'Oceania'],
    'country': ['USA', 'Canada', 'UK', 'Australia',
                'USA', 'Canada', 'UK', 'Australia',
                'USA', 'Canada', 'UK', 'Australia'],
    'city': ['New York', 'Toronto', 'London', 'Sydney',
             'New York', 'Toronto', 'London', 'Sydney',
             'New York', 'Toronto', 'London', 'Sydney'],
    'district': ['Manhattan', 'Downtown', 'Westminster', 'CBD',
                 'Brooklyn', 'Midtown', 'Kensington', 'Circular Quay',
                 'Queens', 'Uptown', 'Camden', 'Bondi'],
    'sale': [5443, 7567, 8678, 7688,
             5675, 4345, 4545, 5645,
             3456, 3345, 3453,5656],
}

df = pd.DataFrame(data)

#dynamic_filters = DynamicFilters(df, filters=['region', 'country', 'city', 'district'])
dynamic_filters = DynamicFilters(df, filters=df.columns)

st.write("Apply filters in any order 👇")

dynamic_filters.display_filters(location='columns', num_columns=2, gap='large')
dynamic_filters.display_df()
#new_df = dynamic_filters.filter_df()
#st.write(new_df)  # did not show the filter jor selected data show blanck  dataframe 

tdf = pd.DataFrame(dynamic_filters.filter_df())
col_lst = tdf.columns.to_list()
col_lst = {col_lst[i]: True for i in range(len(col_lst))}

sc1, sc2 = st.columns((2,8), vertical_alignment='bottom')
sc1.write("Select Cols:")
for k, v in col_lst.items(): col_lst[k] = sc1.checkbox(label=k, value=v)
sc2.dataframe(tdf[[key for key, value in col_lst.items() if value]], use_container_width=False)
#st.write(col_lst.items())
df3 = pd.DataFrame(col_lst.items())
df3.columns = ['Colname', 'Cstatus']
#st.write(df3)
result_df= df3.loc[df3['Cstatus']==True]
#team.columns = ['Name', 'Code', 'Age', 'Score']
#st.write(result_df)
single_column_series = result_df['Colname'].values.tolist()
#st.write(single_column_series)
#list_of_lists = single_column_series.values.tolist()
#st.write(list_of_lists)
#selected_columns_df = tdf[[single_column_series]]
df4 = pd.DataFrame(tdf, columns=single_column_series)
st.write(df4)

if st.button('Check availability'):
    st.write('Muhammad is the Best -------- for graph ')
    mfa7 = pd.DataFrame(df4)
    mfa7.set_index(df4.iloc[:,0], inplace=True)
    first_column_name = mfa7.columns[0]
    
    st.bar_chart(df4)
    st.area_chart(df4)
    st.line_chart(df4)
    st.pyplot(df4.plot.barh(stacked=True).figure)
    st.pyplot(mfa7.plot.bar(stacked=True).figure)
    st.pyplot(mfa7.plot.bar(rot=0).figure)

#colname = df.columns[pos]
#print (colname)

    num_columns = len(df4.columns)-1
   # st.header(num_columns)
    #fig = px.pie(df4, values=df4.columns[1], names=df4.columns[0], title="Muhammad is the best",)
    fig = px.pie(df4, values=df4.columns[num_columns], names=df4.columns[0], title="Muhammad is the best",)
    st.plotly_chart(fig, theme=None)
    

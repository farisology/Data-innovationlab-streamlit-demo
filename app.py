import streamlit as st
import pandas as pd
import numpy as np

st.title('Exploring Netflix Movies & TV Shows')

data_file = ('netflix_titles.csv')

@st.cache
def load_data():
    data = pd.read_csv(data_file)
    data['date_added'] = pd.to_datetime(data['date_added'])
    return data

data_load_state = st.text('Loading data...')
data = load_data()
data_load_state.text("Done! (using st.cache)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.header('Suggesting a random movie or TV show to watch:')


option = st.selectbox(
     'How would you like your movies suggestion to be produced?',
     ('Purely Random', 'Single Filter', 'Multiple Filters'))

st.write('You selected:', option)

if option == 'Purely Random':
    if st.button('Am feeling luck!'):
        random_suggestion = data.sample(n=3)
        st.write(random_suggestion)
        
        st.subheader('First suggestions:')
        for i in random_suggestion.iloc[0:1].iterrows():
            st.write(f"Title: {i[1][2]}")
            st.write(f"Type: {i[1][1]}")
            st.write(f"Country: {i[1][5]}")
            st.write(f"Directed by: {i[1][3]}")
            st.write(f"Rating: {i[1][8]}")
            st.write(f"Released in: {i[1][7]}")
        
        st.subheader('Second suggestions:')
        for i in random_suggestion.iloc[1:2].iterrows():
            st.write(f"Title: {i[1][2]}")
            st.write(f"Type: {i[1][1]}")
            st.write(f"Country: {i[1][5]}")
            st.write(f"Directed by: {i[1][3]}")
            st.write(f"Rating: {i[1][8]}")
            st.write(f"Released in: {i[1][7]}")
        
        st.subheader('Third suggestions:')
        for i in random_suggestion.iloc[2:].iterrows():
            st.write(f"Title: {i[1][2]}")
            st.write(f"Type: {i[1][1]}")
            st.write(f"Country: {i[1][5]}")
            st.write(f"Directed by: {i[1][3]}")
            st.write(f"Rating: {i[1][8]}")
            st.write(f"Released in: {i[1][7]}")

    else:
        st.info('Click the button above!!')

if option == 'Single Filter':
    filter_selected = st.radio('What filter you want to use to pick your movie?'
                            ,('Type', 'Country', 'Release Year', 'Rating'))

    if filter_selected == 'Type':
        movie_type = st.selectbox('Which type are you looking for:'
                                , ('Movie', 'TV Show'))
        
        random_suggestion = data[data['type'] == movie_type].sample(n=3)
        st.write(random_suggestion)
        
        st.subheader('First suggestions:')
        for i in random_suggestion.iloc[0:1].iterrows():
            st.write(f"Title: {i[1][2]}")
            st.write(f"Type: {i[1][1]}")
            st.write(f"Country: {i[1][5]}")
            st.write(f"Directed by: {i[1][3]}")
            st.write(f"Rating: {i[1][8]}")
            st.write(f"Released in: {i[1][7]}")
        
        st.subheader('Second suggestions:')
        for i in random_suggestion.iloc[1:2].iterrows():
            st.write(f"Title: {i[1][2]}")
            st.write(f"Type: {i[1][1]}")
            st.write(f"Country: {i[1][5]}")
            st.write(f"Directed by: {i[1][3]}")
            st.write(f"Rating: {i[1][8]}")
            st.write(f"Released in: {i[1][7]}")
        
        st.subheader('Third suggestions:')
        for i in random_suggestion.iloc[2:].iterrows():
            st.write(f"Title: {i[1][2]}")
            st.write(f"Type: {i[1][1]}")
            st.write(f"Country: {i[1][5]}")
            st.write(f"Directed by: {i[1][3]}")
            st.write(f"Rating: {i[1][8]}")
            st.write(f"Released in: {i[1][7]}")
    

    if filter_selected == 'Country':
        country_choice = st.selectbox('Which type are you looking for:'
                                , (data['country'].unique()))
        random_suggestion = data[data['country'] == country_choice].sample(n=3)
        st.write(random_suggestion)
        
        st.subheader('First suggestions:')
        for i in random_suggestion.iloc[0:1].iterrows():
            st.write(f"Title: {i[1][2]}")
            st.write(f"Type: {i[1][1]}")
            st.write(f"Country: {i[1][5]}")
            st.write(f"Directed by: {i[1][3]}")
            st.write(f"Rating: {i[1][8]}")
            st.write(f"Released in: {i[1][7]}")
        
        st.subheader('Second suggestions:')
        for i in random_suggestion.iloc[1:2].iterrows():
            st.write(f"Title: {i[1][2]}")
            st.write(f"Type: {i[1][1]}")
            st.write(f"Country: {i[1][5]}")
            st.write(f"Directed by: {i[1][3]}")
            st.write(f"Rating: {i[1][8]}")
            st.write(f"Released in: {i[1][7]}")
        
        st.subheader('Third suggestions:')
        for i in random_suggestion.iloc[2:].iterrows():
            st.write(f"Title: {i[1][2]}")
            st.write(f"Type: {i[1][1]}")
            st.write(f"Country: {i[1][5]}")
            st.write(f"Directed by: {i[1][3]}")
            st.write(f"Rating: {i[1][8]}")
            st.write(f"Released in: {i[1][7]}")




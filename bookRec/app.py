'''
Author: weifeng ma
Discription: This is the overall desgin for the book recommender system.
'''

import pickle
import streamlit as st
import numpy as np

# for user authentication
from pathlib import Path
import streamlit_authenticator as stauth


# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="book recommender system", page_icon=":bar_chart:", layout="wide")

# user authentication
names = ["weifeng ma"] # the names of the users
usernames = ["weifengma"] # the usernames of the users

# load our passwords
file_path = Path(__file__).parent / "users.pkl"
with file_path.open("rb") as file: 
    passwords = pickle.load(file)

# create an authenticator obejct
authenticator = stauth.Authenticate(names, usernames, passwords,
                                     "app_home",
                                      "123", cookie_expiry_days=0)

name, authentication_status, username = authenticator.login("Login", 
                                                            "main")

if authentication_status == False:
    st.error("Incorrect username or password. Please try again.")

if authentication_status == None:
    st.warning("Please enter your username and password to login.")

if authentication_status == True:
    st.header('Book Recommender System')
    # load our models
    model = pickle.load(open('pickles/model.pkl','rb'))
    book_names = pickle.load(open('pickles/book_names.pkl','rb'))
    final_rating = pickle.load(open('pickles/final_rating.pkl','rb'))
    book_pivot = pickle.load(open('pickles/book_pivot.pkl','rb'))

    def fetch_poster(suggestion):
        book_name = []
        ids_index = []
        poster_url = []

        for book_id in suggestion:
            book_name.append(book_pivot.index[book_id])

        for name in book_name[0]: 
            ids = np.where(final_rating['title'] == name)[0][0]
            ids_index.append(ids)

        for idx in ids_index:
            url = final_rating.iloc[idx]['image_url']
            poster_url.append(url)

        return poster_url



    def recommend_book(book_name):
        books_list = []
        book_id = np.where(book_pivot.index == book_name)[0][0]
        distance, suggestion = model.kneighbors(book_pivot.iloc[book_id,:].values.reshape(1,-1), n_neighbors=6 )

        poster_url = fetch_poster(suggestion)
        
        for i in range(len(suggestion)):
                books = book_pivot.index[suggestion[i]]
                for j in books:
                    books_list.append(j)
        return books_list , poster_url       


    
    selected_books = st.selectbox(
        "Type or select a book from the dropdown",
        book_names
    )

    if st.button('Show Recommendation'):
        recommended_books,poster_url = recommend_book(selected_books)
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.text(recommended_books[1])
            st.image(poster_url[1])
        with col2:
            st.text(recommended_books[2])
            st.image(poster_url[2])

        with col3:
            st.text(recommended_books[3])
            st.image(poster_url[3])
        with col4:
            st.text(recommended_books[4])
            st.image(poster_url[4])
        with col5:
            st.text(recommended_books[5])
            st.image(poster_url[5])

    
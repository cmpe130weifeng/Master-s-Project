import pickle
from pathlib import Path

import streamlit_authenticator as stauth

names = ["weifeng ma"] # the names of the users
usernames = ["weifengma"] # the usernames of the users
passwords = ["123456"] # the passwords of the users

# encrypt the passwords
hashed_passwords = stauth.Hasher(passwords).generate()
# save the users
file_path = Path(__file__).parent / "users.pkl"

with file_path.open("wb") as file: 
    pickle.dump(hashed_passwords, file)


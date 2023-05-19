# Master-s-Project

Book Recommender System

To run the system:
1. clone 'bookRec' folder
2. open folder 'bookRec' with your IDE
3. pip install -r requirements.txt
4. in terminal type: streamlit run app.py
5. Use username and password to login:
username: weifengma </br>
password: 123456

</br>
If you running with an error: FileNotFoundError: [Errno 2] No such file or directory: 'pickles/model.pkl'
Please: 1. copy all the pkl files in pickles folder (in bookRec), and save it a temporary folder 
2. delete all pkl file in pickles folder (in bookRec)
3. copy and paste all your files from the temporaty folder back to the pickle folder (in bookRec)
4. run streamlit run app.py

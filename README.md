# Master-s-Project
## Book recommender system using various methods
### Team members:  Weifeng Ma,  Aman Shah
</br>
</br>
In this project, we'll build a book recommender system using different approaches(popular-based approach, collaborative filtering approach, and graph neural network approach). In this popular-based approach, we will filter out data and get the top and most popular items for users. This approach often use to create a top list for users to select items they might like. In collaborative filtering approach, the system will filter out items that a user might like on the basis of reactions by similar users. This approach is often done by using matrix factorization. Matrix factorization is the approach of decomposing a matrix into the product of two or more matrices. Lastly, we can also use a graph neural network to build a recommender system. By using a neural network, we can update/adjust the weights of a matrix from matrix factorization to get an optimal rating for each user. Graph neural networks have an advantage in recommender systems. We can easily represent user-item interaction by using a graph. In this project, we'd try all methods to build our recommender system. For demostration (final product), we selected collaborative filtering approach. </br>

</br>

To run the system:
1. clone 'bookRec' folder
2. open folder 'bookRec' with your IDE
3. pip install -r requirements.txt
4. in terminal type: streamlit run app.py
5. Use username and password to login:
username: weifengma </br>
password: 123456

</br>
If you running with an error: FileNotFoundError: [Errno 2] No such file or directory: 'pickles/model.pkl' </br>
Please: 1. copy all the pkl files in pickles folder (in bookRec), and save it a temporary folder  </br>
2. delete all pkl file in pickles folder (in bookRec) </br>
3. copy and paste all your files from the temporaty folder back to the pickle folder (in bookRec) </br>
4. run streamlit run app.py </br>

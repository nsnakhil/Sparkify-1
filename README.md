# Sparkify-1
Introduction
A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app. The dataset can be downloaded from data.zip

 
Task 1: Install MongoDB on the Ubuntu EC2 instance you had launched earlier for the Flask lab. You can find the instructions in this tutorial. 

If you want to be able to connect to MongoDB remotely (like, from your laptop), you will need to follow these steps: 

1)Edit the inbound rules in your EC2 instance's security group to allow connections on port 27017
2)Edit /etc/mongod.conf to comment out bindIp: 127.0.0.1 under # network interfaces in order to allow mongod to accept remote connections

Task 2: Develop a Python 3 script that reads the log data into a MongoDB database. 


Task 3: Create a Python web application with Flask to display the top 10 (i.e., most frequently played) Songs and the top 10 Artists for each week on a web page. You will need to use MongoDB's Aggregation framework to complete this task You can also find a quick tutorial here. 

Deliverables: Please submit your code and screenshots of the web page in a single .zip file. Also, include the URL (or public IP address) and the name of the corresponding EC2 instance in the submission description.  

#windows development setup

1. install git - mysysgit 
2. install python 2.7 
2.1. make sure c:\python27 (for python)  and c:\python27\scripts (for pip) are in your PATH

3.Get dynamodb local
========================================

3.1. install jdk8 
3.2. Get dynamodb local from - http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Tools.DynamoDBLocal.html#Tools.DynamoDBLocal.DownloadingAndRunning
3.3 download the zip/tar file, unarchive it and keep it on your machine.. I generally keep it at c:\users\<username>\bin\dynamodblocal
3.4 run dynamodblocal by using following command
java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -sharedDb


#setup boto credentials


#clone github repo

 git clone https://github.com/rakeshsingh/gullycricket.git



#after installing pip
1. pip install virtualenv
2. pip install virtualenvwrapper
3. pip install virtualenvwrapper-bin

#create and work in a virtualenv
Since you have installed virtualenvwrapper-bin, you will have following commands available : 
a. mkvirtualenv - to create virtualenv
b. workon- to list and select a virtualenv
c. deactivate - to deactivate and come out of virtualenv 
sample commands for our project could be 

mkvirtualenv gullycricket
workon gullycricket






#install required packages
1. pip install flask
2. pip install flywheel
3. pip install flask-WTF






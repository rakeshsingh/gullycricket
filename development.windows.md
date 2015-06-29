#Instructions to setup development environment on Windows

1. install git - mysysgit 
2. install python 2.7
2.1. pip will come with python
2.2. make sure c:\python27 (for python)  and c:\python27\scripts (for pip) are in your PATH

3. Install Dynamodb Local
3.1. install jdk8 
3.2. Get dynamodb local from - http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Tools.DynamoDBLocal.html#Tools.DynamoDBLocal.DownloadingAndRunning
3.3 download the zip/tar file, unarchive it and keep it on your machine.. I generally keep it at c:\users\<username>\bin\dynamodblocal
3.4 run dynamodblocal by using following command
java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -sharedDb


4. setup boto credentials
4.1. Create a file %USERPROFILE%\.aws\credentials with following content
    [default]
    aws_access_key_id = ACCESS_KEY
    aws_secret_access_key = SECRET_KEY
    aws_session_token = TOKEN

5. Install virtualenv tools 
    pip install virtualenv
    pip install virtualenvwrapper
    pip install virtualenvwrapper-bin

6. create and work in a virtualenv
Since you have installed virtualenvwrapper-bin, you will have following commands available : 
a. mkvirtualenv - to create virtualenv
b. workon- to list and select a virtualenv
c. deactivate - to deactivate and come out of virtualenv 
sample commands for our project could be 

    mkvirtualenv gullycricket
    workon gullycricket



7. clone github repo
    git clone https://github.com/rakeshsingh/gullycricket.git

8. cd to the checked in project and install packages required for this project
8.1. core flask packages 
    pip install flask
8.2. for dynamodb conneciton
    pip install flywheel
8.3. for Flask WTF forms 
    pip install flask-WTF

9. Run the flask app. 
Once you have all the packages setup. you should be able to run this app by running following command 
    python run.py


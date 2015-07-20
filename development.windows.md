#Development Manual 
##Setup development environment on Windows

1. install git - mysysgit 
2. install python 2.7
> pip will come with python
><br> make sure c:\python27 (for python)  and c:\python27\scripts (for pip) are in your PATH

3. Install Dynamodb Local
>install jdk8 
><br>Get dynamodb local from [here]( http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Tools.DynamoDBLocal.html#Tools.DynamoDBLocal.DownloadingAndRunning)
><br>download the zip/tar file, unarchive it and keep it on your machine.. I generally keep it at c:\users\<username>\bin\dynamodblocal
><br>run dynamodblocal by using following command
><br>java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -sharedDb

4. setup boto credentials
>Create a file %USERPROFILE%\.aws\credentials with following content
><br>    [default]
><br>    aws_access_key_id = ACCESS_KEY
><br>    aws_secret_access_key = SECRET_KEY
><br>    aws_session_token = TOKEN

5. Install virtualenv tools 
><br>    pip install virtualenv
><br>    pip install virtualenvwrapper
><br>    pip install virtualenvwrapper-bin

6. create and work in a virtualenv
><br>Since you have installed virtualenvwrapper-bin, you will have following commands available : 
><br>a. mkvirtualenv - to create virtualenv
><br>b. workon- to list and select a virtualenv
><br>c. deactivate - to deactivate and come out of virtualenv 
><br>sample commands for our project could be 
><br>
><br>    mkvirtualenv gullycricket
><br>    workon gullycricket

7. clone github repo
><br>    git clone https://github.com/rakeshsingh/gullycricket.git

8. cd to the checked in project and install packages required for this project
><br>8.1. core flask packages 
><br>   pip install flask
><br>8.2. for dynamodb conneciton
><br>    pip install flywheel
><br>8.3. for Flask WTF forms 
><br>    pip install flask-WTF

9. Run the flask app. 
><br>Once you have all the packages setup. you should be able to run this app by running following command 
><br>    python run.py

## Coding style
1. Follow Pep8 standards 

## Deployment Instructions
1. 

## Operations Guide
1. 
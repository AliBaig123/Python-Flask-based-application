Project Description:
    Make basic web application using python flask.FLask is library which is used in python for making web application , the application shows custom message and its route on homepage(/), listen on port 5000 with
    0.0.0.0, runs this application on other devices as well if they are in same network

Steps To Run Application :
.) first to make venv(virtual environment where install dependencies and execute applicaion)
.) then, install dependencies through pip install requiremens.txt
.) then run the application python app.py

Set up Steps:

.) first set up two virtual machines which consist of ubuntu and rocky linux.
.) then configure jenkins and install it from its official website , 
.) after this deploy the application on rocky linux which is dockerized and running in the form of container.
.) after this then the communication establised between two vm, through ssh
.) Now the next phase would be, to make cicd pipeline
.) for this we make two kind of jobs freestyle, pipeline
.)  then select pipeline , make declarative pipeline means in the form of script 
for this we have multiple stages to pull code from github,build docker images,stop and remove old container and make new container after executing pipeline .

TROUBLESHOOTING PROBLEMS OF JENKINS:
.) the first problem whikle executing pipeline is the branch error 
.) another problem is when pipeline executes it shows the error in container that port is already allocated then chanhge the port and run the pipeline 




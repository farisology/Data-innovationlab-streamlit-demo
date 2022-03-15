# Our steps to build the first streamlit data application:

1. Envirnoment setting
    1. Install pip (if its not installed)
    <sudo apt-get install python3-pip>
    
    2. Install virtualenv
    <sudo pip3 install virtualenv>
    
    3. Create a virtualenv
    <virtualenv myenv_name>
    
    4. Activate your virtualenv
    <source myenv_name/bin/activate>
    
    5. Check pre-installed libarries into your new env
    <pip list>
    
    6. install important libraries

    If you face any issue in ubuntu you may need to install:
    <sudo apt-get install build-essential libssl-dev libffi-dev python-dev>

    7. to make our virtual env reproducible we export it into a file:
    <pip freeze >> requirements.txt>

    8. To reproduce the same env in another machine we can simy just install the libraries as per the versions in the requirements file:
    <pip install -r requirements.txt>

    9. Avoid adding your env files into the github repo by writing them down in the .ignore file
    
2. Create a new file called app.py
3. Download Neflix Movies and TV Shows dataset from kaggle
<https://www.kaggle.com/shivamb/netflix-shows>

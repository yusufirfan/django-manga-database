# Installation

```
Rename .env-sample file to .env and change SECRET_KEY

* Terminal Commands *

#1 - python -m venv env

#2 - Powershell=>.\env\Scripts\activate
#2 - Git Bash=> source env/Scripts/Activate
#2 - Linux/Mac => source env/bin/activate

#3 - pip install -r requirements.txt

#4- python manage.py makemigrations

#5 - python manage.py migrate

#6 - python manage.py runserver

!!! If you want to use ./admin/, you should:

#7 python manage.py createsuperuser #After you use this command, you can follow the messages from terminal/console
```

[dj-rest-auth](https://dj-rest-auth.readthedocs.io/en/latest/index.html) 
[MakeReadMe](https://www.makeareadme.com/)
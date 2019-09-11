# API_wikipedia

### This application allows you to work with simple API and wikipedia. 
### You should provide title and url of article and API provides to you all information about this.

## Setting up


##### Clone the repo

```
$ git clone https://github.com/petrovao87/api_wikipedia.git
$ cd api_wikipedia
```

##### Virtual Environment install & activate
```
$ pip install virtualenv
$ python -m venv env  (for Windows systems)
$ python3 -m venv env  (for Unix systems)
$ env\scripts\activate  (for Windows systems)
$ env/bin/activate  (for Unix systems)
```

##### Install the dependencies

```
$ pip install -r requirements.txt
```

#### Connection to your PostgreSQL server and Create the database 

##### create connection to your db. Change file settings.py, DATABASE = ..
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'note_db',
        'USER': 'postgres',
        'PASSWORD': '12345',
        'HOST': 'localhost',
        'PORT': '49928',
    }
}
```
##### and create schemas
```
$ manage.py migrate
```

### Running the app
```
$ manage.py runserver
```

## API_wikipedia methods:

### GET the list of all notes
```
/api/v0/note/all/
```

### GET a single note
```
/api/v0/note/<note_id>/
```

### DELETE a note
```
/api/v0/note/<note_id>/
```

### Update a task

```
/api/v0/note/<note_id>/
```

### Add a new process
```
/api/v0/note/<create/
```
### Parameters to send in your POST 
```
title (String)
url (String)
```
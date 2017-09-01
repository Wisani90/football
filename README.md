# Fantasy Football League Stats
This site is now live at fpl-stats.co.uk
-----
## Set up for local environment
-----
### Requirements
This Django project runs using Python 2.7.11

Install the requirements as follows:
```shell
cd <repo_root>/fpldjango
pip install -r requirements.txt
```

### Running the website
To run the website locally:
#### Using the django web server:
```shell
cd <repo_root>/fpldjango
python manage.py runserver
```
The site can be viewed in your browser at http://localhost:8000/

#### Using heroku:
```shell
cd <repo_root>
heroku local web
```
The site can be viewed in your browser at http://localhost:5000/

#### Using Gunicorn:
```shell
cd <repo_root>/fpldjango
gunicorn fpldjango.wsgi
```
The site can be viewed in your browser at http://localhost:8000/

Any changes made locally will cause the site to rebuild automagically.

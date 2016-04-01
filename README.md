# Fantasy Football League Stats
-----
## Set up for local environment
-----
### Requirements
This Django project runs using Python 2.7.11
Install the requirements as follows:
```shell
cd <path to fantasy_football_league_stats directory>/fpldjango
pip install -r requirements.txt
```
To install PostgreSQL:  
*Mac via Brew:*
```shell
brew install postgres
```  
*Linux via apt-get:  
```shell
sudo apt-get install postgresql postgresql-contrib
```

### Running the website
To run the website locally:
```shell
cd <path to fantasy_football_league_stats directory>/fpldjango
python manage.py runserver
```
You will also need to start PostgreSQL  
*Mac:*
```shell
postgres -D /usr/local/var/postgres
```
*Linux:*
```shell
sudo -i -u postgres
```
The site can be viewed in your browser at http://localhost:8000

Any changes made locally will cause the site to rebuild automagically.

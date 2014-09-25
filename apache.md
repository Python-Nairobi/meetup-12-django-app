Apache + mod_wsgi
================
## Prerequisites
1. `sudo apt-get install apache2`
2. `sudo apt-get install libapache2-mod-wsgi`


## Steps
1. git clone git@github.com:Python-Nairobi/meetup-12-django-app.git meet12
2. virtualenv meet12/.venv
3. source meet12/.venv/bin/activate
4. pip install -r apache_requirements.txt
5. Set up an apache basic configuration file for meet12 application
   using reference 2 and 3.




## Reference links
1. https://www.digitalocean.com/community/tutorials/installing-mod_wsgi-on-ubuntu-12-04
2. https://docs.djangoproject.com/en/1.4/howto/deployment/wsgi/modwsgi/
3. https://code.google.com/p/modwsgi/wiki/IntegrationWithDjango


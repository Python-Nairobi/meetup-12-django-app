Nginx + Gunicorn
================

##Steps
1. git clone git@github.com:Python-Nairobi/meetup-12-django-app.git meet12
2. virtualenv meet12/.venv
3. source meet12/.venv/bin/activate
4. pip install -r nginx_requirements.txt
5. apt-get install nginx
6. service nginx start
7. gunicorn -b 0.0.0.0:8080 wsgi

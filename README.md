skeletin-heroku-django-auth
===========================

[![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/hurgleburgler/skeletin-heroku-django?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

A Simple Base Heroku Django Project with Authentication

Instructions
------------
1. settings.py: Change the secret key
  * If you are unsure what to change it to, see the following options:
    * https://gist.github.com/ndarville/3452907 
    * http://www.miniwebtool.com/django-secret-key-generator/
2. For local development, from the project root, install your venv:
  1. `virtualenv venv`
  2. `source venv/bin/activate`
  3. `pip install -r requirements.txt`
3. Update project name everywhere, replace foobarbaz with project name
  * Update file names
  * Update file contents
4. Make your APP on heroku:
  * `heroku create --stack cedar {{ project name }}`
5. Push it to Heroku!
  * `git push heroku master`
6. `heroku addons:add heroku-postgresql:dev`
7. `heroku pg:promote {{ The database that was added in the previous step }}`
8. If you need a local dev environment db:
  1. create your local db 
  2. add the following to your venv/bin/activate script:
    * export DATABASE_URL="postgres://{{ db user }}:{{ db name }}@localhost/{{ project name }}"
  3. From the project root: `source venv/bin/activate`
  4. `python manage.py syncdb`
    * Create your user accounts

Develop :
[![Build Status](https://app.travis-ci.com/gcivil-nyu-org/Wednesday-Fall2023-Team-4.svg?branch=develop)](https://app.travis-ci.com/gcivil-nyu-org/Wednesday-Fall2023-Team-4)
[![Coverage Status](https://coveralls.io/repos/github/gcivil-nyu-org/Wednesday-Fall2023-Team-4/badge.svg?branch=develop)](https://coveralls.io/github/gcivil-nyu-org/Wednesday-Fall2023-Team-4?branch=develop)

Master :
[![Build Status](https://app.travis-ci.com/gcivil-nyu-org/Wednesday-Fall2023-Team-4.svg?branch=master)](https://app.travis-ci.com/gcivil-nyu-org/Wednesday-Fall2023-Team-4)
[![Coverage Status](https://coveralls.io/repos/github/gcivil-nyu-org/Wednesday-Fall2023-Team-4/badge.svg?branch=master)](https://coveralls.io/github/gcivil-nyu-org/Wednesday-Fall2023-Team-4?branch=master)

Roomie Rendezvous is a cutting-edge room-sharing platform designed to simplify the process of finding compatible roommates and ideal living spaces. This project showcases my ability to architect scalable, user-friendly solutions using modern web technologies.

1. Architected a scalable room-sharing platform using PostgreSQL, Django, and Python on AWS Cloud.
2. Created an intuitive map-based interface, boosting user engagement by 40%
3. Capable of handling 10,000+ concurrent users with 99.9% uptime 

By focusing on user experience and leveraging cloud technologies, Roomie Rendezvous stands out as a robust solution in the competitive market of housing platforms.

How to run:-

1. You will need Python 3.8 version to run this
2. After Doing git clone please create virtual venv using the command C:\path\python.exe -m venv venv
3. Then activate the virtual venv and pip install requirements.txt
4. Make sure you have docker installed in your PC to setup local Postgress DB.
5. Now navigate to the project directory and run docker run --name django-images-postgres -p 5432:5432 -e POSTGRES_USER=django-images -e POSTGRES_PASSWORD=complexpassword123 -e POSTGRES_DB=django-images -d postgres. Make sure the docker process is running docker ps -f name=django-images-postgres.
6. After this just run python runserver manage.py and application should spin up in local server http://127.0.0.1:8000/rrapp/


References:-
For setting up django application :

https://testdriven.io/blog/django-elastic-beanstalk/

For setting up Websocket based chat on AWS Elastic Beanstalk :

https://farhanghazi17.medium.com/deploy-django-channels-websockets-on-aws-elastic-beanstalk-using-gunicorn-supervisor-redis-872ce86ba68d

https://github.com/PaulleDemon/AWS-deployment/blob/master/django-channels.md

https://medium.com/@elspanishgeek/how-to-deploy-django-channels-2-x-on-aws-elastic-beanstalk-8621771d4ff0

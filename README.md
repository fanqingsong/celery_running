# celery_running 

    give a runnable demostration to help understanding distributing tasks runner concept.

# prerequisite

    install rabbitMQ, reference : https://www.cnblogs.com/lightsong/p/10714091.html
    and assure RabbitMQ is running

# install & run
    #install dependency
    pipenv install

    #run tasks proccess
    pipenv run celery -A tasks worker --loglevel=info -P eventlet

    # run producer
    pipenv run python taskscaller.py




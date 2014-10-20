from celery import task

@task()
def light_on():
    print 'light'

@task()
def light_off():
    print 'light off'



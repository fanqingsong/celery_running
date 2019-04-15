# tasks caller

from tasks import sendmail

sendmail.delay(dict(to='celery@python.org'))

print("call done")


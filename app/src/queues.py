import os

from redis import Redis
from rq import Queue

SLOW_QUEUE = 'slow'
FAST_QUEUE = 'fast'


def get_queue(name):
    return Queue(name=name, connection=Redis(
        host=os.environ.get('REDIS_HOST', "127.0.0.1"),
    ))

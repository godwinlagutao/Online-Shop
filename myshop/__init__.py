#import celery
from .celery import app as celery_app 

__all__ = ['celery_app']

# sudo docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672
# celery -A myshop worker -1 info
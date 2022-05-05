from django.apps import AppConfig
import redis


class NewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news'

    def ready(self):
        import news.signals


class PostConfig(AppConfig):
    name = 'news1'
 
    def ready(self):
        import news.signals


red = redis.Redis(
    host ='redis-10094.c296.ap-southeast-2-1.ec2.cloud.redislabs.com',
    port = 10094,
    password='Mvd5hnt5RHZ1YDif1KbkGOJfiL6GIC13'
)
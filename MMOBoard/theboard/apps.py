from django.apps import AppConfig


class TheboardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'theboard'

    def ready(self):
        import theboard.signals

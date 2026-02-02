from django.apps import AppConfig


class HelpRequestsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'help_requests'

    def ready(self):
        import help_requests.signals

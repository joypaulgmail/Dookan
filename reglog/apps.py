from django.apps import AppConfig


class ReglogConfig(AppConfig):
    name = 'reglog'
    def ready(self):
        import reglog.signals


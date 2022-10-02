from django.conf import settings as conf_settings


def django_settings(request):
    config_dict = conf_settings.CURRENT_CONFIG
    config_dict.update(conf_settings.DATABASES)
    return {'DJANGO_SETTINGS': config_dict}

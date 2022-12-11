from django.conf import settings as conf_settings


def django_settings(request):
    config_dict = conf_settings.CURRENT_CONFIG
    config_dict.update(conf_settings.DATABASES)
    config_dict["version"] = "v1 - updated: 2022-12-11"
    return {"DJANGO_SETTINGS": config_dict}

from django.apps import apps
from django.contrib import admin

app_models = apps.get_app_config('api').get_models()
for model in app_models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass

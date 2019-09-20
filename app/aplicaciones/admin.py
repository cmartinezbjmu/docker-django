from django.contrib import admin
from .models import APP, APP_TESTING_ROUND, E2E_TEST
# Register your models here.
admin.site.register(APP)
admin.site.register(APP_TESTING_ROUND)
admin.site.register(E2E_TEST)
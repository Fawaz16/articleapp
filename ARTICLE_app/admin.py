from django.contrib import admin
from .models import Opinion, Topic, Business, Weekend
# Register your models here.
admin.site.register(Topic)
admin.site.register(Business)
admin.site.register(Weekend)
admin.site.register(Opinion)


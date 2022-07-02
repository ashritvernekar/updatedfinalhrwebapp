from django.contrib import admin
from .models import basicinfo,consultant,skills,education

# Register your models here.
admin.site.register(basicinfo)
admin.site.register(consultant)
admin.site.register(skills)
admin.site.register(education)
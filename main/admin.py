from django.contrib import admin
from .models import Writers, FAQ, Feedback

admin.site.register(Writers)
admin.site.register(FAQ)
admin.site.register(Feedback)
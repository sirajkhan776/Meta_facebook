from django.contrib import admin

from .models import *


admin.site.register(user_regis)
admin.site.register(product)
admin.site.register(category)
admin.site.register(order)

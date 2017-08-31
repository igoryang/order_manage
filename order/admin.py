from django.contrib import admin

# Register your models here.
from order import models

# admin.site.register(models.cis,models.ci_type,models.ci_order,models.ci_product)

admin.site.register(models.cis)
admin.site.register(models.ci_type)
admin.site.register(models.ci_order)
admin.site.register(models.ci_product)
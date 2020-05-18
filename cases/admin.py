from django.contrib import admin
from .models import Visual


@admin.register(Visual)
class VisualAdmin(admin.ModelAdmin):
    readonly_fields = [
        "time_created",
        "last_updated",
    ]


# @admin.register(KenyanCase)
# class KenyanCaseAdmin(admin.ModelAdmin):
#     readonly_fields = [
#         "time_created",
#         "last_updated",
#     ]

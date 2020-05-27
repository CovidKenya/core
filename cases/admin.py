from django.contrib import admin
from .models import Visual, KenyanCase, VisualCountry, VisualCases, VisualRecovered, VisualDeaths

admin.site.register(VisualCases)
admin.site.register(VisualCountry)
admin.site.register(VisualRecovered)
admin.site.register(VisualDeaths)


@admin.register(Visual)
class VisualAdmin(admin.ModelAdmin):
    readonly_fields = [
        "time_created",
        "last_updated",
    ]


@admin.register(KenyanCase)
class KenyanCaseAdmin(admin.ModelAdmin):
    readonly_fields = [
        "time_created",
        "last_updated",
    ]

from django.contrib import admin
from .models import Issue, Status

class IssueAdmin(admin.ModelAdmin):
    list_display =[
        "summary", "description"
    ]


admin.site.register(Issue, IssueAdmin)
admin.site.register(Status)
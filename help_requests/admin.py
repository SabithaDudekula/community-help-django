from django.contrib import admin
from .models import HelpRequest


@admin.register(HelpRequest)
class HelpRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'location', 'status', 'created_at')
    list_filter = ('category', 'status')
    search_fields = ('title', 'location')


from .models import UserProfile

admin.site.register(UserProfile)

from django.contrib import admin
from .models import User, Team, TeamMembership, EmployeeProfile, TeamLeaderProfile

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'role', 'department', 'date_of_joining')
    list_filter = ('role', 'department')
    search_fields = ('username', 'email')

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'tech_stack', 'leader')
    search_fields = ('name', 'tech_stack')

@admin.register(TeamMembership)
class TeamMembershipAdmin(admin.ModelAdmin):
    list_display = ('id', 'team', 'user', 'joined_at')

@admin.register(EmployeeProfile)
class EmployeeProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'points', 'notify_status', 'tasks_completed')
    def has_add_permission(self, request):
        return False
    
@admin.register(TeamLeaderProfile)
class TeamLeaderProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)
    def has_add_permission(self, request):
        return False

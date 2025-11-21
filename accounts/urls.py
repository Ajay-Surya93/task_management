from django.urls import path
from .views import CreateUserView, ListUsersView, TeamCreateView, AssignUserToTeam, TeamMembersView

urlpatterns = [
    path('users/', ListUsersView.as_view(), name='list-users'),
    path('users/create/', CreateUserView.as_view(), name='create-user'),
    path('teams/create/', TeamCreateView.as_view(), name='create-team'),
    path('teams/assign/', AssignUserToTeam.as_view(), name='assign-team'),
    path('teams/<int:team_id>/members/', TeamMembersView.as_view(), name='team-members'),
]

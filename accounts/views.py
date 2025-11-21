from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import User, Team, TeamMembership, EmployeeProfile, TeamLeaderProfile
from .serializers import UserSerializer, UserCreateSerializer, TeamSerializer, TeamMembershipSerializer
from .permissions import IsAdminOrTL, IsAdmin
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView

class CreateUserView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdmin]

class ListUsersView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsAdmin]

class TeamCreateView(generics.CreateAPIView):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsAdmin]

class AssignUserToTeam(APIView):
    permission_classes = [permissions.IsAuthenticated, IsAdminOrTL]

    def post(self, request):
        team_id = request.data.get('team_id')
        user_id = request.data.get('user_id')
        team = get_object_or_404(Team, pk=team_id)
        user = get_object_or_404(User, pk=user_id)
        TeamMembership.objects.get_or_create(team=team, user=user)
        return Response({'detail':'Assigned'}, status=status.HTTP_200_OK)

class TeamMembersView(generics.ListAPIView):
    serializer_class = TeamMembershipSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        team_id = self.kwargs.get('team_id')
        return TeamMembership.objects.filter(team_id=team_id)

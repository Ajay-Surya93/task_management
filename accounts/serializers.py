from rest_framework import serializers
from .models import User, Team, TeamMembership, EmployeeProfile, TeamLeaderProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','first_name','last_name','role','contact_number','department','date_of_joining']

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password','role','contact_number','department']

    def create(self, validated_data):
        pwd = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(pwd)
        user.save()
        # create default profile
        if user.role == 'employee':
            EmployeeProfile.objects.create(user=user)
        if user.role == 'teamleader':
            TeamLeaderProfile.objects.create(user=user)
        return user

class TeamSerializer(serializers.ModelSerializer):
    leader = UserSerializer(read_only=True)
    class Meta:
        model = Team
        fields = '__all__'

class TeamMembershipSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = TeamMembership
        fields = '__all__'

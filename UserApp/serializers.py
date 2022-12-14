from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *





# For user list serializer
class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        field = '__all__'
        exclude = ['password', 'is_superuser', 'is_staff', 'is_active', 'date_joined', 'last_login', 'groups', 'user_permissions']


# For user detail serializer
class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']




# For user all info serializer
class UserAllInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'





# For personal info add and update serializer
class PersonalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalInfo
        field = '__all__'
        exclude = ['user']


# For personal info detail serializer
class PersonalInfoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalInfo
        fields = '__all__'





# For academic info add and update serializer
class AcademicInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicInfo
        field = '__all__'
        exclude = ['user']


# For academic info detail serializer
class AcademicInfoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicInfo
        fields = '__all__'





# For training info add and update serializer
class TrainingInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingInfo
        field = '__all__'
        exclude = ['user']


# For training info detail serializer
class TrainingInfoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingInfo
        fields = '__all__'





# For teaching info add and update serializer
class TeachingInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeachingInfo
        field = '__all__'
        exclude = ['user']


# For teaching info detail serializer
class TeachingInfoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeachingInfo
        fields = '__all__'





# For publication info add and update serializer
class PublicationInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicationInfo
        field = '__all__'
        exclude = ['user']


# For publication info detail serializer
class PublicationInfoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicationInfo
        fields = '__all__'





# For award & scholarship info add and update serializer
class AwardAndScholarshipInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AwardAndScholarshipInfo
        field = '__all__'
        exclude = ['user']

# For award & scholarship info detail serializer
class AwardAndScholarshipInfoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = AwardAndScholarshipInfo
        fields = '__all__'





# For experience info add and update serializer
class ExperienceInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienceInfo
        field = '__all__'
        exclude = ['user']


# For experience info detail serializer
class ExperienceInfoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienceInfo
        fields = '__all__'
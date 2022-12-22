from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from django.contrib.auth.models import User
from .serializers import *
from .models import *





# Users List API
class UserListAPI(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    
    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        personalInfoSerializer = PersonalInfoDetailSerializer(PersonalInfo.objects.all(), many=True)

        if serializer.data:
            for data in serializer.data:
                for personalInfo in personalInfoSerializer.data:
                    if data['id'] == personalInfo['user']:
                        data['personal_info'] = personalInfo
            return Response({'status': True, 'message': 'Users list', 'data': serializer.data})
        else:
            return Response({'status': False, 'message': 'No user found'})


# User Detail API
# class UserDetailApi(RetrieveUpdateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserDetailSerializer
#     permission_classes = [IsAuthenticated]

#     def retrieve(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = UsersSerializer(instance)
#         return Response({'status': True, 'message': 'User detail', 'data': serializer.data})

#     def update(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = UserDetailSerializer(instance, data=request.data)
#         returnSerializer = UsersSerializer(instance)
        
#         if request.user == instance:
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response({'status': True, 'message': 'User updated successfully', 'data': returnSerializer.data})
#             else:
#                 return Response({'status': False, 'message': 'User not updated', 'data': serializer.errors})
#         else:
#             return Response({'status': False, 'message': 'You are not authorized to update this user'})
class UserDetailApi(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            user = User.objects.get(id=pk)
            serializer = UsersSerializer(user)
            personalInfoSerializer = PersonalInfoDetailSerializer(PersonalInfo.objects.get(user=user))

            if serializer.data:
                serializer.data['personal_info'] = personalInfoSerializer.data
                return Response({'status': True, 'message': 'User detail', 'data': serializer.data})
            else:
                return Response({'status': False, 'message': 'No user found'})
        except User.DoesNotExist:
            return Response({'status': False, 'message': 'No user found'})

    def put(self, request, pk):
        try:
            user = User.objects.get(id=pk)
            serializer = UserDetailSerializer(user, data=request.data)
            returnSerializer = UsersSerializer(user)

            if request.user == user:
                if serializer.is_valid():
                    serializer.save()
                    return Response({'status': True, 'message': 'User updated successfully', 'data': returnSerializer.data})
                else:
                    return Response({'status': False, 'message': 'User not updated', 'data': serializer.errors})
            else:
                return Response({'status': False, 'message': 'You are not authorized to update this user'})
        except User.DoesNotExist:
            return Response({'status': False, 'message': 'No user found'})


        




# User personal info add API
class UserPersonalInfoAddAPI(CreateAPIView):
    queryset = PersonalInfo.objects.all()
    serializer_class = PersonalInfoSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        serializer = PersonalInfoSerializer(data=request.data)

        if PersonalInfo.objects.filter(user=user).exists():
            return Response({'status': False, 'message': 'Personal info already exists'})
        elif serializer.is_valid():
            serializer.save(user=user)
            return Response({'status': True, 'message': 'Personal info added successfully', 'data': serializer.data})
        else:
            return Response({'status': False, 'message': 'Personal info not added', 'data': serializer.errors})


# User personal info detail and update API
class UserPersonalInfoAPI(RetrieveUpdateAPIView):
    queryset = PersonalInfo.objects.all()
    serializer_class = PersonalInfoDetailSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({'status': True, 'message': 'Personal info detail', 'data': serializer.data})

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = PersonalInfoSerializer(instance, data=request.data)
        if request.user == instance.user:
            if serializer.is_valid():
                serializer.save()
                return Response({'status': True, 'message': 'Personal info updated successfully', 'data': serializer.data})
            else:
                return Response({'status': False, 'message': 'Personal info not updated', 'data': serializer.errors})
        else:
            return Response({'status': False, 'message': 'You are not authorized to update this personal info'})





# User academic info list and add API
class UserAcademicInfoListCreateAPI(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = AcademicInfo.objects.all()
    serializer_class = AcademicInfoSerializer

    def list(self, request, *args, **kwargs):
        queryset = AcademicInfo.objects.all()
        serializer = AcademicInfoDetailSerializer(queryset, many=True)
        return Response({'Status': True, 'message': 'Academic info list', 'data': serializer.data})

    def create(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        serializer = AcademicInfoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=user)
            return Response({'status': True, 'message': 'Academic info added successfully', 'data': serializer.data})
        else:
            return Response({'status': False, 'message': 'Academic info not added', 'data': serializer.errors})


# User academic info detail and update API
class UserAcademicInfoAPI(RetrieveUpdateDestroyAPIView):
    queryset = AcademicInfo.objects.all()
    serializer_class = AcademicInfoDetailSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({'status': True, 'message': 'Academic info detail', 'data': serializer.data})

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = AcademicInfoSerializer(instance, data=request.data)

        if request.user == instance.user:
            if serializer.is_valid():
                serializer.save()
                return Response({'status': True, 'message': 'Academic info updated successfully', 'data': serializer.data})
            else:
                return Response({'status': False, 'message': 'Academic info not updated', 'data': serializer.errors})
        else:
            return Response({'status': False, 'message': 'You are not authorized to update this academic info'})

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user == instance.user:
            instance.delete()
            return Response({'status': True, 'message': 'Academic info deleted successfully'})
        else:
            return Response({'status': False, 'message': 'You are not authorized to delete this academic info'})





# User training info list and add API
class UserTrainingInfoListCreateAPI(ListCreateAPIView):
    queryset = TrainingInfo.objects.all()
    serializer_class = TrainingInfoSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = TrainingInfo.objects.all()
        serializer = TrainingInfoDetailSerializer(queryset, many=True)
        return Response({'Status': True, 'message': 'Training info list', 'data': serializer.data})

    def create(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        serializer = TrainingInfoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=user)
            return Response({'status': True, 'message': 'Training info added successfully', 'data': serializer.data})
        else:
            return Response({'status': False, 'message': 'Training info not added', 'data': serializer.errors})


# User training info detail and update API
class UserTrainingInfoAPI(RetrieveUpdateDestroyAPIView):
    queryset = TrainingInfo.objects.all()
    serializer_class = TrainingInfoDetailSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({'status': True, 'message': 'Training info detail', 'data': serializer.data})

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = TrainingInfoSerializer(instance, data=request.data)

        if request.user == instance.user:
            if serializer.is_valid():
                serializer.save()
                return Response({'status': True, 'message': 'Training info updated successfully', 'data': serializer.data})
            else:
                return Response({'status': False, 'message': 'Training info not updated', 'data': serializer.errors})
        else:
            return Response({'status': False, 'message': 'You are not authorized to update this training info'})

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user == instance.user:
            instance.delete()
            return Response({'status': True, 'message': 'Training info deleted successfully'})
        else:
            return Response({'status': False, 'message': 'You are not authorized to delete this training info'})





# User teaching info list and add API
class UserTeachingInfoListCreateAPI(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = TeachingInfo.objects.all()
    serializer_class = TeachingInfoSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = TeachingInfoDetailSerializer(queryset, many=True)
        return Response({'Status': True, 'message': 'Teaching info list', 'data': serializer.data})

    def create(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        serializer = TeachingInfoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=user)
            return Response({'status': True, 'message': 'Teaching info added successfully', 'data': serializer.data})
        else:
            return Response({'status': False, 'message': 'Teaching info not added', 'data': serializer.errors})

    
# User teaching info detail API
class UserTeachingInfoAPI(RetrieveUpdateDestroyAPIView):
    queryset = TeachingInfo.objects.all()
    serializer_class = TeachingInfoDetailSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({'status': True, 'message': 'Teaching info detail', 'data': serializer.data})

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = TeachingInfoSerializer(instance, data=request.data)

        if request.user == instance.user:
            if serializer.is_valid():
                serializer.save()
                return Response({'status': True, 'message': 'Teaching info updated successfully', 'data': serializer.data})
            else:
                return Response({'status': False, 'message': 'Teaching info not updated', 'data': serializer.errors})
        else:
            return Response({'status': False, 'message': 'You are not authorized to update this teaching info'})

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user == instance.user:
            instance.delete()
            return Response({'status': True, 'message': 'Teaching info deleted successfully'})
        else:
            return Response({'status': False, 'message': 'You are not authorized to delete this teaching info'})




# User publication info list and add API
class UserPublicationInfoListCreateAPI(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = PublicationInfo.objects.all()
    serializer_class = PublicationInfoSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = PublicationInfoDetailSerializer(queryset, many=True)
        return Response({'Status': True, 'message': 'Publication info list', 'data': serializer.data})

    def create(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        serializer = PublicationInfoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=user)
            return Response({'status': True, 'message': 'Publication info added successfully', 'data': serializer.data})
        else:
            return Response({'status': False, 'message': 'Publication info not added', 'data': serializer.errors})


# User publication info detail and update API
class UserPublicationInfoAPI(RetrieveUpdateDestroyAPIView):
    queryset = PublicationInfo.objects.all()
    serializer_class = PublicationInfoDetailSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({'status': True, 'message': 'Publication info detail', 'data': serializer.data})

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = PublicationInfoSerializer(instance, data=request.data)

        if request.user == instance.user:
            if serializer.is_valid():
                serializer.save()
                return Response({'status': True, 'message': 'Publication info updated successfully', 'data': serializer.data})
            else:
                return Response({'status': False, 'message': 'Publication info not updated', 'data': serializer.errors})
        else:
            return Response({'status': False, 'message': 'You are not authorized to update this publication info'})

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user == instance.user:
            instance.delete()
            return Response({'status': True, 'message': 'Publication info deleted successfully'})
        else:
            return Response({'status': False, 'message': 'You are not authorized to delete this publication info'})





# User award and scholarship info list and add API
class UserAwardAndScholarshipInfoListCreateAPI(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = AwardAndScholarshipInfo.objects.all()
    serializer_class = AwardAndScholarshipInfoSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = AwardAndScholarshipInfoDetailSerializer(queryset, many=True)
        return Response({'Status': True, 'message': 'Award and scholarship info list', 'data': serializer.data})

    def create(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        serializer = AwardAndScholarshipInfoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=user)
            return Response({'status': True, 'message': 'Award and scholarship info added successfully', 'data': serializer.data})
        else:
            return Response({'status': False, 'message': 'Award and scholarship info not added', 'data': serializer.errors})


# User award and scholarship info detail and update API
class UserAwardAndScholarshipInfoAPI(RetrieveUpdateDestroyAPIView):
    queryset = AwardAndScholarshipInfo.objects.all()
    serializer_class = AwardAndScholarshipInfoDetailSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({'status': True, 'message': 'Award and scholarship info detail', 'data': serializer.data})

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = AwardAndScholarshipInfoSerializer(instance, data=request.data)

        if request.user == instance.user:
            if serializer.is_valid():
                serializer.save()
                return Response({'status': True, 'message': 'Award and scholarship info updated successfully', 'data': serializer.data})
            else:
                return Response({'status': False, 'message': 'Award and scholarship info not updated', 'data': serializer.errors})
        else:
            return Response({'status': False, 'message': 'You are not authorized to update this award and scholarship info'})

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user == instance.user:
            instance.delete()
            return Response({'status': True, 'message': 'Award and scholarship info deleted successfully'})
        else:
            return Response({'status': False, 'message': 'You are not authorized to delete this award and scholarship info'})





# User experience info list and add API
class UserExperienceInfoListCreateAPI(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ExperienceInfo.objects.all()
    serializer_class = ExperienceInfoSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ExperienceInfoDetailSerializer(queryset, many=True)
        return Response({'Status': True, 'message': 'Experience info list', 'data': serializer.data})

    def create(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        serializer = ExperienceInfoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=user)
            return Response({'status': True, 'message': 'Experience info added successfully', 'data': serializer.data})
        else:
            return Response({'status': False, 'message': 'Experience info not added', 'data': serializer.errors})


# User experience info detail and update API
class UserExperienceInfoAPI(RetrieveUpdateDestroyAPIView):
    queryset = ExperienceInfo.objects.all()
    serializer_class = ExperienceInfoDetailSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({'status': True, 'message': 'Experience info detail', 'data': serializer.data})

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ExperienceInfoSerializer(instance, data=request.data)

        if request.user == instance.user:
            if serializer.is_valid():
                serializer.save()
                return Response({'status': True, 'message': 'Experience info updated successfully', 'data': serializer.data})
            else:
                return Response({'status': False, 'message': 'Experience info not updated', 'data': serializer.errors})
        else:
            return Response({'status': False, 'message': 'You are not authorized to update this experience info'})

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user == instance.user:
            instance.delete()
            return Response({'status': True, 'message': 'Experience info deleted successfully'})
        else:
            return Response({'status': False, 'message': 'You are not authorized to delete this experience info'})
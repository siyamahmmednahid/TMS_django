from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from django.contrib.auth.models import User
from .serializers import *
from .models import *
from TodoApp.models import *
from EmailApp.models import *



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
            return Response({
                'status': True, 
                'message': 'Users list', 
                'data': serializer.data})
        else:
            return Response({
                'status': False, 
                'message': 'No user found'})





# User Detail API
class UserDetailAPI(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, pk):
        try:
            user = User.objects.get(id=pk)
            serializer = UsersSerializer(user)

            if serializer.data:
                if PersonalInfo.objects.filter(user=user).exists():
                    personalInfo = PersonalInfo.objects.get(user=user)
                    return Response({
                        'status': True, 
                        'message': 'User detail', 
                        'data': serializer.data,
                        'personal_info': PersonalInfoDetailSerializer(personalInfo).data})
                else:
                    return Response({
                        'status': False, 
                        'message': 'User detail',
                        'data': serializer.data,
                        'personal_info': {}})
            else:
                return Response({'status': False, 'message': 'No user found'})
        except:
            return Response({'status': False, 'message': 'No user found'})


    def update(self, request, pk):
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
        except:
            return Response({'status': False, 'message': 'No user found'})
        




# User incomplete todo count API
class UserIncompleteTodoCountAPI(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, pk):
        Assignee = User.objects.get(id=pk)
        incompleteTasks = Todo.objects.filter(Assignee=Assignee, TaskCompleted=False).count()
        return Response({'status': True, 'message': 'Incomplete tasks count', 'data': incompleteTasks})
    




# User unread email count API
class UserUnreadEmailCountAPI(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, pk):
        user = User.objects.get(id=pk)
        toReadEmails = Email.objects.filter(Receiver=user, ReceiverRead=False).count()
        ccReadEmails = Email.objects.filter(Cc=user, CcRead=False).count()
        bccReadEmails = Email.objects.filter(Bcc=user, BccRead=False).count()
        unreadEmails = toReadEmails + ccReadEmails + bccReadEmails
        return Response({'status': True, 'message': 'Unread emails count', 'data': unreadEmails})
    




# User deactivate API
class UserDeactivateAPI(UpdateAPIView):
    permission_classes = [IsAuthenticated]

    def update(self, request, pk):
        try:
            user = User.objects.get(id=pk)
            serializer = UserDeactiveSerializer(user, data=request.data)
            if request.user.is_superuser:
                if serializer.is_valid():
                    serializer.save()
                    return Response({'status': True, 'message': 'Update successfully'})
                else:
                    return Response({'status': False, 'message': 'Update failed', 'data': serializer.errors})
            else:
                return Response({'status': False, 'message': 'You are not authorized to deactivate this user'})
        except:
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

    def retrieve(self, request, pk):
        try:
            user = User.objects.get(id=pk)
            if PersonalInfo.objects.filter(user=user).exists():
                personalInfo = PersonalInfo.objects.get(user=user)
                serializer = self.get_serializer(personalInfo)
                return Response({'status': True, 'message': 'Personal info detail', 'data': serializer.data})
            else:
                return Response({'status': False, 'message': 'No personal info found'})
        except:
            return Response({'status': False, 'message': 'No personal info found'})

    def update(self, request, pk):
        try:
            user = User.objects.get(id=pk)
            if PersonalInfo.objects.filter(user=user).exists():
                personalInfo = PersonalInfo.objects.get(user=user)
                serializer = PersonalInfoSerializer(personalInfo, data=request.data)
                if request.user == user:
                    if serializer.is_valid():
                        serializer.save()
                        return Response({'status': True, 'message': 'Personal info updated successfully', 'data': serializer.data})
                    else:
                        return Response({'status': False, 'message': 'Personal info not updated', 'data': serializer.errors})
                else:
                    return Response({'status': False, 'message': 'You are not authorized to update this personal info'})
            else:
                return Response({'status': False, 'message': 'No personal info found'})
        except:
            return Response({'status': False, 'message': 'No personal info found'})





# User academic info list and add API
class UserAcademicInfoListCreateAPI(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = AcademicInfo.objects.all()
    serializer_class = AcademicInfoSerializer

    def list(self, request, *args, **kwargs):
        queryset = AcademicInfo.objects.all().order_by('-id')
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

    def retrieve(self, request, pk):
        try:
            academicInfo = AcademicInfo.objects.get(id=pk)
            serializer = AcademicInfoDetailSerializer(academicInfo)
            return Response({'status': True, 'message': 'Academic info detail', 'data': serializer.data})
        except:
            return Response({'status': False, 'message': 'No academic info found'})

    def update(self, request, pk):
        try:
            academicInfo = AcademicInfo.objects.get(id=pk)
            serializer = AcademicInfoSerializer(academicInfo, data=request.data)

            if request.user == academicInfo.user:
                if serializer.is_valid():
                    serializer.save()
                    return Response({'status': True, 'message': 'Academic info updated successfully', 'data': serializer.data})
                else:
                    return Response({'status': False, 'message': 'Academic info not updated', 'data': serializer.errors})
            else:
                return Response({'status': False, 'message': 'You are not authorized to update this academic info'})
        except:
            return Response({'status': False, 'message': 'No academic info found'})

    def destroy(self, request, pk):
        try:
            academicInfo = AcademicInfo.objects.get(id=pk)
            if request.user == academicInfo.user:
                academicInfo.delete()
                return Response({'status': True, 'message': 'Academic info deleted successfully'})
            else:
                return Response({'status': False, 'message': 'You are not authorized to delete this academic info'})
        except:
            return Response({'status': False, 'message': 'No academic info found'})





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

    def retrieve(self, request, pk):
        try:
            trainingInfo = TrainingInfo.objects.get(id=pk)
            serializer = TrainingInfoDetailSerializer(trainingInfo)
            return Response({'status': True, 'message': 'Training info detail', 'data': serializer.data})
        except:
            return Response({'status': False, 'message': 'No training info found'})

    def update(self, request, pk):
        try:
            trainingInfo = TrainingInfo.objects.get(id=pk)
            serializer = TrainingInfoSerializer(trainingInfo, data=request.data)

            if request.user == trainingInfo.user:
                if serializer.is_valid():
                    serializer.save()
                    return Response({'status': True, 'message': 'Training info updated successfully', 'data': serializer.data})
                else:
                    return Response({'status': False, 'message': 'Training info not updated', 'data': serializer.errors})
            else:
                return Response({'status': False, 'message': 'You are not authorized to update this training info'})
        except:
            return Response({'status': False, 'message': 'No training info found'})

    def destroy(self, request, pk):
        try:
            trainingInfo = TrainingInfo.objects.get(id=pk)
            if request.user == trainingInfo.user:
                trainingInfo.delete()
                return Response({'status': True, 'message': 'Training info deleted successfully'})
            else:
                return Response({'status': False, 'message': 'You are not authorized to delete this training info'})
        except:
            return Response({'status': False, 'message': 'No training info found'})





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

    def retrieve(self, request, pk):
        try:
            teachingInfo = TeachingInfo.objects.get(id=pk)
            serializer = TeachingInfoDetailSerializer(teachingInfo)
            return Response({'status': True, 'message': 'Teaching info detail', 'data': serializer.data})
        except:
            return Response({'status': False, 'message': 'No teaching info found'})

    def update(self, request, pk):
        try:
            teachingInfo = TeachingInfo.objects.get(id=pk)
            serializer = TeachingInfoSerializer(teachingInfo, data=request.data)

            if request.user == teachingInfo.user:
                if serializer.is_valid():
                    serializer.save()
                    return Response({'status': True, 'message': 'Teaching info updated successfully', 'data': serializer.data})
                else:
                    return Response({'status': False, 'message': 'Teaching info not updated', 'data': serializer.errors})
            else:
                return Response({'status': False, 'message': 'You are not authorized to update this teaching info'})
        except:
            return Response({'status': False, 'message': 'No teaching info found'})

    def destroy(self, request, pk):
        try:
            teachingInfo = TeachingInfo.objects.get(id=pk)
            if request.user == teachingInfo.user:
                teachingInfo.delete()
                return Response({'status': True, 'message': 'Teaching info deleted successfully'})
            else:
                return Response({'status': False, 'message': 'You are not authorized to delete this teaching info'})
        except:
            return Response({'status': False, 'message': 'No teaching info found'})




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

    def retrieve(self, request, pk):
        try:
            publicationInfo = PublicationInfo.objects.get(id=pk)
            serializer = PublicationInfoDetailSerializer(publicationInfo)
            return Response({'status': True, 'message': 'Publication info detail', 'data': serializer.data})
        except:
            return Response({'status': False, 'message': 'No publication info found'})

    def update(self, request, pk):
        try:
            publicationInfo = PublicationInfo.objects.get(id=pk)
            serializer = PublicationInfoSerializer(publicationInfo, data=request.data)

            if request.user == publicationInfo.user:
                if serializer.is_valid():
                    serializer.save()
                    return Response({'status': True, 'message': 'Publication info updated successfully', 'data': serializer.data})
                else:
                    return Response({'status': False, 'message': 'Publication info not updated', 'data': serializer.errors})
            else:
                return Response({'status': False, 'message': 'You are not authorized to update this publication info'})
        except:
            return Response({'status': False, 'message': 'No publication info found'})

    def destroy(self, request, pk):
        try:
            publicationInfo = PublicationInfo.objects.get(id=pk)
            if request.user == publicationInfo.user:
                publicationInfo.delete()
                return Response({'status': True, 'message': 'Publication info deleted successfully'})
            else:
                return Response({'status': False, 'message': 'You are not authorized to delete this publication info'})
        except:
            return Response({'status': False, 'message': 'No publication info found'})





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

    def retrieve(self, request, pk):
        try:
            awardAndScholarshipInfo = AwardAndScholarshipInfo.objects.get(id=pk)
            serializer = AwardAndScholarshipInfoDetailSerializer(awardAndScholarshipInfo)
            return Response({'status': True, 'message': 'Award and scholarship info detail', 'data': serializer.data})
        except:
            return Response({'status': False, 'message': 'No award and scholarship info found'})

    def update(self, request, pk):
        try:
            awardAndScholarshipInfo = AwardAndScholarshipInfo.objects.get(id=pk)
            serializer = AwardAndScholarshipInfoSerializer(awardAndScholarshipInfo, data=request.data)

            if request.user == awardAndScholarshipInfo.user:
                if serializer.is_valid():
                    serializer.save()
                    return Response({'status': True, 'message': 'Award and scholarship info updated successfully', 'data': serializer.data})
                else:
                    return Response({'status': False, 'message': 'Award and scholarship info not updated', 'data': serializer.errors})
            else:
                return Response({'status': False, 'message': 'You are not authorized to update this award and scholarship info'})
        except:
            return Response({'status': False, 'message': 'No award and scholarship info found'})

    def destroy(self, request, pk):
        try:
            awardAndScholarshipInfo = AwardAndScholarshipInfo.objects.get(id=pk)
            if request.user == awardAndScholarshipInfo.user:
                awardAndScholarshipInfo.delete()
                return Response({'status': True, 'message': 'Award and scholarship info deleted successfully'})
            else:
                return Response({'status': False, 'message': 'You are not authorized to delete this award and scholarship info'})
        except:
            return Response({'status': False, 'message': 'No award and scholarship info found'})





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

    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)
    #     return Response({'status': True, 'message': 'Experience info detail', 'data': serializer.data})
    def retrieve(self, request, pk):
        try:
            experienceInfo = ExperienceInfo.objects.get(id=pk)
            serializer = ExperienceInfoDetailSerializer(experienceInfo)
            return Response({'status': True, 'message': 'Experience info detail', 'data': serializer.data})
        except:
            return Response({'status': False, 'message': 'No experience info found'})

    def update(self, request, pk):
        try:
            experienceInfo = ExperienceInfo.objects.get(id=pk)
            serializer = ExperienceInfoSerializer(experienceInfo, data=request.data)

            if request.user == experienceInfo.user:
                if serializer.is_valid():
                    serializer.save()
                    return Response({'status': True, 'message': 'Experience info updated successfully', 'data': serializer.data})
                else:
                    return Response({'status': False, 'message': 'Experience info not updated', 'data': serializer.errors})
            else:
                return Response({'status': False, 'message': 'You are not authorized to update this experience info'})
        except:
            return Response({'status': False, 'message': 'No experience info found'})

    def destroy(self, request, pk):
        try:
            experienceInfo = ExperienceInfo.objects.get(id=pk)
            if request.user == experienceInfo.user:
                experienceInfo.delete()
                return Response({'status': True, 'message': 'Experience info deleted successfully'})
            else:
                return Response({'status': False, 'message': 'You are not authorized to delete this experience info'})
        except:
            return Response({'status': False, 'message': 'No experience info found'})
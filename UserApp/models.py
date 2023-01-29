from django.db import models
from django.contrib.auth.models import User, AbstractUser
import uuid


# For user personal info model
class PersonalInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='user')
    ProfilePic = models.ImageField(upload_to='profile_pics', blank=True)
    EmployeeID = models.CharField(max_length=20, blank=True)
    Phone = models.CharField(max_length=14, blank=True)
    Designation = models.CharField(max_length=200, blank=True)
    Department = models.CharField(max_length=100, blank=True)
    Gender_Choices = (
        ('0', 'Select'),
        ('1', 'Male'),
        ('2', 'Female'),
        ('3', 'Other'),
    )
    Gender = models.CharField(max_length=10, choices=Gender_Choices, default=0)
    BloodGroup_Choices = (
        ('0', 'Select'),
        ('1', 'A+'),
        ('2', 'A-'),
        ('3', 'B+'),
        ('4', 'B-'),
        ('5', 'AB+'),
        ('6', 'AB-'),
        ('7', 'O+'),
        ('8', 'O-'),
    )
    BloodGroup = models.CharField(max_length=10, choices=BloodGroup_Choices, default=0)
    DateOfBirth = models.DateField(blank=True, null=True)
    Nationality = models.CharField(max_length=50, blank=True)
    NIDNumber = models.CharField(max_length=17, blank=True)
    Religion_Choices = (
        ('0', 'Select'),
        ('1', 'Islam'),
        ('2', 'Hinduism'),
        ('3', 'Buddhism'),
        ('4', 'Christianity'),
    )
    Religion = models.CharField(max_length=20, choices=Religion_Choices, default=0)
    MaritalStatus_Choices = (
        ('0', 'Select'),
        ('1', 'Single'),
        ('2', 'Married'),
        ('3', 'Divorced'),
        ('4', 'Widowed'),
    )
    MaritalStatus = models.CharField(max_length=15, choices=MaritalStatus_Choices, default=0)
    PresentAddress = models.CharField(max_length=260, blank=True)
    PermanentAddress = models.CharField(max_length=260, blank=True)

    def __str__(self):
        return self.user.username



# For user education info model
class AcademicInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Degree = models.CharField(max_length=200)
    Major = models.CharField(max_length=200)
    Institute = models.CharField(max_length=200)
    PassingYear = models.CharField(max_length=4)
    CGPA = models.CharField(max_length=4, blank=True)

    def __str__(self):
        return self.user.username



class TrainingInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Title = models.CharField(max_length=200)
    Institute = models.CharField(max_length=200)
    Duration = models.CharField(max_length=200)
    Year = models.CharField(max_length=4)

    def __str__(self):
        return self.user.username



# For teaching info model
class TeachingInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    CourseCode = models.CharField(max_length=100)
    CourseTitle = models.CharField(max_length=200)
    Credit = models.CharField(max_length=2, blank=True)
    Semester = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.user.username



class PublicationInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Title = models.CharField(max_length=200)
    Journal = models.CharField(max_length=200)
    Year = models.CharField(max_length=4)
    Volume = models.CharField(max_length=10)
    Page = models.CharField(max_length=10)

    def __str__(self):
        return self.user.username



class AwardAndScholarshipInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Title = models.CharField(max_length=100)
    Organization = models.CharField(max_length=50)
    Year = models.CharField(max_length=4)

    def __str__(self):
        return self.user.username



class ExperienceInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Designation = models.CharField(max_length=200)
    Organization = models.CharField(max_length=200)
    Duration = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username
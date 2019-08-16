from django.db import models

# GENDER_CHOICES = (
#     ('Male', 'Male'),
#     ('Female', 'Female'),
#     ('Other', 'Other')
# )

# Create your models here.
class testdata(models.Model):
    studentName = models.CharField(max_length=30)
    course = models.CharField(max_length=20,blank=True,null=True)
    age = models.IntegerField()
    email = models.EmailField()
    # gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    def __str__(self):
        return self.studentName

"""
.IntegerField
.ImageField
.URLField
.PositiveIntegerField
.IpAddressField
.DateField
.DateTimeField

"""
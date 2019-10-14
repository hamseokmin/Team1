from django.db import models

# Create your models here.
class UserScheduleDB(models.Model):
    student_code = models.CharField(max_length=8,blank=True)
    time = models.CharField(max_length=50,blank=True)
    A = models.CharField(max_length=50,blank=True)
    B = models.CharField(max_length=50, blank=True)
    C = models.CharField(max_length=50, blank=True)
    D = models.CharField(max_length=50, blank=True)
    E = models.CharField(max_length=50, blank=True)
    F = models.CharField(max_length=50, blank=True)

    time50 = models.CharField(max_length=50, blank=True)
    A50 = models.CharField(max_length=50, blank=True)
    B50 = models.CharField(max_length=50, blank=True)
    C50 = models.CharField(max_length=50, blank=True)
    D50 = models.CharField(max_length=50, blank=True)
    E50 = models.CharField(max_length=50, blank=True)
    F50 = models.CharField(max_length=50, blank=True)





    def __str__(self):
        return '{} : {}'.format(self.student_code, self.time)


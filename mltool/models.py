from django.db import models

# Create your models here.

class Person(models.Model):
    
    person_name = models.CharField(max_length=200)
    person_surname = models.CharField(max_length=200)
    person_dob = models.DateField()
    
    def __str__(self):
        
        return "Person's name is " + str(self.person_name)

class Student(Person):
    student_of = models.CharField(max_length=20,default="UniSA")
    GPA = models.IntegerField()
    
class ResearchStudent(Student):
    field_of_research = models.CharField(max_length=200, default="STEM")
    
    

    
    
from django.db import models

# Create your models here.
class Student(models.Model):
    rollno=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    course=models.CharField(max_length=30)
    year=models.CharField(max_length=1)
class Book(models.Model):
    bookid=models.IntegerField(primary_key=True)
    bookname=models.CharField(max_length=50)
    isbnno=models.CharField(max_length=20)
    quantity=models.IntegerField()
    def __str__(self):
        return str(self.bookname)
class Issue(models.Model):
    r=models.ForeignKey(Student,on_delete=models.CASCADE)
    rollno=models.IntegerField()
    bookid=models.IntegerField()
    name=models.CharField(max_length=30)
    issuedate=models.DateField()
class Register(models.Model):
    user_name = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=20)
    f_name=models.CharField(max_length=20)
    l_name=models.CharField(max_length=20)
    dob=models.DateField()
    m_no=models.IntegerField()


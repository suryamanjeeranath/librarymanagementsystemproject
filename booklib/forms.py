from django import forms
from .models import Student,Issue,Book,Register
class student(forms.ModelForm):
    class Meta:
      model = Student
      fields=['rollno','name','course','year']
class book(forms.ModelForm):
    class Meta:
      model = Book
      fields=['bookid','bookname','isbnno','quantity']
class issue(forms.Form):
    #fields=['rollno','bookid']
    rollno=forms.IntegerField()
    bookid=forms.IntegerField()
class RegisterForm(forms.ModelForm):
    class Meta:
        model=Register
        fields=['user_name','password','f_name','l_name','dob','m_no']
        widgets={'password':forms.PasswordInput()}
class LoginForm(forms.Form):
    user_name=forms.CharField(max_length=30)
    password=forms.CharField(widget=forms.PasswordInput())



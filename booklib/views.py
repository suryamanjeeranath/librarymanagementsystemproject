from django.shortcuts import render
from django.http import HttpResponse
from .models import Student,Issue,Book,Register
from .forms import student,book,issue,RegisterForm,LoginForm
import datetime
def home(request):
   return render(request, 'home.html')
def reg(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponse('reg success')
        else:
            print(form.errors)
            return HttpResponse("error")
    else:
        form = RegisterForm()
        return render(request, 'reg.html',
                      {'form': form})
def login(request):
    if request.method == "POST":
        MyLoginForm = LoginForm(request.POST)
        if MyLoginForm.is_valid():
            un = MyLoginForm.cleaned_data['user_name']
            pw = MyLoginForm.cleaned_data['password']
            dbuser = Register.objects.filter(user_name=un,
                                        password=pw)
            if not dbuser:
                return HttpResponse('login faild')
            else:
                return render(request,'mainmenu.html')
    else:
        form = LoginForm()
        return render(request, 'loginpage.html'
                      , {'form': form})


def mainmenu(request):
    return render(request,'mainmenu.html')
def addStudent(request):
    if request.method=='POST':
        form=student(request.POST)
        if form.is_valid():
            form.save(commit=True)
            form = student()
            return render(request, 'addstudent.html', {'form': form})
    else:
        form=student()
        return render(request,'addstudent.html',{'form':form})
def addbook(request):
    if request.method=='POST':
        form=book(request.POST)
        if form.is_valid:
            form.save(commit=True)
            form=book()
            return render(request,'addbook.html',{'form':form})
        else:
            return HttpResponse("fail")

    else:
        form=book()
        return render(request,'addbook.html',{'form':form})
def issuebook(request):
 if request.method=='POST':
     form=issue(request.POST)
     if form.is_valid():
         rno=form.cleaned_data['rollno']
         bid=form.cleaned_data['bookid']
         d=datetime.date.today()
         #id=d[:10]
         z=Issue.objects.filter(rollno=rno)
         s=len(z)
         if s<3:
             sobj=Student.objects.filter(rollno=rno)
             sobject=sobj[0]
             p=Book.objects.filter(bookid=bid)
             bna=str(p[0])
             #bna=s[5:]
             e=Issue(r=sobject,rollno=rno,bookid=bid,name=bna,issuedate=d)
             e.save()
             form=issue()
             return render(request,'issueh.html',{'form':form})
         else:
             return HttpResponse("You Have Crossed Maximum Limit Of Issue")
 else:
     form=issue()
     return render(request,'issueh.html',{'form':form})
def returnbook(request):
    return render(request,'returnbook.html')
def returnbk(request):
    rlno=int(request.POST['rl'])
    isobj=Issue.objects.filter(rollno=rlno)
    #return render(request, 'test.html', {'obj': isobj})
    l = []
    k = []
    fine=[]
    for i in isobj:
        l.append(i.issuedate)
    d = datetime.date.today()
    for j in l:
        s = (d-j).days
        k.append(s)
    for a in k:
        if a>=1:
            fine.append(a*2)
        else:
            fine.append(0)
    Total_fine=0
    for q in fine:
        Total_fine+=q
    fine.append(Total_fine)
    return render(request,'studentissuedbooklist.html',{'obj':isobj,'fine':fine})
def issuedbookdelete(request):
     p=request.POST['de']
    #p contain two data rollno and bookid
     a,b=p.split(',')
     rno=int(a)
     bno=int(b)
     if bno!=9807:
         p=Issue.objects.filter(rollno=rno,bookid=bno)
         if len(p)>0:
          p[0].delete()
          isobj = Issue.objects.filter(rollno=rno)
          return render(request, 'studentissuedbooklist.html',{'obj': isobj})
         else:
             HttpResponse("No Book Is Issued To Him")
     else:
         isobj = Issue.objects.filter(rollno=rno)
         return render(request, 'studentissuedbooklist.html', {'obj': isobj})
def studentlist(request):
    p=Student.objects.all()
    p.order_by('rollno')
    return render(request,'studentlist.html',{'p':p})
def booklist(request):
    p=Book.objects.all()
    p.order_by('bookname')
    return render(request,'booklist.html',{'p':p})
def issuedbooklist(request):
    p=Issue.objects.all()
    p.order_by('issuedate')
    return render(request,'issuedbooklist.html',{'p':p})
#def finecalculate(request):
 #   return render(request,)
def searchbook(request):
      bn=request.POST['sb']
      p=Book.objects.filter(bookname__startswith=bn)
      return render(request, 'booklist.html', {'p': p})
def issuedbooksearch(request):
      bn = request.POST['sb']
      p = Issue.objects.filter(name__startswith=bn)
      return render(request, 'issuedbooklist.html', {'p': p})
# Create your views here.
'''def returnbk(request):
    rlno=int(request.POST['rl'])
    isobj=Issue.objects.filter(rollno=rlno)
    l=[]
    k=[]
    for i in isobj:
        l.append(i.issuedate)
    d=datetime.date.today()
    for j in l:
        s=((d - datetime.datetime.strptime(j, "%Y,%m,%d").date()).days)
        k.append(s)
    return (str(k))'''


    #return render(request, 'test.html', {'obj': isobj})
    #return render(request,'studentissuedbooklist.html',{'obj':isobj})

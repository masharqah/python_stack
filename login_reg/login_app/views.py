from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User , Course , Student
import bcrypt

# Create your views here.
def index(request):
    return render (request,'index.html')

def login(request):
    postData=request.POST
    errors = User.objects.login_validator(postData)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect ('/')
    else:
        users=User.objects.filter(email=request.POST['email'])
        logged_user=users[0]
        request.session['user']= logged_user.id
        request.session['name']=f"{logged_user.fname} {logged_user.lname}"
        request.session['logged']=True
        return redirect ('/classes')

def reg(request):
    errors = User.objects.reg_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect ('/')
    else:
        User.objects.create (
            fname= request.POST['fname'],
            lname= request.POST['lname'],
            email= request.POST['email'],
            password=bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
            ).save()
    return redirect ('/success')

def success(request):
    return render (request, 'success.html')

def welcome(request):
    if request.session['logged']!= True: 
        return redirect('/')
    logged_user= User.objects.get(id = request.session['user'])
    context = {
        'name' : request.session['name'],
        'status' : request.session['logged'],
        'courses': Course.objects.all(),
        'users': User.objects.all() ,
        'logged_user' : logged_user
    }
    return render (request, 'welcome.html', context)

def logout(request):
    if request.method == 'POST':
        del request.session['name']
        del request.session['logged']
        request.session.flush()
    return redirect ('/')

def create_course_form(request):
        if request.session['logged']!= True: 
            return redirect('/')
        context = {
        'name' : request.session['name'],
        'status' : request.session['logged']
        }
        return render (request, 'create_course_form.html', context)

def add_course(request):
    if request.session['logged']!= True: 
        return redirect('/')


    postData=request.POST
    errors = Course.objects.course_validator(postData)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect ('classes/create_course')
    else:
        new_course=Course.objects.create (
           name = request.POST['course_name'],
           Weekday= request.POST['weekday'],
           price= request.POST['price'],
           time=request.POST['time'],
           desc=request.POST['desc'],
        )
        new_course.save()
        id = int(request.session['user'])
        instructor = User.objects.get(id = id)
        new_course.instructors.add(instructor)
    return redirect ('/classes')

def course_info(request, id):
    if request.session['logged']!= True: 
        return redirect('/')

    course= Course.objects.get(id=id)
    instructors=course.instructors.all()
    students = Student.objects.all()
    context= {
        'course' : course,
        'instructor' : instructors,
        'students' : students,
    }
    return render (request, 'course_info.html', context)


def edit_course(request, id):
    if request.session['logged']!= True: 
        return redirect('/')

    course = Course.objects.get(id=id)
    context= {
        'course' : course,
    }
    return render (request, 'edit_course_form.html', context)

def update_course(request, id):
    if request.session['logged']!= True: 
        return redirect('/')

    postData=request.POST
    errors = Course.objects.course_validator(postData)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
    page = f"classes/{id}/edit"
    return redirect (page)

    course= Course.objects.get(id=id)
    course.name= request.POST['course_name']
    course.Weekday= request.POST['weekday']
    course.price= request.POST['price']
    course.time=request.POST['time']
    course.desc=request.POST['desc']
    course.save()
    return redirect ('/classes')

def del_course(request, id):
    if request.session['logged']!= True: 
        return redirect('/')
    course = Course.objects.get(id=id)
    course.delete()
    return redirect('/classes')

def add_student(request, id):
    if request.session['logged']!= True: 
        return redirect('/')

    added_student= Student.objects.create (
        fname = request.POST['fname'],
        lname = request.POST['lname'],
        email = request.POST['email']
    )
    added_student.save()
    page = f"/classes/{id}"
    return redirect (page)

def add_student_to_course (request, id):
    if request.session['logged']!= True: 
        return redirect('/')
    course= Course.objects.get (id = id)
    student = Student.objects.get(id= request.POST['added_student'])
    course.students.add(student)
    course.save()
    page = f"/classes/{id}"
    return redirect (page)


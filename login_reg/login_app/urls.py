from django.urls import path     
from . import views

urlpatterns = [ 
    path('', views.index),
    path('login', views.login),
    path('reg', views.reg),
    path('classes', views.welcome),
    path ('success', views.success),
    path('logout', views.logout),
    path('classes/create_course', views.create_course_form),
    path('classes/create_course/add_course', views.add_course),
    path ('classes/<int:id>', views.course_info),
    path('classes/<int:id>/edit' , views.edit_course),
    path('classes/<int:id>/edit/update' , views.update_course),
    path('classes/<int:id>/edit/del' , views.del_course),
    path('classes/<int:id>/add_student' , views.add_student),
    path('classes/<int:id>/add_student_to_course' , views.add_student_to_course)
  ]
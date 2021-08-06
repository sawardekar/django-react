from django.urls import path, include
from django.conf.urls import url
from . import views
from .apiviews import TeacherDetail
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'todos', views.TodoView, 'todo')
urlpatterns = [
    path('', views.index, name='index'),
    path('api/', include(router.urls)),
    url(r'^api/student$', views.student_detail),
    url(r'^api/student/(?P<pk>[0-9]+)$', views.student_detail),
    path('api/teacher', TeacherDetail.as_view()),
    path('api/teacher/<int:pk>', TeacherDetail.as_view()),
]
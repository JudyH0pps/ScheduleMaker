from django.urls import path
from . import views

app_name= 'schedules'

urlpatterns=[
    path('',views.index, name='index'),
    path('create/', views.create, name="create"),
    path('<int:schedule_pk>/detail/', views.detail, name="detail"),
    path('<int:schedule_pk>/detail/comment/', views.comment_create, name="comment_create"),
]
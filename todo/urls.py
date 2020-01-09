from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('task', views.TaskView)
router.register('list',views.ListView)
router.register('context', views.ContextView)

urlpatterns = [
    path('/api/',include(router.urls))
    # path('list/', views.list_list),
    # path('list/<int:pk>/', views.list_detail),
    # path('task/', views.list_task),
    # path('create_task/',views.create_task),
    # path('task/<int:pk>/', views.task_detail),
    # path('context/', views.context_list),
    # path('context/<int:pk>/', views.context_detail),

]
from django.contrib import admin
from django.urls import path
from tasks import views

urlpatterns = [
    path("", views.index, name="home"),
    path("add-collection/", views.add_collection, name="add-collection"),
    path("add-task/", views.add_task, name="add-task"),
    path("get-task/<int:collection_pk>/", views.get_tasks, name="get-task"),
    path("admin/", admin.site.urls),
]

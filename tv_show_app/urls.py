from django.urls import path
from . import views

urlpatterns=[
    path("", views.index),
    path("new_show", views.new_show),
    path("show/<int:show_id>", views.show),
    path("edit_show/<int:show_id>", views.edit_show),
    path("create_show", views.create_show),
    path("update_show/<int:show_id>", views.update_show)
]
from django.urls import path
from . import views
urlpatterns = [
    path('',views.doc),
    path('pat/',views.pat)


]

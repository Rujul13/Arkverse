from django.urls import path 
from .import views 
from res import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns =[
    path("",views.index, name="index"),
    path('unis/',views.uni_list),
    path('unis/<int:id>',views.uni_name)
    ]

urlpatterns = format_suffix_patterns(urlpatterns)
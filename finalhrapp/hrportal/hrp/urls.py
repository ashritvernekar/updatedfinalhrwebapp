from posixpath import basename
from xml.dom.minidom import Document
from django.urls import include, re_path 
from hrp import views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import DefaultRouter



urlpatterns = [
    re_path(r'^Basicinfo/$',views.FileView.as_view()),
    re_path(r'^Basicinfo/([0-9]+)$',views.FileView.as_view()),
    re_path(r'Searchapi/$',views.Searchapi.as_view()),
    re_path(r'Basic/$',views.BasicviewSet.as_view()),
   
   
    #re_path('delete_event/<event_id>', views.delete_event)
    
    #re_path(r'^Basicinfo/saveApi$',views.saveApi),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 


from django.urls import path,include
from . import views
from django.views.generic.base import TemplateView
from .views import *

urlpatterns = [
    path('',views.index,name='home'),
    path('empReg/', views.empReg,name='empReg'),
    path('comp', views.comp),
    path('show', views.show),
    path('edit/<str:cName>', views.edit),
    path('update/<str:cName>', views.update),
    path('delete/<str:cName>', views.delete), 

    #employee paths
    path('emp', views.emp),
    path('showemp', views.showemp),
    path('empProf/',views.empProf),
    path('empProf1/',views.empProf1),
    path('empProf2/',views.empProf2),
    path('deleteEmp/<str:eFname>', views.deleteEmp),
    path('editemp/<str:eFname>', views.editemp), 
    path('updateEmp/<str:eFname>', views.updateEmp),

    #Homepage path
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

    #inbuilt login path
    path('accounts/', include('django.contrib.auth.urls')), 
    #Project paths
    path('project',views.project),
    path('showstatus',views.showstatus),
    path('deleteStatus/<str:pk>', views.deleteStatus), 
    # path('editeStatus/<str:pk>', views.editeStatus),
    # path('updateStatus/<str:pk>', views.updateStatus),
    #employee registration path 
    path('empReg/emplogin/',views.emplogin,name='emplogin'),
    path('empReg/emplogin/ViewEmpProfile',views.ViewEmpProfile,name='ViewEmpProfile') 
]



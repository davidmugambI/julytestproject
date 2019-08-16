from django.urls import path
from testapp import views


urlpatterns = [
# http://127.0.0.1:8000/firstview
    path('',views.first_view,name='home'), #http://127.0.0.1:8000/firstview
# http://127.0.0.1:8000/form
    path('form/', views.savedata,name='form'),
    # path('login/', views.savedata,name='form'),
    path('forms2/', views.regularFormView,name='forms2'),
    path('forms3/', views.modelFormView,name='forms3'),
    path('display/', views.retrieveData, name='display'),
    path('update/<int:data_id>/',views.update, name='update'),
    path('delete/<int:data_id>/',views.delete_data, name='delete'),

]
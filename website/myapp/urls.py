from django.urls import path,include
from myapp import views

urlpatterns = [
    
    path('',views.index,name='index'),
    path('feature/',views.feature,name='feature'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup ,name="signup"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('logout/',views.logoutpage,name="logout"),
    path('profile/',views.profilepage,name='profile'),
    
]
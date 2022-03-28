from django.urls import path,include
from App import views

urlpatterns = [
    path('', views.home),

    path('accounts/',include('django.contrib.auth.urls')),
    path('logout/',views.logoutview),
    path('signup/',views.signupview),

    path('paidstories/',views.paid),
    path('editorpick/',views.editor),
    path('adventurestor/',views.adventure),
    path('shortstories/',views.short),


]

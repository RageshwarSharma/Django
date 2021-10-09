from . import views 
from django.urls import path

app_name = 'park'
urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.signup,name='signup'),
    path('terms/',views.terms_and_conditions,name='terms_and_conditions'),
    path('login/',views.login,name='login'),
    path('signupsave/',views.signup_save,name='signup_save'),
    path('bookticket/<int:pk>/',views.booking_data,name='booking_data'),
    path('bookingsave/<int:pk>/',views.booking_datasave,name='booking_datasave'),
    path('updatebookticket/<int:pk>/',views.updatebookticket,name='updatebookticket'),
    path('updatebooking/<int:pk>/',views.updatebooking,name='updatebooking'),
    path('get_all_bookings/<int:pk>/',views.get_all_booking,name='get_all_booking'),
]

from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

# def about(request):
    # return render(request,'park/login.html')

def index(request):
    return render(request,'park/login.html')

def signup(request):
    return render(request,'park/signup.html')

def terms_and_conditions(request):
    return render(request,'park/terms_and_conditions.html')

def login(request):
    user_name = request.POST['user_name']
    password = request.POST['password']

    try:
        user_obj = UserDetail.objects.get(user_name = user_name)
    except:
        user_obj = None
    if user_obj is None:
        return render(request,'park/signup.html')

    else:
        if user_obj.password == password:
            context={'user_id':user_obj.id}
            return render(request,'park/home.html',context)
        else:
            return HttpResponse('Password is Incorrect')

def signup_save(request):
    user_obj = UserDetail()
    user_obj.user_name = request.POST['user_name']
    user_obj.first_name = request.POST['first_name']
    user_obj.last_name = request.POST['last_name']
    user_obj.phone_number = request.POST['phone_number']
    user_obj.email = request.POST['email']
    user_obj.password = request.POST['password']
    user_obj.save()


    context={'user_id':user_obj.id}
    return render(request,'park/home.html',context)

def booking_data(request,pk):
    context={'user_id':pk}
    return render(request,'park/booking_ticket.html',context)


def booking_datasave(request,pk):
    booking_obj = BookingDetail()
    booking_obj.user = UserDetail.objects.get(id=pk)
    booking_obj.adult = request.POST['adult']
    booking_obj.minor = request.POST['minor']
    booking_obj.infant = request.POST['infant']
    bp = BookingPrice.objects.get(id=1)

    total_price = bp.adult_price*int(booking_obj.adult) + bp.minor_price*int(booking_obj.minor) + bp.infant_price*int(booking_obj.infant)

    booking_obj.total_price = total_price
    booking_obj.save()

    a = BookingDetail.objects.filter(user=pk)
    context={'a':a}
    return render(request,'park/my_booking.html',context)

def updatebookticket(request,pk):
    update_obj = BookingDetail.objects.get(id=pk)

    update_obj.adult = request.POST['adult']
    update_obj.minor = request.POST['minor']
    update_obj.infant = request.POST['infant']

    bp = BookingPrice.objects.get(id=1)
    total_price = bp.adult_price*int(update_obj.adult) + bp.minor_price*int(update_obj.minor) + bp.infant_price*int(update_obj.infant)
    update_obj.total_price = total_price
    update_obj.save()

    obj = BookingDetail.objects.filter(user=update_obj.user)
    context = {'a':obj}
    return render(request,'park/my_booking.html',context)

def updatebooking(request,pk):
    update_obj = BookingDetail.objects.get(id=pk)
    context = {'a':update_obj}
    return render(request,'park/updatebookticket.html',context)

def get_all_booking(request,pk):
    obj = BookingDetail.objects.filter(user=pk)
    context = {'a':obj}
    return render(request,'park/my_booking.html',context)
    
            
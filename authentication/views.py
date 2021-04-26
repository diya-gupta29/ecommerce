from django.shortcuts import render, redirect
from django.views import View
# from .models import Item,Customer,Cart,OrderStatus
from .forms import CusRegistrationForm, ProfileForm
from django.contrib import messages
from .models import Customer

# Create your views here.

class registration_view(View):
    def get(self,request):
        form = CusRegistrationForm()
        return render(request, 'authentication/cusreg.html',{'form':form})
    def post(self,request):
        form = CusRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request,'Congratulations!! Registered Successfully')
            form.save()
        return render(request, 'authentication/cusreg.html',{'form':form})

class ProfileView(View):
    def get(self,request):
        if request.user.is_authenticated:
            form = ProfileForm()
            return render(request,'authentication/profile.html',{'form':form,'active':'btn-primary'})
        else:
            return redirect('/auth/login')

    def post(self,request):
        if request.user.is_authenticated:
            form=ProfileForm(request.POST)
            if form.is_valid():
                user = request.user
                name = form.cleaned_data['name']
                gender = form.cleaned_data['gender']
                phone_number = form.cleaned_data['phone_number']
                locality = form.cleaned_data['locality']
                city = form.cleaned_data['city']
                state = form.cleaned_data['state']
                zipcode = form.cleaned_data['zipcode']
                cus = Customer(user=user,name=name,gender=gender,phone_number=phone_number,locality=locality,city=city,state=state,zipcode=zipcode)
                cus.save()
                messages.success(request,'Congratulations!! Profile Updated Successfully')
            return render(request,'authentication/profile.html',{'form':form})
        else:
            return redirect('/auth/login')

def address(request):
    address = Customer.objects.filter(user=request.user.id)
    print("##########3")
    print(address)
    print(Customer.objects.all())
    print(request.user)
    return render(request,'authentication/address.html',{'address':address})

        

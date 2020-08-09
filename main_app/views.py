from django.shortcuts import render
from  django.http import  HttpResponse
from .models import Contact,Donor_details,Blood_DATA
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def mainapp_home(request):
    Blood_info = Blood_DATA.objects.all()
    params = {'Blood_informations':Blood_info}
    return render(request,'home.html',params)

def contactus(request):
    if request.method=="POST":
        name = request.POST.get('fname','') + ' ' + request.POST.get('mname','') + ' ' + request.POST.get('lname','')
        address = request.POST.get('address1','') + ' ' + request.POST.get('address2','')
        state = request.POST.get('stateSelect','')
        district = request.POST.get('districtSelect','')
        city = request.POST.get('city','')
        pincode = request.POST.get('PinCode','')
        phone = request.POST.get('phone','')
        email = request.POST.get('email','')
        query = request.POST.get('contactQuery','')
        contact = Contact(name=name,address=address,state=state,district=district,city=city,pincode=pincode,phone_number=phone,email=email,query=query)
        contact.save()
    return render(request,'contactus.html')
def aboutus(request):
    return render(request,'aboutus.html')

def donors(request):
    donor_info = Donor_details.objects.all()
    params = {'donor_information': donor_info}
    return render(request,'donors.html',params)

def donorRegistration(request):
    if request.method=="POST":
        donor_name = request.POST.get('donor_fname','') + ' ' + request.POST.get('donor_mname','') + ' ' + request.POST.get('donor_lname','')
        donor_bloodgroup = request.POST.get('donor_bloodGroup','')
        donor_address = request.POST.get('donor_address1','') + ' ' + request.POST.get('donor_address2','')
        donor_state = request.POST.get('donor_stateSelect','')
        donor_district = request.POST.get('donor_districtSelect','')
        donor_city = request.POST.get('donor_city','')
        donor_pincode = request.POST.get('donor_PinCode','')
        donor_phone = request.POST.get('donor_phone','')
        donor_email = request.POST.get('donor_email','')
        donor_image = request.FILES['donor_image']
        donor_details = Donor_details(donor_name=donor_name,donor_bloodgroup=donor_bloodgroup,donor_address=donor_address,donor_state=donor_state,donor_district=donor_district,donor_city=donor_city,donor_pincode=donor_pincode,donor_phone_number=donor_phone,donor_email_id=donor_email,donor_profile_pic=donor_image)
        donor_details.save()
    return render(request,'donorRegistration.html')

@login_required
def donordetails(request,donorid):
    donor = Donor_details.objects.filter(id=donorid)
    print(donor)
    return render(request,'donordetails.html',{'donor':donor[0]})

@login_required
def search(request):
    query = request.GET['query']
    if len(query)>60:
        searchedDonor=Donor_details.objects.none()
    else:
        searchName=Donor_details.objects.filter(donor_name__contains=query)
        searchBloodGroup=Donor_details.objects.filter(donor_bloodgroup__contains=query)
        searchAdress=Donor_details.objects.filter(donor_address__contains=query)
        searchState=Donor_details.objects.filter(donor_state__contains=query)
        searchDistrict=Donor_details.objects.filter(donor_district__contains=query)
        searchCity=Donor_details.objects.filter(donor_city__contains=query)
        searchPincode=Donor_details.objects.filter(donor_pincode__contains=query)

        searchedDonor=searchName.union(searchBloodGroup,searchAdress,searchState,searchDistrict,searchCity,searchPincode)
    
    if searchedDonor.count()==0:
        messages.warning(request,"No donor Found")
    else:
        messages.warning(request,"Donor Found")
    params={'searchedDonor':searchedDonor,"query":query}
    return render(request,"search.html",params)
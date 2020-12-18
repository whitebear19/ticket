from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator
import math
import requests
import time
import datetime
import json
import os 
import random
from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy

from account.models import CustomUser

import datetime
from datetime import timedelta
import random
import string
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, authenticate, logout
from PIL import Image
from django.core.mail import send_mail,EmailMessage
from django.template.loader import render_to_string, get_template
from django.utils.html import strip_tags
from twilio.rest import Client
from ticket.models import Tickets,VehicleManufacturer,TowToWorkshop,Location

PAGINATION_COUNT = 21


def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    user = request.user     
    nav = 'ticket'
    return render(request,'ticket/dashboard.html',{'nav':nav}) 

def create(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    user = request.user 
    vehicle_manufacturer = VehicleManufacturer.objects.all().order_by('name')
    towtoworkshop = TowToWorkshop.objects.all().order_by('name')
    nav = 'ticket'
    return render(request,'ticket/create.html',{'nav':nav,'towtoworkshop':towtoworkshop,'vehicle_manufacturer':vehicle_manufacturer}) 

def edit(request,id):
    try:        
        row = Tickets.objects.get(id=id)
        vehicle_manufacturer = VehicleManufacturer.objects.all().order_by('name')
        towtoworkshop = TowToWorkshop.objects.all().order_by('name')
        nav = 'ticket'
        return render(request,'ticket/create.html',{'nav':nav,'ticket':row,'towtoworkshop':towtoworkshop,'vehicle_manufacturer':vehicle_manufacturer})         
    except:
        nav = 'ticket'
        return redirect('/ticket/dashboard')

# ajax
def store(request):

    if not request.user.is_authenticated:
        results = False
        return JsonResponse({'results':results})    
    else:
        user = request.user 
        id = request.POST.get('which')
        if id == "0":            
            date_of_incident = request.POST.get('date_of_incident')
            contact_name = request.POST.get('contact_name')
            contact_number = request.POST.get('contact_number')
            insurer = request.POST.get('insurer')
            ticket_type = request.POST.get('ticket_type')
            ticket_status = request.POST.get('ticket_status')
            vehicle_reg_num = request.POST.get('vehicle_reg_num')
            vehicle_manufacturer = request.POST.get('vehicle_manufacturer')
            vehicle_model = request.POST.get('vehicle_model')
            assigned_to = request.POST.get('assigned_to')
            tow_from = request.POST.get('tow_from')
            tow_to_workshop = request.POST.get('tow_to_workshop')
            tow_to_address = request.POST.get('tow_to_address')
            locationID = request.POST.get('locationID')
            row = Tickets(date_of_incident=date_of_incident,contact_name=contact_name,contact_number=contact_number,insurer=insurer,ticket_type=ticket_type,ticket_status=ticket_status,vehicle_reg_num=vehicle_reg_num,vehicle_manufacturer=vehicle_manufacturer,vehicle_model=vehicle_model,assigned_to=assigned_to,tow_from=tow_from,tow_to_workshop=tow_to_workshop,tow_to_address=tow_to_address,locationID=locationID)
            row.save() 
        else:
            row = Tickets.objects.get(id=id)
            row.date_of_incident = request.POST.get('date_of_incident')
            row.contact_name = request.POST.get('contact_name')
            row.contact_number = request.POST.get('contact_number')
            row.insurer = request.POST.get('insurer')
            row.ticket_type = request.POST.get('ticket_type')
            row.ticket_status = request.POST.get('ticket_status')
            row.vehicle_reg_num = request.POST.get('vehicle_reg_num')
            row.vehicle_manufacturer = request.POST.get('vehicle_manufacturer')
            row.vehicle_model = request.POST.get('vehicle_model')
            row.assigned_to = request.POST.get('assigned_to')
            row.tow_from = request.POST.get('tow_from')
            row.tow_to_workshop = request.POST.get('tow_to_workshop')
            row.tow_to_address = request.POST.get('tow_to_address')
            row.save()
        results = True
        return JsonResponse({'results':results})    

def get_tickets(request):
    tickets = ''
    results = []
    pagenum = 0

    try:
        user = request.user
        currentPage = request.GET.get('currentPage')       
        
        tickets = Tickets.objects.filter(assigned_to=user.username).order_by('-created_at')        
        
        pagenum = math.ceil(tickets.count()/PAGINATION_COUNT)
        paginator = Paginator(tickets,PAGINATION_COUNT)   
        resultscollection = paginator.get_page(currentPage) 
    
        for item in resultscollection:
            data = {}
            data['id'] = item.id       
            data['date_of_incident'] = item.date_of_incident
            data['contact_name'] = item.contact_name
            data['contact_number'] = item.contact_number
            data['insurer'] = item.insurer
            data['ticket_type'] = item.ticket_type
            data['ticket_status'] = item.ticket_status
            data['vehicle_reg_num'] = item.vehicle_reg_num
            data['vehicle_manufacturer'] = item.vehicle_manufacturer
            data['vehicle_model'] = item.vehicle_model
            data['assigned_to'] = item.assigned_to
            data['tow_from'] = item.tow_from
            data['tow_to_workshop'] = item.tow_to_workshop
            data['tow_to_address'] = item.tow_to_address
            results.append(data)
            
        return JsonResponse({'results':results,'pagenum':pagenum})
    except:
        return JsonResponse({'results':results,'pagenum':pagenum})

def delete(request):
    try:
        id = request.GET.get('id')
        row = Tickets.objects.get(id=id)
        row.delete()
        return JsonResponse({'results':True})
    except:
        return JsonResponse({'results':False})

def send_link(request):
    try:        
        row = Location(city='',zipcode='',country='',lat='',lng='',state='')
        row.save()
        id = row.id
        auth_token  = "your_auth_token"
        client = Client(account_sid, auth_token)
        verified_code = "Verify code from www.flickerface.com: " + verified_code
        phone = "+"+email
        message = client.messages.create(
            to=phone, 
            from_="+15017250604",
            body=verified_code)
        print(message.sid)
        return JsonResponse({'results':True,'id':id})
    except:
        return JsonResponse({'results':False})

def get_location_response(request):
    try:
        url = 'http://ticket.thetravelstreet.com/userinfo.return'
        resp = requests.get(url=url)
        data = resp.json()
        results=json.dumps(data) 
        results=json.loads(results)        
        for item in results:
            locations = Location.objects.all()
            for row in locations:               
                if str(row.id) == item['userid']:
                    try:
                        if item['latitude']:
                            row.lat = item['latitude']
                        if item['longitude']:
                            row.lng = item['longitude']
                        if item['country']:
                            row.country = item['country']
                        if item['zipcode']:
                            row.zipcode = item['zipcode']
                        if item['state']:
                            row.state = item['state']
                        if item['city']:
                            row.city = item['city']
                        row.save()
                    except:
                        print("issue")
                        pass
        return JsonResponse({'results':True})
    except:
        return JsonResponse({'results':False})
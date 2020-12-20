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

PAGINATION_COUNT = 200


def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    user = request.user     
    nav = 'ticket'
    vehicle_manufacturer = VehicleManufacturer.objects.all().order_by('name')
    towtoworkshop = TowToWorkshop.objects.all().order_by('name')
    return render(request,'ticket/dashboard.html',{'nav':nav,'towtoworkshop':towtoworkshop,'vehicle_manufacturer':vehicle_manufacturer}) 

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
        date_of_incident = request.GET.get('date_of_incident')
        contact_name = request.GET.get('contact_name')
        contact_number = request.GET.get('contact_number')
        insurer = request.GET.get('insurer')
        ticket_type = request.GET.get('ticket_type')
        ticket_status = request.GET.get('ticket_status')
        vehicle_reg_num = request.GET.get('vehicle_reg_num')
        vehicle_manufacturer = request.GET.get('vehicle_manufacturer')
        vehicle_model = request.GET.get('vehicle_model')
        assigned_to = request.GET.get('assigned_to')
        tow_from = request.GET.get('tow_from')
        tow_to_workshop = request.GET.get('tow_to_workshop')
        tow_to_address = request.GET.get('tow_to_address')
        
        user = request.user
        currentPage = request.GET.get('currentPage')       
        
        # tickets = Tickets.objects.filter(assigned_to=user.username).order_by('-created_at')  
        tickets = Tickets.objects.all() 
        if date_of_incident:
            tickets = tickets.filter(date_of_incident__contains=date_of_incident)
        if contact_name:
            tickets = tickets.filter(contact_name__contains=contact_name) 
        if contact_number:
            tickets = tickets.filter(contact_number__contains=contact_number)
        if insurer:
            tickets = tickets.filter(insurer__contains=insurer)
        if ticket_type:
            tickets = tickets.filter(ticket_type__contains=ticket_type)
        if ticket_status:
            tickets = tickets.filter(ticket_status__contains=ticket_status)
        if vehicle_reg_num:
            tickets = tickets.filter(vehicle_reg_num__contains=vehicle_reg_num)
        if vehicle_manufacturer:
            tickets = tickets.filter(vehicle_manufacturer__contains=vehicle_manufacturer)
        if vehicle_model:
            tickets = tickets.filter(vehicle_model__contains=vehicle_model)
        if assigned_to:
            tickets = tickets.filter(assigned_to__contains=assigned_to)
        if tow_from:
            tickets = tickets.filter(tow_from__contains=tow_from)
        if tow_to_workshop:
            tickets = tickets.filter(tow_to_workshop__contains=tow_to_workshop)
        if tow_to_address:
            tickets = tickets.filter(tow_to_address__contains=tow_to_address)
        tickets = tickets.order_by('-created_at')
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
        num = request.GET.get('num')
        
        # auth_token  = "your_auth_token"
        # account_sid = ""
        # client = Client(account_sid, auth_token)
        # data = "http://ticket.thetravelstreet.com/user/"+str(id)
        # message = client.messages.create(
        #     to=phone, 
        #     from_="+15017250604",
        #     body=data)
        # print(message.sid)
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

def get_location(request):
    try:
        id = request.GET.get('id')
        location = ""
        url = 'http://ticket.thetravelstreet.com/userinfo.return'
        resp = requests.get(url=url)
        data = resp.json()
        results=json.dumps(data) 
        results=json.loads(results)   
        print(results)   
        allow = ''  
        for item in results:
            locations = Location.objects.all()
            for row in locations:    
                if item['userid'] == id:
                    location = item['city'] + " " +  item['state'] + " " + item['country']
                    allow = item['allow'] 
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
                
        return JsonResponse({'results':True,'location':location,'allow':allow})
    except:
        return JsonResponse({'results':False})
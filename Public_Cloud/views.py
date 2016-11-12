from django.shortcuts import render
import django.forms
from django.views.decorators.csrf import csrf_exempt
import os
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from Public_Cloud.models import Users
from Public_Cloud.models import Files
from os import walk
from os.path import isfile, join
from .forms import RegistrationForm
from flask import Flask
from django.views.decorators.csrf import csrf_exempt
from django.utils.encoding import smart_str
import re
from django.contrib import messages

def login(request):
	if request.method =='POST':	
		if Users.objects.filter(user_name=request.POST.get('your_name',False),password=request.POST.get('your_password',False)).exists():
			request.session['user'] = request.POST.get('your_name',False)
			q=[]
			q = Files.objects.filter(owner_name=request.POST.get('your_name',False))
			return render(request,'index.html',{'q':q})
	#render("success")
	else:
		return render(request,'login.html', {})
def register(request):
	if request.method == 'POST':
		form = RegistrationForm(data=request.POST)
		if form.is_valid():
			passw=form.cleaned_data['password']
			if len(passw)<6:
				messages.error(request,'passoword shorter than 6 char')
				form = RegistrationForm()
				return render(request,'register.html', {'form':form})
			user = Users(user_name=form.cleaned_data['username'], user_email=form.cleaned_data['email'],
                password=form.cleaned_data['password'])
			user.save();
			file = Files(owner_name=form.cleaned_data['username'],file_name="demofile")
			file.save();
			return render(request,'login.html', {})
			
		else:
			console.log("error")
			return render(request,'login.html', {})			
	else:
		form = RegistrationForm()
        #return redirect(url_for('login'))
		return render(request,'register.html', {'form':form})
def upload(request):
	for	x in request.FILES.getlist("files"):
		def process(f):
			with open(r'C:\Python34\Scripts\test_project\Public_Cloud\static\%s ' %f.name , 'wb+') as destination:
					if Files.objects.filter(file_name=f.name).exists():
						print("hello");
					else:
						b = Files(file_name=f.name,owner_name=request.session['user'])
						print(b.id);
						b.save()
						for chunk in f.chunks():
							destination.write(chunk)
		process(x)
	q=[]
	q = Files.objects.filter(owner_name=request.session['user'])
	return render(request,  "index.html", {'q' : q})
@csrf_exempt
def play_file(request): 
	#file=Files.objects.get(id=37)
	file=request.POST.get('file_name', False)
	fsock = open(r'C:\Python34\Scripts\test_project\Public_Cloud\static\%s' %file, 'rb')
	response = HttpResponse()
	response['Content-Type'] ='audio/mp3'
	response['Content-Length'] =os.path.getsize(r'C:\Python34\Scripts\test_project\Public_Cloud\static\%s' %file)
	response.write(fsock.read())
	return response
def removefile(request):
	Files.objects.filter(file_name=request.POST.get('file_name',False)).delete()
	
def logout(request):
	request.session['user']=" "
	return render(request,'login.html', {})
@csrf_exempt
def viewpdf(request):
		pdf_name=request.POST.get('file_name')
		#response['Content-Type'] ='application/pdf'
		response['Content-Length'] =os.path.getsize(r'C:\Python34\Scripts\test_project\Public_Cloud\static\%s' %pdf_name)
		return render(request,  "view.html", {'pdf_name' : pdf_name})
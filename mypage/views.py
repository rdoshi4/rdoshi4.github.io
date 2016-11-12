from django.shortcuts import render
from django.shortcuts import render_to_response

def about(request):
	return render(request,'about.html', {})
def info(request):
	return render(request,'info.html', {})


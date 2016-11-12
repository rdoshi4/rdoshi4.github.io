from django.shortcuts import render
import django.forms
from django.views.decorators.csrf import csrf_exempt
import os
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from os import walk
from os.path import isfile, join
from .forms import RegistrationForm
from flask import Flask


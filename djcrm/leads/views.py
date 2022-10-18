
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render,redirect

from .forms import LeadForm

from .models import Agent, Lead


# Create your views here.

def lead_list(request):
    leads = Lead.objects.all()
    context = {
        'leads': leads
    }
    return render(request, 'leads/lead_list.html', context)


def lead_details(request,pk):
    lead = Lead.objects.get(id=pk)
    context = {
        'lead':lead
    }
    return render(request,'leads/lead_details.html',context)


def lead_create(request):

 if request.method  == 'POST':
  form = LeadForm(request.POST)
  if form.is_valid():
    first_name = form.cleaned_data['first_name']
    last_name = form.cleaned_data['last_name']
    age = form.cleaned_data['age']
    agent = Agent.objects.first()
    Lead.objects.create(
        first_name=first_name,
        last_name = last_name,
        age = age,
        agent = agent
    )
    return redirect('/leads')

 else:
    form = LeadForm()
    context = {
        'form':form
    }


    return render(request,'leads/lead_create.html',context)
     


     

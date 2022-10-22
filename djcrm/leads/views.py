
from django.core.mail import send_mail
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect,reverse

from .forms import  CustomUserCreatinForm, LeadModelForm

from .models import Agent, Lead


class SignupView(CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreatinForm

    def get_success_url(self):
        return reverse('login')


class LeadListView(LoginRequiredMixin,ListView):
    template_name = "leads/lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"


class LeadDetailView(LoginRequiredMixin,DetailView):
    template_name = 'leads/lead_details.html'
    queryset = Lead.objects.all()
    context_object_name = "lead"

class LeadCrateView(LoginRequiredMixin,CreateView):
    template_name ="leads/lead_create.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead-list")

    def form_valid(self, form):
        send_mail(
            subject = "A lead has been created",
            message = 'Go to the site to see the new lead',
            from_email = ' test@test.com',
            recipient_list = ['test2@test.com']
        )
        return super(LeadCrateView,self).form_valid(form)

class LeadUpdateView(LoginRequiredMixin,UpdateView):
    
    template_name ="leads/lead_update.html"
    queryset = Lead.objects.all()
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead-list")



class LeadDeleteView(LoginRequiredMixin,DeleteView):
    template_name ="leads/lead_delete.html"
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse("leads:lead-list")



# def lead_create(request):

#     if request.method == 'POST':
#         form = LeadModelForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/leads')

#     form = LeadModelForm()
#     context = {
#             'form': form
#         }

#     return render(request, '', context)


# def lead_update(request, pk):
#     lead = Lead.objects.get(id=pk)
#     form = LeadModelForm(instance=lead)
#     print(request.method)
#     if request.method == 'POST':
#         form = LeadModelForm(request.POST, instance=lead)
#         if form.is_valid():
#             form.save()
#             return redirect('/leads')

#     context = {
#         'lead': lead,
#         'form': form
#     }
#     return render(request, 'leads/lead_update.html', context)


# def lead_delete(request, pk):
#     lead = Lead.objects.get(id=pk)
#     lead.delete()
#     return redirect('/leads') 



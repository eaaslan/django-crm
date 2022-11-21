from django.core.mail import send_mail
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, reverse

from .forms import CustomUserCreationForm, LeadModelForm

from .models import Agent, Lead
from agents.mixins import OrganisorAndLoginRequiredMixin

class LandingPageView(TemplateView):
     template_name = "landpage.html"


class SignupView(CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse('login')


class LeadListView(LoginRequiredMixin, ListView):
    template_name = "leads/lead_list.html"
    context_object_name = "leads"

    def get_queryset(self):
        user = self.request.user
        # initial queryset of leads for the entire organisation
        if user.is_organisor:
            queryset = Lead.objects.filter(
                organisation=user.userprofile, 
                agent__isnull = False
                
            )
        else:
            queryset = Lead.objects.filter(
                organisation=user.agent.organisation, 
                agent__isnull = False
                
            )
            # filter for the agent that is logged in
            queryset = queryset.filter(agent__user=user)
        return queryset

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super(LeadListView,self).get_context_data(**kwargs)
        if user.is_organisor:
            queryset = Lead.objects.filter(
                    organisation = user.userprofile,
                    agent__isnull = True )

            context.update({
                    'unassigned_leads':queryset

                })
        return context




class LeadDetailView(LoginRequiredMixin, DetailView):
    template_name = 'leads/lead_details.html'
    queryset = Lead.objects.all()
    context_object_name = "lead"


class LeadCrateView(OrganisorAndLoginRequiredMixin, CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead-list")

    def form_valid(self, form):
        send_mail(
            subject="A lead has been created",
            message='Go to the site to see the new lead',
            from_email=' test@test.com',
            recipient_list=['test2@test.com']
        )
        return super(LeadCrateView, self).form_valid(form)


class LeadUpdateView(OrganisorAndLoginRequiredMixin, UpdateView):
    template_name = "leads/lead_update.html"
    queryset = Lead.objects.all()
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead-list")


class LeadDeleteView(OrganisorAndLoginRequiredMixin, DeleteView):
    template_name = "leads/lead_delete.html"
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

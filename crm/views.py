from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render,redirect
from django.views.generic import TemplateView,ListView,DeleteView,UpdateView,CreateView,View
from django.urls import reverse_lazy,reverse
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail

from .models import Customer, Communication
from .forms import EmailForm, CommunicationForm

class home(TemplateView):
    template_name = "crm/home.html"


# Customer Views
# To list all Customer
class CustomerListView(ListView):
    model = Customer
    template_name = "crm/customer_info.html"
    context_object_name = "customers"

# To create Customer
class CustomerCreateView(LoginRequiredMixin,CreateView):
    model = Customer
    template_name = "crm/customer_create.html"
    fields = '__all__'

# to Delete Customer
class CustomerDeleteView(LoginRequiredMixin,DeleteView):
    model = Customer
    template_name = "crm/customer_delete.html"
    success_url = reverse_lazy('home')

# to Update Customer
class CustomerUpdateView(LoginRequiredMixin,UpdateView):
    model = Customer
    fields ='__all__'
    template_name = "crm/customer_update.html"

# all Communication Views

class CustomerCommunicationListView(ListView):
    model = Communication
    template_name = "crm/communication.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()
        customer = get_object_or_404(Customer,pk=self.kwargs.get('pk'))       
        communications = queryset.filter(customer=customer).order_by('timestamp')
        # communications = Communication.objects.filter(customer=customer).order_by('timestamp')
        context["customer"] = customer
        context["communications"] = communications
        return context
    
# To create Customer Communication 
class CommunicationCreateView(LoginRequiredMixin,CreateView):
    model = Communication
    template_name = "crm/communication_create.html"
    fields = ['comm_detail','timestamp']

    def form_valid(self,form):
        form.instance.customer = Customer.objects.get(pk =self.kwargs.get('pk'))
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customer = get_object_or_404(Customer,pk=self.kwargs.get('pk'))
        context['customer'] = customer
        return context
        

# To Delete Customer Communication 
class CommunicationDeleteView(LoginRequiredMixin,DeleteView):
    model = Communication
    template_name = "crm/communication_delete.html"

    def get_success_url(self):
        customer = self.object.customer
        return reverse_lazy("customer-communication",kwargs ={'pk' : customer.pk})

# To Update Customer Communication 
class CommunicationUpdateView(LoginRequiredMixin,UpdateView):
    model = Communication
    fields = '__all__'
    template_name = "crm/communication_update.html"

class SendEmailView(LoginRequiredMixin,View):
    def get(self,request,pk,*args, **kwargs):
        form = EmailForm()
        #  to get email of customer to show in front-end
        # print(pk)
        communication = Communication.objects.get(pk=pk)
        # print(communication)
        email = communication.customer.email
        context = {
            'form' : form,
            'email' : email
        }
        return render (request,'crm/send_email.html',context)


    def post(self,request,pk,*args, **kwargs):
        form = EmailForm(request.POST)
        comm_form  = CommunicationForm()
        # To get email of customer and using it to send a mail
        communication = Communication.objects.get(pk=pk)
        email = communication.customer.email

        # checking form Validity and making necessory changes
        if form.is_valid():
            e_form = form.save(commit=False)
            # to update this email details as Communication in communication table
            c_form = comm_form.save(commit=False)
            c_form.customer = communication.customer
            c_form.comm_detail = e_form.content 
            c_form.save()
            
            
            e_form.receiver = email

            # setting form filled value to respective term for sending email
            send_mail(
                e_form.subject, # Subject
                e_form.content, # message
                e_form.sender,  # from Email
                [email,],# to email
                fail_silently=False,
            )
            # to save form or email info in database
            e_form.save()
            return redirect('customer-communication',pk=communication.customer.pk)

        context = {
            'form' : form
        }
        return render(request,'crm/send_email.html',context)


# to show all communications

class CommunicationListView(ListView):
    model = Communication
    template_name = "crm/communication_all.html"
    context_object_name = 'communications'

class CommunicationAnyCustomerCreateView(LoginRequiredMixin,CreateView):
    model = Communication
    fields = '__all__'
    template_name = "crm/communication_create_any.html"


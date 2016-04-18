from django.shortcuts import render, get_object_or_404
from django.views.generic import View, UpdateView
from django.conf import settings
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from .forms import *
from .models import *
# Create your views here.

def index(request):
    return render(request,'index.html')

class HomeView(View):
    template_name = 'index.html'
    def get(self,request):
        form = ContactForm()
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = ContactForm(request.POST or None)
        if form.is_valid():
            contact=form.save(commit=False)
            contact.save()
	    subject= 'Pesan pada website NoteIT dari {}'.format(contact.nama)
	    message= 'nama: {} \nemail: {} \nno telepon: {} \nmessage: {}'.format(contact.name,contact.email,contact.message)
	    email_from= settings.EMAIL_HOST_USER
	    email_to= 'note.id@gmail.com'
	    send_mail(subject, message, email_from, [email_to], fail_silently=False)
            messages.success(request,'Your comment has been successfully saved')
            return HttpResponseRedirect(reverse('index'))
        else:
            messages.error(request,'An error has occured, please try again')
            return render(request,self.template_name,{'form':form})

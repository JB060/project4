from django.shortcuts import render, redirect 
from django.urls import reverse_lazy
from django.views.generic import TemplateView, View, CreateView
from django.contrib.auth import authenticate, login 
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserRegisterForm
from .models import InventoryItem

class Index(TemplateView):
    template_name = 'inventory/index.html'

class Dashboard(LoginRequiredMixin, View):
    def get(self, request):
        items = InventoryItem.objects.filter(user=self.request.user.id).order_by('id')

        return render(request, 'inventory/dashboard.html', {'items': items})

class SignUpView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render (request, 'inventory/signup.html', {'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            user = authenticate(
                username=form.clean_data['username'],
                password=form.clean_data['password1']
            )

            login (request, user)
            return redirect ('index')

        return render (request, 'inventory/signup.html', {'form':form})

    class AddItem(LoginRequiredMixin, CreateView):
	    model = InventoryItem
	    form_class = InventoryItemForm
	    template_name = 'inventory/item_form.html'
	    success_url = reverse_lazy('dashboard')



# Create your views here.

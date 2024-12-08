from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, View, CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserRegisterForm, InventoryItemForm
from .models import InventoryItem, Category
from inventory_management.settings import LOW_QUANTITY
from django.contrib import messages

class Index(TemplateView):
    """
    View that renders the index page. This view is used as the home page of the site.
    """
    template_name = 'inventory/index.html'

class Dashboard(LoginRequiredMixin, View):
    """
    View that renders the dashboard page for a logged-in user.
    Displays the user's inventory items and highlights low inventory items.
    """
    def get(self, request):
        # Retrieve all items belonging to the logged-in user
        items = InventoryItem.objects.filter(user=self.request.user.id).order_by('id')

        # Retrieve items with low inventory (based on LOW_QUANTITY setting)
        low_inventory = InventoryItem.objects.filter(
            user=self.request.user.id,
            quantity__lte=LOW_QUANTITY
        )

        # Display a message if there are any items with low inventory
        if low_inventory.count() > 0:
            if low_inventory.count() > 1:
                messages.error(request, f'{low_inventory.count()} items have low inventory')
            else:
                messages.error(request, f'{low_inventory.count()} item has low inventory')

        # Collect the IDs of low inventory items
        low_inventory_ids = InventoryItem.objects.filter(
            user=self.request.user.id,
            quantity__lte=LOW_QUANTITY
        ).values_list('id', flat=True)

        # Render the dashboard template, passing the items and low inventory IDs
        return render(request, 'inventory/dashboard.html', {'items': items, 'low_inventory_ids': low_inventory_ids})

class SignUpView(View):
    """
    View for handling user sign-up.
    Displays the sign-up form and handles the POST request for new user registration.
    """
    def get(self, request):
        # Render the sign-up form
        form = UserRegisterForm()
        return render(request, 'inventory/signup.html', {'form': form})

    def post(self, request):
        # Handle form submission for user registration
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            # Save the user and authenticate them
            form.save()
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )

            # Log the user in and redirect to the index page
            login(request, user)
            return redirect('index')

        # If form is invalid, re-render the sign-up page with form errors
        return render(request, 'inventory/signup.html', {'form': form})

class AddItem(LoginRequiredMixin, CreateView):
    """
    View for adding a new inventory item. Requires the user to be logged in.
    """
    model = InventoryItem
    form_class = InventoryItemForm
    template_name = 'inventory/item_form.html'
    success_url = reverse_lazy('dashboard')

    def get_context_data(self, **kwargs):
        """
        Adds category data to the context so it can be rendered in the template.
        """
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

    def form_valid(self, form):
        """
        Sets the current logged-in user as the owner of the inventory item before saving.
        Displays a success message after the item is successfully added.
        """
        form.instance.user = self.request.user
        response = super().form_valid(form)
        messages.success(self.request, 'Item successfully added!')
        return response

class EditItem(LoginRequiredMixin, UpdateView):
    """
    View for editing an existing inventory item. Requires the user to be logged in.
    """
    model = InventoryItem
    form_class = InventoryItemForm
    template_name = 'inventory/item_form.html'
    success_url = reverse_lazy('dashboard')

class DeleteItem(LoginRequiredMixin, DeleteView):
    """
    View for deleting an inventory item. Requires the user to be logged in.
    """
    model = InventoryItem
    template_name = 'inventory/delete_item.html'
    success_url = reverse_lazy('dashboard')
    context_object_name = 'item'






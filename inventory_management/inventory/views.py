class Index(TemplateView):
    """
    A view that renders the index page of the inventory system.
    
    Inherits from TemplateView and uses the template 'inventory/index.html'.
    This is typically the landing page of the inventory system.
    """
    template_name = 'inventory/index.html'


class Dashboard(LoginRequiredMixin, View):
    """
    A view that displays the user's inventory dashboard.
    
    Inherits from View and requires the user to be logged in (LoginRequiredMixin).
    This view shows a list of inventory items, as well as alerts for low inventory items
    (based on the threshold defined by the LOW_QUANTITY setting). If there are low inventory
    items, a flash message is displayed indicating how many items are low in stock.
    """
    
    def get(self, request):
        items = InventoryItem.objects.filter(user=self.request.user.id).order_by('id')

        low_inventory = InventoryItem.objects.filter(
            user=self.request.user.id,
            quantity__lte=LOW_QUANTITY
        )

        if low_inventory.count() > 0:
            if low_inventory.count() > 1:
                messages.error(request, f'{low_inventory.count()} items have low inventory')
            else:
                messages.error(request, f'{low_inventory.count()} item has low inventory')

        low_inventory_ids = InventoryItem.objects.filter(
            user=self.request.user.id,
            quantity__lte=LOW_QUANTITY
        ).values_list('id', flat=True)

        return render(request, 'inventory/dashboard.html', {'items': items, 'low_inventory_ids': low_inventory_ids})


class SignUpView(View):
    """
    A view that handles user registration for the inventory system.
    
    This view supports both GET and POST requests. The GET request renders a form to register a new user,
    and the POST request processes the submitted form, creating the user and logging them in.
    Upon successful registration, the user is redirected to the index page.
    """
    
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'inventory/signup.html', {'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )

            login(request, user)
            return redirect('index')

        return render(request, 'inventory/signup.html', {'form': form})


class AddItem(LoginRequiredMixin, CreateView):
    """
    A view to add a new inventory item.
    
    Inherits from CreateView and requires the user to be logged in (LoginRequiredMixin).
    The form is populated with the fields for an inventory item, and upon successful submission,
    the new item is saved. A success message is displayed when the item is successfully added.
    """
    
    model = InventoryItem
    form_class = InventoryItemForm
    template_name = 'inventory/item_form.html'
    success_url = reverse_lazy('dashboard')

    def get_context_data(self, **kwargs):
        """
        Adds categories to the context for rendering the item form.
        """
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

    def form_valid(self, form):
        """
        Custom form validation. Sets the user of the item to the current logged-in user
        and displays a success message upon successful form submission.
        """
        form.instance.user = self.request.user
        response = super().form_valid(form)
        messages.success(self.request, 'Item successfully added!')
        return response


class EditItem(LoginRequiredMixin, UpdateView):
    """
    A view to edit an existing inventory item.
    
    Inherits from UpdateView and requires the user to be logged in (LoginRequiredMixin).
    The form is populated with the existing data of the item, and upon successful submission,
    the updated item is saved.
    """
    
    model = InventoryItem
    form_class = InventoryItemForm
    template_name = 'inventory/item_form.html'
    success_url = reverse_lazy('dashboard')


class DeleteItem(LoginRequiredMixin, DeleteView):
    """
    A view to delete an inventory item.
    
    Inherits from DeleteView and requires the user to be logged in (LoginRequiredMixin).
    Upon successful deletion, a success message is displayed, and the user is redirected to the dashboard.
    """
    
    model = InventoryItem
    template_name = 'inventory/delete_item.html'
    success_url = reverse_lazy('dashboard')
    context_object_name = 'item'

    def delete(self, request, *args, **kwargs):
        """
        Custom delete logic. Displays a success message upon deletion of the item
        and proceeds to delete the item from the database.
        """
        item = self.get_object()
        messages.success(self.request, f'Item "{item.name}" successfully deleted!')
        return super().delete(request, *args, **kwargs)






from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.views import View
from .models import Item
from .froms import ItemForm


class ItemsList(ListView):
    model = Item


class ItemsCreate(CreateView):
    model = Item
    template_name = 'items/item_create.html'
    fields = ('name', 'serial_number', 'description', 'main_image', 'item_images')
    success_url = reverse_lazy('items:list')


class ItemsDetail(DetailView):
    model = Item


class ItemsUpdate(UpdateView):
    model = Item
    form_class = ItemForm
    template_name = 'items/item_update.html'

    def get_success_url(self):
        return reverse_lazy('items:detail', kwargs={'pk': self.object.pk})


class ItemsDelete(View):
    def get(self, request, *args, **kwargs):
        item_id = kwargs['pk']
        try:
            item = Item.objects.get(pk=item_id)
            item.delete()
        except Item.DoesNotExist:
            pass
        return redirect(reverse_lazy('items:list'))

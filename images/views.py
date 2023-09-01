from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views import View
from .models import Image
from .forms import ImageForm


class ImagesList(ListView):
    model = Image


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('images:list')
    else:
        form = ImageForm()
    return render(
        request,
        'images/upload.html',
        {"form": form}
    )


class ImageDetail(DetailView):
    model = Image


class ImagesDelete(View):
    def get(self, request, *args, **kwargs):
        image_id = kwargs['pk']
        try:
            image = Image.objects.get(pk=image_id)
            image.delete()
        except Image.DoesNotExist:
            pass
        return redirect(reverse_lazy('images:list'))

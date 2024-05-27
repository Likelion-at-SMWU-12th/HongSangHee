from django.shortcuts import render

from django.views.generic import TemplateView

# Create your tests here.

class info(TemplateView):
    template_name='info.html'

def page(request):
    print(f'request.POST: {request.POST}')
    return render(request, 'page.html')



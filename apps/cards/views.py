from django.views.generic import TemplateView
from django.http import HttpResponse
import datetime

def HomePageView(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

# class HomePageView(TemplateView):
#     template_name = 'home.html'
from django.views.generic import TemplateView, ListView
from .models import CardModel



class HomePageView( ListView):
    template_name = 'home.html'
    model = CardModel
    queryset = CardModel.objects.all()
    context_object_name = 'card_list'
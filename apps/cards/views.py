from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView
from .models import CardModel



class HomePageView( ListView):
    template_name = 'cards/home.html'
    model = CardModel
    queryset = CardModel.objects.all()
    context_object_name = 'card_list'

class CreateCardView(CreateView):
    model = CardModel
    template_name = 'cards/create_card.html'
    fields = ['question', 'answer', 'box']
    success_url = reverse_lazy('home')
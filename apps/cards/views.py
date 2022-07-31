from django.urls import reverse_lazy
from django.views.generic import (
TemplateView, ListView, CreateView, UpdateView
)
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
    context_object_name = 'card'

class UpdatecardView(CreateCardView, UpdateView):
    success_url = reverse_lazy('home')

class BoxView(ListView):
    template_name: str = 'cards/box.html'
    context_object_name = 'card_list'

    def get_queryset(self):
        return CardModel.objects.filter(box=self.kwargs['box_num'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['box_number'] = self.kwargs['box_num']
        return context
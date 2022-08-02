from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import (
TemplateView, ListView, CreateView, UpdateView
)
import random

from .forms import CardCheckForm

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
    form_class = CardCheckForm

    def get_queryset(self):
        return CardModel.objects.filter(box=self.kwargs['box_num'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['box_number'] = self.kwargs['box_num']
        if self.object_list:
            context["random_card"] = random.choice(self.object_list)
        return context
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            card_id = form.cleaned_data['card_id']
            solved = form.cleaned_data['solved']

            card = get_object_or_404(CardModel, id=card_id)
            card.move_card(solved)

        return redirect(request.META.get("HTTP_REFERER"))
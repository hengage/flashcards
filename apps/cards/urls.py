from django.urls import path

from .views import HomePageView, CreateCardView, UpdatecardView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('new', CreateCardView.as_view(), name='create-card'),
    path('edit/<int:pk>', UpdatecardView.as_view(), 'update-card')
]
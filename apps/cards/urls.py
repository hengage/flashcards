from django.urls import path

from .views import HomePageView, CreateCardView, UpdatecardView, BoxView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('new', CreateCardView.as_view(), name='create-card'),
    path('edit/<int:pk>', UpdatecardView.as_view(), name='update-card'),
    path('box/<int:box_num>', BoxView.as_view(), name='box')
]
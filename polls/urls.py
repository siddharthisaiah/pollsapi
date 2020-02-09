from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import polls_list, polls_detail
from .apiviews import ChoiceList, CreateVote #, PollList, PollDetail
from .apiviews import PollViewSet

router = DefaultRouter()
router.register('polls', PollViewSet, basename='polls')

urlpatterns = [
    # path('polls/', PollViewSet, name='polls_list'),
    # path('polls/<int:pk>/', PollViewSet, name='polls_detail'),
    path('polls/<int:pk>/choices/', ChoiceList.as_view(), name='polls_choices'),
    path('polls/<int:pk>/choices/<int:choice_pk>/vote/',
         CreateVote.as_view(), name='create_vote')
]

urlpatterns += router.urls

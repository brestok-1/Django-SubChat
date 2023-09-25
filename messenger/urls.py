from django.urls import path

from messenger.views import ChatView

app_name = 'messenger'

urlpatterns = [
    path('', ChatView.as_view(), name='home')
]

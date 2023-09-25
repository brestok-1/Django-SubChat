from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from messenger.forms import CreateMessage, UserRegistrationForm, UserLoginForm
from messenger.models import Message, CustomUser

from messenger.utils import get_first_message_id


class ChatView(CreateView):
    template_name = 'messenger/main.html'
    form_class = CreateMessage
    success_url = reverse_lazy('messenger:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = CustomUser.objects.all()
        first_message_id = get_first_message_id(self.request.user)
        context['messages'] = Message.objects.filter(id__gte=first_message_id)
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get(self, *args, **kwargs):
        return super().get(self.request, *args, **kwargs)


class SignInView(LoginView):
    form_class = UserLoginForm
    template_name = 'messenger/sign-in.html'


class SignUpView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'messenger/sign-up.html'
    success_url = reverse_lazy('login')


@login_required
def logoutuser(request):
    logout(request)
    return HttpResponseRedirect(reverse('messenger:home'))

from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import UserRegisterForm
from users.models import User

from config.settings import EMAIL_HOST_USER


class UserCreateView(CreateView):
    model = User
    template_name = 'register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()

        send_mail(
            subject='Вы зарегистрированы',
            message="Спасибо, что зарегистрировались в нашем сервисе!",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email]
        )

        return super().form_valid(form)


from apps.core.custom_router import router
from django.urls import reverse_lazy
from django.views.generic import CreateView
from apps.accounts.forms import SignupForm


@router.path('signup/', name='signup')
class SignUpView(CreateView):
    form_class = SignupForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

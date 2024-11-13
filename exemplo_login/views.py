from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required



def home(request):
    return render(request, 'index.html')

@login_required
def user_page(request):
    return render(request, 'user_page.html')

@login_required
def adm_page(request):
    if not request.user.is_staff:
        # Se o usuário não for admin, redireciona para outra página
        return render(request, 'registration/admin-only.html')
    return render(request, 'adm_page.html')


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')  # Redireciona para a página de login após o cadastro

		
    def form_valid(self, form):
        messages.success(self.request, 'Conta criada com sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Erro ao criar conta. Tente novamente.')
        return super().form_invalid(form)
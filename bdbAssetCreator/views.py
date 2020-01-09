from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import AliasForm


class HomePageView(FormView):
    template_name = 'home.html'
    form_class = AliasForm
    success_url = ''

    def form_valid(self, form):
        form.get_data()
        return super().form_valid(form)
    
    
    




from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views import View


class MainView(View):
    template_name = 'main/index.html'
    context = {}

    def get(self, request):
        return render(request, self.template_name, self.context)
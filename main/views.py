from typing import Any
from django.db.models.query import QuerySet
from .models import Writers, FAQ 
from django.views.generic import DetailView, ListView, View
from django.shortcuts import render, redirect
from .forms import MessageForm, MessageForm, FeedbackForm
from django.http import JsonResponse
import akhmatova, esenin, gorky, lermontov, mayakovsky, pushkin, tsvetaeva

writers_dict = {
    'akhmatova' : akhmatova,
    'esenin' : esenin,
    'gorky' : gorky,
    'lermontov': lermontov,
    'mayakovsky': mayakovsky,
    'pushkin': pushkin,
    'tsvetaeva': tsvetaeva
}

class WritersDetailView(DetailView):
    model = Writers
    template_name = 'main/person_page.html'
    context_object_name = 'writer'
    
    def get(self, request, pk):
        writer = self.get_object()
        persons = Writers.objects.order_by('name')
        form = MessageForm()
        context = {'writer':writer, 'persons':persons, 'form':form}
        return render(request, self.template_name, context)

    def post(self, request, pk):
        message = request.POST.get('message')
        response = writers_dict[pk].response(message)
        return JsonResponse({'message': message, 'response': response})


# def index(request):
#     persons = Writers.objects.order_by('name')
#     return render(request, 'main/index.html', {'persons': persons})

class IndexView(ListView):
    model = Writers
    template_name = 'main/index.html'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["persons"] = Writers.objects.order_by('name')
        return context


class FAQView(View):
    template_name = 'main/faq.html'
    form_class = FeedbackForm
    model = FAQ

    def get(self, request):
        voprosi = self.model.objects.all()
        form = self.form_class()
        return render(request, self.template_name, {'voprosi': voprosi, 'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        voprosi = self.model.objects.all()
        return render(request, self.template_name, {'voprosi': voprosi, 'form': form})

# def faq(request):
#     if request.method == 'POST':
#         form = FeedbackForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
  
#     voprosi = FAQ.objects.all()
#     form = FeedbackForm()
#     return render(request, 'main/faq.html', {'voprosi': voprosi,'form': form}) 

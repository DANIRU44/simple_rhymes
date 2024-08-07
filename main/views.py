from .models import Writers, FAQ 
from django.views.generic import DetailView
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
        form = MessageForm() 
        context = {'writer': writer, 'form': form}
        return render(request, self.template_name, context)

    def post(self, request, pk):
        message = request.POST.get('message')
        response = writers_dict[pk].response(message)
        return JsonResponse({'message': message, 'response': response})

def index(request):
    persons = Writers.objects.order_by('name')
    return render(request, 'main/index.html', {'persons': persons})

def faq(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
  
    voprosi = FAQ.objects.all()
    form = FeedbackForm()
    return render(request, 'main/faq.html', {'voprosi': voprosi,'form': form}) 

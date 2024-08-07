from django.shortcuts import render
from django.views import View
from main.models import Writers

class BioHomeView(View):
    def get(self, request):
        persons = Writers.objects.order_by('name')
        return render(request, 'bio/bio_home.html', {'persons': persons})

class BioDetailView(View):
    template_name = None

    def get(self, request):
        return render(request, self.template_name)

class BioPushkinView(BioDetailView):
    template_name = 'bio/bio_pushkin.html'

class BioAkhmatovaView(BioDetailView):
    template_name = 'bio/bio_akhmatova.html'

class BioDostoevskyView(BioDetailView):
    template_name = 'bio/bio_dostoevsky.html'

class BioEseninView(BioDetailView):
    template_name = 'bio/bio_esenin.html'

class BioGorkyView(BioDetailView):
    template_name = 'bio/bio_gorky.html'

class BioLermontovView(BioDetailView):
    template_name = 'bio/bio_lermontov.html'

class BioMayakovskyView(BioDetailView):
    template_name = 'bio/bio_mayakovsky.html'

class BioTsvetaevaView(BioDetailView):
    template_name = 'bio/bio_tsvetaeva.html'
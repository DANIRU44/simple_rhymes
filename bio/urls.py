from django.urls import path
from .views import BioHomeView, BioPushkinView, BioAkhmatovaView, \
                    BioDostoevskyView, BioEseninView, BioGorkyView, \
                    BioLermontovView, BioMayakovskyView, BioTsvetaevaView

urlpatterns = [
    path('', BioHomeView.as_view(), name='bio_home'),
    path('pushkin/', BioPushkinView.as_view(), name='bio_pushkin'),
    path('akhmatova/', BioAkhmatovaView.as_view(), name='bio_akhmatova'),
    path('dostoevsky', BioDostoevskyView.as_view(), name='bio_dostoevsky'),
    path('esenin', BioEseninView.as_view() , name='bio_esenin'),
    path('gorky', BioGorkyView.as_view(), name='bio_gorky'),
    path('lermontov', BioLermontovView.as_view(), name='bio_lermontov'),
    path('mayakovsky', BioMayakovskyView.as_view(), name='bio_mayakovsky'),
    path('tsvetaeva', BioTsvetaevaView.as_view(), name='bio_tsvetaeva')
] 

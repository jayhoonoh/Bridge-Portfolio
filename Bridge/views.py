from django.shortcuts import render, redirect, reverse
from Bridge.models import Bridges
from Bridge.forms import ClientForm, CsvImportForm, CsvExportForm
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.http import HttpResponse
import csv

class clientindex(TemplateView):
  template_name = 'Bridge_index.html'

  def get(self, request):
    form1 = ClientForm()
    form2 = CsvImportForm()
      
    context = {
      'form1': form1,
      'form2': form2,
    }
    return render(request, self.template_name, context)

  def post(self, request):
    if 'f1' in request.POST:
      form1 = ClientForm(request.POST)
      if form1.is_valid():
        clientname = form1.cleaned_data.get('Client_List')
      return redirect('clientview', clientname)

    elif 'f2' in request.POST: 
      form2 = CsvImportForm(request.POST, request.FILES)
      if form2.is_valid():
        form2.process_import_data()
      return redirect('/Bridge/')

    elif 'f3' in request.POST:
      exp = Bridges.objects.all()

      csv_response = HttpResponse(content_type='text/csv')
      csv_response['Content-Disposition'] = 'attachment; filename = "All Client Info.csv"'

      writer = csv.writer(csv_response)
      writer.writerow(['BILLING_DATE','POLICY_NUMBER','CLIENT_NAME','LIFE_RATE','LIFE_VOLUME','LIFE_PREMIUM','EHC_S_RATE','EHC_S_VOLUME','EHC_S_PREMIUM', 'EHC_C_RATE','EHC_C_VOLUME','EHC_C_PREMIUM','EHC_F_RATE','EHC_F_VOLUME','EHC_F_PREMIUM'])

      for data in exp:
        writer.writerow([data.BILLING_DATE,data.POLICY_NUMBER,data.CLIENT_NAME,data.LIFE_RATE,data.LIFE_VOLUME,data.LIFE_PREMIUM,data.EHC_S_RATE,data.EHC_S_VOLUME,data.EHC_S_PREMIUM,data.EHC_C_RATE,data.EHC_C_VOLUME,data.EHC_C_PREMIUM,data.EHC_F_RATE,data.EHC_F_VOLUME,data.EHC_F_PREMIUM])
      return csv_response

    return redirect('/Bridge/')
        


class clientview(View):
    def get(self, request, clientname):
        Client = Bridges.objects.get(CLIENT_NAME=clientname)
        context = { 
          'Client': Client
        }
        return render(request, 'Bridge_client.html', context)  



    

    

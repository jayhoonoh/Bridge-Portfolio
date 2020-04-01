from django import forms
from Bridge.models import Bridges
import csv, io
from django.http import HttpResponse

class ClientForm(forms.Form):
    Client_List = forms.ModelChoiceField(
            queryset=Bridges.objects.values_list("CLIENT_NAME", flat=True).distinct(),
            empty_label=None
    )
    
class CsvImportForm(forms.Form):
        my_csv_list = forms.FileField()

        def process_import_data(self):
                f = io.TextIOWrapper(self.cleaned_data['my_csv_list'].file)
                reader = csv.DictReader(f)
                for data in reader:      
                        Bridges.objects.update_or_create(BILLING_DATE=data['BILLING_DATE'],POLICY_NUMBER=data['POLICY_NUMBER'],CLIENT_NAME=data['CLIENT_NAME'],LIFE_RATE=data['LIFE_RATE'],LIFE_VOLUME=data['LIFE_VOLUME'],EHC_S_RATE=data['EHC_S_RATE'],EHC_S_VOLUME=data['EHC_S_VOLUME'],EHC_C_RATE=data['EHC_C_RATE'],EHC_C_VOLUME=data['EHC_C_VOLUME'],EHC_F_RATE=data['EHC_F_RATE'],EHC_F_VOLUME=data['EHC_F_VOLUME'])
                return f

class CsvExportForm(forms.Form):
        Export_List = forms.ModelChoiceField(
                queryset=Bridges.objects.values_list("CLIENT_NAME", flat=True).distinct(),
                empty_label=None
        )



        
        
      


         


        
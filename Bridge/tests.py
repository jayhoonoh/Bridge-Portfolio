from django.test import TestCase
import csv, io
# Create your tests here.
class CsvImportForm(forms.Form):
        my_csv_list = forms.FileField()
       
def process_data():
f = open('C:/Users/joh/Desktop/CSVDATA.csv' , newline= ',')
reader = csv.DictReader(f)
                
for data in reader:      
    print(data['POLICY_NUMBER'])
                          

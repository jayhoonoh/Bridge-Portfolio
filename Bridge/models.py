from django.db import models

class Bridges(models.Model):
    BILLING_DATE = models.DateField()
    POLICY_NUMBER = models.IntegerField()
    CLIENT_NAME = models.CharField(max_length=50,primary_key=True)
    LIFE_RATE = models.FloatField()
    LIFE_VOLUME = models.IntegerField()
    EHC_S_RATE = models.FloatField()
    EHC_S_VOLUME = models.IntegerField()
    EHC_C_RATE = models.FloatField()
    EHC_C_VOLUME = models.IntegerField()
    EHC_F_RATE = models.FloatField()
    EHC_F_VOLUME = models.IntegerField()
    
    @property
    def LIFE_PREMIUM(self):
        return round(self.LIFE_RATE * self.LIFE_VOLUME / 1000,2)

    @property
    def EHC_S_PREMIUM(self):
        return round(self.EHC_S_RATE * self.EHC_S_VOLUME,2)

    @property
    def EHC_C_PREMIUM(self):
        return round(self.EHC_C_RATE * self.EHC_C_VOLUME,2)

    @property
    def EHC_F_PREMIUM(self):
        return round(self.EHC_F_RATE * self.EHC_F_VOLUME,2)

    @property
    def EHC_TOTAL_PREMIUM(self):
        return round(self.EHC_S_PREMIUM + self.EHC_C_PREMIUM + self.EHC_F_PREMIUM,2)





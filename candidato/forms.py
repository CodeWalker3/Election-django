from django.forms import ModelForm

from .models import Candidato

class CreateCandidatoForm(ModelForm):
    class Meta:
        model = Candidato
        fields = ['question','option_one','option_two','option_three']
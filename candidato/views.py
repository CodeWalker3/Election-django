from django.shortcuts import render , redirect
from django.http import HttpResponse
from .forms import CreateCandidatoForm
from .models import Candidato
# Create your views here.
def home(request):
    candidatos = Candidato.objects.all()
    context = {
        'candidatos' : candidatos
    }
    return render(request, 'home.html', context)

def create(request):
    if request.method == 'POST':
        form = CreateCandidatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateCandidatoForm()
    context = {
        'form' : form
    }
    return render(request, 'create.html', context)

def vote(request, candidato_id):
    candidato = Candidato.objects.get(pk=candidato_id)

    if request.method == 'POST':

        selected_option = request.POST['poll']
        if selected_option == 'option1':
            candidato.option_one_count += 1
        elif selected_option == 'option2':
            candidato.option_two_count += 1
        elif selected_option == 'option3':
            candidato.option_three_count += 1
        else:
            return HttpResponse(400, 'Invalid form')

        candidato.save()

        return redirect('results', candidato.id)

    context = {
        'candidato' : candidato
    }
    return render(request, 'vote.html', context)

def results(request, candidato_id):
    candidato = Candidato.objects.get(pk=candidato_id)
    context = {
        'candidato' : candidato
    }
    return render(request, 'results.html', context)
from django.shortcuts import render
from django import forms


class cmdForm(forms.Form):
    your_cmd = forms.CharField(label='cmd: ', max_length=20)


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def neo(request):
    return render(request, 'main/textneo.html')

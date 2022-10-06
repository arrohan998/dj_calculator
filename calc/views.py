from django.shortcuts import render

# Create your views here.
def calc(request):
    #my_dict = {'Insert_Me': "I am a text from registration/Views.py"}
    return render(request,'newtemp/calculator_b4.html')
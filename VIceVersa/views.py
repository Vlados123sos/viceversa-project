from django.shortcuts import render

def main_page(responce):
    return render(responce,'home.html')
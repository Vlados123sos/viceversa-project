from django.shortcuts import render

def main_page(request):
    return render(request,'home.html')
def reverse(request):
    user_text=request.GET['usertext']
    s=user_text.split()
    sum_of_words=len(s)
    reversed_text=user_text[::-1]
    return render(request,'reverse.html',{'usertext':user_text,'reversedtext':reversed_text,'sumwords':sum_of_words})

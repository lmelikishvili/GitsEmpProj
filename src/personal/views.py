from django.shortcuts import render
#from personal.models import Questions
from account.models import Account

# Create your views here.

def home_screen_view(request):
    context = {}
    # list_of_values = [
    #     "Levani",
    #     "Melikishvili",
    #     33
    # ]
    # context['list_content'] = list_of_values
    # quests = Questions.objects.all()
    # context['questions'] = quests

    acc = Account.objects.all()
    context['acc_list'] = acc

    return render(request, 'personal/home.html', context)

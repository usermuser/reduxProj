from django.shortcuts import render
# from django.http import HttpResponse


def landing_view(request):
    # example
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context = {'latest_question_list': latest_question_list}
    # return render(request, 'polls/index.html', context)
    return render(request, 'landing/base.html')

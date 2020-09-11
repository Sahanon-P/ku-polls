from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from .models import Question
from django.template import loader
# Create your views here.


def index(request):
    latest_question_list = Question.objects.order_by
    # output = ', '.join([q.question_text for q in latest_question_list])
    # template = loader.get_template('polls/index.html')
    context = {'lastest_question_list': latest_question_list, }
    return render(request, 'polls/index.html', context)
    # return HttpResponse(template.render(context,request))


def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does nit exist")
    # return HttpResponse("You're looking at question %s" % question_id)
    question = get_object_or_404(Question,pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    respone = "You're looking at the results of question %s."
    return HttpResponse(respone % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s" % question_id)

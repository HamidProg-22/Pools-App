from django.shortcuts import render, get_object_or_404
from django.http import Http404
# from django.http import HttpResponse
from polls.models import Question
# from django.template import loader

# Create your views here.

def index(request):
    # return HttpResponse("Hello, World. You're the polls index.")
    # latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # output = ", ".join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    # template = loader.get_template("polls/index.html")
    # context = {"latest_question_list": latest_question_list}
    # return HttpResponse(template.render(context, request))
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)
    



# detail
def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question Doesn't Exist")
    # return render(request, "polls/details.html", {'question':question})
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/details.html", {'question':question})


# results
def results(request, question_id):
    response = "You're Looking at the Results of Question %s."
    return HttpResponse(response % question_id)


# vote
def vote(request, question_id):
    return HttpResponse("You're Voting on Question %s." % question_id)




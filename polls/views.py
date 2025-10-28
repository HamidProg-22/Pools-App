from django.shortcuts import render
from django.http import HttpResponse

from polls.models import Question
from django.template import loader

# Create your views here.

def index(request):
    # return HttpResponse("Hello, World. You're the polls index.")
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # output = ", ".join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    template = loader.get_template("polls/index.html")
    context = {"latest_question_list": latest_question_list}
    return HttpResponse(template.render(context, request))



# detail
def detail(request, question_id):
    return HttpResponse("You're Looking at Question %s." % question_id)

# results
def results(request, question_id):
    response = "You're Looking at the Results of Question %s."
    return HttpResponse(response % question_id)


# vote
def vote(request, question_id):
    return HttpResponse("You're Voting on Question %s." % question_id)




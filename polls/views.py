from audioop import reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Choice, Question
from django.views import generic


# Create your views here.


# fuction view
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]

#     context = {
#         'latest_question_list': latest_question_list
#     }

#     return render(request, 'polls/index.html', context)


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]


# fuction view
# def detail(request, question_id):
#     # try:
#     #     question = Question.objects.get(pk = question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404('Question does not exist')

#     question = get_object_or_404(Question, pk=question_id)

#     return render(request, 'polls/detail.html', {'question': question})


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


# fuction view
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)

#     return render(request, 'polls/results.html', {'question': question})


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {"question": question, "error_message": "You did not select a choice."}

    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html", context)
    else:
        selected_choice.votes += 1
        selected_choice.save()

        # http://127.0.0.1:8000/polls/1/results/
        # return HttpResponseRedirect('https://www.baidu.com')
        return HttpResponseRedirect(
            f"http://127.0.0.1:8000/polls/{question.id}/results/"
        )
        # HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

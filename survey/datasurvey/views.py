from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.views import generic

from .models import Question, Choice

# Get question and display them


class IndexView(generic.ListView):
    template_name = 'datasurvey/index.html'
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]

# Show specific question and choices


class DetailView(generic.DetailView):
    model = Question
    template_name = 'datasurvey/detail.html'


# Get question and display results
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'datasurvey/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        select_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'datasurvey/detail.html',
                      {'question': question, 'error_message': "You didn't select a choice"})
    else:
        select_choice.vote += 1
        select_choice.save()

    return HttpResponseRedirect(reverse('datasurvey:results', args=(question.id,)))

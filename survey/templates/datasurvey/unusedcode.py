# urlpatterns = [
#     path('', views.IndexView.as_view(), name='index'),
#     path('<int:question_id>/', views.detail, name='detail'),
# path('<int:question_id>/results/', views.results, name='results'),
#     path('<int:question_id>/vote/', views.vote, name='vote'),
# ]

# Get questions and display them
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'datasurvey/index.html', context)

# Show specific question and choices


# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'datasurvey/detail.html', {'question': question})

# Get question and display results


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'datasurvey/results.html', {'question': question})

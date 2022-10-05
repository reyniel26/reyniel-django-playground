from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render
from django.db.models import F
from django.views import generic
from django.utils import timezone

from .models import Choice, Question

# Create your views here.
# def index(request):
#     """
#     Because it's convenient, let's use Django's own database API,
#     which we covered in Tutorial 2. Here's one stab at a new index() view,
#     which displays the latest 5 poll questions in the system, separated
#     by commas, according to publication date:
#     """
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]

#     # template = loader.get_template('polls/index.html') # template/polls/index.html

#     context = {
#         'latest_question_list':latest_question_list
#     }

#     # return HttpResponse(template.render(context,request))

#     # Note that once we’ve done this in all these views,
#     # we no longer need to import loader and HttpResponse
#     # (you’ll want to keep HttpResponse if you still have
#     # the stub methods for detail, results, and vote).
#     return render(request,'polls/index.html',context)

# def detail(request,question_id):
#     # return HttpResponse("You're looking at question %s." % question_id)

#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist")

#     # The get_object_or_404() function takes a Django model
#     # as its first argument and an arbitrary number of keyword arguments,
#     # which it passes to the get() function of the model’s manager.
#     # It raises Http404 if the object doesn’t exist.
#     question = get_object_or_404(Question,pk=question_id)
#     return render(request,'polls/detail.html',{'question':question})

# def results(request,question_id):
#     # response = "You're looking at the results of question %s."
#     # return HttpResponse(response % question_id)
#     question = get_object_or_404(Question,pk=question_id)
#     return render(request,'polls/results.html',{'question':question})


def vote(request,question_id):
    # return HttpResponse("You're voting on question %s." % question_id)

    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError,Choice.DoesNotExist):
        # Redifplay the question voting form
        return render( request,'polls/detail.html',{
            'question':question,
            'error_message':"You didn't select a choice,",
        })
    else:
        selected_choice.votes = F('votes') + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))


# Generic View for Index, Detail, and Result

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """ Return the last five published questions. """
        # return Question.objects.order_by('-pub_date')[:5]

        # Fix bug
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Exclude any questions that aren't published yet
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


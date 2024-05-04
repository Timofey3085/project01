from django.shortcuts import render, redirect
from .models import Survey, Question
from .forms import QuestionForm
from django.views.generic import DetailView, UpdateView, DeleteView


class PageDetailView(DetailView):
    model = Survey
    template_name = 'main/page_view.html'
    context_object_name = 'page'


class PageUpdateView(UpdateView):
    model = Survey
    template_name = 'main/question.html'
    form_class = QuestionForm
    success_url = '/detail/'


class PageDeleteView(DeleteView):
    model = Survey
    template_name = 'main/delete.html'
    success_url = '/detail/'


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def next(request):
    return render(request, 'main/next.html')


def detail(request):
    survey = Survey.objects.all().order_by('-date')
    return render(request, 'main/detail.html', {'survey': survey})


def question_view(request):
    error = ''
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('detail')
        else:
            error = 'Форма не верно заполнена'

    form = QuestionForm()

    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/question.html', context)



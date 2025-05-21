from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from .models import Problem, Submission

@login_required
def dashboard(request):

    problems    = Problem.objects.all().order_by('id')
    submissions = Submission.objects.filter(user=request.user).order_by('-submitted_at')

    template = loader.get_template('dashboard.html')
    context = {
        'problems':    problems,
        'submissions': submissions,
    }
    return HttpResponse(template.render(context, request))

@login_required
def problems_list(request):

    problems = Problem.objects.all().order_by('id')
    template = loader.get_template('problems_list.html')
    context = {'problems': problems}
    return HttpResponse(template.render(context, request))

@login_required
def my_submissions(request):

    submissions = Submission.objects.filter(user=request.user).order_by('-submitted_at')
    template = loader.get_template('my_submissions.html')
    context = {'submissions': submissions}
    return HttpResponse(template.render(context, request))
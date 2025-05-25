import subprocess, tempfile, os
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Problem, TestCase, Submission

@login_required
def dashboard(request):
    problems = Problem.objects.filter(created_by__is_superuser=True)
    submissions = Submission.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'problems': problems, 'submissions': submissions})

@login_required
def problem_detail(request, pk):
    problem = Problem.objects.get(pk=pk)
    public_cases = problem.testcases.filter(is_public=True)
    return render(request, 'problem_detail.html', {'problem': problem, 'public_cases': public_cases})

@login_required
def submit_solution(request, pk):
    problem = Problem.objects.get(pk=pk)
    if request.method == 'POST':
        code = request.POST['code']
        sub = Submission.objects.create(user=request.user, problem=problem, code=code)
        verdict, details = run_testcases(problem, code)
        sub.status = verdict
        sub.verdict_details = details
        sub.save()
        return HttpResponseRedirect(reverse('dashboard:dashboard'))
    return HttpResponseRedirect(reverse('dashboard:problem_detail', args=[pk]))

# Helper to execute code and compare outputs

def run_testcases(problem, code_text):
    verdict = 'A'
    details = ''
    for tc in problem.testcases.filter(is_public=False):
        with tempfile.NamedTemporaryFile(delete=False, suffix='.py') as f:
            f.write(code_text.encode())
            fname = f.name
        try:
            proc = subprocess.run(
                ['python3', fname],
                input=tc.input_data.encode(),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=2
            )
            actual = proc.stdout.decode().strip()
            expected = tc.expected_output.strip()
            if proc.returncode != 0:
                verdict = 'E'
                details += f"Error in TC {tc.id}: {proc.stderr.decode()}\n"
                break
            if actual != expected:
                verdict = 'R'
                details += f"TC {tc.id} failed: expected '{expected}', got '{actual}'\n"
                break
        except subprocess.TimeoutExpired:
            verdict = 'T'
            details += f"TC {tc.id} timed out.\n"
            break
        finally:
            os.remove(fname)
    return verdict, details
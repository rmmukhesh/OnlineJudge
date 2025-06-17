import subprocess, tempfile, os
from django.shortcuts import render, get_object_or_404
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
        language = request.POST.get('language', 'CPP')
        sub = Submission.objects.create(user=request.user, problem=problem, code=code, language=language)
        verdict, details = run_testcases(problem, code, language)
        sub.status = verdict
        sub.verdict_details = details
        sub.save()
        return HttpResponseRedirect(reverse('dashboard:dashboard'))
    return HttpResponseRedirect(reverse('dashboard:problem_detail', args=[pk]))

# Helper to execute code and compare outputs

def run_testcases(problem, code_text, language):
    suffix = '.py' if language == 'PY' else '.cpp'
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as src:
        src.write(code_text.encode())
        src_name = src.name

    exe_path = None
    try:
        if language == 'CPP':
            exe_path = src_name + '.out'
            compile_proc = subprocess.run(
                ['g++', src_name, '-o', exe_path],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=5
            )
            if compile_proc.returncode != 0:
                return 'E', f"Compilation error"

        run_cmd = ['python3', src_name] if language == 'PY' else [exe_path]
 
        all_cases = problem.testcases.all().order_by('id')
        for idx, tc in enumerate(all_cases, start=1):
            try:    
                proc = subprocess.run(
                    run_cmd,
                    input=tc.input_data.encode(),
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    timeout=2
                )
            except subprocess.TimeoutExpired:
                return 'T', f"Time Limit Exceeded on test case #{idx}"

            actual   = proc.stdout.decode().strip()
            expected = tc.expected_output.strip()

            if proc.returncode != 0:
                return 'E', f"Runtime error on test case #{idx}"
            if actual != expected:
                return 'R', f"Wrong answer on test case #{idx}"
    
        return 'A', ''

    finally:
        os.remove(src_name)
        if exe_path and os.path.exists(exe_path):
            os.remove(exe_path)

@login_required
def submission_detail(request, pk):
    sub = get_object_or_404(Submission, pk=pk, user=request.user)
    return render(request, 'submission_detail.html', {'submission': sub})

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from .models import Submission
from code_evaluation.views import evaluate_code

def submit_code(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        test_cases = request.POST.get('test_cases')
        
        # Evaluate the code using the existing evaluation function
        evaluation_result = evaluate_code(request, code, test_cases)
        if evaluation_result['verdict'] == 'Passed':
            # If the code passes the test cases, proceed with submission
            submission = Submission.objects.create(code=code, test_cases=test_cases, verdict='')
            return JsonResponse({
                'message': 'Code submitted successfully!',
                'submission_id': submission.id,
            })
        else:
            # If the code fails the test cases, return the evaluation result
            return JsonResponse(evaluation_result)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed.'}, status=405)

def view_submissions(request, submission_id):
    try:
        submission = Submission.objects.get(id=submission_id)
        return JsonResponse({
            'code': submission.code,
            'test_cases': submission.test_cases,
            'verdict': submission.verdict,
            'timestamp': submission.timestamp,
        })
    except Submission.DoesNotExist:
        return JsonResponse({'error': 'Submission not found'}, status=404)

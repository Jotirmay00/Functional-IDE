from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from .models import Submission

def submit_code(request):
    if request.method == 'POST':
        code = request.POST.get('code')

        # Create and save the submission
        submission = Submission.objects.create (code=code)
        submission.save()

        return JsonResponse({'message': 'Code submitted successfully!'})

    return JsonResponse({'error': 'Only POST requests are allowed.'}, status=405)

def view_submissions(request):
    if request.method == 'GET':
        user = request.user
        submissions = Submission.objects.all().order_by('-timestamp')

        return render(request, 'submissions.html', {'submissions': submissions})

    return JsonResponse({'error': 'Only GET requests are allowed.'}, status=405)

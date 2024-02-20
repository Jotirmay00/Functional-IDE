from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Submission
from .serializers import SubmissionSerializer
from code_evaluation.views import evaluate_code
from django.http import HttpRequest

@api_view(['POST'])
def submit_code(request):
    if request.method == 'POST':
        serializer = SubmissionSerializer(data=request.data)
        if serializer.is_valid():
            # Save the code submission
            submission = serializer.save()
            return Response({
                'message': 'Code submitted successfully!',
                'submission_id': submission.id,
            })
        else:
            return Response(serializer.errors, status=400)
    else:
        return Response({'error': 'Only POST requests are allowed.'}, status=405)
@api_view(['GET'])
def view_submissions(request):
    try:
        submission = Submission.objects.all()
        serializer = SubmissionSerializer(submission,many=True)
        return Response(serializer.data)
    except Submission.DoesNotExist:
        return Response({'error': 'Submission not found'}, status=404)

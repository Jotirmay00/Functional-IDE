
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Submission
from .serializers import SubmissionSerializer
from code_evaluation.views import evaluate_code

@api_view(['POST'])
def submit_code(request):
    if request.method == 'POST':
        serializer = SubmissionSerializer(data=request.data)
        if serializer.is_valid():
            code = serializer.validated_data['code']
            test_cases = serializer.validated_data['test_cases']
            
            # Evaluate the code using the existing evaluation function
            evaluation_result = evaluate_code(request, code, test_cases)
            if evaluation_result['verdict'] == 'Passed':
                # If the code passes the test cases, proceed with submission
                submission = serializer.save(verdict='')
                return Response({
                    'message': 'Code submitted successfully!',
                    'submission_id': submission.id,
                })
            else:
                # If the code fails the test cases, return the evaluation result
                return Response(evaluation_result, status=400)
        else:
            return Response(serializer.errors, status=400)
    else:
        return Response({'error': 'Only POST requests are allowed.'}, status=405)

@api_view(['GET'])
def view_submissions(request, submission_id):
    try:
        submission = Submission.objects.get(id=submission_id)
        serializer = SubmissionSerializer(submission)
        return Response(serializer.data)
    except Submission.DoesNotExist:
        return Response({'error': 'Submission not found'}, status=404)

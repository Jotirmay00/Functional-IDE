
import subprocess
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CodeEvaluationSerializer

@api_view(['POST'])
def evaluate_code(request):
    if request.method == 'POST':
        serializer = CodeEvaluationSerializer(data=request.data)
        if serializer.is_valid():
            user_code = serializer.validated_data.get('code')
            # Predefined testcases to check the correctness of the program
            test_cases = [
                (([2, 7, 11, 15], 9), [0, 1]),               
                (([-3, 4, 3, 90], 0), [0, 2]),           
                (([3, 3], 6), [0, 1]),    
            ]
            # Results dict for storing the outputs
            results = {}

            for idx, (input_value, expected_output) in enumerate(test_cases, start=1):
                try:
                    # Executing the code by creating a subprocess 
                    process = subprocess.Popen(
                        ['python', '-c', user_code],
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        text=True
                    )
                    stdout, stderr = process.communicate(input=str(input_value).encode(), timeout=10)
                    output = stdout.strip() if stdout else None  # Capture output
                    
                    if stderr:
                        results[f"Test Case {idx}"] = {"result": "Failed", "error": stderr, "output": output}
                    else:
                        actual_output = [int(x) for x in stdout.strip().split()] if stdout else None
                        if actual_output == expected_output:
                            results[f"Test Case {idx}"] = {"result": "Passed", "output": output}
                        else:
                            results[f"Test Case {idx}"] = {"result": "Failed", "error": "Output mismatch", "output": output}

                except subprocess.TimeoutExpired:
                    results[f"Test Case {idx}"] = {"result": "Failed", "error": "Execution timed out", "output": None}

                except Exception as e:
                    results[f"Test Case {idx}"] = {"result": "Failed", "error": str(e), "output": None}
            verdict = "Passed" if all(result["result"] == "Passed" for result in results.values()) else "Failed"
            
            # Return the evaluation result along with the output
            return Response({"verdict": verdict, "results": results})
        else:
            return Response(serializer.errors, status=400)
    else:
        return Response({'error': 'Only POST requests are allowed.'}, status=405)

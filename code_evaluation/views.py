from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CodeEvaluationSerializer

@api_view(['POST'])
def evaluate_code(request):
    if request.method == 'POST':
        # Deserialize the request data using CodeEvaluationSerializer
        serializer = CodeEvaluationSerializer(data=request.data)
        
        # Check if the serializer is valid
        if serializer.is_valid():
            # Extract function code from the validated data
            function_code = serializer.validated_data.get('code')

            # Define predefined test cases
            test_cases = [
                (([2, 7, 11, 15], 9), [0, 1]),                 # Basic scenario
                (([-3, 4, 3, 90], 0), [0, 2]),                # Negative and zero sum
                (([3, 3], 6), [0, 1]),                        # Duplicate elements
                (([1, 2, 3, 4, 5], 9), [3, 4]),               # Larger array with positive sum
                (([-1, -2, -3, -4, -5], -8), [2, 4]),          # Larger array with negative sum
                (([0, 1, 2, 3], 4), [1, 3]),                  # Zero included in the array
                (([1, 2, 3, 4], 10), []),                      # No elements sum up to the target
                (([], 5), []),                                # Empty array
                (([1], 1), []),                               # Single element array
                (([1, 2, 3, 4], 0), []),                       # Zero as the target
                (([1, 2, 3, 4], -5), []),                      # Negative target
            ]

            # Initialize results dictionary
            results = {}

            try:
                # Execute the provided function code
                for idx, (input_value, expected_output) in enumerate(test_cases, start=1):
                    # Execute the function code in a local namespace
                    namespace = {}
                    exec(function_code, namespace)
                    
                    # Extract the function from the namespace
                    function = namespace.get('find_two_sum')

                    # Call the function with input value
                    output = function(*input_value)

                    # Compare output with expected output
                    if output == expected_output:
                        results[f"Test Case {idx}"] = {"result": "Passed", "output": output}
                    else:
                        results[f"Test Case {idx}"] = {"result": "Failed", "error": "Output mismatch", "output": output, "expected_output": expected_output}

                # Determine overall verdict
                verdict = "Passed" if all(result["result"] == "Passed" for result in results.values()) else "Failed"
                
                # Return response with verdict and detailed results
                return Response({"verdict": verdict, "results": results})
            
            except Exception as e:
                # Return any exceptions that occurred during execution
                return Response({'error': str(e)}, status=400)
        
        else:
            # If serializer is not valid, return errors
            return Response(serializer.errors, status=400)
    else:
        return Response({'error': 'Only POST requests are allowed.'}, status=405)

from django.shortcuts import render

import subprocess
from django.http import JsonResponse

def evaluate_code(request):
    if request.method == 'POST':
        user_code = request.POST.get('code')

        # Define predefined test cases (format: (input_value, expected_output))
        test_cases = [
            (([2, 7, 11, 15], 9), [0, 1]),               
            (([-3, 4, 3, 90], 0), [0, 2]),           
            (([3, 3], 6), [0, 1]),    
           
        ]

        # Results dictionary to store the results of each test case
        results = {}

        # Iterate over test cases
        for idx, (input_value, expected_output) in enumerate(test_cases, start=1):
            try:
                # Executing user's code for every test case
                process = subprocess.Popen(
                    ['python', '-c', user_code],
                    stdin=subprocess.PIPE,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True
                    
                )
                stdout, stderr = process.communicate(input=input_value, timeout=10)

                # Check if there's any error during code execution
                if stderr:
                    results[f"Test Case {idx}"] = {"result": "Failed", "error": stderr}
                else:
                    # Compare the output with the expected output
                    if stdout.strip() == expected_output.strip():
                        results[f"Test Case {idx}"] = {"result": "Passed"}
                    else:
                        results[f"Test Case {idx}"] = {"result": "Failed", "error": "Output mismatch"}

            # Error for time out or memory exceeded
            except subprocess.TimeoutExpired:
                results[f"Test Case {idx}"] = {"result": "Failed", "error": "Execution timed out"}

            except Exception as e:
                results[f"Test Case {idx}"] = {"result": "Failed", "error": str(e)}


        # Check if all test cases passed and sending the verdict
        verdict = "Passed" if all(result["result"] == "Passed" for result in results.values()) else "Failed"

        return JsonResponse({"verdict": verdict, "results": results})

    else:
        return JsonResponse({'error': 'Only POST requests are allowed.'}, status=405)



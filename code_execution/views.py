from django.shortcuts import render
import subprocess
from django.http import JsonResponse

def execute_code(request):
    if request.method == 'POST':
        # Get the code from the user
        code = request.POST.get('code')

        # Defining the command to execute the Python Code 
        command = ['python', '-c', code]

        try:
            # Executing the code by creating a subprocess 
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            stdout, stderr = process.communicate(timeout=10)  # Adjust timeout

            # Check if there's any error
            if stderr:
                output = stderr
            else:
                output = stdout

            # Return the output
            return JsonResponse({'output': output})
        
        # Return Execution taking too long
        except subprocess.TimeoutExpired:
            return JsonResponse({'output': 'Execution timed out.'}, status=500)

    else:
        return JsonResponse({'error': 'Only POST requests are allowed.'}, status=405)

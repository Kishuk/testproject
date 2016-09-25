from django.shortcuts import render
from .forms import NameForm
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from time import time


def print_fibonacci_series(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            start = time()
            number = form.cleaned_data['number']
            if number < 1:
                return HttpResponse("Invalid input, Please enter number equal to and greater than 1")

            result = recur_fibo(number)
            total_time = time() - start
            return HttpResponse("%dth element in the sequence is %s and total time taken in processing is %.6f seconds" % (number,result,total_time))
    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'fibonacci/name.html', {'form': form})

def recur_fibo(n):
   """Recursive function to
   print Fibonacci sequence"""
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))
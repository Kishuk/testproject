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
   
    if n <= 1:
	return n
    else if n==2:
	return 1
  # temp1, temp2 to keep track of (p-2)th and (p-1)th term respectively and temp3 is pth term: p is any number
    else:
        temp1=1
	temp2=1
	while (n>2):
	    temp3=temp1+temp2
    	    temp1=temp2
	    temp2=temp3
	    n-=1
	return temp3
       

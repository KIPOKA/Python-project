from django.shortcuts import render

# Create your views here.


def example_view(request):
    return render(request, 'my_app/example.html')


def variable_view(request):
    my_var = {
        'first_name': 'Katabe',
        'last_name': 'Kipoka Lady',
        'some_list': [1, 2, 3, 3], 'user_logged_in': True
    }
    return render(request, 'my_app/variables.html', context=my_var)

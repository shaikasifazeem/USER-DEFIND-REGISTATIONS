from django.shortcuts import render

# Create your views here.

def insert_filters(request):
    import datetime
    t=datetime.datetime.now()
    d={'data':'hai this is FILTER functions '}
    d={'t':t}

    return render(request,'insert_filters.html',d)


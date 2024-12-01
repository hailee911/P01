from django.shortcuts import render
from datetime import datetime

def main(request):
    todate = datetime.now()
    return render(request, 'main.html', {'todate':todate})

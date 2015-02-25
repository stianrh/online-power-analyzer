from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from flash.models import Flash

@csrf_protect
def index(request):
    return render(request, 'flash/index.html', {})

def compile(request):
    obj = Flash.objects.get(id = 1)
    obj.compile()
    print "HELLO"
    return redirect('flash_index')

from django.shortcuts import render, redirect
from measure.forms import TestForm
from measure.models import Measure
from django.views.decorators.csrf import csrf_protect
import SCPI, time
from types import *
import numpy as np
from pylab import *
import json
from measure import tasks

@csrf_protect
def index(request):
    if (request.method == 'POST'):
        form = TestForm(request.POST)
        if form.is_valid():
            q = Measure.objects.start()
            q.voltage = form.cleaned_data['voltage']
            q.time = form.cleaned_data['time']
            q.resolution = form.cleaned_data['resolution']
            q.save()
            context = {
                'testform': form,
            }
    else:
        form = TestForm()
        context = {
            'testform': form,
        }
    obj = Measure.objects.all().order_by('id').reverse()
    context.update({
        'objects': obj,
    })
    return render(request, 'measure/index.html', context)

def measure(request, num):
    obj = Measure.objects.get(id = num)
    avg_ua = obj.average*1000000
    context = {
        'testid': num,
        'obj': obj,
        'avg': avg_ua,
    }
    return render(request, 'measure/measure.html', context)

def start(request, num):

    obj = Measure.objects.get(id = num)
    from tasks import current_measure
    current_measure.delay(obj)
    context = {
        'obj': obj,
        'testid': num,
        'avg': obj.average,
    }
    return redirect('measure', num)

def get_image(request, num):
    obj = Measure.objects.get(id = num)
    y = json.loads(obj.measure_list)
    x = np.linspace(0, obj.time, len(y)).tolist()
    plot(x,y)
    from django.http import HttpResponse
    fig = HttpResponse(content_type="image/png")
    savefig(fig, format='png')
    close()
    return fig


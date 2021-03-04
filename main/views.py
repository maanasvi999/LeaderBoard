from django.shortcuts import render, redirect
from .models import Marks
from .forms import MarksForm
from django.contrib import messages
from django.db.models import Q

def homepage(request):
    return render(request = request,
                  template_name = "main/home.html")

def leaderboard(request):
    context = {}
    marks = [m for m in Marks.objects.all().order_by('-percentage')]
    context  = {'marks': marks}
    return render(request = request, template_name = 'main/leaderboard.html', context = context)

def addmarks(request):
    form = MarksForm()
    if request.method == 'POST':
        form = MarksForm(request.POST)
        roll_no = form['roll_no'].value()
        if Marks.objects.filter(roll_no = roll_no).exists():
            messages.error(request, "User Data Already exists.")
            return redirect('main:addmarks')
        
        name = form['name'].value()
        math_marks = int(form['math_marks'].value())
        physics_marks = int(form['physics_marks'].value())
        chemistry_marks = int(form['chemistry_marks'].value())
        total = math_marks + physics_marks + chemistry_marks 
        percentage = total/3
        percentage = round(percentage, 2)
        
        if form.is_valid():
            if (math_marks<0 or math_marks>100) or (chemistry_marks<0 or chemistry_marks>100) or (physics_marks<0 or physics_marks>100):
                messages.error(request, 'Invalid data Entry. Try again.')
            else:
                data = form.save(commit = False)
                data.total = total
                data.percentage = percentage
                data.save()
                messages.success(request, "Added to Leaderboard!")
                context = {'form':form, 'total':total, 'percentage':percentage}
                return render(request, 'main/addmarks.html', context)
        else:
            messages.error(request, "Invalid Entry. Try Again")
    
    context = {'form':form}
    return render(request, 'main/addmarks.html', context)

def search(request):
    if request.method == 'GET':
        srh = request.GET.get('query')
        if srh != "":
            marks = Marks.objects.filter(Q(roll_no__icontains = srh) | Q(name__icontains = srh) | Q(total__icontains = srh) | Q(percentage__icontains = srh))
        else:
            messages.error(request, "Invalid Search. Try Again")
            return redirect("main:leaderboard")
    return render(request, 'main/leaderboard.html', {'marks': marks})

def single_slug(request, single_slug):
    messages.info(request, 'No Corresponding data for that request')
    return redirect('main:homepage')

from rest_framework import viewsets
from .serializers import MarksSerializer

class MarksViewSet(viewsets.ModelViewSet):
    queryset = Marks.objects.all().order_by('-percentage')
    serializer_class = MarksSerializer
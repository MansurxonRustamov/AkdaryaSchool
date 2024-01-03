from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import *
from .forms import *
from .models import *
from chsb.models import *

# Create your views here.

def Home(request):
    prizes = Yutuqlar.objects.all()
    context={
        'yutuq':prizes
    }
    return render(request, 'index.html', context)
def About(request):
    prizes = Yutuqlar.objects.all()
    context={
        'yutuq':prizes
    }
    return render(request, 'about-us.html', context)
subject = [
    'Matematika', "Ingliz tili", "Fizika", "Tarix", "Ona Tili va Adabiyot", "Huquq"
]

def TeacherDetail1(request):
    
    if ("techsearch" in request.GET) or ("techsubject" in request.GET) :
        result = request.GET['techsearch']
        res = request.GET['techsubject']
        data = Teachers.objects.filter(full_name__contains=result, subject__icontains=res).order_by('subject')
    else:
        data = Teachers.objects.all().order_by('subject')
    try:
        context ={
            'data':data,
            'subject': subject,
            'count': data.count(),
            'result': result if request.GET['techsearch'] else "",
            'res': res if request.GET['techsubject'] else "",
        }
    except:
        context ={
            'data':data,
            'subject': subject,
            'count': data.count(),
            }
    return render(request, 'teachers.html', context)



class ContactSuccess(TemplateView):
	template_name = 'contactSuccess.html'
def contactus(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success') 
    else:
        form = ContactForm()

    return render(request, 'contact-us.html', {'form': form})

def rooms(request):
    room = Rooms.objects.all().order_by("name")
    context={
        'room':room
    }
    return render(request, 'rooms.html', context)

# Dashboard

def dashPanel(request):

    if not request.user.is_authenticated:
        return redirect('login')
    
    chsbCount = Chsblar.objects.all()
    data = Students.objects.get(user=request.user)
    groupAllMark = Marks.objects.filter(grade__icontains=data.grade, chsbCount__contains=chsbCount.count()).order_by("-jamiBaho")
    groupAllMarkOld = Marks.objects.filter(grade__icontains=data.grade, chsbCount__contains=(chsbCount.count()-1))
    # ownMark = Marks.objects.filter(grade__icontains=data.grade, chsbCount__contains=chsbCount.count())
    
    jamione=[]
    jamiallold=[]
    for i in groupAllMarkOld:
        jamiallold.append(i.jamiBaho)

    for i in groupAllMark:
        jamione.append(i.jamiBaho)
    dssum = sum(jamione)
    if groupAllMark[0].geometriya != None and groupAllMark[0].fizika != None:
        dataAllprosent = (dssum*5) / (8 * len(jamione))
        dataAllOldprosent = (sum(jamiallold)*5) / (8 * len(jamiallold))
        # ownProsent = (ownMark.jamiBaho * 5 )/ 8
    else:
        dataAllprosent = (dssum*5) / (4 * len(jamione))
        dataAllOldprosent = (sum(jamiallold)*5) / (4 * len(jamiallold))
        # ownProsent = (ownMark.jamiBaho * 5 )/ 4

    prosUp = dataAllprosent - dataAllOldprosent

    contaxt ={
    'data':data,
    # "ownMark":ownMark,
    # "ownProsent":ownProsent,
    "markall":groupAllMark, 
    'jamiAllp':round(dataAllprosent, 1),
    'jamiAll': dssum,
    'prosUp':round(prosUp, 1)



    }
    return render(request, 'dashboard.html', contaxt)

def tablesWorks(request):
    data = Students.objects.get(user=request.user)
    context={'data':data}
    return render(request, 'tables.html', context)


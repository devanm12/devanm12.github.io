from django.shortcuts import render
from django.http import HttpResponseRedirect
from first_app.models import Program, Student
#from models import Program, Student

# Create your views here.

from django.http import HttpResponse
from .forms import StudentForm

clicked = 0

# 'request' name is convention. It can be some other name too.
def index(request) :
  global clicked
  clicked += 1
  program_values = Program.objects.all()
  my_dict = {'count' : clicked, 'program_rows' : program_values}
  return render(request, 'index.html', my_dict)

def help(request) :
  return render(request, 'help.html')

# def get_student(request):    
#   if request.method == 'POST':          
#     form = StudentForm(request.POST)     
#     if form.is_valid():
#         s_name = form.cleaned_data['name']
#         s_roll = form.cleaned_data['roll']
#         s_degree = form.cleaned_data['degree']        
#         s_branch = form.cleaned_data['branch']
 
#         return HttpResponseRedirect('/student/')
#   else: 
#       form =StudentForm()
#       return render(request, 'StudentForm.html', {'form': form})

def get_student(request) :
  if request.method == 'POST':
    form = StudentForm(request.POST)
    if form.is_valid():
        s_name = form.cleaned_data['name']
        s_roll = form.cleaned_data['roll']
        s_year = form.cleaned_data['year']
        s_dob = form.cleaned_data['dob']
        s_degree = form.cleaned_data['degree']
        s_branch = form.cleaned_data['branch']
        print(s_name, s_roll, s_year, s_dob, s_degree, s_branch)
        # Now insert into the model
        p = Program.objects.filter(title=s_degree,branch=s_branch).count()
        if p :
            s = Student(program=p, roll_number=s_roll, name=s_name, year=s_year, dob=s_dob)
            s.save()
        else :
            np = Program(title=s_degree, branch=s_branch)
            np.save()
            s = Student(program=np, roll_number=s_roll, name=s_name, year=s_year, dob=s_dob)
            s.save()
    return HttpResponseRedirect('/student/')
  else:
      form = StudentForm()
      return render(request, 'StudentForm.html', {'form': form})
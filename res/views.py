from django.shortcuts import render
from .forms import Resume, Academic, Skills, Ach, Prj, Con, Cert

def home(request):
    if request.method =='POST':
        form= Resume(request.POST)
        if form.is_valid():
            pass
    else:
        form= Resume()
    if request.method =='POST':
        form2= Academic(request.POST)
        if form2.is_valid():
            pass
    else:
        form2= Academic()
    
    
    if request.method =='POST':
        form3= Skills(request.POST)
        if form3.is_valid():
            pass
    else:
        form3= Skills()

    
    if request.method =='POST':
        form4= Ach(request.POST)
        if form4.is_valid():
            pass
    else:
        form4= Ach()
    
    
    if request.method =='POST':
        form5= Prj(request.POST)
        if form5.is_valid():
            pass
    else:
        form5= Prj()

    if request.method =='POST':
        form6= Cert(request.POST)
        if form6.is_valid():
            pass
    else:
        form6= Cert()

    if request.method =='POST':
        form7= Con(request.POST)
        if form7.is_valid():
            pass
    else:
        form7= Con()
    return render(request,"home.html",{'form': form, 'form2':form2, 'form3':form3, 'form4':form4, 'form5': form5, 'form6':form6, 'form7':form7})

def data(request):
    
    if request.method =='POST':
        form= Resume(request.POST)
        if form.is_valid():
           pass
    else:
        form= Resume()

    if request.method =='POST':
        form2= Academic(request.POST)
        if form2.is_valid():
            pass
    else:
        form2= Academic()
    
    if request.method =='POST':
        form3= Skills(request.POST)
        if form3.is_valid():
            pass
    else:
        form3= Skills()

    
    if request.method =='POST':
        form4= Ach(request.POST)
        if form4.is_valid():
            pass
    else:
        form4= Ach()

    if request.method =='POST':
        form5= Prj(request.POST)
        if form5.is_valid():
            pass
    else:
        form5= Prj()

    if request.method =='POST':
        form6= Cert(request.POST)
        if form6.is_valid():
            pass
    else:
        form6= Cert()

    if request.method =='POST':
        form7= Con(request.POST)
        if form7.is_valid():
            pass
    else:
        form7= Con()
    return render(request,"resum.html",{'name':form.cleaned_data['name'],
                                         'email':form.cleaned_data['email'],
                                         'Co': form.cleaned_data['Career_objective'],
                                         'Ins1':form2.cleaned_data['Institution_of_passing_10th'],
                                         'Marks1':form2.cleaned_data['Marks_in_10th_Class'],
                                         'Ins2':form2.cleaned_data['Institution_of_passing_12th'],
                                         'Marks2':form2.cleaned_data['Marks_in_12th_Class'],
                                         'Ins3':form2.cleaned_data['Name_of_respective_institution'],
                                         'Marks3':form2.cleaned_data['Marks_in_other_institution'],
                                         'Deg3':form2.cleaned_data['Name_of_Degree_'],
                                         'Sk1' : form3.cleaned_data['Skill_1'],
                                         'Sk2' : form3.cleaned_data['Skill_2'],
                                         'Sk3' : form3.cleaned_data['Skill_3'],
                                         'Sk4' : form3.cleaned_data['Skill_4'],
                                         'Sk5' : form3.cleaned_data['Skill_5'],
                                         'Ach1' : form4.cleaned_data['Ach1'],
                                         'Ach2' : form4.cleaned_data['Ach2'],
                                         'Ach3' : form4.cleaned_data['Ach3'],
                                         'Ach4' : form4.cleaned_data['Ach4'],
                                         'Ach5' : form4.cleaned_data['Ach5'],
                                         'Prj1' : form5.cleaned_data['Prj1'],
                                         'Prj2' : form5.cleaned_data['Prj2'],
                                         'Prj3' : form5.cleaned_data['Prj3'],
                                         'Prj4' : form5.cleaned_data['Prj4'],
                                         'Prj5' : form5.cleaned_data['Prj5'],
                                         'WorkEx':form5.cleaned_data['WorkEx'],
                                         'Cert1':form6.cleaned_data['Cert1'],
                                         'Cert2':form6.cleaned_data['Cert2'],
                                         'Cert3':form6.cleaned_data['Cert3'],
                                         'Cont':form7.cleaned_data['Cont']
                                         


                                          
                                                                 })
    



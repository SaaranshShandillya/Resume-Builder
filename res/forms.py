from django import forms

class Resume(forms.Form):
    name= forms.CharField(max_length=30)
    email=forms.EmailField(max_length=300)
    Career_objective= forms.CharField(
        max_length=3000,
        widget=forms.Textarea(),
    )
    
    

    def clean(self):
        clean_data=super(Resume,self).clean()
        name=clean_data.get('name')
        email=clean_data.get('Email Id')
        Career_objective=clean_data.get('Career Objective')

class Academic(forms.Form):
    Marks_in_10th_Class=forms.CharField()
    Institution_of_passing_10th= forms.CharField()
    Marks_in_12th_Class=forms.CharField()
    Institution_of_passing_12th= forms.CharField()
    Marks_in_other_institution=forms.CharField(required=False)
    Name_of_Degree_=forms.CharField(required=False)
    Name_of_respective_institution=forms.CharField(required=False)

    def clean2(self):
        clean2_data=super(Academic,self).clean()
        Marks_in_10th_Class=clean2_data.get('Marks in 10th Class')
        Institution_of_passing_10th=clean2_data.get('Institution of passing(10th)')
        Marks_in_12th_Class=clean2_data.get('Marks in 12th Class')
        Institution_of_passing_12th=clean2_data.get('Institution of passing(12th)')
        Marks_in_other_institution=clean2_data.get('Marks in other institution')
        Name_of_Degree_=clean2_data.get('Name of Degree')
        Name_of_respective_institution=clean2_data.get('Name of respective institution')

class Skills(forms.Form):
    Skill_1=forms.CharField()
    Skill_2=forms.CharField()
    Skill_3=forms.CharField(required=False)
    Skill_4=forms.CharField(required=False)
    Skill_5=forms.CharField(required=False)
        
    def clean3(self):
        clean3_data=super(Skills,self).clean()
        Skill_1=clean3_data.get('Skill 1')
        Skill_2=clean3_data.get('Skill 2')
        Skill_3=clean3_data.get('Skill 3')
        Skill_4=clean3_data.get('Skill 4')
        Skill_5=clean3_data.get('Skill 5')

class Ach(forms.Form):
    Ach1=forms.CharField(label='Acheivement 1')
    Ach2=forms.CharField(label='Acheivement 2')
    Ach3=forms.CharField(label='Acheivement 3', required=False)
    Ach4=forms.CharField(label='Acheivement 4', required=False)
    Ach5=forms.CharField(label='Acheivement 5', required=False)

    def clean4(self):
        clean4_data=super(Ach,self).clean()
        Ach1=clean4_data.get('Ach 1')
        Ach2=clean4_data.get('Ach 2')
        Ach3=clean4_data.get('Ach 3')
        Ach4=clean4_data.get('Ach 4')
        Ach5=clean4_data.get('Ach 5')

class Prj(forms.Form):
    Prj1=forms.CharField(label='Project 1')
    Prj2=forms.CharField(label='Project 2')
    Prj3=forms.CharField(label='Project 3', required=False)
    Prj4=forms.CharField(label='Project 4', required=False)
    Prj5=forms.CharField(label='Project 5', required=False)
    WorkEx= forms.CharField(
        max_length=500,
        widget=forms.Textarea(),
        label='Previous Work Experience'
    )
    

    def clean5(self):
        clean5_data=super(Prj,self).clean()
        Prj1=clean5_data.get('Prj 1')
        Prj2=clean5_data.get('Prj 2')
        Prj3=clean5_data.get('Prj 3')
        Prj4=clean5_data.get('Prj 4')
        Prj5=clean5_data.get('Prj 5')

class Cert(forms.Form):
    Cert1=forms.CharField(label='Cerification 1')
    Cert2=forms.CharField(label='Certification 2', required=False)
    Cert3=forms.CharField(label='Certification 3', required=False)

    def clean6(self):
        clean6_data=super(Cert,self).clean()
        Cert1=clean6_data.get('Cert 1')
        Cert2=clean6_data.get('Cert 2')
        Cert3=clean6_data.get('Cert 3')

class Con(forms.Form):
    Cont= forms.CharField(
        max_length=800,
        widget=forms.Textarea(),
        label='Further Contact Details or References'
    )

    def clean7(self):
        clean7_data=super(Con,self).clean()
        Cont=clean7_data.get('Cont')
    


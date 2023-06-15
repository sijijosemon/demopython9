from django import forms
from django.forms.widgets import DateInput

DEPARTMENT_CHOICES = [
    ('commerce', 'Commerce'),
    ('science', 'Science'),
    ('arts', 'Arts'),
]

COURSE_CHOICES = {
    'commerce': [
        ('bba', 'BBA'),
        ('bcom', 'BCom'),
    ],
    'science': [
        ('bsc', 'BSc'),
        ('btech', 'BTech'),
    ],
    'arts': [
        ('ba', 'BA'),
        ('bsw', 'BSW'),
    ],
}

PURPOSE_CHOICES = [
    ('enquiry', 'Enquiry'),
    ('place_order', 'Place Order'),
    ('return', 'Return'),
]

MATERIALS_PROVIDED_CHOICES = [
    ('debit_notebook', 'Debit Note Book'),
    ('pen', 'Pen'),
    ('exam_papers', 'Exam Papers'),
]

class RegistrationForm(forms.Form):
    name = forms.CharField(label='Name')
    dob = forms.DateField(label='DOB', widget=DateInput(attrs={'type': 'date'}))
    age = forms.IntegerField(label='Age')
    gender = forms.ChoiceField(label='Gender', widget=forms.RadioSelect,
                               choices=(('male', 'Male'), ('female', 'Female'), ('other', 'Other')))
    phone_number = forms.CharField(label='Phone Number')
    email = forms.EmailField(label='Email')
    address = forms.CharField(label='Address')
    department = forms.ChoiceField(label='Department', choices=DEPARTMENT_CHOICES)
    course = forms.ChoiceField(label='Course', choices=[], required=False)
    purpose = forms.ChoiceField(label='Purpose', choices=PURPOSE_CHOICES)
    materials_provided = forms.MultipleChoiceField(
        label='Materials Provided',
        choices=MATERIALS_PROVIDED_CHOICES,
        widget=forms.CheckboxSelectMultiple
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        department = self['department'].value()
        self.fields['course'].choices = COURSE_CHOICES.get(department, [])

    def clean(self):
        cleaned_data = super().clean()
        department = cleaned_data.get('department')
        course = cleaned_data.get('course')
        if department and course:
            if course not in [c[0] for c in COURSE_CHOICES.get(department, [])]:
                self.add_error('course', 'Invalid course selection.')

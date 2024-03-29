from django.contrib import admin
from .models import Person, Student, YEAR_IN_SCHOOL_CHOICES

# Register your models here.

admin.site.register(Student)

from django import forms
from django.contrib import messages


class PersonAdminForm(forms.ModelForm):

    extra_field = forms.ChoiceField(choices=YEAR_IN_SCHOOL_CHOICES)
    is_checked = forms.BooleanField()

    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(PersonAdminForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['is_checked'].required = False

    def save(self, commit=True):
        extra_field = self.cleaned_data.get('extra_field', None)
        is_checked = self.cleaned_data.get('is_checked', None)
        return super(PersonAdminForm, self).save(commit=commit)

    def clean_student(self):
        if self.cleaned_data.get('is_checked'):
            import ipdb; ipdb.set_trace()
            student = Student.objects.last()
            return student
        else:
            return self.cleaned_data.get('student')

    class Meta:
        model = Person
        fields = ('name', 'shirt_size', )


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_filter = ('name', )
    list_display_links = ('name', )
    form = PersonAdminForm
    fields = ('is_checked', 'name', 'student', 'shirt_size', 'extra_field', )

    class Media:
            js = ('js/conditional.js',)

    def save_model(self, request, obj, form, change):
        obj.student = Student.objects.last()
        messages.add_message(request, messages.INFO, 'Hello world.')
        super(PersonAdmin, self).save_model(request, obj, form, change)
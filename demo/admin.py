from django.contrib import admin
from .models import Person, Student, YEAR_IN_SCHOOL_CHOICES

# Register your models here.

admin.site.register(Student)

from django import forms


class PersonAdminForm(forms.ModelForm):

    extra_field = forms.ChoiceField(choices=YEAR_IN_SCHOOL_CHOICES)

    def save(self, commit=True):
        extra_field = self.cleaned_data.get('extra_field', None)
        student = Student.objects.last()
        self.cleaned_data['student'] = student
        import ipdb; ipdb.set_trace()
        # ...do something with extra_field here...
        return super(PersonAdminForm, self).save(commit=commit)

    class Meta:
        model = Person
        fields = ('name', 'shirt_size', )


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_filter = ('name', )
    list_display_links = ('name', )
    form = PersonAdminForm
    fields = ('name', 'student', 'shirt_size', 'extra_field', )

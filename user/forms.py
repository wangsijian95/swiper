from django import forms

from user.models import Profile


class ProfileForm(forms.ModelForm):
    def clean_max_distance(self):
        max_distance=self.cleaned_data.get('max_distance',0)

        min_distance=self.cleaned_data.get('min_distance',0)
        if max_distance<min_distance:
            raise forms.ValidationError('最大距离不能小于最小距离')
        return max_distance
    class Meta:
        model=Profile
        fields='__all__'
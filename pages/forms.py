from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username','first_name','last_name','email', 'age','password1', 'password2')

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustomUser
        fields = ('first_name','last_name', 'age')
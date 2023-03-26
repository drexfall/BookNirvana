from django.forms import forms, ModelForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import User,Review, Settings

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("first_name","last_name","email","username")

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        exclude = ("reviewer",)

class ProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ("first_name","last_name","profile_photo","bio")

class SettingsForm(ModelForm):
    class Meta:
        model = Settings
        exclude = ("user_id",)
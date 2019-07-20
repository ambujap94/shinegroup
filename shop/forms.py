from django import forms
from .Lists import PRODUCT_CHOICES, SPEAKER, STORAGE_SPEC, SPEAKER_TYPE, STORAGE, CAMERA_SPEC, BRAND, SMALL_STORAGE, KB_MOUSE, UPS, USER, ANTIVIRUS, PRINTER,COMP_PERIPHERALS, DVR_SMPS, CAMERA, CCTV
from django.contrib.auth import authenticate


class ContactForm(forms.Form):
    name = forms.CharField(required=False, max_length=100)
    subject = forms.CharField(required=False, max_length=100)
    sender = forms.EmailField(required=False)
    phone = forms.CharField(required=False, max_length=13)
    message = forms.CharField(required=False, max_length=200, widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))


class ProductView(forms.Form):
    Item            = forms.CharField(label='It Is', required=False, widget=forms.Select(attrs = {'class' : 'input-sm'},choices=sorted(PRODUCT_CHOICES, reverse=False)))
    brand           = forms.CharField(required=False, widget=forms.Select(choices=sorted(BRAND, reverse=False)))
    typep            = forms.CharField(max_length=120, label='Type',  required=False)
    SPEAKER         = forms.CharField(label='Type', required=False, widget=forms.Select(choices=sorted(SPEAKER, reverse=False)))
    STORAGE         = forms.CharField(label='Type', required=False, widget=forms.Select(choices=sorted(STORAGE, reverse=False)))
    CCTV            = forms.CharField(label='Item', required=False, widget=forms.Select(choices=sorted(CCTV, reverse=False)))
    CAMERA          = forms.CharField(label='Type', required=False, widget=forms.Select(choices=sorted(CAMERA, reverse=False)))
    DVR_SMPS        = forms.CharField(label='Type', required=False, widget=forms.Select(choices=DVR_SMPS))
    COMP_PERIPHERALS= forms.CharField(label='Type', required=False, widget=forms.Select(choices=sorted(COMP_PERIPHERALS, reverse=False)))
    KB_MOUSE       = forms.CharField(label='Specification', required=False, widget=forms.Select(choices=sorted(KB_MOUSE, reverse=False)))
    UPS             = forms.CharField(label='Type', required=False, widget=forms.Select(choices=sorted(UPS, reverse=False)))
    ANTIVIRUS       = forms.CharField(label='Type', required=False, widget=forms.Select(choices=sorted(ANTIVIRUS, reverse=False)))
    PRINTER         = forms.CharField(label='Type', required=False, widget=forms.Select(choices=sorted(PRINTER, reverse=False)))
    specificationp   = forms.CharField(max_length=120, label='Specification',  required=False)
    USER            = forms.CharField(label='Specification', required=False, widget=forms.Select(choices=USER))
    CAMERA_SPEC     = forms.CharField(label='Specification', required=False, widget=forms.Select(choices=sorted(CAMERA_SPEC, reverse=False)))
    STORAGE_SPEC    = forms.CharField(label='Specification', required=False, widget=forms.Select(choices=STORAGE_SPEC))
    SMALL_STORAGE    = forms.CharField(label='Specification', required=False, widget=forms.Select(choices=SMALL_STORAGE))
    SPEAKER_TYPE    = forms.CharField(label='Specification', required=False, widget=forms.Select(choices=sorted(SPEAKER_TYPE, reverse=False)))
    model           = forms.CharField(max_length=120, required=False)
    purchase_price = forms.DecimalField(max_digits=10, decimal_places=2)
    selling_price   = forms.DecimalField(max_digits=10, decimal_places=2)


    def clean(self, *args, **kwargs):
        selling_price = self.cleaned_data.get("selling_price")
        purchase_price = self.cleaned_data.get("purchase_price")
        if selling_price <= purchase_price:
            raise forms.ValidationError("Ismein Tera Ghata")
        return super(ProductView, self).clean(*args, **kwargs)

class ProductView1(forms.Form):
    product= forms.CharField(label='What are you looking for?', required=False, widget=forms.Select(choices=PRODUCT_CHOICES))


class LoginForm(forms.Form):
    username     = forms.CharField(label='User', required=True)
    password     = forms.CharField(label='Password', required=True, widget=forms.PasswordInput())

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("User does not exists.")

            if not user.check_password(password):
                raise forms.ValidationError("Incorrect Password")

            if not user.is_active:
                raise forms.ValidationError("User is not active")
        return super(LoginForm, self).clean(*args, **kwargs)



class NoticeForm(forms.Form):
    Notice = forms.CharField(required=False, max_length=100)


class Demand(forms.Form):
    Item     = forms.CharField(required=True, max_length=100)
    Quantity = forms.IntegerField(required=True, min_value=1)
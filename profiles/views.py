from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes,force_text
from django.template.loader import render_to_string
from django.views import View
from django.views.generic import CreateView, FormView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm
from django.contrib.auth import login,update_session_auth_hash
from .forms import DoctorRegistration,PatientRegistration,UserSetPassword
from utils.random_util import generator
from utils.tokens import account_activation_token
from .models import UserProfile
from django.conf import settings
# Create your views here.
class AddPatientView(SuccessMessageMixin,CreateView):
    form_class = PatientRegistration
    template_name = 'accounts/register_patient.html'
    success_message = "Congratulations! Registration successful. We just sent you an email for account activation.\nKindly Check your inbox.!!"

    def get_success_url(self):
        return reverse('profiles:patient-register')
    def form_valid(self, form):
        instance =form.save(commit=False)
        instance.identity = generator()
        # this account should not login until activated, but lets set and email this password
        instance.is_active =False
        randPass = UserProfile.objects.make_random_password()
        instance.random_password = randPass
        instance.set_password(randPass)
        # try with unusable so we'll automatically login a user when activation link is clicked
        #instance.set_unusable_password()
        instance.save()
        #about to email the user for account activation
        current_site =get_current_site(self.request)
        subject= "iMed Clinic,new patient registration"
        userid =urlsafe_base64_encode(force_bytes(instance.pk))# the encode is of the form b'OA' but we need a string
        message=render_to_string('accounts/patient_account_activate.html',
                                 {
                                     'user':instance,
                                     'domain':current_site.domain,
                                     'uid':''.join(map(chr,userid)),#converts our bytes into pure strying
                                     'token':account_activation_token.make_token(instance)
                                 })
        emailfrom = settings.EMAIL_HOST_USER
        send_mail(subject=subject,message=message,from_email=emailfrom,recipient_list=[instance.email],fail_silently=False)

        return super().form_valid(form)
class StaffRegister(SuccessMessageMixin,CreateView):
    template_name = 'accounts/add_staff.html'
    form_class = DoctorRegistration
    success_message = "You were successfully registered. Kindly login to your email to activate your account"

    def get_success_url(self):
        return reverse('profiles:staff-register')
    def form_valid(self, form):
        instance =form.save(commit=False)
        instance.is_active=False
        instance.is_doctor=True
        randPass = UserProfile.objects.make_random_password()
        instance.random_password = randPass
        instance.set_password(randPass)
        instance.save()
        current_site = get_current_site(self.request)
        userid = urlsafe_base64_encode(force_bytes(instance.pk))
        subject = "iMed Clinic,new staff registration"
        message = render_to_string('accounts/patient_account_activate.html',
                                   {
                                       'user': instance,
                                       'domain': current_site.domain,
                                       'uid': ''.join(map(chr,userid)) ,
                                       'token': account_activation_token.make_token(instance)
                                   })
        emailfrom = settings.EMAIL_HOST_USER
        send_mail(subject=subject, message=message, from_email=emailfrom, recipient_list=[instance.email],
                  fail_silently=False)

        return super().form_valid(form)
'''Here we do all the magic, checking if the user exists, if the token is valid.
If everything checks, we switch the flags is_active and email_confirmed to True and log the user in.

By changing the value of the email_confirmed field, it will cause the link to be invalidated.'''
class ActivateAccount(SuccessMessageMixin,View):
    success_message = "Your password was successfully set. You can now login"
    def get(self,request, uidb64, token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = UserProfile.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, UserProfile.DoesNotExist):
            user = None
        print("user ", user)
        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            login(request, user)
            form = SetPasswordForm(request.user)
            # return redirect('home')
            # return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
            return render(request, 'accounts/account_activation_success.html',{'form':form})
        else:
            # return HttpResponse('Activation link is invalid!')
            return render(request, 'accounts/account_activation_invalid.html',)
    def post(self,request):
        form = PasswordChangeForm(request.user)
        print(form)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)#update the session with the new password
            return redirect(reverse('homepage:index'))
def activate_account(request, uidb64, token):
    form = SetPasswordForm(request.user)
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = UserProfile.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, UserProfile.DoesNotExist):
        user = None
    print ("user ",user)
    print(account_activation_token.check_token(user=user,token=token))
    if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            #login(request, user)#dont be quick to login the user
            # return redirect('home')
            #return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
            if request.method == 'POST':
                form = SetPasswordForm(user=request.user)
                pass1 =request.POST.get('new_password1')
                pass2 = request.POST.get('new_password2')
                print(pass1,pass2)
                if pass2 == pass1:
                    user.set_password(pass2)
                    user.save()
                    update_session_auth_hash(request, user)  # update the session with the new password
                    return HttpResponseRedirect(reverse('homepage:index'))
                else:
                    messages.error(request,"The two passwords must match")
            return render(request,'accounts/account_activation_success.html',{'form':form})
    else:
            #return HttpResponse('Activation link is invalid!')
            return render(request, 'accounts/account_activation_invalid.html')
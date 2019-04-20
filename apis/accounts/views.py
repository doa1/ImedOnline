from django.shortcuts import redirect
from django.views.generic import CreateView
from rest_framework import permissions,authentication
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model, authenticate, login,logout

Users = get_user_model()
class LoginApi(APIView):
    def get(self,request,*args,**kwargs):
        return
    def post(self,request,*args,**kwargs):
        form_data = request.data
        print(form_data)
        email = form_data['username']
        password = form_data['password']
        response ={}
        # check the existance of the user
        user_exists =Users.objects.filter(email=email).exists()
        response['user_exists']=user_exists
        # we customized the auth model to use the email field as the username field, so we can use either to authenticate the user
        user = authenticate(request, email=email,password=password)
        if user is not None:
            # auth good, login anyway
            login(request=request,user=user)
            #can handle redirect here, but i would use ajax, since i need to return somethin to the user
            response['success_login']=True
        else:
            error ="Incorrect Login Details!!"
            response['auth_error']=error
        return Response(response)

class LogoutApi(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect('homepage:index')#Response({'success':'Successfully logged out'})
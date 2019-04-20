from django.contrib.auth import get_user_model
from django.contrib.auth import models
from django.utils.timezone import now
from django.utils.deprecation import MiddlewareMixin
User =get_user_model()

class SetLastVisitMiddleware(MiddlewareMixin):
    '''This is a middleware to track the user online status for every request the user makes '''
    def process_response(self,request,response):
        assert hasattr(request,'user'), "The LastSeenMiddlware requires authentication model to be installed"

        if request.user.is_authenticated:
            print(request.user.last_visit)
            #process last visit time after after request finished processing
            User.objects.filter(pk=request.user.pk).update(last_visit=now())
        return response
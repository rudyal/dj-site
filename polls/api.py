from tastypie.resources import ModelResource
from polls.models import PictureObject
from tastypie import fields
from django.contrib.auth.models import User

class UserResource(ModelResource):
	class Meta:
		queryset = User.objects.all()
		resource_name = 'user'
		fields = ['username', 'first_name', 'last_name', 'last_login']
		allowed_methods = ['get']
		
class PicResource(ModelResource):
    class Meta:
        queryset = PictureObject.objects.all()
        resource_name = 'pic'
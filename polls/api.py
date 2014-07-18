from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from polls.models import PictureObject
from tastypie import fields
from tastypie.fields import ListField
from django.contrib.auth.models import User
from taggit.models import Tag

class UserResource(ModelResource):
	class Meta:
		queryset = User.objects.all()
		resource_name = 'user'
		fields = ['username', 'first_name', 'last_name', 'last_login']
		allowed_methods = ['get']

class TagResource(ModelResource):

    class Meta:
        queryset = Tag.objects.all()
        detail_uri_name = 'slug'
        resource_name = 'tag'
        filtering = dict(
            resource_uri = ALL,
        )

class PicResource(ModelResource):

    tags = fields.ToManyField(TagResource, 'tags')

    class Meta:
        queryset = PictureObject.objects.all()
        filtering = dict(
            tags = ALL_WITH_RELATIONS,
            gender = ALL,
        )
        resource_name = 'pic'
        limit = 0
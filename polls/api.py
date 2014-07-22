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
            slug = ALL,
            tags = ALL,
        )

class PicResource(ModelResource):

    tags = fields.ToManyField(TagResource, 'tags')

    class Meta:
        queryset = PictureObject.objects.all()
        filtering = dict(
            tags = ALL,
            gender = ALL,
            tags1 = ALL,
        )
        resource_name = 'pic'
        limit = 0

    def build_filters(self, filters=None):
        if filters is None:
            filters = {}

        orm_filters = super(PicResource, self).build_filters(filters)

        if "land" in filters:
            #sqs = SearchQuerySet().auto_query(filters['q'])
            orm_filters["tags1__in"] = ['land']
            #orm_filters["pk__in"] = [i.pk for i in sqs]
        if "art" in filters:
        	orm_filters["tags1__in"] = ['art']

        return orm_filters

    # def apply_filters(self, request, applicable_filters):
    #     base_object_list = super(PicResource, self).apply_filters(request, applicable_filters)
    #     query = request.GET.get('query', None)
    #     ids = request.GET.get('ids', None)
    #     filters = {}
    #     if ids:
    #         ids = ids.replace('+', ' ').split(' ')
    #         filters.update(dict(id__in=ids))
    #     if query:
    #         qset = (
    #             Q(tags1__in='art', **filters)
    #             # |
    #             # Q(description__icontains=query, **filters)
    #         )
    #         base_object_list = base_object_list.filter(qset).distinct()
    #     return base_object_list.filter(**filters).distinct()
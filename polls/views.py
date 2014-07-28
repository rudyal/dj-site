from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User, Group
from polls.models import Choice, Poll, PictureObject
from polls.forms import PictureObjectForm
from polls.serializers import UserSerializer, GroupSerializer, PictureSerializer
from rest_framework import viewsets
from django.core.urlresolvers import reverse
from django.http import Http404
from django.views import generic
from django.core.context_processors import csrf
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_poll_list'

	def get_queryset(self):
		"""Return the last five published polls."""
		return Poll.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
	model = Poll
	template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
	model = Poll
	template_name = 'polls/results.html'

def vote(request, poll_id):
	p = get_object_or_404(Poll, pk=poll_id)
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# Redisplay the poll voting form.
		return render(request, 'polls/detail.html', {
			'poll': p,
			'error_message': "You didn't select a choice.",
		})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		# Always return an HttpResponseRedirect after successfully dealing
		# with POST data. This prevents data from being posted twice if a
		# user hits the Back button.
		return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

def CreatePicObModel(request):
        if request.method == 'POST':
            form = PictureObjectForm(request.POST, request.FILES)
            if form.is_valid():
                new_picob = form.save()
                #new_picob.picture = PictureObject(picture = request.FILES['picture'])
                #new_picob.save()
                return HttpResponseRedirect('/polls')
        else:        
            form = PictureObjectForm()
        c = { 'form' : form }
        return render(request, 'polls/demo.html', c)

def ViewPicOb(request):
        pic_info = PictureObject.objects.all()

        pic_data = {
            "pic_detail" : pic_info
        }

        return render(request, 'polls/demo2.html', pic_data)

def Viewer(request):
        # put id from picture into url

        # figure out how to retreive picture based on ID and put it into page

        # also figure out how to make template that is re-usable for ID's

        # Put href in pics on front page

        return render(request, 'polls/demo2.html', pic_data)

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class PicViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = PictureObject.objects.all()
    serializer_class = PictureSerializer
from django.shortcuts import render,render_to_response
from models import Blocks
from django.template import RequestContext
# Create your views here.
def block_list(request):
    blocks=Blocks.objects.all().order_by("-id")
    return render_to_response("block_list.html",{"blocks":blocks},context_instance=RequestContext(request))

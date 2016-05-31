from django.shortcuts import render,render_to_response
from models import Blocks
# Create your views here.
def block_list(request):
    blocks=Blocks.objects.all().order_by("-id")
    return render_to_response("block_list.html",{"blocks":blocks})

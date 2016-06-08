from django.shortcuts import render,render_to_response
from block.models import Blocks
from models import Article

# Create your views here.
def article_list(request,block_id):
    block_id=int(block_id)
    block=Blocks.objects.get(id=block_id)
    articles=Article.objects.filter(block=block).order_by("-last_update_timestamp")
    return render_to_response("articles_list.html",{"articles":articles,"b":block})
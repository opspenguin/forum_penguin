from django.conf.urls import url

urlpatterns = [
    url(r'^list/(?P<block_id>\d+)',"article.views.article_list",name="article_list"),
]
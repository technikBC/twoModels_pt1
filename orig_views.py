#imports go here:


urlpatterns =
[url(r'^$', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:20],template_name="reviews/reviews.html”)),]

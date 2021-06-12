from django.views.generic import TemplateView, CreateView
from .models import Comment

class HomePageView(TemplateView):
    template_name = 'home.html'
    context_object_name = 'all_comments_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_comments_list'] = Comment.objects.all()
        return context

class AboutPageView(TemplateView): # new
    template_name = 'about.html'

class ZakyskiPageView(TemplateView): # new
    template_name = 'zakyski.html'
    
class SovetiPageView(TemplateView): # new
    template_name = 'soveti.html'

class CommentCreateView(CreateView):
    model = Comment
    template_name = 'comment_new.html'
    fields = ('text',)
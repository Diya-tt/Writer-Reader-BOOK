from django.shortcuts import render,redirect
from django.views.generic import TemplateView,ListView,DetailView,FormView,CreateView
from writerapp.models import StoryModel
from django.views import View
from viewerapp.forms import CommentForm
from viewerapp.models import CommentModel
from django.urls import reverse_lazy,reverse
from django.contrib import messages
# Create your views here.

class Home1(TemplateView):
    template_name='index1.html'
    

class ViewerView(ListView):
    model=StoryModel
    template_name='listview.html'
    context_object_name='stories'


class ViewerDetailView(DetailView):
    template_name='detailview.html'
    model=StoryModel
    pk_url_kwarg='id'
    context_object_name = 'story'


class CommentCreateView(CreateView):
    template_name = 'comment.html'
    form_class = CommentForm
    model = CommentModel

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.user = self.request.user
        comment.blog = StoryModel.objects.get(id=self.kwargs.get("id"))
        comment.save()
        messages.success(self.request, "Commented successfully!")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('viewer_view', kwargs={'id': self.kwargs['id']})


class CommentListView(ListView):
    template_name = 'listcomment.html'
    model = CommentModel
    context_object_name = 'comments'

    def get_queryset(self):
        book_id = self.kwargs.get('book_id')
        if book_id:
            return CommentModel.objects.filter(blog_id=book_id)  
        return CommentModel.objects.none()  
from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,ListView,DeleteView,DetailView,UpdateView
from writerapp.forms import UserSignUpForm,UserSignInForm,StoryForm,StoryEditForm
from writerapp.models import StoryModel
from django.contrib.auth.models import User
from django.contrib import messages
from django.views import View
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse_lazy

# from writerapp.forms import StoryForm
# from writerapp.models import Story
# from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin


# Create your views here.

class Home(TemplateView):
    template_name='index.html'   

class SignUpView(CreateView):
    template_name="signup.html"
    form_class=UserSignUpForm
    model=User
    def form_valid(self,form):
        User.objects.create_user(**form.cleaned_data)
        messages.success(self.request,"SIGNUP SUCCESSFUL")
        return redirect('signin_view')
    def form_invalid(self, form):
        messages.warning(self.request,"INVALID USERNAME OR PASSWORD")
        return redirect('signup_view')

class SignInView(CreateView):
    template_name='signin.html'
    form_class=UserSignInForm
    model=User
    def post(self, request):
        uname=request.POST.get("username")
        psw=request.POST.get("password")
        user_type = request.POST.get('user_type')
        user=authenticate(request,username=uname,password=psw)
        if user:
            login(request,user)
            messages.success(self.request,"LOGIN SUCCESSFUL")
            if user_type == 'writer':
                return redirect('home_view')  # Example admin dashboard
            elif user_type == 'viewer':
                return redirect('home1_view') 
        else:
            messages.success(self.request,"INVALID USERNAME OR PASSWORD")
            return redirect('signin_view')

class SignOutView(View):
    def get(self,request):
        logout(request)
        messages.success(request,"LOGOUT SUCCESSFULLY")
        return redirect('signin_view')
    
class CreateStory(CreateView):
    template_name='create.html'
    form_class=StoryForm
    model=StoryModel
    success_url=reverse_lazy('home_view')
    
    def form_valid(self,form):
        form.instance.user=self.request.user
        messages.success(self.request,"CREATED SUCCESSFULLY")
        return super().form_valid(form)

class ListFormView(ListView):
    template_name='list.html'
    model=StoryModel
    ordering = ['-created_at']  
    context_object_name='samples'

    def get_queryset(self):
        return StoryModel.objects.filter(user=self.request.user)

class DeleteFormView(DeleteView): #(here they ask confirmtion) #generic method0
    model=StoryModel
    pk_url_kwarg='id'
    success_url=reverse_lazy('list_view')
    template_name='delete.html'

class StoryDetailView(DetailView):
    template_name='detail.html'
    model=StoryModel
    pk_url_kwarg='id'
    context_object_name = 'story'

class StudEditView(UpdateView):
    template_name='edit.html'
    model=StoryModel
    form_class=StoryEditForm
    pk_url_kwarg='id'
    success_url=reverse_lazy("list_view")
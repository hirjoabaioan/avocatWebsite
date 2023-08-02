from django.db.models import Count
from django.contrib import messages
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage,\
                                  PageNotAnInteger
from django.core.mail import send_mail, mail_admins, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView
from .models import Comentariu, Întrebări, Postări
from .forms import ContactForm, EmailPostForm, QuestionForm
from taggit.models import Tag


# Home view
def home(request):
    return render(request, 'blog/other/home.html')


# Contact view
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Sending email
            sender_name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']     
            subject = "Ați primit un mesaj nou de la {0}".format(sender_name)
            message = "Subiect: {0}\n\nMesaj: {1}\n\n Email primit de la {2}: {3}".format(form.cleaned_data['subject'], form.cleaned_data['message'], sender_name, sender_email)
            mail_admins(subject, message)
            
            form.save()
            messages.add_message(request, messages.INFO, 'Formular trimis.')
            
            try:
                send_mail(subject, message, sender_email, ['hirjoaba.ioan@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            
            return redirect('/contact')
    else:
        form = ContactForm()
        
    return render(request, 'blog/other/contact.html', {'form': form})


# Fees view
def fees(request):
    return render(request, 'blog/other/fees.html')


# Activity Domains views
def activity_domain_1(request):
    return render(request, 'blog/other/activity_domain_1.html')

def activity_domain_2(request):
    return render(request, 'blog/other/activity_domain_2.html')

def activity_domain_3(request):
    return render(request, 'blog/other/activity_domain_3.html')

def activity_domain_4(request):
    return render(request, 'blog/other/activity_domain_4.html')


# Blog view - list
def post_list(request, tag_slug=None):
    object_list = Postări.published.all()
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])

    paginator = Paginator(object_list, 3) # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request,
                 'blog/post/list.html',
                 {'page': page,
                  'posts': posts,
                  'tag': tag})


# Blog view - post detail
def post_detail(request, year, month, day, post):
    post = get_object_or_404(Postări, slug=post,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)

    # List of similar posts
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Postări.published.filter(tags__in=post_tags_ids)\
                                  .exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags'))\
                                .order_by('-same_tags','-publish')[:4]

    return render(request,
                  'blog/post/detail.html',
                  {'post': post,
                   'similar_posts': similar_posts})


class PostListView(ListView):
    queryset = Postări.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


# Question view - list
def question_list(request):
    
    object_list = Întrebări.published.all()
    
    paginator = Paginator(object_list, 5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
        
    return render(request, 
                  'blog/question/question_list.html',
                  {'page': page,
                   'posts': posts})


# Question view - post detail
def question_detail(request, year, month, day, post):
    post = get_object_or_404(Întrebări, slug=post,
                                       status='published',
                                       publish__year=year,
                                       publish__month=month,
                                       publish__day=day)
    
    comments = post.comments.filter(active=True)
    
    return render(request,
                  'blog/question/question_detail.html',
                  {'post':post,
                   'comments':comments})

class PostListView(ListView):
    queryset = Postări.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/question/question_list.html'
    
# Question view - asking
def question_ask(request):
    
    new_question = None
    
    if request.method == 'POST':
        question_form = QuestionForm(data=request.POST)
        if question_form.is_valid():
            new_question = question_form.save(commit=False)
            
            new_question.save()
    else:
        question_form = QuestionForm()
        
    return render(request,
                  'blog/question/question_ask.html',
                  {
                   'new_question': new_question,
                   'question_form': question_form,})



            
# # Sharing a post view - to delete
# def post_share(request, post_id):
#     # Retrieve post by id
#     post = get_object_or_404(Postări, id=post_id, status='published')
#     sent = False

#     if request.method == 'POST':
#         # Form was submitted
#         form = EmailPostForm(request.POST)
#         if form.is_valid():
#             # Form fields passed validation
#             cd = form.cleaned_data
#             post_url = request.build_absolute_url(post.get_absolute_url())
#             subject = f"{cd['name']} recommends you read {post.title}"
#             message = f"Read {post.title} at {post_url}\n\n" \
#                       f"{cd['name']}\'s comments: {cd['comments']}"
#             send_mail(subject, message, 'hirjoaba.ioan@gmail.com', [cd['to']])
#             sent = True

#     else:
#         form = EmailPostForm()
#     return render(request, 'blog/post/share.html', {'post': post,
#                                                     'form': form,
#                                                     'sent': sent})
    
    

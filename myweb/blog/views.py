from django.shortcuts import render,get_object_or_404
from blog.models import Post,Tag,Category
import markdown
# Create your views here.

def home(request):
    post_list=Post.objects.all()
    tag_list=Tag.objects.all()[:5]
    category_list=Category.objects.all()[:5]
    post_time=post_list.order_by('-modified_time')
    return render(request,'index.html',context={'post_list':post_list,'tag_list':tag_list,'category_list':category_list,'post_time':post_time})

def post(request,pk):
    pk=int(pk)
    tag_list = Tag.objects.all()[:5]
    category_list = Category.objects.all()[:5]
    post_list = Post.objects.all()
    post=post_list[pk-1]
    post_time = post_list.order_by('-modified_time')
    post.body = markdown.markdown(post.body, extensions=['markdown.extensions.extra', 'markdown.extensions.codehilite',
                                                         'markdown.extensions.toc', ])
    return render(request,'post.html',context={'post':post,'tag_list':tag_list,'category_list':category_list,'post_list':post_list[:5],'post_time':post_time})

def search(request):
    post_list=Post.objects.all()
    tag_list=Tag.objects.all()[:5]
    category_list=Category.objects.all()[:5]
    post_time = post_list.order_by('-modified_time')
    c=request.GET.get('c',0)
    t=request.GET.get('t',0)
    print(c)
    print(t)
    search_1=post_list.filter(category__name=c)
    search_2=post_list.filter(tags__name=t)
    m=post_list.filter(title='')
    if search_1.count()!=0:
        print(search_1)
        return render(request,'search.html',{'post_list':post_list[0:5],'tag_list':tag_list,'category_list':category_list,'search_list':search_1,'post_time':post_time})
    elif search_2.count()!=0:
        print(search_2)
        return render(request,'search.html',{'post_list':post_list[0:5],'tag_list':tag_list,'category_list':category_list,'search_list':search_2,'post_time':post_time})
    else:
        return render(request, 'search.html',{'post_list': post_list[0:5], 'tag_list': tag_list, 'category_list': category_list,'search_list': [],'post_time':post_time})
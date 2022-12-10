from django.shortcuts import render, get_object_or_404,redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

def post_list(request):
    #published_date기준으로 정렬
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    
    #render함수에는 매개변수 request(사용자가 요청하는 모든 것)와 'blog/post_list.html' 템플릿이 있습니다.
    # {}}이 보일 텐데, 이곳에 템플릿을 사용하기 위해 매개변수를 추가할 거에요. 
    # (이 매개변수를'posts'라고 할거에요){'posts': posts}이렇게 작성할거에요
    return render(request, 'blog/post_list.html', {'posts':posts}) 

def post_detail(request, pk):
    #쿼리셋(queryset)
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    #post 저장
    if request.method == "POST":
        #POST 데이터 할당
        form = PostForm(request.POST)
        if form.is_valid():#저장하는 값이 모두 있는지 점검
            post = form.save(commit=False) #사용자를 추가해서 저장해야하므로 post 변수 할당
            post.author = request.user # 사용자정보 추가
            post.published_date = timezone.now() #시가정보 추가 
            post.created_date= timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk): #pk 받아서 처리함
    post = get_object_or_404(Post, pk=pk) # 호출하여 수정하고자 하는 글의 Post 모델 인스턴스(instance)로 가져옴
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
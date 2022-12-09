from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html', {})#모델에서 필요한 정보를 받아와서 템플릿에 전달하는 역할

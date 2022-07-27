from django.shortcuts import render, get_object_or_404, redirect

from .models import Post
# 우리가 만든 Post 모델(models)을 불러온다

from django.utils import timezone
from .forms import PostCreateForm


def posts(request):
    posts = Post.objects.filter(published_at__isnull=False).order_by('-published_at')
    # published_at 필드가 null이 아닌경우 (__isnull==False)에 대이터를 가져옴
    # order_by는 published_at 필드를 내림차순으로 정렬한다

    return render(request, 'blog/posts.html', {'posts': posts})
    # 가져온 데이터를 / blog/post.html페이지에 / posts란 변수명으로 전달한다


def post_detail(request, id):  # 새로운 URL과 매핑되는 함수이다 파라미터로 넘겨준 id를 별도의 변수로 전달 받는다
    post = get_object_or_404(Post, id=id)
    # 장고에서 기본적으로 주는 함수고 데이터가 없으면 404에러를 발생시킨다
    return render(request, 'blog/post_detail.html', {'post': post})
    #


def post_create(request):
    if request.method == "POST":
    # 만약 request라는 메소드가 POST라면
        # 함수에는 기본적으로 request파라미터가 설정 되어있는데 이 requst의 메소드가 GET/POST인지 구별한다
        # POST일 경우 폼을 작성해 데이터를 저장함

        form = PostCreateForm(request.POST)
        # 폼으로 전송한 POST데이터는 request.POST에 담겨있다 이걸로 Form class를 통해 폼 객체를 생성함

        if form.is_valid():
            # 장고가 유효성 체크를 하여 POST로 보내온 데이터를 확인함

            post = form.save(commit=False)
            # 폼 객체로 데이터를 저장함 하지만 commit=false 옵션으로 DB에 반영 안돼게함

            post.author = request.user
            # 저장할 데이터의 author를 현재 request를 보낸 사용자로 넣는다
            # 이때 나는 관리자 화면으로 이미 로그인 해서 requst.user에는 관리자 화면에 로그인한 사용자 정보가 담김

            post.published_at = timezone.now()
            # published_at 이 현 시각을 표시함

            post.save()
            # 최종적으로 데이터 베이스 저장

            return redirect('post_detail', id=post.id)
            # 데이터가 잘 저장 되었는지 확인할려고 redirect로 post_detail로 리다이렉트함

    else:  # POST가 아닐경우
        form = PostCreateForm()  # 만든 폼을 가져와서

    return render(request, 'blog/post_create.html', {'form': form})
    # 값을 화면에 출력

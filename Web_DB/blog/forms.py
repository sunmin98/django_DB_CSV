from django import forms
#장고의 기본적인 form을 불러옴
from .models import Post
#폼을 통해 데이터를 추가하거나 수정할 post모델을 불러옴


class PostCreateForm(forms.ModelForm):
#PostCreateForm이라는 이름으로 클래스를 생성해 forms.ModelForm을 상속받음

    class Meta:
        model = Post
        #폼이 다룰 model 은 Post다
        fields = ('title', 'content')
        #그중에서 title 과 content를 다룬다
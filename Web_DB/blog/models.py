from django.db import models
from django.utils import timezone


class Post(models.Model):  # Post는 author, title, content, created_at, updated_at, published_at 필드를 가지고 있습니다.
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # author는 ForeignKey 함수를 사용하여, 장고(django)에서 기본적으로 제공하는 auth 어플리케이션의 User 모델을 참조하게 만들었습니다.
    # (auth.User: 앱이름.모델)

    title = models.CharField(max_length=100)
    # title은 블로그의 제목으로 CharField 타입를 사용하여 길이가 정해진 문자열을 저장하도록 하였습니다.
    # max_length 옵션을 사용해 길이가 100인 문자열을 저장하도록 설정하였습니다.

    content = models.TextField()
    # content는 블로그의 내용으로 TextField 타입를 통해 길이가 정해져있지 않는 문자열을 저장할 수 있도록 하였습니다

    created_at = models.DateTimeField(auto_now_add=True)
    # created_at은 블로그 생성 날짜로 DateTimeField을 통해 날짜와 시간을 저장할 수 있도록 하였으며,
    # auto_now_add 옵션은 한번 쓰고 업데이트 안하는거

    updated_at = models.DateTimeField(auto_now=True)
    # updated_at는 블로그 수정일로 역시 DateTimeField을 통해 날짜와 시간을 저장할 수 있도록 하였으며,
    # auto_now 옵션은 계속 쓸떼마다 데이터가 갱신되는거

    published_at = models.DateTimeField(blank=True, null=True)

    # published_at는 블로그를 공개한 날짜로 역시 DateTimeField을 통해 날짜와 시간을 저장할 수 있도록 하였습니다.

    # blank: 필드가 빈체로 저장을 허용 ex) ''
    # null: 필드값이 NULL을 허용함

    def publish(self):
        self.published_at = timezone.now()
        self.save()
        # publish: 블로그 서비스에서 자주 사용되는 기능인 공개(publish) 기능을 함수로 만들었습니다.
        # 이 함수를 통해 블로그를 공개(publish)할 때 날짜를 갱신하기 위해 만들었습니다.

    def __str__(self):
        return self.title
        # __str__: 표준 파이썬 클래스 메소드이며 사람이 읽을 수 있는 문자열을 반환하도록 합니다.


# Django

파이썬 웹 프레임워크

- MTV 패턴

HTTP(Request)  => URLS(urls.py) => View(views.py) <= Template(<filename>.html) 

​                                                                          ^

​                                                             Model(models.py)  



## 기초 내용

### 설치

```python
$ pip install django==2.1.15
```



## Django 프로젝트 시작

#### 프로젝트 생성

```python
$ django-admin startproject {프로젝트명}
```

#### 서버 실행

- django_intro 폴더의 settings.py 파일에 아래와 같이 수정한다.

  ```python
  # line 28
  ALLOWED_HOSTS = ['*']  # 와일드 카드
  ```

- 반드시 서버 실행시 명령어가 실행되는 디렉토리를 확인할 것

  보통 프로젝트 폴더에서 시작되며, 마스터 앱과 프로젝트를 구분지어 주기 위하여 프로젝트 폴더 이름을 대문자로 rename한다.

  ```python
  ~/INTRO/ $ python manage.py runserver 8080
  ```

- 서버 종료는 터미널에서 ctrl + c 함께 입력한다.

  

## App 생성

```python
$ python manage.py startapp {앱 명}
```



### App 등록(settings.py)

```python
INSTALLED_APPS[]에 만든 App을 추가 등록 ex) 'pages'
```



# Model

- model(ing) 은 현실세계의 무언가를 컴퓨터로 옮기기 위해 하는 일, MTV 패턴에서 데이터를 관리

- IT와 ICT가 유망해진 이유는 'Data(All about Data)'가 각광받기 때문이다.

  - 어떤 데이터를 어떻게 제공할 것인가? ex) google은 검색 데이터를 보여준다, airbnb는 숙박 데이터를 web/ app에 보여준다.
  - Data를 효과적으로 탐색/정렬 하기 위해서 Algorism을 배우고 있다.
  - Data를 가장 쉽게 다수에게 제공하기 위해서 Web을 배우고 있다.
  - 서버는 Data를 제공과 처리가 목적이다.

- where? Data는 Database에 있다.

  - Database는 프로그램이다. 그렇기에 명령 및 조작을 해야한다.
    - 프로그램을 조작하는 언어 = SQL (Structed Query Language)
    - Database가 하는 일은 크게 4가지가 있다 : Create, Read(Retrieve), Update, Delete => CRUD operation

- Django

  - Request로 들어온 Data를 저장할 곳이 필요하다. => Database
  - 표(table)에 속성값과 col를 정해주는 작업이 Schema(스키마)
  - 사용자가 보내는 Data를 검증하는 작업을 해줘야 한다. 왜냐면 제 각각으로 입력을 하기 때문이다. 그렇기에 제약조건(속성)을 걸어야한다. ex) 빅데이터의 GIGO(Garbage In Garbage Out)
    - 짧은 문자열 (CharField) : max_length라는 조건을 꼭 줘야한다.
    - 긴 문자열 (TextField) 
    - 숫자(정수) (IntegerField)
    - 날짜 (DateTimeField)

  - Table에는 Unique, Primary, Identity한 key가 필요하다.  ex) id, 주민등록번호, 사원번호

  - Django와 Database는 다른 세계이다. 그렇기 때문에 중간에 중계자가 필요하다.

    => Python으로 명령을 하면 Database에 접근하게 가능하게 도와주는 것이 ORM.

  - ORM : Object Relation Mapper ( Python은 oop(객체지향언어), RDBMS(관계형데이터베이스)의 앞글자인 Object와 Relation을 따서 연동시켜주는 것) , 데이터베이스를 조작
  
- 그 중에 우리는 Django에서 제공하는 ORM을 사용
    - ORM은 Instance를 save하면 자동으로 SQL을 실행한다.
    
  - 마이그레이션(Migration) - 모델의 변경사항들을 데이터베이스 스키마에 반영하는 방법, Model로 정의된 데이터베이스 스키마를 반영
  
    

## GET과 POST

 URL이 길어질 경우에 method='POST'로 넘겨준다.

우리는 DB가 변경되는 요청은 POST로 한다. (C, U, D)

그게 아니라면 GET (R) - 실질적으로 90%

- GET - R (Get/articles) => 목록, (Get/articles/1) => 1번 내놔
- POST - C (Post/articles) => 생성
- PUT/PATCH - U (Patch/articles/1) => 1번 수정
- DELETE - D (Delete/articles/1) => 1번 삭제

 그러나 Django에는 GET/POST만 존재한다.



### static 파일 관리

 앱별로 관리를 하고 싶다면 static폴더를 만들고 그 안에 templates와 같이 앱이름의 폴더를 만들어주고 그 안에 이미지와 같은 파일을 넣어준다. 



## admin.py

```python
from .models import Article  # 추가

# 선택
class ArticleAdmin(admin.ModelAdmin):

	list_display = ('id', 'title', 'content', 'created_at', 'updated_at',)

# 등록
admin.site.register(Article)
```



 위와 같이 admin.py에 선택적으로 추가를 해주면 admin 페이지에서 해당 table을 대시보드와 같이 보기 좋게 나타난다.



## forms.py

```python
from django import forms

class ArticleForm(forms.form):
    title = forms.CharField(max_length=30)  # 여기서 max_length는 선택
    content = forms.CharField(widget=forms.Textarea)
    
```



 forms.py 에서 정의해준 ArticleForm을 views.py에서 models와 비슷하게 사용가능하다.

그러나 models.py에서 정의해준 것과 forms.py에서 정의하는 것이 중복되는 현상이 발생한다.

이러한 불편한 사항을 해결하는 방법이 다음과 같다.



```python
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
	class Meta:
		model = Article
        fields = ['title', 'content']  # 사용할 field
```


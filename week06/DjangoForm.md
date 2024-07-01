# Django Forms
***

### HTML 양식
1. <form></form>은 HTML에서 방문자의 텍스트 입력, 선택등의 컨트롤 조작에 대한 정보를 서버로 다시 보내는 내부 요소 모음집
    * action 속성을 통해 특정 url로 전송
    * /admin/에 지정된 http 매커니즘을 사용하여 전송할 것

2. <input 양식> : 사용자 입력 데이터를 반환할 url지전(where)과 데이터의 어떤 방식으로 반환될지에 대한 http 메서드 정의(how)가 필요

***

### GET 과 POST   
: form을 처리하는 유일한 http 메서드

#### POST
1. 장고의 로그임 폼은 POST 메서드에 의해 반환된다
    * 과정: 폼 데이터 묶기, 인코딩, 서버 전송, 서버로부터 응답받기
2. 시스템 상태의 변경 즉, 데이터베이스를 변경하는 요청에는 POST를 사용
    
#### GET
1. 제출된 데이터를 문자열로 묶어 이를 URL 구성에 활용
    * URL이 데이터 전송 대상 URL/데이터 키와 값이 포함됨
2. 대용량의 데이터나 민감한 데이터 양식에 GET메소드를 사용하지 않음 (URL 노출)
3. 웹 검색 양식과 같이 단순 URL을 받아오는데 주로 사용하는 메서드

***

### 폼에서의 장고의 역할
1. 렌더링을 위한 자동 데이터 재구성
2. 데이터에 대한 HTML 양식 생성
3. 클라이언트로부터 제출된 양식 및 데이터 수신 및 처리

### 장고에서의 FORM
* html <form>을 의미하기도 하고 양식을 생성해내는 django의 app이나 제출시 반환되는 구조화된 데이터를 가리키기도 한다.

### 장고에서의 FORM Class
전제: 모델 클래스처럼 필드가 데이터베이스 필드에 매핑
1. 폼 클래스의 필드는 html form <input>요소에 매핑
2. 폼의 필드는 그 자체로 클래스이기 때문에, 그 에 대한 데이터를 관리 및 제출시 검증해야한다.
    * 서로 다른 필드(ex.DateField와 FileField)는 서로 다른 종류의 데이터를 처리하고 작동한다
3. 폼의 필드는 html 위젯으로써 브라우저에 띄워지고 기본 위젯 클래스가 있지만 재정의 또한 가능

### 양식 인스턴스화와 처리 및 렌더링
* 객체의 렌더링 과정
    1. view에서 form의 내용을 잡는다(db에서 그 객체를 가져와서..?)   
    2. 그 내용을 template context에 전달   
    3. template 변수를 사용하여 html 마크업으로 확장   
    
    * form을 instance화 할때는 양식을 비워두거나 미리 채워놓을 수 있다.
        * 저장된 데이터 ( or 미리 수집한 데이터)
        * 이전 html 양식에서 제출받은 데이터(사용자와 주고받은 특정 데이터)

***

### 장고에서 폼 만들기

#### Form Class

    '''
    from django import forms

    class NameForm(forms.Form):
        your_name = forms.CharField(label="Your name", max_length=100)
    '''
이 자동으로 아래와 같은 코드로 렌더링이 수행된다.

    '''
    <label for="your_name">Your name: </label>
    <input id="your_name" type="text" name="your_name" maxlength="100" required>
    '''
* 이때 form에 대한 instance에 대해서는 is_valid()메소드가 존재하여 유효성을 살펴볼 수 있다. 
    * 모든 필드에 대해 유효하다면 return True를 하고 이를 cleaned_data 속성을 통해 해당 데이터들을 자동으로 cleaned_data로 옮긴다.

### View
장고 웹사이트로 전송된 form data들은 view에 처리된다(데이터 처리 logic)
    
    '''python
    from django.http import HttpResponseRedirect
    from django.shortcuts import render

    from .forms import NameForm


    def get_name(request):
        # if this is a POST request we need to process the form data
        if request.method == "POST":
            # create a form instance and populate it with data from the request:
            form = NameForm(request.POST)
            # check whether it's valid:
            if form.is_valid():
                # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
                return HttpResponseRedirect("/thanks/")

        # if a GET (or any other method) we'll create a blank form
        else:
            form = NameForm()

        return render(request, "name.html", {"form": form})
    '''

1. 클리언트 요청에 의해 이 view에 도착한다면 먼저 그 요청이 POST인지 GET인지 구분한다.(DB 변경이 필요한 요청인지 구분)
2. POST 메서드를 통해 요청한 경우 forms.py에서 정의한 NameForm 클래스에 요청에 의해 받은 data(request.POST)를 전달하여 form 객체를 생성한다   (=> form으로 data를 binding한다고 표현)
2-1. 이 form 객체가 유효성검사에 통과하면 html의 form이 해당 내용을 채워지며 /thanks/라는 새 url로 연결(HttpResponseRedirect)
3. POST 이외의 메소드 요청에 view에 도달한 경우 (ex.GET: 사용자가 form이 필요한 페이지로 연결하기 위한 요청을 넣은경우) NameForm()이라는 빈 form 객체를 생성하여 해당내용을 context로 render함수를 통해 name.html이라는 템플릿에 변수로 전달하여 화면에 흩뿌린다.

### Template

    '''
    <form action="/your-name/" method="post">
    {% csrf_token %}
    {{ form }}
    <input type="submit" value="Submit">
    </form>
    '''

* 템플릿 문법을 사용하여 form의 모든 양식과 속성은 {{form}}으로 압축 및 해제되어 html에 넘어간다.

* 정리: 웹에서 작동되는 form을 장고의 form을 통해 생성하고 이를 view를 통해 처리하여 해당 내용들은 <form>의 형태로 html에 자동 렌더링된다.

***

## Django Form Class에 대한 추가 학습

* 바인딩 되어 있는 form instance를 확인할 것
    * 바인딩 되지 않은 (unbound) form에는 연결된 데이터가 아예 없기에 렌더링 된 후, 빈 form으로 사용자에게 나타난다
    * binding된 form에는 데이터가 정상 제출이 된것이기 때문에 이에 대한 추가적인 유효성 검사와 인라인 오류 메시지와 같은 요구가 가능하다
    * is_bound()를 통해 연결된 데이터가 있는지 그 여부에 대해 확인 가능

### Field

        '''
        from django import forms

        class ContactForm(forms.Form):
            subject = forms.CharField(max_length=100)
            message = forms.CharField(widget=forms.Textarea)
            sender = forms.EmailField()
            cc_myself = forms.BooleanField(required=False)
        '''

* 총 4개 (subject, messange, sender, cc_myself)의 필드가 생성
* 각각의 필드들은 charfield, emailfield, booleanfield 중 하나로 채워진다.

### Widgets(위젯)
각각의 form field에 대해서 상응하는 widget classes들이 존재한다.

### Field data
* 필드 데이터들이 성공적으로 제출되고 유효성 검사를 통과했다면   이는 form.cleaned_data라는 python의 dictionary타입으로 정의된 곳에 자동으로 전환되어 저장되어있을 것이다.

    '''
    from django.core.mail import send_mail

    if form.is_valid():
        subject = form.cleaned_data["subject"]
        message = form.cleaned_data["message"]
        sender = form.cleaned_data["sender"]
        cc_myself = form.cleaned_data["cc_myself"]

        recipients = ["info@example.com"]
        if cc_myself:
            recipients.append(sender)

        send_mail(subject, message, sender, recipients)
        return HttpResponseRedirect("/thanks/")
    '''
- 몇몇 필드 타입들은 추가로 다뤄줘야 하는 부분들이 있음
  - 폼으로 업로드되는 파일들은 다르게 처리되어야 함
  - `request.POST`가 아닌 `request.FILES`로 접근해야 한다.

***
### Form을 템플릿으로 가져오기
* 폼 렌더링 시의 html은 template을 통해 만들어지므로 form의 template 이름을 overriding 하면서 커스텀이 가능하다

#### 재사용 가능한 form templates
    '''
    # In your template:
    {{ form }}

    # In form_snippet.html:
    {% for field in form %}
        <div class="fieldWrapper">
            {{ field.errors }}
            {{ field.label_tag }} {{ field }}
        </div>
    {% endfor %}
    '''
위와 같이 작성했을 때 아래와 같이 FORM_RENDERER setting을 구성할 수 있다.

    '''
    from django.forms.renderers import TemplatesSetting


    class CustomFormRenderer(TemplatesSetting):
        form_template_name = "form_snippet.html"


    FORM_RENDERER = "project.settings.CustomFormRenderer"
    '''
또는 단일 form을 통해 다음과 같이 나타낼 수 있다.

    '''
    class MyForm(forms.Form):
        template_name = "form_snippet.html"
    '''

    '''
    def index(request):
        form = MyForm()
        rendered_form = form.render("form_snippet.html")
        context = {"form": rendered_form}
        return render(request, "index.html", context)
    '''
### 폼 필드 반복하기 

    '''
    {% for field in form %}
        <div class="fieldWrapper">
            {{ field.errors }}
            {{ field.label_tag }} {{ field }}
            {% if field.help_text %}
            <p class="help" id="{{ field.auto_id }}_helptext">
                {{ field.help_text|safe }}
            </p>
            {% endif %}
        </div>
    {% endfor %}
    '''
* {{field.errors}} 를 통해 해당 필드에 해당하는 모든 검증 오류를 포함하는 출력 물론 루프를 통해 사용자 정의대로 조작할 수 있다.
    * `<ul class="errorlist">`형식으로 출력
    * {% for error in field.errors %}와 같이 에러 표현 커스텀이 가능하다. 
* {{field.field}} : 필드 속성에 접근하기
* {{field.help_Text}} : 필드와 연결된 도움말 텍스트
* {{field.html_name}} : input 요소의 name 필드로 사용되는 필드의 이름
* {{field.id_for_label}} : 필드 속성에 사용될 id
* {{field.is_hidden}}: form field가 hidden이라면 True 아니라면 False를 반환

    '''
    {% if field.is_hidden %}
    {# Do something special #}
    {% endif %}
    '''
* {{field.label}}: field의 label
* {{field.label_tag}}: <label> 태그로 감싸져있는 field의 label 접근
* {{field.legend}}: field.label_tag의 legend 버젼
* {{field.use_fieldset}}: form field의 widget이 여러개의 input을 가지면 True
* {{field.value}}: field의 값








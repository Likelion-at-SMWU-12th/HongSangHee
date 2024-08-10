<br><br>
### 🦁 멋사 6주차 과제 🦁

| 실습 <br> 번호 | week06 | 
|:------:|:------|
|`Model`|<img width="782"> ![스크린샷 2024-05-10 012138](https://github.com/Likelion-at-SMWU-12th/HongSangHee/assets/128593886/e3d54eb2-2c00-47e0-8e23-6f70f5be0c6d) |
|`View`| ![스크린샷 2024-05-09 224520](https://github.com/Likelion-at-SMWU-12th/HongSangHee/assets/128593886/4a013d76-2a34-43f1-8e64-afafbb61580e)| 
<br>
<p dir="ltr"><span style="font-size: 14px;"><strong>MTV 패턴은 Model, Template, View의 약어이다.&nbsp;</strong></span><strong style="font-size: 1rem;">이는 어플리케이션의 역할을<span lang="EN-US"> 3</span>가지로
구분한 개발 방법론이다<span lang="EN-US">.</span></strong><u>Model</u>은 DB에 저장되는 데이터를 말한다.&nbsp;</p>
<p dir="ltr"></p>
<ul>
    <li>&nbsp;모델은 클래스로 정의되며 하나의 클래스가 하나의 DB Table이 된다.</li>
</ul>
<p></p>
<p dir="ltr">&nbsp; &nbsp; &nbsp;장고는 DB에서의 작업을 ORM 기법을 통해 데이터베이스와 연결하여 데이터를 저장한다.&nbsp;</p>
<p dir="ltr">&nbsp; &nbsp; &nbsp;즉, 장고에서 DB와의 상호작용은 Model을 통해 이루어지며, Model에서는 데이터의 구조와 동작(CRUD 등)이 정의된다.</p>
<p dir="ltr"></p>
<ul>
    <li><span style="font-size: 14px;"><u>View</u>에서는 데이터의 가공 및 처리를 담당한다. 웹의 요청을 받으면, 데이터를 가져와 어플리케이션의 로직을 바탕으로 처리한 결과를 Template에 반환한다.</span></li>
    <li><span style="font-size: 14px;"><u>Template</u>은 사용자에게 보여지는 화면(User Interface)이다. 여기서는 view의 응답 결과(데이터)가 사용자에게 적절한 형태로 표현된다.</span></li>
</ul>
<p></p>

<br><br>
### 🦁 멋사 스프링 2주차 과제 🦁
#### 1. 어노테이션(@, annotation)의 정의
➡️Annotation은 Java5부터 새롭게 추가된 문법요소로 사전적 의미로는 '주석'이라는 뜻을 가진다.<br>
➡️코드 사이에 주석처럼 쓰이며 프로그램에게 추가적인 정보(메타데이터)를 제공한다.<br>

#### 2. 어노테이션(@, annotation)의 종류 및 개념 정리
| 이름 | 기능 | 추가사항 |
|-------|-------|-------|
| @RestController | RESTful API의 컨트롤러를 정의하는 어노테이션으로 자동으로 데이터를 JSON 형식으로 반환한다. | @RequestBody와 @Controller를 결합한 어노테이션이다.|
| @RequestMapping | HTTP 요청을 특정 메서드나 클래스에 매핑하는 어노테이션으로 특정 URL, HTTP 메서드, 요청 헤더, 파람터 등을 설정할 수 있다. | 별도 요청에 따라 모든 http 메서드에 처리하거나 특정에 대해서만도 처리가 가능하나 스프링 4.3이후로 사용하지 않음 |
| @GetMapping | HTTP GET 요청을 처리하는 메서드이다. | @RequestMapping(method = RequestMethod.GET)와 같다.|
| @PostMapping| HTTP POST 요청을 처리하는 메서드이다. | @RequestMapping(method = RequestMethod.POST)와 같다. |
| @PutMapping | HTTP PUT 요청을 처리하는 메서드이다. | @RequestMapping(method = RequestMethod.PUT)와 같다. |
| @DeleteMapping | HTTP DELETE 요청을 처리하는 메서드이다.  | @RequestMapping(method = RequestMethod.DELETE)와 같다. |
| @PathVariable | URL 경로의 일부로 전달된 변수를 메서드의 매개변수의 값과 연결한다. | @GetMapping 어노테이션과 @PathVariable에 지정된 변수의 이름을 동일하게 맞추어야 한다.|
| @RequestBody | HTTP의 Body 내용을 해당 어노테이션이 지정된 객체에 매핑한다. | 주로 POST 또는 PUT 요청에서 JSON 데이터를 받을 때 사용한다. |
| @RequestParam | HTTP 요청 파라미터를 메서드의 매개변수로 사용하게 한다. | 쿼리스트링 값도 받을 수 있다.  |

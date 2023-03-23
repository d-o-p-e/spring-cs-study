# Spring MVC 아키텍쳐

### 엠 비 씨 ..

목적: 관심사에 집중하기 위한 분리. OO을 할때는 OO에만 집중하자.

- 컨트롤러
    - HTTP 요청을 받음
    - 파라미터검사
    - 비즈니스 로직 실행 (서비스, 레파지토리 호출..)
    - 모델에 데이터 담아서 뷰에 전달
- 모델
    - 뷰에 전달할 데이터 담는 ‘공간’ (특별한 로직이라 생각하지 말자)
    - 덕분에 뷰는 비즈니스 로직을 몰라도 됨
- 뷰
    - 모델에서 데이터 꺼내서 화면만 출력

### Spring MVC - 컨트롤러 모델 뷰만 있는줄 알았제?

> 어림도없지
> 

### ‘MVC 디자인 패턴’ 을 구현한 것이 스프링 MVC.

전체적인 구조는 같지만 컨트롤러가 무친듯이 크고 복잡하다.

헷갈릴 수 있는데, 우리가 흔히 사용하는 레이어드 아키텍쳐(컨트롤러-서비스-레포지토리) 에서의 컨트롤러는 여기에서 얘기하는 컨트롤러랑 다름.

MVC의 컨트롤러를 → 컨트롤러/서비스/레포지토리 이렇게 삼등분.

### 으마으마한 목-차

> 하나하나 알아봅시다
> 
1. Dispatcher Servlet
2. Handler Mapping
3. Handler Adapter
4. Controller
5. Service
6. Repository
7. Model
8. View Name
9. View Resolver
10. View

### 시나리오1 - 요청이 들어와서 Dispatcher Servlet이 호출

DispatcherServlet은 HttpServlet을 상속받은 ‘서블릿’이다

> **“DispatcherServlet은 서블릿이다.”**
> 

1. 요청이 들어와서 Dispatcher Servlet이 호출
    - `HttpServletRequest`, `HttpServletResponse` 객체 생성 후 다음 함수들의 파라미터로 넘김
2. sevlet이 service() 라는 매서드가 호출
3. service() 매서드는 doDistpatch() 를 호출

### 시나리오2 - doDispatch 의 시작

> 아래의 과정은 모두 doDispatch()의 동작입니다.
> 

1. HandlerMapping 을 호출
    
    - HTTP 요청과 매칭되는 `등록된 핸들러(`@RequestMapping`)’를 찾음
    - 만약 적절한 핸들러가 없으면, `404 NOT_FOUND` 반환
2. HandlerAdapter 호출
    
    - 핸들러를 인자로 넣어서, 해당 핸들러가 사용 가능한 어뎁터를 조회하고 호출(생성?). `HandlerAdapter(핸들러)`
        - 핸들러 어뎁터란? 해당 핸들러를 실행시켜주는 요소.
        - Controller 빈 등록 방식이 다양하게 존재하기 때문에 어뎁터 패턴으로 구현.
3. 어뎁터 실행 결과로 ModelView 반환
    
    - `@Controller` 에서 return 형태를 기억하시나요?
    
    ```java
    @GetMapping("/test")
    public String home(Model model) {
    		
    		String data = homeService.doSomething();
        model.addAttribute("someData", data );
        
        return "home";
    }
    ```
    
    - Model이라는 객체에 MVC의모델에 들어갈 객체를 넣어줍니다!.
    - @Controller의 마지막에 `return ‘home';` 이렇게 return 해주는 것을 본 적이 있으신가요?
    다음 step에서 호출할 모델 이름을 명시해주는 것 입니다.

### 시나리오3  - ViewResolver 호출

1. 컨트롤러 실행의 결과인 ModelView 를 가져옵니다!
    - 이 ModelView 객체에는 컨트롤러에서 return 한 값이 들어있습니다.
2. ViewResolver를 호출하여 진짜 view를 가져옵니다!
    - 컨트롤러에서 반환했던 string 값으로 찾아옵니다.

> 이 ViewResolver도 다양한 방식으로 구현되어 있어서, 의존성 추가한 것을 바탕으로 구현체가 교체됩니다.
익히 알고 있는 템플릿 엔진들: JSP, 머스테치, 타임리프 등등..
Q. 뭐가 이렇게 자동을 설정을 해줄까요?
> 

### 시나리오4 - View 렌더링

뷰리졸버에서 찾은 뷰 껍데기와, 모델에 있는 데이터를 조합하여 Html을 만들어서 response로 반환합니다

---

### 김영한 교주님의 그림을 볼까요?

---

자.. 스프링 엠-비-씨 에 대해서 아시겟-어요?

### 그렇다면 `@Controller` 는 무엇인가?

컨트롤러는 `@RequestMapping`으로 정의되어 있는 함수들을 핸들러로 등록해줍니다. 

### 그렇다면 **`@RestController`** 는 무엇인가?

`@Controller`를 상속받아서 다른 동작은 같지만, ViewResolver 대신 `MessageConverter` 가 작동합니다.

메시지 컨버터를 거치면 응답 객체는 JSON 형식으로 변환되어 HTTP Response Body에 들어갑니다.

`MessageConverter` 도 구현체가 다양하게 있으며, 기본은 Jackson 라이브러리를 활용한 메시지 컨버터를 사용합니다. 

> Jackson은 JSON데이터 등의 다양한 문서 포멧을 다루기 위한 라이브러리입니다.
그리고 메시지 컨버터 또한 스프링 부트에서 자동으로 기본 설정을 등록해줍니다. → 이게 뭐라고?
> 

---

### 엥 그렇다면 `@Service` `@Repository` `@Component` 의 차이점은 무엇인가?

사실 없음. 이라고 하면 맞습니다. 진짜 쳐맞음 ㅋㅋ

- 일단 표면적으로 레이어드 아키텍쳐의 구분을 위함.
- 어노테이션을 통해 스프링 AOP 적용을 하는 경우가 있음
- **@Repository 의 기능… 알고계셨나요?**
    - hibernate 오류를 `org.springframework.dao.DataAccessException` 의 서브클래스로 자동전환
    - 이건 저도 이번에 플젝하면서 알았음
- ~~“님 이거 왜 예외가 안잡힘?”~~
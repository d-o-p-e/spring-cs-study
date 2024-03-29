### Java의 특징에 대해 설명해주세요

자바는 전통적인 객체지향언어입니다.

운영체로부터 독립적으로 실행 가능한 JVM 환경을 제공합니다.


### JVM의 역할에 대해 설명해주세요

JVM은 운영체제로부터 독립적인 환경을 보장합니다.

각 운영체제별로 JVM이 구분되어 있으며, 컴파일된 자바 바이트 코드를 machine language 로 변환합니다.

오라클에서 표준을 정의하면 아마존, 애저 등에서도 JVM 을 개발하기도 합니다.

최신 자바에는 JIT가 포함되어 있는데, 반복되는 코드를 컴파일 시켜서 인터프리터의 중복 작업을 줄입니다.

### Overriding과 Overloading에 대해 설명해주세요

오버라이딩은 기존 부모 함수를 덮어써서 구현하는 방식입니다. 매서드의 확장을 제공합니다.

오버로딩은 같은 함수를 파라미터의 형태에 따라서 다른 동작을 하게 구현하는 방식입니다. 매서드 네이밍의 일관성을 제공합니다.

### 객체지향 프로그래밍이란 무엇인지 설명해주세요

상태와 행동을 담고있는 객체들이 상호작용하는 관점에서 설계하는 프로그래밍 방식입니다.

### 객체지향 설계원칙에 대해 설명해주세요

S: SRP 단일 책임 원칙: 하나의 객체 또는 주체가 하나의 동작만 하도록 만드는 것. 책임의 영역을 확실하게 하고, 유지보수와 가독성 향상에 도움을 줌

O: OCP 개방 폐쇄 원칙: 객체는 변경에는 닫혀있고, 확장에는 열려있게 설계. 기존 요소들에 대한 변경은 최소화할 수 있게 구현하고, 상속 등을 통해서 쉽게 활용할 수 있게 구성. 추상화와 다형성을 극대화.

L: 리스코프 치환 원칙: 서브타입은 항상 상위타입으로 교체 가능해야 한다. 객체 간의 상속관계 억지로 만들지 마라. 복잡도만 올라간다. 차라리 기능만 명세한 인터페이스 써라.

I: 인터페이스 분리 원칙: 인터페이스에서 정의한 기능 명세 영역이 겹칠 경우, 분리를 고려하자.

D: 의존성 역전의 원칙: 하위 모듈의 변경이 상위 모듈에 영향을 끼치지 않게 해라. 구현체 클래스에 의존하지 말고, 추상클래스나 인터페이스에 의존하게 하고 주입하는 형태의 코드를 작성.

### 인터페이스와 추상 클래스의 차이점에 대해 설명해주세요.

인터페이스는 구현에 대한 명세서만을 선언하고 있습니다.

추상 클래스는 추상 매서드를 통해 구현에 대한 명세와, 공통된 기능에 대한 구현을 제공합니다.

둘 다 직접 생성자를 호출하여 인스턴스화 시킬 수 없지만, 추상 클래스의 static method와 variable에는 접근이 가능하다는 차이도 있습니다.

### 클래스와 객체, 인스턴스에 대해 설명해주세요

객체: 상태와 행동을 담은 주체. 프로그래밍의 관점이 아닌 것 같음.

클래스: 객체를 만들기 위한 설계도

인스턴스: 클래스로부터 만들어진 객체


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


### 데이터의 형태에 따라 내부 정렬 방식은 다르다.

대부분의 언어에서 조금 더 효율적인 정렬을 제공하기 위해, type 마다 다른 방식의 정렬을 제공.

참조 지역성의 원리(Local of Reference)를 고려하여 CPU 캐싱을 효율적으로 활용하거나 안정성 필요의 유무에 따라 다른 알고리즘을 적용.

### Array.sort() 의 정렬

듀얼피봇 퀵정렬(Dual-Pivot QuickSort) 을 사용.

기존 퀵정렬을 개선하여 분할 지점을 하나 더 추가.

랜덤 데이터에 대해서 조금 더 준수한 성능.

sort 같은 경우

### Collection.sort() 의 정렬

팀정렬(Tim sort) 을 사용.

insert sort 와 merge sort를 결합하여 만든 정렬 방식

메모리에서 값들이 연속적으로 존재하기 때문에, CPU의 데이터 접근 시간(참조 지역성)이 좋다.

### Reference

팀정렬에 대한 설명

https://d2.naver.com/helloworld/0315536

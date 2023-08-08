1. Spring vs Spring Boot
    
    [https://www.geeksforgeeks.org/difference-between-spring-and-spring-boot/](https://www.geeksforgeeks.org/difference-between-spring-and-spring-boot/)
    
    - 스프링과 스프링부트의 차이점이 있다면 설명하시오.
    
        <img width="860" alt="Screenshot 2023-03-19 at 1 00 01 PM" src="https://user-images.githubusercontent.com/51287461/226155544-4179bd4a-d6e2-4adf-94cf-affeee2e8619.png">

        Spring은 오픈소스 자바 프레임워크이며, 손쉬운 애플리케이션 개발을 위해 광범위하게 사용되고 있으며, 이중 Spring Boot은 이 위에 만들어져 REST API 개발에 주로 사용되고 있다.
        
        Spring Boot은 Spring 위에 Autoconfiguration을 대표로 한 다양한 자동화된 기능을 포함하고 있다.
        
        Spring만을 사용하면 모듈이 분리된 애플리케이션을 제작하지만, Spring Boot을 이용해서 바로 Stand-alone Application의 제작이 가능하다.
        
        Spring을 사용하면 별도로 서버를 구축해야 하지만, Spring Boot은 Tomcat, 아니면 Jetty 등을 이용한 내장된 서버가 존재한다.
        
        Spring Boot은 자체적으로 내부에 메모리 DB (H2 Database)를 내장할 수 있도록 지원하고 있어 간편하게 사용이 가능하다.
        
        Boilerplate가 Spring Boot에서 현격히 감소한다.
        
        `pom.xml` (혹은 `build.gradle` )을 미리 제작해줘서 라이브러리를 불러오기 쉽다.
        
        —> Spring Boot는 Spring에서 반복되고 Hard Coding을 요구하는 요소들을 자동화 시켜줘 애플리케이션 개발의 속도를 줄여준다.
        
    - Spring Boot Starter란?
        
        [https://nortal.com/us/blog/starters-connecting-infrastructure/#:~:text=In the world of Spring,paste loads of dependency descriptors](https://nortal.com/us/blog/starters-connecting-infrastructure/#:~:text=In%20the%20world%20of%20Spring,paste%20loads%20of%20dependency%20descriptors).
        
        Spring Boot에서 사용할 수 있는 dependency들을 모아놓은 descriptor로서, Spring Boot의 손쉬운 외부 dependency 연결을 용이하게 만들어준다. 주로 특정 기능을 이용하기 위해 필요한 dependency들을 한 패키지로 묶어주어 삽입과 삭제가 용이하다.
        
        종류로는 Application Starters, Production Starters, Technical Starters가 있으며, 그 목록은 아래 링크에 있다.
        
        [https://www.geeksforgeeks.org/spring-boot-starters/](https://www.geeksforgeeks.org/spring-boot-starters/)
        
        - Application Starters
            
            JPA, mail, security 등 Application마다 추가해서 사용하는 dependency들이 대부분 여기에 포함되어 있다.
            
        - Production Starters
            
            `spring-boot-starter-actuator` 라는 dependency로서, 프로덕션 서버의 상태를 API 형식으로 빠르게 확인할 수 있도록 돕는다.
            
        - Technical Starters
            
            jetty, tomcat 등의 내장 서버를 포함하고 있으며, log4j2, logging 등의 로깅 dependency를 포함하고 있다.
            
        
2. Gradle
    
    [https://stackify.com/gradle-vs-maven/](https://stackify.com/gradle-vs-maven/)
    
    - Gradle과 Maven에 대해 설명하시오.
        
        두 툴 모두 의존성 관리 툴이며, 빌드, 테스트, 패키징에 이르는 과정들을 자동화하는데 도움을 준다. 
        
        Maven은 아파치에서 만들었으며, pom.xml이라는 XML configuration file을 이용하여 의존성을 추가하고 매우 다양한 서드파티 플러그인들을 지원하고 있다.
        
        Gradle은 이후 Maven보다 유연한 범용적인 빌드 도구를 위해서 만들어졌다.
        
        Android OS에서 기본 빌드 도구로 채택되면서 범용적으로 사용되었으며, Ivy, Maven repository 또한 지원한다.
        
        또한 Groovy 언어를 이용한다.
        
    - Gradle과 Maven의 차이는?
        
        Gradle이 Maven보다 늦게 나왔고, Maven의 단점들을 보완하려는 측면이 개발과정에 있어서 뛰어난 점이 있음.
        
        - XML로 하면 가독성이 떨어지고 작성하기 어려운 Build의 동적 요소들을 쉽게 적용할 수 있음
        - Groovy 스크립트로 플러그인을 호출하거나 아예 직접 코드를 작성할 수도 있음
        - Maven에 비해 Gradle의 Build 속도가 월등히 빠름
    - Spring에서 Gradle의 역할
        
        Gradle은 Spring에서 라이브러리 의존성들을 기록하며, Spring 프로젝트를 개발하는 전반적인 과정에서 prerequisite setting들을 설정해줄 수 있음.
        
3. Servlet + Tomcat
    - Tomcat이란?
        
        Apache 재단의 WAS(Web Application Server)이며, Java Servlet과 JSP가 포함된 웹페이지를 배포해준다.
        
        [https://exhibitlove.tistory.com/312#:~:text=Tomcat 은 Java로 작성된,의 Process 로써 동작합니다](https://exhibitlove.tistory.com/312#:~:text=Tomcat%20%EC%9D%80%20Java%EB%A1%9C%20%EC%9E%91%EC%84%B1%EB%90%9C,%EC%9D%98%20Process%20%EB%A1%9C%EC%8D%A8%20%EB%8F%99%EC%9E%91%ED%95%A9%EB%8B%88%EB%8B%A4).
        
        ![image](https://user-images.githubusercontent.com/51287461/226155577-09374911-50cd-4333-9c4a-cbcce488a324.png)
        
        웹서버에서 HTTP Request를 받으면 Servlet Container에 전송
        
        1) Http Request를 Servlet Container에 전송
        
        2) Servlet Container는 HttpServletRequest, HttpServletResponse 두 객체를 생성
        
        3) 사용자가 요청한 URL을 분석해 어느 서블릿에 대한 요청인지 탐색
        
        4) 만약 해당 서블릿이 한 번도 실행된 적 없거나, 현재 메모리에 생성된 인스턴스가 없다면 새로 인스턴스를 생성하고 init() 메소드를 실행하여 초기화한 뒤 스레드를 하나 생성 이미 인스턴스가 존재할 경우에는 스레드만 하나 생성
        
        (각 서블릿 인스턴스는 서블릿 컨테이너 당 하나만 존재하기 때문)
        
        5) 컨테이너는 서블릿 service() 메소드를 호출하며, POST, GET 여부에 따라 doGet() 또는 doPost()를 호출
        
        6) 실행된 메소드는 동적인 페이지를 생성한 후 HttpServletResponse 객체에 응답을 보냄
        
        7) 응답이 완료되면 HttpServletRequest, HttpServletResponse 두 객체를 소멸
        
        ![image](https://user-images.githubusercontent.com/51287461/226155594-30f6d8fb-4166-4597-9a1a-af7482082da5.png)

        
        Tomcat 또한 JVM 위에서 돌아가며, Tomcat Instance들이 각각 Process 로서 동작함.
        
        Controller: 특정 TCP port에서 request들을 engine으로 보내줌.
        
        Engine: 정의된 Connector로 들어온 요청을 하위의 Host에게 전달함.
        
        Host: 하나 이상의 Context가 존재하며, Context는 하나의 Web Application을 나타냄. 외장 톰캣으로 사용시 주로 War 형태로 배포함.
        
    - Servlet이란?
        
        Servlet이란 Java에서 웹페이지를 동적으로 생성하기 위해 만든 서버측 프로그램이며, 웹 서버의 성능향상을 위한 자바 클래스의 일종이다.
        
        Servlet의 특징으로는 다음이 있다;
        
        - 클라이언트의 Request에 대해 동적으로 작동하는 웹 애플리케이션 컴포넌트
        - HTML을 사용하여 Response 한다.
        - JAVA의 스레드를 이용하여 동작한다.
        - MVC 패턴에서의 컨트롤러로 이용된다.
        - HTTP 프로토콜 서비스를 지원하는 javax.servlet.http.HttpServlet 클래스를 상속받는다.
    - Spring에서는 둘을 어떻게 활용하는가?
        
        Spring Boot에서는 내장 톰캣을 이용하여 서블렛을 올리기에, 통째로 Jar로 빌드할 수 있다. 그러나 그렇지 않은 Spring Project는 외장 톰캣으로 연결을 해야하기 때문에 war로 빌드하여 톰캣 위에 Servlet/JSP 형태로 사용해야 한다. 물론 Spring Boot에서도 내장 톰캣을 제거하고, WAR 형태로 배포할 수 있다.

# 

### 1. Spring MVC 구조

- **MVC란 어떤 구조인가?**
    
    [https://developer.mozilla.org/ko/docs/Glossary/MVC](https://developer.mozilla.org/ko/docs/Glossary/MVC)
    
    MVC (Model-View-Controller)는 User Interface, Data & Logic manipulation을 구현하는데 널리 사용되는 소프트웨어 디자인 패턴이다. 주로 Business Logic과 화면을 구분하는데 중점을 두고 있다. 이를 통해 더나은 업무의 분리와 향상된 관리를 제공한다. MVC에 기반을 둔 다른 디자인패턴들로는 MVVM(Model-View-ViewModel), MVP(Model-View-Presenter), MVW (Model-View-Whatever)등이 있다.
    
    ![image](https://user-images.githubusercontent.com/51287461/226871213-614f07b5-4e1b-45b9-b3bf-3756a931a1aa.png)
    
    - Model : Model은 앱이 포함해야할 데이터가 무엇인지를 정의함. Data의 상태가 변경되면 Model을 일반적으로 View에게 알리며, 가끔 컨트롤러에게 알리기도 한다 (업데이트된 뷰를 제거하기 위해 다른 로직이 필요한 경우)
    - View : 앱의 Data를 보여주는 방식을 정의한다. 즉, UI를 담당한다.
    - Controller : Controller는 User로부터의 입력에 대한 응답으로 Model 및/또는 View를 업데이트하는 Logic을 포함한다. 
    Model, View에게 직접 지시 또한 가능하다.

**MVC 패턴의 흐름**

- Controller - Model : Controller는 Model에게 언제든지 접근이 가능하지만, 반대로 Model은 Controller에게 접근할 방법이 없다.
- Controller - View : Controller는 UI의 Logic을 포함하기 때문에 둘은 서로 접근이 가능하다. 그러나, View에서 Controller로 접근할 때 내부의 구조를 인지하고 접근하는 것이 아니기에 구조화된 interface를 통해 접근해야 한다.
- Model과 View는 서로 독립되어 있어야 하기 때문에 서로 접근이 불가능하다.
- **Spring에서의 MVC 구조는 어떻게 사용되는가?**
    
    [https://catsbi.oopy.io/f52511f3-1455-4a01-b8b7-f10875895d5b](https://catsbi.oopy.io/f52511f3-1455-4a01-b8b7-f10875895d5b)
    
    ![image](https://user-images.githubusercontent.com/51287461/226871256-51ec39d1-1ece-4899-88a6-7b16b5af1ebf.png)
    
    ### Spring MVC 동작 순서
    
    1. 핸들러 조회 : 핸들러 매핑을 통해 URL에 매핑된 핸들러(Controller) 조회
    2. 핸들러 어댑터 조회 : 핸들러를 실행할 수 있는 핸들러 어댑터 조회
    3. 핸들러 어댑터 실행
    4. 핸들러 실행 : 핸들러 어댑터가 실제 핸들러를 실행
    5. ModelAndView 반환 : 핸들러 어댑터는 핸들러가 반환하는 정보를 ModelAndView로 변환해 반환
    6. viewResolver 호출
    7. View 반환 : View Resolver는 뷰의 논리 이름은 물이 이름을 바꾸고 렌더링 역할을 담당하는 뷰 객체를 반환
    8. View 렌더링 : View를 통해서 View를 렌더링한다.
    - **Dispatcher Servlet**
        
        부모 클래스에서 HttpServlet을 상속받아 사용, 서블렛으로 동작함.
        
        `DispatcherServelt` → `FrameworkServlet` → `HttpServletBean` → `HttpServlet`
        
        Spring Boot 구동시 DispatcherServlet을 서블렛으로 자동등록하며, urlPatterns=”/”, 즉 모든 경로에 대한 매핑을 등록한다.
        
        서블렛을 호출하면 `HttpServlet`이 제공하는 `service()` 메소드가 호출된다.
        
        스프링 MVC는 DispatcherServlet의 부모인 FrameworkServlet에서 service()를 override 해뒀다
        
        FrameworkServlet.service()를 시작으로 여러 메서드가 실행되며 DispatcherServlet.doDispatch()가 호출된다.
        
        doDispatch() : 적절한 컨트롤러를 찾아 매핑해주고 View를 찾아서 반환해 렌더링까지 해주는 메소드
        
    - **핸들러 매핑 & 핸들러 어댑터**
        
        URL을 통해 해당되는 컨트롤러를 찾기 위해서는 이 두가지가 필요하다;
        
        - HandlerMapping
            - 핸들러 매핑 내에서 컨트롤러를 찾을 수 있어야 한다.
            - Spring Bean의 이름으로 핸들러를 찾을 수 있는 핸들러 매핑이 필요하다.
        - HandlerAdapter
            - 핸들러 매핑을 통해 찾은 핸들러를 실행할 수 있는 핸들러 어댑터가 필요하다.
            - Controller interface를 실행할 수 있는 핸들러 어댑터를 찾아야 한다.
            
            이는 Spring Boot 내에서 자동으로 등록해준다.
            
            **❗️어댑터 패턴 - 서로 다른 두 인터페이스 사이를 연결해주어 기존 코드를 건드리지 않고 새로운 동작이 가능하다.**
            
    - **viewResolver**
        
        데이터를 View로 전달할때, 어떤 View를 사용할지 설정하는 위치.
        
        이때 JSP를 제외한 다른 뷰들은 실제 View를 렌더링하지만, JSP의 경우 forward()를 통해 직접 이동해야 렌더링이 된다.
        
    
    **@Controller** : 스프링이 자동으로 스프링 빈으로 등록하고, Annotation-based Controller로 인식하여 HandlerMapping에서 매핑이 가능한 핸들러가 된다.
    
    **@RequestMapping** : 요청 정보를 매핑해서 해당 URL이 호출되면 이 메서드가 호출된다.
    
    **ModelAndView** : 모델과 뷰 정보를 담아서 반환된다.
    

### 2. DI + IoC Container

- **DI(Dependency Injection이란?**
    
    객체에게 variable로서 다른 객체를 만들때, 생성자로 만드는 것이 아닌, 외부에서 이미 만들어진 객체를 삽입해주는 것을 뜻한다. 이는 두 클래스의 결합을 느슨하게 만들어주어 유연성을 확보해준다. 주로 Singleton 객체를 삽입해주며, 이를 통해 기존에 생성자로 만들어서 객체간의 관계가 아닌 클래스 간의 관계였다면, 의존성주입을 통해 객체간의 관계로 만들어줄 수 있다.
    
- **IoC Container란?**
    
    …그리고 의존성주입을 위해서는 주입할 객체가 미리 생성되어 있어 존재하고 있어야 하는데, 이를 보관하는 곳이 IoC Container이다.
    
    IoC (Inversion of Control)이란, 객체에 대한 책임을 넘기는 것을 말한다. 여기서는 Spring 프레임워크에게 주입되는 객체들을 넘겨주고 받는 객체는 수동적으로 주입만 받는다.
    
- **이 둘을 Spring에서는 어떻게 활용하는가?**
    
    Spring에서는 IoC Container, 즉 프레임워크에서 주입되어야 할 객체들을 시작함과 동시에 생성하며, 필요한 곳에 주입해주어 객체에 대한 관리를 프레임워크에서 맡게 된다. 이를 통해 주입되는 객체와 주입받는 객체의 관계가 형성되며, 이는 생성자로 객체를 생성하는 방식보다 훨씬 유연하며 결합이 느슨하다.
    

### 3. Spring AOP

- **AOP란?**
    
    AOP (Aspect-Oriented Programming)이란, 핵심 business logic과 부가적인 기능들을 분리하여 Application 전체에 부가기능들을 모듈화 시켜서 재사용할 수 있도록 하고자 하는 개발론이다.
    
    OOP에서 modularizing의 기준이 business logic이었다면, AOP에서는 인프라/부가기능으로 구분합니다. 전체적으로 많이 반복되는 부가기능들은 상속, 위임으로 깔끔한 모듈화가 어렵다. 그래서 application 전체에 흩뿌려져있는 부가기능들을 한 곳으로 모아 관리하자는 것이 골자이다.
    
    **용어 정리**
    
    Aspect : 부가기능들을 모듈화 한 것.
    
    Target : aspect를 적용하는 곳
    
    Advice : 실질적인 부가기능을 담은 구현체
    
    Join Point : Advice가 적용될 위치, 즉 메서드가 실행되는 시점
    
    Point Cut : Join Point의 상세한 스펙
    
    AOP는 컴파일 시점, 클래스 로딩 시점, 런타임 시점 중 하나에 적용할 수 있으며, Spring에서는 런타임 시점에 적용하고 있다.
    
    → 특정 Bean을 만들 때 같은 타입의 Proxy Bean을 만들어 런타임 때 Proxy Bean에서 Aspect를 추가하여 동작시키는 방법이다.
    
- **프록시 패턴이란?**
    
    원래 객체를 감싼 객체를 프록시 객체라 하여 객체로 접근이 왔을 때, 원래 객체의 기능에 더불어 추가적인 기능을 더하여 실행할 수 있도록 해주는 디자인 패턴
    
    ![image](https://user-images.githubusercontent.com/51287461/226871323-fd0c5691-b0d8-48d6-8433-1109785181f5.png)
    

### 4. Bean

- **Java Bean, Spring Bean이란?**
    
    Java Bean이란 JavaBean API Specification의 규칙들을 만족하는 클래스를 일컫는다.
    
    - No argument constructor가 존재한다.
    - 모든 필드들을 private으로 지정하고, 외부접근을 위한 public get, set 메소드를 정의해야 함
    - java.io.Serializable 인터페이스를 구현한다.
    
    Spring Bean은 Spring IoC Container에서 관리하는 객체들을 말한다.
    
    객체를 Spring Bean으로 등록해주려면, 즉 Spring IoC Container에 등록하려면 @Controller를 클래스에 사용하는 법, 그리고 @Configuration 클래스 안에 @Bean을 이용하여 등록하는 법 중 하나를 사용하면 된다.
    
- **Spring에서 Bean의 생명주기**
    
    [https://velog.io/@destiny1616/스프링-빈-생명주기](https://velog.io/@destiny1616/%EC%8A%A4%ED%94%84%EB%A7%81-%EB%B9%88-%EC%83%9D%EB%AA%85%EC%A3%BC%EA%B8%B0)
    
    Spring Container 생성 → Spring Bean 생성 → DI → 초기화 콜백 → 사용 → 소멸전 콜백 → Spring 종료
    
    ![image](https://user-images.githubusercontent.com/51287461/226871411-42580435-7d8b-4349-9b64-b5c1720eb53b.png)
    
    **빈 생성 페이즈**
    
    - 빈 객체를 초기화 한다.
    - 객체 초기화 후 Aware interface (BeanNameAware, BeanFactoryAware, etc.)를 구현한 Bean을 스캔해서 관련된 property들을 세팅하기 시작한다.
    - BeanPostProcessor 구현체의 postProcessBeforeInitialization 들이 작동한다.
    - @PostConstruct Annotation의 메서드가 바로 이후 실행된다.
    - InitializingBean interface를 구현한 Bean들의 afterPropertiesSet() 메서드를 실행한다.
    - @Bean Annotation의 initMethod attribute에 정의되어있는 초기화 메서드를 발동한다.
    - BeanPostProcessor 구현체의 postProcessAfterInitialization이 작동한다.
    
    **빈 소멸 페이즈**
    
    - @PreDestroy Annotation의 메서드들을 실행한다.
    - DisposableBean 구현체의 destroy() 메서드를 실행한다.
    - @Bean annotation의 destroyMethod attribute에 custom destruction 훅을 정의하면 마지막 페이즈에서 실행한다.
    
    노랑 : Spring interface들을 활용한 Callback
    
    **파랑 : @PostConstruct, @PreDestroy annotation “ → 최신 스프링에서 권장하는 방법**
    
    초록 : @Bean annotation의 attribute “
    
- **@Bean과 @Component의 차이는?**
    
    @Component는 클래스 레벨에서 선언해서 Spring이 runtime 시점에 component scan을 통해 자동으로 찾아낸다면, @Bean은 메소드 레벨에서 선언해서 return되는 객체를 수동으로 Bean으로서 등록하는 것이다.

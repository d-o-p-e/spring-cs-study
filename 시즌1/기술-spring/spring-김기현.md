# Spring(3주차)

1. Spring vs Spring Boot
    - 스프링과 스프링부트의 차이점이 있다면 설명하시오.
    - Spring Boot Starter란?
2. Gradle
    - Gradle과 Maven에 대해 설명하시오.
    - Gradle과 Maven의 차이는?
    - Spring에서 Gradle의 역할
3. Servlet + Tomcat
    - Tomcat이란?
    - Servlet이란?
    - Spring에서는 둘을 어떻게 활용하는가?

---

1. 스프링과 스프링부트 차이점
스프링은 자바 기반 어플리케이션을 만드는 데 사용되지만 스프링부트는 REST API 개발을 위해 사용된다. 또한 스프링은 dependency를 직접 주입해주어야 하고 서버를 명시적으로 설정 스프링부트는 자동적으로 auto-configuration이 주어진다. 
2. 스프링부트 스타터
스타터는 사용자가 프로젝트를 빠르게 시작하고 실행하는데 필요한 의존성들이 포함되어있다.
    - spring-boot-starter-aop : 관점 지향 프로그래밍(AOP)을 위한 스타터 (AOP의 관해서는 따로 포스팅을 할 예정이다.)
    - spring-boot-starter-batch : 스프링 배치를 사용하는데 필요한 스타터
    - spring-boot-starter-data-jpa: 스프링 데이터 JPA와 하이버네이트를 사용하는 데 필요한 스타터
    - spring-boot-starter-data-redis : 메모리 저장 방식의 저장소인 레디스와 자바에서 쉽게 레디스를 사용하게끔 도와주는 제디스 설정 자동화 스타터
    - spring-boot-starter-data-rest : 스프링 데이터 저장소 방식에 맞춘 REST API를 제공하는 데 사용하는 스타터
    - spring-boot-starter-thymeleaf : 타임리프 템플릿 엔진을 사용하는 데 필요한 스타터
    - spring-boot-starter-jdbc : 톰캣 JDBC 커넥션 풀에 사용하는 스타터
    - spring-boot-starter-securiy : 각종 보안에 사용하는 스프링 시큐리티 스타터
    - spring-boot-starter-oauth2 : Oauth2 인증에 사용하는 스타터
    - spring-boot-starter-validation : 자바 빈 검증에 사용하는 스타터
    - spring-boot-starter-web : 웹을 만드는 데 사용하는 스타터(스프링 MVC, REST형, 임베디드 톰캣, 기타 라이브러리 포함)
    
    [https://johngrib.github.io/wiki/spring/boot/starter/](https://johngrib.github.io/wiki/spring/boot/starter/)
    
3. Gradle과 Maven
빌드 배포 도구
4. 둘 차이
maven 은 xml로 라이브러리를 정의하고 활용하도록 되어 있다.
이와 다르게 gradle 은 별도의 스크립트 언어로 구성되어 있어 if else for 등의 로직이 구현 가능하다.

5. Spring에서 gradle 역할

[https://velog.io/@smallcherry/Spring-스프링에서-Gradle과-build.gradle코드의-의미](https://velog.io/@smallcherry/Spring-스프링에서-Gradle과-build.gradle코드의-의미)

1. 톰캣
클라이언트의 요청과 스프링에서 서비스가 동작하기 위해 필요한 미들웨어이다. 웹 서버의 기능과 웹 어플리케이션 서버 기능을 모두 포함하고 있다고 봐도 무방하다.

2. 서블랫
웹 페이지 혹은 결과값을 동적으로 생성해 주기 위한 역할을 하는 자바 프로그램이다.

3. 둘을 어떻게 활용하는가
SpringMvc 에서 제공하고 있는 DispatcherServlet은 컨트롤러에 테스크를 위임하여 요청을 처리한다. 따라서 별도의 서블릿을 개발할 필요 없이 컨트롤러의 구현만으로 response를 클라이언트에 줄 수 있다.
클라이언트로 부터 들어온 request를 분석하여 매핑된 controller가 있는지 확인하고 해당 controller에 request 요청을 보내준다. 여기서 ViewResolver 가 controller가 view를 return 할때 해당 view를 찾아 client에게 return하는 역할을 한다.
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5cb44f36-c87e-4dcc-9071-fb2af7c83037/Untitled.png)
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b9bcd0ef-ea4a-4364-b45b-c9cfa4721e74/Untitled.png)
    
    전체적인 프로세스는 다음과 같다.
    
    1. 클라이언트가 웹 서버로 request를 보낸다
    2. 동적 웹 서버가 servlet 컨테이너로 전달한다
    3. 서블릿 컨테이너에서 쓰레드를 생성한다
    4. 생성된 쓰레드에서 DispatcherServlet 의 service() 메소드가 호출된다
    5. HandlerMapping을 통해 메핑된 컨트롤러를 찾는다
    6. HandlerAdapter를 통해 매핑된 컨트롤러에 request를 전달한다
    7. 개발자가 만든 로직에 따라 컨트롤러 > 서비스 > 레포지토리로 동작한다



1. 의존성 주입이란?
두 객체를 연결시켜 주는 것. 하나의 클래스가 다른 클래스에 의존하고 있는 것.
 A라는 클래스가 B라는 클래스를 사용하고 있으면 A는 B에 의존하고 있다는 것.
즉 이때 A는 B클래스의 인스턴스를 생성해서 주입해준다.
**?? 상속과는 어떻게 다른가요?**
    
    의존성이 감소된다 (의존하는 모듈이 변화한다고 해서 문제가 없)
    
2. IOC 컨테이너
의존성에 대한 제어권을 클래스 A와 B의 매개체에 주는데 이 매개체가 IOC컨테이너이다.
의존성을 관리하고 인스턴스를 생성하여 주입하고 메모리도 해제해준다. 여러 프레임워크들이 이  IOC컨테이너를 포함하고있다.
3. Spring에서 어떻게 활용되는가
의존성을 주입해주고 인스턴스를 생성하고 관리하는 것이 Spring 프레임워크에서 알아서 해준다. Java Bean(POJO)을 생성하고 서비스 삭제에 대한 기능을 하며 개발자가 하나하나 작업해줄 필요 없이 컨테이너가 알아서 만들어 준다. 
의존성의 경우 @Component와 @Bean을 통해 등록이 가능하며 생성자, 필드, 세터 주입이 있다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2f0dcd49-616f-456f-b738-94d7e2e298a8/Untitled.png)

1. AOP
관점지향 프로그래밍이다. 하나의 로직을 핵심적인 관점, 부가적인 관점으로 나누고 이를 기준으로 모듈화 하는 것.
    
    윗 부분처럼 작업을 하면 중복되는 메서드들이 존재하는데 객체지향 프로그래밍인 SOLID에 위반된다… 따라서 같은 기능을 하는 메서드 들을 하나로 묶어 관리한다면 유지보수에 용이하다.
    AOP 관련 용어는 다음과 같다.
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/58ea550e-7231-4500-8d85-3c91c03ebfbc/Untitled.png)
    
    - Aspect : 같은 메소드를 한 데 모아 모듈화
    - Target : Aspect 를 적용하는 클래스 혹은 메서드
    - Advice : 실질적인 기능을 구현하는 구현체
    - Join Point : Advice 가 적용될 위치, 메서드 실행 시점
    - Point Cut : Join Point 를 정의하는 필드?
    
    AOP는 런타임을 적용하는 방법으로 AOP를 구상한다. A라는 클래스 타입의 Bean을 만들 때 A타입의 프록시 빈을 만들고 이 프록시 빈이 Aspect 코드를 추가하여 동작하도록 한다.
    
2. 프록시패턴
    
    프록시의 뜻은 대리자 대변인 이라는 의미이다. 프록시에게 어떤 일을 대신 시키는 것이다.
    
    런타임을 적용 하는 방법으로 AOP를 구현할 수 있다. A라는 클래스 타입의 Bean을 만들 때 A 타입의 프록시 빈을 만들고 이 프록시 빈에 Aspect 코드를 추가하여 동작한다. 즉 프록시 빈에 등록된 Aspect 코드들을 여러 클래스에서 사용할 수 있도록 모듈화 한 것인데 결국 해당 클래스에서 할 일을 프록시 빈이 대신 하고 있다는 의미이다.
    
3. 자바의 빈, 스프링 빈
    
    자바 빈의 규약
    
    - 클래스는 반드시 패키지화 되어야 한다
    - 멤버변수는 프로퍼티라고 부른다
    - 이 프로퍼티의 접근제어자는 private
    - 외부접근은 게터세터로 접근
    - 프로퍼티가 boolean 이면 get 이 아니라 is 도 가능
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d1f90cf9-f8bf-49ad-895c-90db4e176b97/Untitled.png)
    
    스프링에서 빈은 IoC 컨테이너가 관리하는 자바의 객체이다. IoC컨테이너가 객체를 생성하고 관리하기 때문에 어노테이션을 통해서 개발자가 등록해줄 수 있다.
    
    도메인 클래스마다 @Bean을 등록해주어도 되지만 컨피그 파일을 만들어 @Configuration 으로 클래스를 등록해주고 이 곳에 Bean을 등록해주어도 무방하다. 이 때는 새로운 Bean을 만들때 갈아 끼우기 용이하다. 객체지향 프로그래밍이 바로 이 맛 아닐까
    
4. 스프링에서 빈의 생명주기
    
    간단히 말하면 객체를 생성하고(빈을 생성하고) → 의존관계를 주입하는 과정이다.
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/325e618a-3555-42a8-be13-ba45330dfe8c/Untitled.png)
    
    가장 처음에는 Spring IoC 컨테이너가 만들어지고 빈으로 등록된 객체를 스캔하여 해당 빈이 Service 인지 Controller 인지 Entity인지 확인한다.
    
    다음 과정을 이해하기 위해서는 콜백함수에 대해 알아야한다.
    
    콜백함수를 등록하면 특정 이벤트가 발생했을 때 해당 메소드가 호출된다. 예를 들어서 DB, 네트워크와 같이 시작 시점에 이들을 연결한 뒤 어플리케이션 종료 시점에 해당 연결을 종료하는 작업이 필요하다.
    
    의존관계 주입이 완료되면 스프링 빈에게 콜백함수를 통해 초기화 시점을 알리고 스프링이 종료되는 시점에 소멸 시점을 알린다.
    
    따라서 정리해보자면 생명주기는 다음과 같다
    
    스프링 컨테이너 생성(IoC컨테이너) → 빈 생성 → 의존관계 주입 → 콜백 → 스프링 사용 → 콜백(종료) → 스프링 컨테이너 종
    
5. 빈과 컴포넌트 차이
스프링 프레임워크의 빈과 컴포넌트를 살펴보면 사용 시점이 다르다는 것을 알 수 있다.
    
    빈 같은 경우는 @Target({ElementType.METHOD … })
    
    컴포넌트 같은 경우는 @Target(ElementType.TYPE)
    
    즉 빈은 메소드 단에서 선언이 가능하고 컴포넌트는 클래스 단에서 선언이 가능하다.
    
    그럼 개발자가 빈 등록할 경우와 컴포넌트를 등록할 경우를 알아보자면 다음과 같다.
    
    @Configuration 을 통해 Config 클래스를 만들어 빈을 관리할 경우 서비스, 컨트롤러, 도메인을 모두 Config 클래스 안에서 빈으로 등록해 관리할 수 있따,
    
    컴포넌트의 경우 Configuration 파일을 만들지 않고 서비스, 컨트롤러, 도메인 클래스에서 직접 선언이 가능해 개발자가 컨트롤할 수 있다. @Service @Controller 를 통해 각각 컴포넌트로서 사용 가능한 것이다.
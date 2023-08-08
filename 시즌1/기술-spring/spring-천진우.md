### 스프링과 스프링부트의 차이점이 있다면 설명하시오.

1. 설정의 자동화.
2. 빌드 & 배포: 자바
3. 기존 dependency에 대한 XML 설정을 auto configuration.

auto configuration?
dependency 를 적용하게 되면 해당 dependency의 설정파일이 있는데 이 설정파일을 자동으로 활성화. 또 설정파일 활성화 순서도 자동으로 설정해줌. 개발자가 정의한 @Component이 먼저 등록됨. 따로 등록하지 않으면 기본 설정이 자동으로 들어갔던듯.

### Spring Boot Starter란?

의존성의 버전을 스프링/자바에 적절하게 맞춰주고, dependency의 dependency의 버전 자동으로 맞춰줌.

spring-boot-starter-? 로 시작하는 애들은 해당 그룹에 대한 의존성들을 자동으로 추가하고 auto configuration에 의해 설정될 수 있게 설정을 제공한다!

### Gradle과 Maven에 대해 설명하시오.

빌드에 대한 설정을 명시한 파일. gradle은 groovy 플러그인을 지원하기 때문에, 동적인 요소에 대한 편리한 작성. 그리고 빌드 속도 개선

### Tomcat이란?
### Servlet이란?

서블릿 컨테이너를 지원하는 어플리케이션 서버.

여기서 서블릿 컨테이너란, 다양한 HTTP 요청에 대한 파싱과 동적인 대응을 할 수 있게 해주는 요소. 요청과 응답을 처리해주기 때문에 횡단 관심사에 대한 편의성을 제공.

서블릿은 HTTP 메시지를 파싱해서 HttpServeletRequest, HttpServeletResponse 에 담아준다.


### Spring에서는 둘을 어떻게 활용하는가?

원래 서블릿은 톰캣 같은 웹어플리케이션을 직접 띄우고, 그 위에 서블릿 코드를 클래스 파일로 빌드해서 넣어서 실행시켜야 하는데, 스프링부트는 내장톰캣이 있어서 이 과정을 직접 하지 않아도 됨.

@ServletComponentScan 어노테이션이 서블릿을 등록해줌.

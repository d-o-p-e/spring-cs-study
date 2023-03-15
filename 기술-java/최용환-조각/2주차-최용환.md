# 스터디 메모

### Java - 정의

1. Java의 특징에 대해 설명해주세요

[https://life-with-coding.tistory.com/430](https://life-with-coding.tistory.com/430)

1) 객체 지향 프로그래밍(OOP)

객체지향 프로그래밍 언어로 상속, 캡슐화, 다형성, 추상화를 지원

2) 자동 메모리 관리(gc)

C, C++와 다르게 Garbage Collecting을 하여 더 이상 사용하지 않는 메모리를 free 해줄 필요가 없다

3) 운영체제에 독립적

JVM(Java Virtual Machine)을 사용하여 운영체제와 상관없이 코드 재활용 가능

4) 멀티쓰레드 지원

멀티쓰레딩을 통해 효율적 시간분배 가능

5) 동적 로딩 지원

모든 클래스를 한번에 로딩하지 않고, 객체를 생성할 때 필요한 클래스만 메모리에 올라간다.

1. JVM의 역할에 대해 설명해주세요

[https://asfirstalways.tistory.com/158](https://asfirstalways.tistory.com/158)

- 컴파일된 바이트 코드를 기계가 이해할 수 있는 기계어로 변환
- 스택 기반의 가상 머신
- 메모리 관리와 GC를 수행

![Untitled](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/58953304-8a87-441b-a3f0-6efa4850636f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230315%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230315T013457Z&X-Amz-Expires=86400&X-Amz-Signature=f38e07a24684666840ee41d4b4e49b264aa8556ec3033cf79fec08e94785c549&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject)

**JVM 구성**

- Class Loader
    
    JVM 내로 클래드를 로스, 링크를 통해 배치하는 작업을 수행
    Runtime 때 동적으로 클래스를 로딩함.
    
    JAR파일의 클래스들을 JVM 위에 올린 다음 사용하지 않는 클래스는 메모리에서 삭제함 → 컴파일러 역할
    
- Execution Engine
    
    클래스를 실행시키는 역할
    클래스 로더가 JVM의 Runtime Data Area에 Bytecode를 배치하고, 실행 엔진에 의해 실행됨.
    
    Java Bytecode는 여기서 Java를 컴파일한 언어로서, 이를 JVM에서 사용하는 형태로 변경한 것이다. 이 변경과정을 Interpreter, 또는 JIT를 사용해서 진행한다.
    
- Interpreter
    
    Bytecode를 명령어 단위로 읽어서 실행한다. 일반적인 Interpreter와 동일하게 작용하며 따라서 속도도 느림
    
- JIT
    
    Interpretion을 하다가 적절한 시점부터 전체를 컴파일해서 네이티브코드 (JVM 외부에 맞는 코드)로 변경하고, 이후에는 Interpreting 없이 컴파일한 결과물로 직접 실행.
    네이티브 코드는 캐시에 보관해서 빠르게 수행이 되나, 컴파일 과정이 오래걸리기 때문에 한번만 실행되는 코드의 경우 컴파일 없이 Interpreting이 유리함.
    JIT 컴파일러를 사용하면 JVM은 내부적으로 메서드의 실행빈도를 체크해서 일정 수준 이상을 넘는 경우 Compilation을 진행한다.
    
- Garbage Collector
    
    사용하지 않는 메모리를 수거함
    
    ![Untitled](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/4e8ebea9-a865-440c-a167-70bc8e94cc4e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230315%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230315T013517Z&X-Amz-Expires=86400&X-Amz-Signature=59c5c48a2a6a76ab2914dc4e2ea1c608a8eff9f744ff07e87688e8c7078e469c&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22Untitled.png%22&x-id=GetObject)
    
- PC Register
    
    스레드의 시작에 생성되며 스레드당 하나씩 존재함. 어떤 부분을 어떤 명력으로 실행해야할지 매핑되어있으며, 현재 수행 중인 JVM 명령의 주소를 가지고 있음.
    
- JVM Stack
    
    프로그램 실행과정에서 임시로 할당되고 메소드를 나오면 소멸되는 데이터를 위한 영역.
    각종 변수, 임시 데이터, 스레드-메소드 정보를 저장함. 메소드마다 각각의 스택 프레임이 생성되며, 메소드 종료와 동시에 프레임이 삭제됨.
    
- Native Method Stack
    
    Java가 아닌 다른 언어로 작성된 코드가 컴파일/인터프리팅 되어 기계어로 작성되어 보관되는 공간. 여기는 별개로 스택을 잡아 독자적인 프로그램을 실행하는 영역이며, 여기서 C 프로그램을 실행시켜 커널에 접근할 수 있다.
    
- Method Area (a.k.a. Class area, Static area)
    
    클래스 정보를 메모리에 처음 올릴 때 초기화되는 대상을 저장하기 위한 메모리 공간. 프로그램의 흐름을 구성하는 바이트 코드가 올라간다. 그러나 Java 프로그램은 Main 메소드의 호출부터 시작해서 계속된 메소드의 호출을 흐름을 만들기 때문에, 바이트코드의 대부분이 메소드 바이트코드이기에 대부분의 바이트코드가 올라간다. Runtime Constant Pool이라는 별도의 관리 영역이 존재하는데, 여기는 상수 자료형을 저장해서 참조하고 중복을 막는다.
    
    - Field Information - 멤버변수의 이름, 데이터 타입, 접근 제어자에 대한 정보
    - Method Information - 메소드의 이름, 리턴타입, 매개변수, 접근제어자에 대한 정보
    - Type Information - Class인지 Interface 인지의 여부 저장 /Type의 속성, 전체 이름, super class의 전체 이름(interface, object 제외)
- Heap
    
    ![image](https://user-images.githubusercontent.com/51287461/225182092-8a55f56b-63e7-47e5-9b88-00ecfe66b2e9.png)
    

객체를 저장하는 가상 메모리 공간. new 연산자로 생성된 객체, 배열을 저장하며, Method Area에 올라간 클래스들만 객체로 생성 가능하며, 힙은 Permanent Generation, New(Young), Old 영역으로 나뉜다.

- Permanent Generation
    
    생성된 객체들의 정보의 주소값이 저장된 공간. Class, Method의 metadata가 저장되며 JVM이 사용한다. Relection을 사용하여 동적으로 클래스를 로딩하는 경우에 사용한다.
    
- New(Young)
    
    Eden : 객체들이 최초로 생성되는 공간
    
    Survivor : 0 / 1 : Eden에서 참조되는 객체들이 저장되는 공간
    
- Old
    
    New 영역에 일정 시간 참조된 살아남은 객체가 많아 Eden 영역이 가득차면, GC가 발생해서 Survivor 1로 복사해서 넣어주고 나머지를 영역을 삭제한다.
    

### Java - 오버라이딩/오버로딩

1. Overriding과 Overloading에 대해 설명해주세요
    - Overriding : 부모 클래스의 메소드 동작방법을 자식 클래스에서 새롭게 정의해서 덮는 것
    - Overloading : 같은 이름의 메소드를 Parameter, Return Type을 바꿔 중복으로 선언하는 것

### Java - 객체 지향

1. 객체지향 프로그래밍이란 무엇인지 설명해주세요
    
    [https://www.techtarget.com/searchapparchitecture/definition/object-oriented-programming-OOP](https://www.techtarget.com/searchapparchitecture/definition/object-oriented-programming-OOP)
    
    객체지향 프로그래밍이란 함수와 로직보다 데이터와 객체를 기반으로 디자인하는 방식이다. 여기서 객체란 자기만의 변수와 로직이 있는 데이터를 말한다.
    
    OOP는 데이터를 변경하는 로직보다 그 데이터 자체에 집중해서 크고 복잡하고, 유지보수가 잦은 프로그램에 사용하기 위해 구상되었다.
    
    OOP에서의 구조는 Class, Object, Method, Attribute으로 나눈다.
    
    - Class : Object, Method, Attribute의 청사진이 되는 데이터 타입이다.
    - Object : Class의 Instance로서, 각자 개별적으로 데이터를 보관하고 있다. Object는 실제 객체, 또는 추상적인 존재와 연결할 수 있다. Class가 처음 정의될 때 description이 존재하는 유일한 Object이다.
    - Method : Class 내의 함수로서, Object의 행동을 정의할 수 있다. Class에 기본적으로 정의한 Method들은 Class가 아닌 각 개체를 참조하고 있다.
    - Attributes : Class 내에서 정의되어 Object의 상태를 보관하는 데이터 필드이다. Class attribute은 Object가 아닌 Class 자체에 속한다
2. 객체지향 설계원칙에 대해 설명해주세요

[https://hckcksrl.medium.com/solid-원칙-182f04d0d2b#:~:text=객체지향 설계5대,따서 SOILD 원칙이라고 부른다](https://hckcksrl.medium.com/solid-%EC%9B%90%EC%B9%99-182f04d0d2b#:~:text=%EA%B0%9D%EC%B2%B4%EC%A7%80%ED%96%A5%20%EC%84%A4%EA%B3%845%EB%8C%80,%EB%94%B0%EC%84%9C%20SOILD%20%EC%9B%90%EC%B9%99%EC%9D%B4%EB%9D%BC%EA%B3%A0%20%EB%B6%80%EB%A5%B8%EB%8B%A4).

- Single Responsibility Principle
    
    모든 클래스는 하나의 책임만을 가져야 하며, 캡슐화를 통해 그 책임만을 져야 한다.
    
- Open Closed Principle
    
    기존의 코드를 수정하는 것이 아닌, 기능을 새로이 추가하기 쉬운 설계가 되어야 한다.
    
- Liskov Substitution Principle
    
    자식 클래스는 부모 클래스를 대체할 수 있어야 한다. 즉 부모 클래스의 자리에 자식 클래스를 넣어도 문제없이 작동해야 한다.
    
- Interface Segregation Principle
    
    클래스는 자신이 사용하지 않는 인터페이스는 구현하지 않아야 한다. 따라서 인터페이스를 여러개의 구체적인 인터페이스로 나누어 사용하는 것이 중요하다.
    
- Dependency Inversion Principle
    
    변화가 드문 것에 의존하라. 즉 인터페이스, 추상 클래스와의 관계를 권장한다.
    

### Java - 인터페이스/ 추상 클래스

1. 인터페이스와 추상 클래스의 정의에 대해 설명해주세요
    - 인터페이스 : 안이 비어있는 추상메소드들을 모아놓은 것이며 상속하는 클래스들에 대해 해당되는 메소드들의 내용 구현을 강제함. 인터페이스 변수는 무조건 static이어야 하며, 일반변수는 사용할 수 없다.
    - 추상 클래스 : 0개 이상의 추상 메소드를 가진, 실제 클래스의 공통적인 부분을 추출해 규격을 잡은 추상적인 클래스. abstract method로 parameter와 return type만 정의할 수도 있으며, 일반적인 메소드 또한 존재할 수 있으면 일반변수도 존재한다. 그러나 구현을 위해서는 클래스에서 extends를 통해 상속해야 한다.
2. 둘의 차이점에 대해 설명해주세요.
    
    인터페이스는 추상메소드만으로 이루어져 있어, 모든 메소드를 overriding 해야하는 반면, 추상 클래스는 구현이 되어있는 메소드 또한 포함되어 있어 추상메소드만 구현해도 문제없다. 그러나 추상클래스는 DDD의 문제로 인하여 다중상속이 불가능하며, 인터페이스는 추상메소드로만 이루어져 있기에 다중상속이 가능하다.
    

### Java - 클래스/객체/인스턴스

1. 클래스와 객체, 인스턴스에 대해 설명해주세요
    - Class : Object, Method, Attribute의 청사진이 되는 데이터 타입이다.
    - Object : Class의 Instance로서, 각자 개별적으로 데이터를 보관하고 있다. Object는 실제 객체, 또는 추상적인 존재와 연결할 수 있다. Class가 처음 정의될 때 description이 존재하는 유일한 Object이다.
    - Instance : 실제로 구현된 Object를 일컬음. 보통은 개념의 관점에서 보면 Object이고, 실제로 메모리에 올라가면 Instance로 본다.

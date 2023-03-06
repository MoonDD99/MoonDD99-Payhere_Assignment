## ❤️구현 완료

- 회원관리
    - 이메일과 비밀번호를 통해 **회원가입 가능**
        - 이미 가입된 이메일은 회원가입 불가
    - 회원가입 이후 **로그인**, **로그아웃** 가능
    - 로그인하지 않은 고객은 가계부 내역에 대한 접근 처리
        - JWT 토큰 발행해서 인증 제어
- 가계부
    - 가계부
        - 회원별로 여러개의 가계부를 가지고 있음
        - 가계부에는 여러개의 가계부 내역을 가지고 있음
        - 가계부는 `제목`과 `설명`과 함께 생성할 수 있음
        - **가계부 리스트 조회 가능**
    - 가계부 내역
        - **가계부에는** `사용한 금액 내역`**과** `메모`**를 함께 생성할 수 있음**
        - **수정할 시에는 금액과 메모를 수정할 수 있음**
        - **가계부 내역 삭제 가능**
        - **가계부 상세내역 조회 가능**
        - **가계부 내역 복제 가능**
        

### 🧡구현 미완료

- 공유 가능한 단축 URL 생성
- 테스트 코드

## 💛설계

### API Dodcs

[Postman Document](https://documenter.getpostman.com/view/10099049/2s93JowRLK) 

### ERD

![ERD](https://user-images.githubusercontent.com/57447658/223129478-773a3030-c7f5-4d3c-8302-0db1d226a4f0.png)


## 💚 그라운드 룰

### 1. Commit 규칙

**양식**

```
[말머리] 커밋 제목
>>
본문
```

**말머리**

- feat : 새로운 기능 추가
- refactor : 코드 리팩토링
- fix : 버그 수정
- test : 테스트 코드 작성
- docs : 문서
- chore : 환경설정 파일
- style : 코드 형식, 정렬, 린트 등의 변경

### 2. Pull Request 규칙

- PR 제목
    - `[말머리] 내용`
    
    **말머리**
    
    - feat : 새로운 기능 추가
    - refactor : 코드 리팩토링
    - fix : 버그 수정
    - test : 테스트 코드 작성
    - docs : 문서
    - chore : 환경설정 파일
    - style : 코드 형식, 정렬, 린트 등의 변경

### 3. Code 규칙

- Class명 : CamelCase
- 함수명 : snake_case
- 변수명 : snake_case

### 4. Branch 규칙

 main ← (develop | hotfix) ← (feat-account | feat- household | … )

- branch 종류
    - main : 배포용
    - develop : 배포전 모든 기능들 합치고 오류 확인
    - hotfix : 긴급 오류 해결
    - feat - {기능명} : 기능별 브랜치

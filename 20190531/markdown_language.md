마크다운 markdown 작성법
======================

# 1. 마크다운이란?
텍스트 기반의 마크업언어로 2004년 존그루버에 의해 만들어졌으며 쉽게 쓰고 읽을 수 있으며 HTML로 변환이 가능하다. 특수기호와 문자를 이용한 매우 간단한 구조의 문법을 사용하여 웹에서도 보다 빠르게 컨텐츠를 작성하고 보다 직관적으로 인식할 수 있다.

****
# 2. 마크다운 사용법(문법)
## 2.1. 헤더Headers
* 큰제목: 문서 제목
    ```
    This is an H1
    =============
    ```
    This is an H1
    =============

* 작은제목: 문서 부제목
    ```
    This is an H2
    -------------
    ```
    This is an H2
    -------------

* 글머리: 1~6까지만 지원
```
# This is a H1
## This is a H2
### This is a H3
#### This is a H4
##### This is a H5
###### This is a H6
```
# This is a H1
## This is a H2
### This is a H3
#### This is a H4
##### This is a H5
###### This is a H6
####### This is a 7.

## 2.2. BlockQuote
```>``` 블럭인용문자를 이용한다.
```
> This is a blockqute.
```
> This is a first blockqute.
>	> This is a second blockqute.
>	>	> This is a third blockqute.

다른 마크다운 요소를 포함할 수 있다.
> ### This is a H3
> * List
>	```
>	code
>	```

## 2.3. 목록
### ● 순서있는 목록(번호)
순서있는 목록은 숫자와 점을 사용한다.
```
1. 첫번째
2. 두번째
3. 세번째
```
1. 첫번째
2. 두번째
3. 세번째

### ● 순서없는 목록(글머리 기호)
```
* 빨강
  * 녹색
    * 파랑

+ 빨강
  + 녹색
    + 파랑

- 빨강
  - 녹색
    - 파랑
```
* 빨강
  * 녹색
    * 파랑

+ 빨강
  + 녹색
    + 파랑

- 빨강
  - 녹색
    - 파랑

혼합해서 사용하는 것도 가능
```
* 1단계
    - 2단계
    	+ 3단계
            = 4단계
```

* 1단계
    - 2단계
    	+ 3단계
			= 4단계

## 2.4. 코드```<pre><code></code></pre>```
4개의 공백 또는 하나의 탭으로 들여쓰기를 만나면 변환되기 시작하여 들여쓰지 않은 행을 만날때까지 변환이 계속된다.

> 한줄 띄어쓰면 인식이 제대로 안되는 문제가 발생하곤 합니다.

```
This is a normal paragraph:

    This is a code block.
end code block.
```

<code>
```
This is a normal paragraph:
    This is a code block.
end code block.
```
</code>

실제로 적용해보면,
This is a normal paragraph:

    This is a code block.
end code block.

## 2.5. 수평선```<hr/>```
페이지 나누는 용도로 많이 사용
```
* * *

***

*****

- - -

---------------------------------------
```

* * *

***

*****

- - -

---------------------------------------


## 2.6. 링크
* 참조링크

```
[link keyword][id]
[id]: URL "Optional Title here"

Link: [Google][googlelink]
[googlelink]: https://google.com "Go google"
```

Link: [Google][googlelink]
[googlelink]: https://google.com "Go google"

* 인라인 링크
```
syntax: [Title](link)
```
Link: [Google](https://google.com, "google link")

* 자동연결
```
<http://example.com/>
<address@example.com>
```

<http://example.com/>
<address@example.com>

## 2.7. 강조
```
*single asterisks*
_single underscores_
**double asterisks**
__double underscores__
++underline++
~~cancelline~~
```
*single asterisks*
_single underscores_
**double asterisks**
__double underscores__
++underline++
~~cancelline~~

## 2.8. 이미지
```
![Alt text](/path/to/img.jpg)
![Alt text](/path/to/img.jpg "Optional title")
```
![강아지](https://i.pinimg.com/originals/7d/93/b5/7d93b58056c9533337a1498a529d1a61.jpg)
![강아지](https://i.pinimg.com/originals/7d/93/b5/7d93b58056c9533337a1498a529d1a61.jpg "dog")

사이즈 조절 기능은 없기 때문에 ```<img width="" height=""></img>```를 이용한다.

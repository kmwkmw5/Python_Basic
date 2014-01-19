# -*- coding:utf-8 -*-
"""
4) 터플 (tuple)
터플 또는 튜플이라고 부른다.

터플이란 리스트와 몇 가지 점을 제외하곤 모든 것이 동일하다. 그 다른 점은 다음과 같다.

리스트는 [ 과 ] 으로 둘러싸지만 터플은 (과 )으로 둘러싼다.
리스트는 그 값을 생성, 삭제, 수정이 가능하지만 터플은 그 값을 변화시킬 수 없다.
터플은 다음과 같은 모습이다.

	>>> t1 = ()
	>>> t2 = (1,)
	>>> t3 = (1,2,3)
	>>> t4 = 1,2,3
	>>> t5 = ('a', 'b', ('ab', 'cd'))
리스트와 생김새가 거의 비슷하지만, 특이할 만한 점이라면
단지 한 개의 요소만을 갖는 터플은 t2 = (1,)처럼 한 개의 요소와 그 뒤에 콤마(',')를 넣어야 한다는 점과
네 번째 보기 t4 = 1, 2, 3 처럼 괄호()를 생략해도 무방하다는 점이다.

얼핏 보면 터플과 리스트는 비슷한 역할을 한다. 하지만 프로그래밍을 할 때 터플과 리스트는 구분해서 사용하는것이 유리하다.
터플과 리스트의 가장 큰 차이는 값을 변화시킬 수 있는 지 없는 지의 차이라고 했다.
리스트의 항목 값은 변화가 가능하고 터플의 항목 값은 변화가 불가능하다.
따라서 프로그램이 진행되는 동안 그 값이 항상 변하지 않기를 바란다면 또는 바뀔까 걱정하고 싶지 않다면
주저하지 말고 터플을 사용해야 할 것이다. 이와는 반대로 수시로 그 값을 변화시켜야 할 경우라면 리스트를 사용해야 한다.
실제 프로그램에서는 평균적으로 터플보다는 리스트를 훨씬 많이 쓰게 된다.
""""""
	터플의 인덱싱, 슬라이싱, 더하기와 반복
값을 변화시킬 수 없다는 점만 제외하면 리스트와 완전히 동일하므로 간단하게만 살펴 보기로 하자.
아래의 예제는 서로 연관 되어 있으므로 예1부터 차례대로 수행해 보기를 바란다.

예 1) 인덱싱

	>>> t1 = (1, 2, 'a', 'b')
	>>> t1[0]
	1
	>>> t1[3]
	'b'
	문자열, 리스트와 마찬가지로 t1[0], t1[3]처럼 인덱싱이 가능하다.

예 2) 슬라이싱

	>>> t1 = (1, 2, 'a', 'b')
	>>> t1[1:]
	(2, 'a', 'b')
	슬라이싱의 예이다.

예 3) 터플 더하기(합)

	>>> t2 = (3, 4)
	>>> t1 + t2
	(1, 2, 'a', 'b', 3, 4)
	터플을 합하는 방법을 보여준다.

예 4) 터플 곱(반복)

	>>> t2 * 3
	(3, 4, 3, 4, 3, 4)
	터플의 곱(반복)을 보여준다.
"""
t1 = (1, 2, 'a', 'b')
t2 = 3, 4
#1
print(t1[0])
print(t1[3])
#2
print(t1[1:])
#3
print(t1 + t2)
#4
print(t2 * 3)
print("")
"""
터플의 요소 값은 변경시킬 수 없다 터플의 요소값은 한 번 정하면 지우거나 변경할 수 없다.
다음에 소개하는 두 개의 예를 살펴보면 좀 더 이해가 쉬울 것이다.

예 1) 터플 요소 지우려고 할 때의 에러

>>> del t1[0]
Traceback (innermost last):
File "", line 1, in ?del t1[0]
TypeError: object doesn't support item deletion
터플의 요소를 리스트처럼 del 함수로 지우려고 한 예이다. 터플은 요소를 지우는 행위가 지원되지 않는다는 메시지를 확인 할 수 있다.

예 2) 터플 요소값 변경시 에러

>>> t1[0] = 'c'
Traceback (innermost last):
File "", line 1, in ?t1[0] = 'c'
TypeError: object doesn't support item assignment
터플의 요소 값을 변경하려고 해도 마찬가지로 에러가 발생하는 것을 확인할 수 있다.
"""
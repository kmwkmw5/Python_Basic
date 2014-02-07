#===============================================================================
# 제 14 장 연산자의 중복과 장식자
#===============================================================================

#===============================================================================
# 14.1 연산자의 중복
#===============================================================================

#===============================================================================
# 14.1.1 수치 연산자 중복
# 이항 연산자, 역 이항 연산자, 확장 산술 연산자, 단항 연산자, 기타 형변환
#===============================================================================

#------------------------------------------------------------------------------ 
'''
이항 연산자
역 이항 연산자는 앞에 r, 확장 산술 연산자는 앞에 i를 붙임
__add__			+
__sub__			-
__mul__			*
__truediv__		/
__floordiv__	//
__mod__			%
__divmod__		divmod()
__pow__			pow(), **		(self, other[, modulo])
__lshift__		<<
__rshift__		>>
__and__			&
__xor__			^
__or__			|

단항 연산자
__neg__			-
__pos__			+
__abs__			abs()
__invert__		~				비트 반전
'''

class MyStr:
	def __init__(self, s):
		self.s = s
	# 이항 연산자
	def __truediv__(self, other):
		return self.s.split(other)
	def __add__(self, other):
		return self.s + other
	# 역이항 연산자
	def __radd__(self, other):
		return other + self.s
	# 확장 산술 연산자
	def __iadd__(self, other):
		self.s = self.s + other
		return self

s1 = MyStr('a:b:c')
print(s1 / ':')
#['a', 'b', 'c']
print(s1 + ':d')
#a:b:c:d
print('z:' + s1)
#z:a:b:c
s1 += ':d'
print(s1.s)
#------------------------------------------------------------------------------ 

#------------------------------------------------------------------------------ 
'''
기타 형변환 416p
__complex__		complex()
__int__			int()
__float__		float()
__round__		round()
__index__		operator.index()	인덱스 값으로 사용될 때 호출
'''
class Index:
	def __index__(self):
		print('__index__ called')
		return 3
L = [1,2,3,4,5]
i = Index()
print(L[i])
#__index__ called
#4
print(bin(i))
#0b11
print(oct(i))
#0o3
print(hex(i))
#0x3
#------------------------------------------------------------------------------ 

#===============================================================================
# 14.1.2 컨테이너 자료형의 연산자 중복
#===============================================================================

#------------------------------------------------------------------------------ 
# 기본적으로 구현해야 하는 것들
#		__len__, __contains__, __getitem__, __setitem__, __delitem__
# 시퀀스형이면서 변경 가능한 자료형
#		append, count, index, extend, insert, pop, remove, reverse, sort
# 사전과 같은 매핑 자료형
#		keys, values, items, get, clear, copy, setdefault, pop, popitem, update
# 산술 연산
#		__add__, __radd__, __iadd__, __mul__, __rmul__, __imul__
# 반복자 지원
#		__iter__
#------------------------------------------------------------------------------ 

#===============================================================================
# 1 인덱싱
#===============================================================================

#------------------------------------------------------------------------------
# __getitem__() : s1[0]      : s1.__getitem__(0) 
# __setitem__() : s1[0] = 10 : s1.__setitem__(0, 10)
# __delitem__() : del s1[0]  : s1.__delitem__(0)
#------------------------------------------------------------------------------ 

#------------------------------------------------------------------------------ 
# __getitem__()의 구현과 예외처리(TypeError, IndexError)
class Square:
	def __init__(self, end):
		self.end = end
	def __len__(self):
		return self.end
	def __getitem__(self, k):
		if type(k) != int:
			raise TypeError('...')
		if k<0 or k>=self.end:
			raise IndexError('index {} out of range'.format(k))
		return k*k

s1 = Square(10)
print(len(s1))
#10
print(s1[4])
#16
#print(s1[20])
#IndexError: index 20 out of range
#print(s1['a'])
#TypeError: ...
#------------------------------------------------------------------------------ 

#------------------------------------------------------------------------------ 
# for문은 __getitem__() 메소드를 0부터 호출하기 시작한다.
for x in s1:
	print(x, end=' ')
print('')
#0 1 4 9 16 25 36 49 64 81 

# 다른 시퀀스 자료형으로 변환
print(list(s1))
#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(tuple(s1))
#(0, 1, 4, 9, 16, 25, 36, 49, 64, 81)
#------------------------------------------------------------------------------ 

#===============================================================================
# 2 슬라이싱
#===============================================================================

#------------------------------------------------------------------------------ 
# slice 객체 : slice([start,] stop [, step]) : [start:stop:step]

print(slice(1, 10, 2))
#slice(1, 10, 2) : [1:10:2]
print(slice(10))
#slice(None, 10, None) : [:10]
print(slice(1, None))
#slice(1, None, None) : [1:]

l = [1,2,3,4,5,6,7,8]
print(l[slice(1, None)])
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------ 
# __getitem__() : m[1:5] : m.__getitem(slice(1,5))
class Square2:
	def __init__(self, end):
		self.end = end
	def __len__(self):
		return self.end
	def __getitem__(self, k):
		if type(k) == slice:
			start = k.start or 0
			stop = k.stop or self.end
			step = k.step or 1
			return map(self.__getitem__, range(start, stop, step))
		elif type(k) == int:
			if k<0 or k>=self.end:
				raise IndexError('index {} out of range'.format(k))
			return k*k
		else:
			raise TypeError('...')
#------------------------------------------------------------------------------ 

#===============================================================================
# 3 매핑 자료형
#===============================================================================

#------------------------------------------------------------------------------ 
# __getitem__() : m['day']           : m.__getitem__('day')
# __setitem__() : m['day'] = 'light' : m.__setitem__('day', 'light')
#------------------------------------------------------------------------------ 

#===============================================================================
# 4. 반복자 지원(18.2절)
#===============================================================================

#===============================================================================
# 14.1.3 문자열 변환 연산
#===============================================================================

#===============================================================================
# 1 문자열로의 변환
#===============================================================================

#------------------------------------------------------------------------------ 
# __str__()  : print(), str()에 의해 호출 : 읽기 편한 형태
# __repr__() : repr()에 의해 호출         : 유일하게 표현할 수 있는 문자열 형태

# __str__()
print(str(2))
#2		(console)
#'2'	(shell)
print(str('2'))
#2
#'2'
print(str('abc'))
#abc
#'abc'
print(str([1,2,3]))
#[1, 2, 3]
#'[1, 2, 3]'

# __repr__()
print(repr(2))
#2
#'2'
print(repr('2'))
#'2'
#"'2'"
print(repr('abc'))
#'abc'
#"'abc'"
print(repr([1,2,3]))
#[1, 2, 3]
#'[1, 2, 3]'
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------ 
# 컨테이너 자료형 : __str__() 메소드가 __repr__() 메소드를 호출함.
# __str__() 메소드가 정의되어 있지 않으면 __repr__() 메소드가 호출됨.
# 반대로 __repr__() 메소드가 __str__() 메소드를 대신하지는 않음!!
#------------------------------------------------------------------------------ 

#===============================================================================
# 2 바이트로의 변환
# __bytes__() : bytes(b) : b.__bytes__()
#===============================================================================

#===============================================================================
# 3 서식 기호 새로 지정하기 : __format__()
#===============================================================================

#------------------------------------------------------------------------------ 
# __format__() : format() 함수나 문자열의 format() 메소드
# format(클래스, 변환형식)     : 클래스.__format__(변환형식)
# "{:변환형식}".format(클래스) : 클래스.__format__(변환형식)

class MyStr2:
	def __init__(self, s):
		self.s = s
	def __format__(self, fmt):
		print(fmt)				# 서식 문자열을 확인해 보기 위해 테스트 출력
		if fmt[0] == 'u':		# u : upper 사용자 지정 변환 기호
			s = self.s.upper()
			fmt = fmt[1:]
		elif fmt[0] == 'l':		# l : lower
			s = self.s.lower()
			fmt = fmt[1:]
		else:
			s = str(self.s)
		return s.__format__(fmt)
	
s = MyStr2('Hello')
print(format(s, 's'))
#s
#Hello
print('{0:s} {0:u^20} {0:l} {0:*^20}'.format(s))
#s
#u^20	# ^ : 가운데 정렬
#l
#*^20	# * : 채우기 문자
#Hello        HELLO         hello *******Hello********
#------------------------------------------------------------------------------ 

#===============================================================================
# 14.1.4 진리값과 비교 연산
#===============================================================================

#------------------------------------------------------------------------------ 
# __bool__() : 객체의 진리값 판별.
# 만약 정의되어 있지 않으면 __len__()을 호출 -> 0:False, 나머지 True
# 둘 다 정의되어 있지 않으면 모든 인스턴스는 True

# 비교 연산
# <		__lt__(self, other)
# <=	__le__(self, other)
# >		__gt__(self, other)
# >=	__ge__(self, other)
# ==	__eq__(self, other)
# !=	__ne__(self, other)		정의되이 있지 않으면 __eq__() 메소드의 반대 논리 적용
#------------------------------------------------------------------------------ 

#===============================================================================
# 14.1.5 해시 값에 접근하기 : __hash__()
#===============================================================================

#------------------------------------------------------------------------------ 
# __hash__() : hash(m) : m.__hash__()
# 클래스가 키로 사용될 때 그 키의 해시 값을 돌려주는 메소드
# 반드시 정수로 변환
# __eq__() 메소드도 함께 정의해야 함

class Obj:
	def __init__(self, a, b):
		self.a = a
		self.b = b
	def _key(self):
		return (self.a, self.b)
	def __eq__(self, o):
		return self._key() == o._key()
	def __hash__(self):
		return hash(self._key())
o1 = Obj(1, 2)
o2 = Obj(3, 4)
print(hash(o1))
#3713081631934410656
print(hash(o2))
#3713083796997400956
d = {o1:1}
print(d)
#{<__main__.Obj object at 0x10f41d0>: 1}

# 해시 키는 변경이 가능해서는 안 된다.
# 만약 변경 가능한 클래스라면 hash()를 호출 했을 때 TypeError를 발생시켜야 한다.
class Obj2:
	def __init__(self, a, b):
		self.a = a
		self.b = b
	def __hash__(self):
		raise TypeError('not proper type')
o1 = Obj2(1, 2)
#d = {o1:1}
#TypeError: not proper type
#------------------------------------------------------------------------------ 

#===============================================================================
# 14.1.6 속성 값에 접근하기
#===============================================================================

#------------------------------------------------------------------------------ 
# __getattr__() : 이름 공간에 정의되지 않은 이름에 접근할 때 호출 및 처리
# __getattribute__() : 모든 속성에 접근하면 호출

# 객체.속성 : getattr(객체, '속성')      : __getattribute__('속성')이 호출됨
# object.__getattribute__(객체, '속성') : 객체의 속성만 가져옴(__getattribute__호출 안함)

# 직접 호출하지 않음(재귀적으로 계속 호출) -> object.__getattribute__(객체, '속성')

# 두 메소드를 같이 정의하면?
# __getattribute__를 먼저 호출하고 예외가 발생하면 __getattr__을 호출한다.

class GetAttr3:						# class GetAttr3(object):
	def __getattr__(self, x):
		print('__getattr__', x)
		raise AttributeError
	def __getattribute__(self, x):
		print('__getattribute__', x)
		return object.__getattribute__(self, x)
g3 = GetAttr3()
g3.c = 10
print(g3.c)
#__getattribute__ c
#10
#print(g3.a)
#__getattribute__ a		# return문에서 AttributeError 발생
#__getattr__ a
#AttributeError
#------------------------------------------------------------------------------ 

#------------------------------------------------------------------------------ 
# __setattr__()
# 객체.속성 = 값 : setattr(객체, '속성', 값) : 객체.__setattr__('속성', 값)

# __delattr__()
# del 객체.속성 : delattr(객체, '속성') : 객체.__delattr__('속성')

class Attr:
	def __setattr__(self, name, value):
		print("__setattr__('%s')=%s called" % (name, value))
		object.__setattr__(self, name, value)
	def __delattr__(self, name):
		print("__delattr__('%s') called" % (name))
		object.__delattr__(self, name)
a = Attr()
a.x = 10
#__setattr__('x')=10 called
print(a.x)
#10
del a.x
#__delattr__('x') called
#------------------------------------------------------------------------------ 

#===============================================================================
# 14.1.7 인스턴스 객체 호출하기 : __call__()
#===============================================================================

#------------------------------------------------------------------------------ 
# __call__() 메소드가 있으면 그 클래스의 인스턴스는 함수처럼 사용할 수 있다.
class Factorial:
	def __init__(self):
		self.cache = {}
	def __call__(self, n):
		if n not in self.cache:
			if n==0:
				self.cache[n] = 1
			else:
				self.cache[n] = n * self.__call__(n-1)
		return self.cache[n]
fact = Factorial()
for i in range(10):
	print(fact(i))

# 호출 가능한지 확인하기 : collections.Callable
import collections
print(isinstance(fact, collections.Callable))
#True
#------------------------------------------------------------------------------ 

#===============================================================================
# 14.1.8 인스턴스 객체 생성하기 : __new__()
#===============================================================================

#------------------------------------------------------------------------------ 
# 싱글톤(Singleton)에서 활용
# 정적 메소드, 객체의 생성을 제어함

# 일반 예제
class NewTest:
	def __new__(cls, *args, **kw):
		print("__new__ called", cls)
		instance = object.__new__(cls)
		return instance
	def __init__(self, *args, **kw):
		print("__init__ called", self)
t = NewTest()
#__new__ called <class '__main__.NewTest'>
#__init__ called <__main__.NewTest object at 0x25b51d0>

# 싱글톤 예제
class Singleton:
	__instance = None
	def __new__(cls, *args, **kw):
		if cls.__instance is None:
			cls.__instance = object.__new__(cls)
		return cls.__instance
class Sub(Singleton):
	pass
s1 = Sub()
s2 = Sub()
print(s1 is s2)
#True
#------------------------------------------------------------------------------ 

#===============================================================================
# 14.1.9 with 문 구현하기
#===============================================================================

#------------------------------------------------------------------------------ 
# __enter__(), __exit__()
# __enter__()에서 리턴값 -> as 변수명에 치환

# 임계 영역(Critical Section)을 구현하는 예제
import threading
class Locked:
	def __init__(self, lock):
		self.lock = lock
	def __enter__(self):
		print('__enter__', self)
		self.lock.acquire()
	def __exit__(self, type, value, tb):
		print('__exit__', self)
		self.lock.release()
lock = threading.Lock()
with Locked(lock):
	print('I am in C.S.')
#__enter__ <__main__.Locked object at 0x2603dd0>
#I am in C.S.
#__exit__ <__main__.Locked object at 0x2603dd0>

# 장식자와 생성자를 이용한 문맥 관리 객체를 구현하는 예제(위와 동일한 예제)
from contextlib import contextmanager
import threading

@contextmanager
def Locked2(lock):
	lock.acquire()
	yield lock
	lock.release()

lock = threading.Lock()
with Locked2(lock):
	print('I am in C.S.')
#I am in C.S.
#------------------------------------------------------------------------------ 
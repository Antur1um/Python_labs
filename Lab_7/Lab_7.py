# Task_1

class BigBell():
    x = True

    def sound(self):
        if self.x:
            print('ding')
            self.x = not self.x
        else:
            print('dong')
            self.x = not self.x


bell = BigBell()
bell.sound()
bell.sound()
bell.sound()
bell.sound()
bell.sound()


# Task_2
class Balance:
    right = 0
    left = 0

    def add_left(self, n):
        self.left += n

    def add_right(self, n):
        self.right += n

    def result(self):
        if self.left > self.right:
            return ' L '
        elif self.left < self.right:
            return ' R '
        else:
            return ' = '


balance = Balance()
# ball = Balance()
print(balance.result())
balance.add_right(10)
balance.add_left(2)
print(balance.result())
balance.add_left(10)
balance.add_right(1)
print(balance.result())


# print(ball.left, ball.right, end=' ')


# Task_3

class Selector:
    def __init__(self, l):
        self.f = l

    def get_odds(self):
        return [i for i in self.f if i % 2 > 0]

    def get_evens(self):
        return [i for i in self.f if i % 2 == 0]


values = [11, 12, 13, 15, 64, 32, 1, 3, 7]
selector = Selector(values)
odds = selector.get_odds()
evens = selector.get_evens()
print(odds)
print(evens)


# Task_4
class Point:
    def __init__(self, x1, y1):
        self.x = x1
        self.y = y1

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.x != other.x or self.y != other.y:
            return True
        else:
            return False


p1 = Point(0, 0)
p2 = Point(0, 1)

if p1 != p2:
    print("Not equal True")
else:
    print("Equal False")


# Task_5
class ReversedList:
    f = []

    def __init__(self, t):
        self.f = list(reversed(t))

    def __getitem__(self, key):
        return self.f[key]

    def __len__(self):
        return len(self.f)


r1 = ReversedList([1, 2, 3])
print(r1.f)
# print(r1[0])
for i in range(len(r1)):
    print(r1[i])


# Task_6
class SparseArray:
    def __init__(self):
        self.f = {}

    def __getitem__(self, key):
        return self.f.get(key, 0)

    def __setitem__(self, key, value):
        self.f[key] = value

a = SparseArray()
a[3] = 3
a[12] = 12
print([a[i] for i in range(20)])








#Task_7
class Polynomial:
    def __init__(self, c):
        self.data = c

    def __call__(self, x):
        return sum([self.data[i] * x ** i for i in range(len(self.data))])

    def __add__(self, other):
        a = self.data
        b = other.data
        if len(a) < len(b):
            a += [0] * (len(b) - len(a))
        else:
            b += [0] * (len(a) - len(b))
        return Polynomial([a[i] + b[i] for i in range(len(a))])


poly = Polynomial([10])
poly1 = poly + poly
print(poly1(1))

poly = Polynomial([10, -1])
print(poly(0))
print(poly(1))
print(poly(2))
print()
poly2 = Polynomial([0, 0, 1])
print(poly2(-2))
print(poly2(-1))
print(poly2(0))
print(poly2(1))
print(poly2(2))
print()
poly3 = Polynomial([0, 0, 2])
print(poly3(-2))
print(poly3(-1))
print(poly3(0))
print(poly3(1))
print(poly3(2))
print()
poly4 = poly2 + poly3
print(poly4(-2))
print(poly4(-1))
print(poly4(0))
print(poly4(1))
print(poly4(2))


class Polynomial:
    def __init__(self, koef):
        self.koef = koef

    def __call__(self, x):
        s = 0
        for i in range(len(self.koef)):
            s += self.koef[i] * pow(x, i)
        return s

    def __add__(self, other):
        st = []
        k = Polynomial(st)
        if len(self.koef) < len(other.koef):
            m = len(self.koef)
        else:
            m = len(other.koef)
        for i in range(m):
            st.append(self.koef[i] + other.koef[i])
        if len(self.koef) > m:
            st += self.koef[m::]
        else:
            st += other.koef[m::]
        k.koef = st
        return k

poly = Polynomial([10])
poly1 = poly + poly
print(poly1(1))


#Task_8
class Queue:
    def __init__(self, q):
        self.data = q

    def __add__(self, other):
        self.data.append(other)

    def __copy__(self):
        return Queue(self.data)

    def __








#Task_9
class Triangle:
    def __init__(self, a, b, c):
        self.side_a = a
        self.side_b = b
        self.side_c = c

    def perimetr(self):
        return self.side_a + self.side_b + self.side_c

class EquilateralTriangle(Triangle):
    def __init__(self, side):
        super().__init__(side, side, side)


tri = Triangle(12, 10, 15)
eq = EquilateralTriangle(15)
print(tri.perimetr())
print(eq.perimetr())


#Task_10
class Summator:
    def transform(self, n):
        return n

    def Sum(self, N):
        return sum(self.transform(i) for i in range(N + 1) )

class SquareSummator(Summator):
    def transform(self, n):
        return n ** 2

class CubeSummator(Summator):
    def transform(self, n):
        return n ** 3

s = Summator()
print(s.Sum(5))
s = SquareSummator()
print(s.Sum(3))
s = CubeSummator()
print(s.Sum(3))

#Task_11
class Summator:
    def transform(self, n):
        return n

    def Sum(self, N):
        return sum(self.transform(i) for i in range(N + 1))

class PowerSummator(Summator):
    def __init__(self, n):
        self.p = n

    def transform(self, n):
        return n ** self.p

class SquareSummator(PowerSummator):
    def __init__(self):
        super().__init__(2)

class CubeSummator(PowerSummator):
    def __init__(self):
        super().__init__(3)



s = PowerSummator(2)
print(s.Sum(3))
s = SquareSummator()
print(s.Sum(5))
s = CubeSummator()
print(s.Sum(3))

#Task_12

class A:
    def __str__(self):
        return 'A.__str__method'

    def hello(self):
        print("Hello")

class B:
    def __str__(self):
        return 'B.__str__method'

    def good_evening(self):
        print('Good evening')

class C(A,B):
    pass



class D(B, A):
    pass




def new_method(arg):
    return "new method"

def new_method2(arg):
    return "new method 2"


c = C()
c.hello()
c.good_evening()
d = D()
d.hello()
d.good_evening()
print(c)
print(d)








A.__str__ = new_method
B.__str__ = new_method2
c = C()
c.hello()
c.good_evening()
d = D()
d.hello()
d.good_evening()
print(isinstance(c,A), isinstance(c, B))
print(isinstance(d,A), isinstance(d, B))
print(c)
print(d)


#Task_14
class MailClient:
    def __init__(self, s, u):
        self.user = u
        self.server = s


    def send_mail(self, server1, user1, message):
        server1.get_mail(message, user1)

    def recive_mail(self):
        return self.server.sent_to_client(self.user)


class MailServer:
    def __init__(self, n):
        self.name = n
        self.vault = {}

    def get_mail(self, message, client):
        self.vault.fromkeys([client], message)

    def sent_to_client(self, user):
        self.vault.pop(user)


server = MailServer("myserver")
client = MailClient(server, "User1")
client2 = MailClient(server, "User2")

client.send_mail(server, "User2", "Hello there")

print(client2.recive_mail())




#Task_15




























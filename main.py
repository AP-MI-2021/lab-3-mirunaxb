# 1. Citire date

def citirea():
    n = int(input("Introduceti n="))
    list = []
    for i in range(0, n):
        el = int(input("a=[{}]=".format(i + 1)))
        list.append(el)
    k = int(input("Introduceti k="))
    return get_longest_div_k(list, k)

def citireb():
    n = int(input("Introduceti n="))
    lst = []
    for i in range(0, n):
        el = int(input("a=[{}]=".format(i + 1)))
        lst.append(el)
    return get_longest_same_div_count(lst)

def citirec():
    n = int(input("Introduceti n="))
    lst = []
    for i in range(0, n):
        el = int(input("a=[{}]=".format(i + 1)))
        lst.append(el)
    return get_longest_all_palindromes(lst)

# 2. Lungime max proprietatea 1

'''
Toate numerele sunt divizibile cu k (citit).
'''
def nr_div_k(n , k):
    '''
    Verificam ca nr sa fie divizbil cu k
    :param n: nr intreg
    :return: True daca nr e divizibil cu k, False altfel
    '''
    return n % k == 0

def test_nr_div_k():
    assert nr_div_k(130 , 10) == True
    assert nr_div_k(13 , 3) == False


def list_elem_div_k(list , k):
    '''
    Verificam ca lista are doar elemente cu propr. div k.
    :param lista: lista de nr intregi
    :return: True daca lista are are doar elem div k, False altfel
    '''
    for x in list:
        if not nr_div_k(x , k):
            return False
    return True

def test_list_elem_div_k():
    assert list_elem_div_k([] , 1) == True
    assert list_elem_div_k([10, 30, 50] , 10) == True
    assert list_elem_div_k([10, 3, 50] , 9) == False
    assert list_elem_div_k([1, 3, 5] , 2) == False


def get_longest_div_k(list , k):
    '''
    Determinarea secventei de lungime maxima a numerelor divizibile cu k.
    :param lista: lista de nr. intregi
    :param k: numar intreg
    :return: (nr intreg) lungimea maxima de multipli ai lui k din lista citita
    '''
    rez = []
    lung_lista = len(list)
    for i in range(lung_lista):
        for j in range(i, lung_lista):
            list_de_verificat = list[i:j + 1]
            if list_elem_div_k(list_de_verificat , k) and len(list_de_verificat) > len(rez):
                rez = list_de_verificat[:]
    return rez

def test_get_longest_div_k():
    assert get_longest_div_k([] , 3) == []
    assert get_longest_div_k([3,4,16,24,32,51,60,99,100] , 2) == [4,16,24,32]

# 3. Lungime max proprietatea 2

'''
Toate au numerele același număr de divizori.
'''
def nr_div(n , m):
    '''
    Verifica cati divizori are n
    :param n: nr intreg
    :return: True daca nr sunt in pa, False altfel
    '''
    t = 0
    nr = 0
    for i in range(1,n):
        if n%i == 0:
            t = t+1
    for j in range(1,m):
        if m%j == 0:
            nr = nr+1
    if t == nr:
        return True
    return False

def test_nr_div():
    assert nr_div(3 , 13) == True
    assert nr_div(12 , 13) == False

def list_elem_nr_div(lst):
    '''
    Verifica daca lista are doar elem cu proprietatea data
    :param lst: lista de nr intregi
    :return: True daca verifica, False altfel
    '''
    for x in lst:
        for y in lst[1:]:
            if not nr_div(x , y):
                return False
    return True

def test_list_elem_nr_div():
    assert list_elem_nr_div([3, 13, 17]) == True
    assert list_elem_nr_div([12, 24, 27]) == False

def get_longest_same_div_count(lst):
    '''
    Determinarea secventei de lungime maxima a numerelor cu acelasi nr de divizori.
    :param lista: lista de nr. intregi
    :return: (nr intreg) lungimea maxima de elemente care verifica proprietatea
    '''
    rez = []
    lung_lista = len(lst)
    for i in range(lung_lista):
        for j in range(i, lung_lista):
            list_de_verificat = lst[i:j + 1]
            if list_elem_nr_div(list_de_verificat) and len(list_de_verificat) > len(rez):
                rez = list_de_verificat[:]
    return rez

def test_get_longest_same_div_count():
    assert get_longest_same_div_count([]) == []
    assert get_longest_same_div_count([3, 13, 17, 24, 29]) == [3, 13, 17]

'''
Toate numerele sunt nr. palindrom.
'''
def nr_pal(n):
    '''
    Verifica daca numarul este palindrom
    :param n: nr. intreg
    :return: True daca verifica, False altfel
    '''
    og = 0
    c = n
    while n:
        og = og * 10 + n % 10
        n = n // 10
    if not c == og:
        return False
    return True

def test_nr_pal():
    assert nr_pal(131) == True
    assert nr_pal(231) == False

def list_elem_pal(lst):
    '''
    Verifica daca lista are doar elemente palindrom.
    :param lst: lista de nr intregi
    :return: True daca verifica, False altfel
    '''
    for x in lst:
        if not nr_pal(x):
            return False
    return True

def test_list_elem_pal():
    assert list_elem_pal([131 , 22 , 474]) == True
    assert list_elem_pal([27 , 89]) == False

def get_longest_all_palindromes(lst):
    '''
    Determinarea secventiei de lungime maxima a numerelor care sunt palindrom
    :param lst: lista de nr. intregi
    :return: lungimea maxima a secventei de numere palindorm
    '''
    rez = []
    lung_lista = len(lst)
    for i in range(lung_lista):
        for j in range(i, lung_lista):
            list_de_verificat = lst[i:j + 1]
            if list_elem_pal(list_de_verificat) and len(list_de_verificat) > len(rez):
                rez = list_de_verificat[:]
    return rez

def test_get_longest_all_palindromes():
    assert get_longest_all_palindromes([]) == []
    assert get_longest_all_palindromes([12 , 242 , 676]) == [242 , 676]
    assert get_longest_all_palindromes([19 , 24 , 737]) == [737]

def teste():
    test_nr_div_k()
    test_list_elem_div_k()
    test_get_longest_div_k()
    test_nr_div()
    test_list_elem_nr_div()
    test_get_longest_same_div_count()
    test_nr_pal()
    test_list_elem_pal()
    test_get_longest_all_palindromes()
teste()

# 4. Iesire (din meniu)

def main():
    while True:
        print('''
        	    1. (Nr6.) Longest div k
        	    2. (Nr12.) Longest same div count
        	    3. (Nr5.) Longest all palindromes
        	''')
        x = int(input("Comanda:"))
        if (x == 1):
            # Toate nr divizibile cu k
            print(citirea())
        if (x == 2):
            # Nr au acelasi număr de divizori.
            print(citireb())
        if (x == 3):
            # Nr sunt palindrom
            print(citirec())
        if(x == 0):
            # Comanda stop program
            print("Comanda inexistenta")
            return
if __name__ == '__main__':
    main()

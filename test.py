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
test_nr_pal()

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
test_list_elem_pal()

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
    assert get_longest_all_palindromes([22 , 44 ]) == [22 , 44]
test_get_longest_all_palindromes()
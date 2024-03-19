from string_utils import StringUtils
import pytest

@pytest.mark.parametrize('st, result',[
    ('capitalize','Capitalize'),
    ('Capitalize','Capitalize'),
    ('капитализация','Капитализация'),
    ('capitalize несколько слов','Capitalize несколько слов'),
    ('',''), #негативный
    (' ', ' '), #негативный
    ])
def test_cap(st, result):
    s = StringUtils()
    res = s.capitilize(st)
    assert res == result

@pytest.mark.parametrize('st, result',[
    (' trim','trim'),
    ('  Обработка', 'Обработка'),
    ('    trim some разные языки вконце пробел ','trim some разные языки вконце пробел '),
    ('',''), #негативный
    (' ', '') #негативный
    ])
def test_trim(st, result):
    s = StringUtils()
    res = s.trim(st)
    assert res == result

@pytest.mark.parametrize('st, dl, result',[
    ('1:2:3:4:5', ':', ['1', '2', '3', '4', '5']),
    ('1,2,c,d', ',', ['1', '2', 'c', 'd']),
    ('z!д!@!3!/', '!', ['z', 'д', '@', '3', '/']),
    ('1a1a1a1', 'a', ['1', '1', '1','1']),
    ('a111a111a111a', '111', ['a', 'a', 'a', 'a']),
    ('', '', []) #негативный
    ])
def test_list(st, dl, result):
    s = StringUtils()
    res = s.to_list(st, dl)
    assert res == result

@pytest.mark.parametrize('st, sm, result', [
    ('String', 'S', True),
    ('String', 's', False),
    ('string', 'g', True),
    ('','', True), #негативный
    ('', ' ', False), #негативный
    (' ', ' ', True) #негативный
    ])
def test_cont(st, sm, result):
    s = StringUtils()
    res = s.contains(st, sm)
    assert res == result 

@pytest.mark.parametrize('st, sm, result', [
    ('SkyPro', 'k', 'SyPro'),
    ('SkyPro', 'Pro', 'Sky'),
    ('Sky Pro', ' ', 'SkyPro'),
    ('SkyPro', 's', 'SkyPro'),
    ('','',''), #негативный
    (' ','', ' '), #негативный
    (' ',' ','') #негативный
    ])
def test_delete_sym(st, sm, result):
    s = StringUtils()
    res = s.delete_symbol(st, sm)
    assert res == result

@pytest.mark.parametrize('st, sm, result', [
    ('SkyPro', 'S', True),
    ('SkyPro', 'P', False),
    ('SkyPro', 's', False),
    (' SkyPro', ' ', True),
    ('','', True),
    (' ',' ', True),
    (' ','', False),
    ('',' ', False)
    ])
def test_starts(st, sm, result):
    s = StringUtils()
    res = s.starts_with(st, sm) 
    assert res == result

@pytest.mark.parametrize('st, sm, result', [
    ('SkyPro', 'o', True),
    ('SkyPro', 'S', False),
    ('','', True), #негативный
    (' ',' ', True), #негативный
    ('', ' ', False), #негативный
    (' ', '', False) #негативный
    ])
def test_end_w(st, sm, result):
    s = StringUtils()
    res =s.end_with(st, sm)
    assert res == result

@pytest.mark.parametrize('st, result', [
    ('', True),
    (' ', True),
    ('SkyPro', False),
    (' скай ', False)
    ])
def test_empty(st, result):
    s = StringUtils()
    res = s.is_empty(st)
    assert res == result

@pytest.mark.parametrize('lst, j, result', [
    ([1,2,3,4], ', ', '1, 2, 3, 4'),
    (['Sky', 'Pro'], '', 'SkyPro'),
    (['Sky', 'Pro', 1], '/', 'Sky/Pro/1'),
    (['',''], '', ''), #негативный
    ([' ',' '], ' ', '   '), #негативный
    (['',''], ' ', ' ') #негативный 
    ])
def test_l_to_s(lst, j, result):
    s = StringUtils()
    res = s. list_to_string(lst, j)
    assert res == result

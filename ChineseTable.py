import re
import botpy

LU_B = '┏'
RU_B = '┓'
LD_B = '┗'
RD_B = '┛'
H_B = '━'
V_B = '┃'
TL_B = '┣'
TR_B = '┫'
BD_B = '┻'
BU_B = '┳'
T_B = '╋'

def setStyle(style: str) -> None: # type: ignore
    """
    设置表格样式
    =
    
    Args:
        style (str): 样式，可填写thin, double, bold

    Returns:
        None
    """
    global LU_B,RU_B,LD_B,RD_B,H_B,V_B,TL_B,TR_B,BD_B,BU_B,T_B
    if style == 'thin':
        LU_B = '┌'
        RU_B = '┐'
        LD_B = '└'
        RD_B = '┘'
        H_B = '─'
        V_B = '│'
        TL_B = '├'
        TR_B = '┤'
        BD_B = '┴'
        BU_B = '┬'
        T_B = '┼'
    elif style == 'double':
        LU_B = '╔'
        RU_B = '╗'
        LD_B = '╚'
        RD_B = '╝'
        H_B = '═'
        V_B = '║'
        TL_B = '╠'
        TR_B = '╣'
        BD_B = '╩'
        BU_B = '╦'
        T_B = '╬'
    elif style == 'bold':
        LU_B = '┏'
        RU_B = '┓'
        LD_B = '┗'
        RD_B = '┛'
        H_B = '━'
        V_B = '┃'
        TL_B = '┣'
        TR_B = '┫'
        BD_B = '┻'
        BU_B = '┳'
        T_B = '╋'
    else:
        raise ValueError('style must be (thin, double or bold)')

def _betterLen(s):
    c = 0
    for i in s:
        if bool(re.match(r'[\u4e00-\u9fa5]', i)):
            c += 2
        else:
            c += 1
    return c

def ljust(s, length, fillchar=' '):
    c = _betterLen(s)
    if c < length:
        return s + fillchar * (length - c)
    return s



class Raw:
    '''
    横行
    =
    Args:
        contents (list[str]): 横行内容
    Returns:
        None
    '''
    def __init__(self, contents: list):
        self.contents = contents
        self.max = max([_betterLen(i) for i in contents])

class Table:
    '''
    表格类
    =
    
    Args:
        raws (list[Raw1, Raw2, ...]): 表格内容
    
    Returns:
        None
    
    如何使用表格类?
    =
    直接使用Table类即可，例如:
        print(Table([Raw(['a', 'b', 'c']), Raw(['d', 'e', 'f'])]))

    结果:
        ╔═╦═╦═╗
        ║a║b║c║
        ╠═╬═╬═╣
        ║d║e║f║
        ╚═╩═╩═╝
        (提示页面可能无法正常显示)
    '''
    def __init__(self, raws: list[Raw]): # type: ignore
        self.max = max([i.max for i in raws])
        self.raws = []
        for th in raws:
            rawC = []
            for td in th.contents:
                td: str
                rawC.append(ljust(td,self.max))
            self.raws.append(rawC)
        
        txt = LU_B
        txt += ((H_B * self.max+ BU_B) * (len(raws)- 1))[:-1] + RU_B +'\n'

        for raw in self.raws:
            for td in raw:
                txt += V_B + td
            txt = txt + V_B + '\n'
            txt2 = txt
            txt += TL_B + ((H_B * self.max+ T_B) * (len(raws)- 1))[:-1] + TR_B +'\n'
        
        txt = txt2

        txt += LD_B + ((H_B * self.max+ BD_B) * (len(raws)- 1))[:-1] + RD_B +'\n'
        
        self.txt = txt

    def __str__(self):
        return self.txt

if __name__ == '__main__':
    table = Table([
    Raw(['Name', 'Age', 'City']),
    Raw(['Alice', '30', 'New York']),
    Raw(['Bob', '25', 'San Francisco']),
    Raw(['Charlie', '35', 'Los Angeles'])
    ])
    print(table)
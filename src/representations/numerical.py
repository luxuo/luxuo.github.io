
# natural number compression representation
def nncr(num: int, one:str ='1', zero: str ='0'):
    count = num * (-1 if num < 0 else 1)
    return one * count + (zero * count if num < 0 else '')

# basic decimal number compression representation
# multiplie le chiffre à la précision décimale, le convertit en nombre naturel, et effectue nncr
def bdncr(num: float, precision_expo:int, one:str = '1', zero: str='0'):
    num_int = int(num * 10 ** precision_expo)
    return nncr(num=num_int, one=one, zero=zero)
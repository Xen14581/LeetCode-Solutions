class Solution:
    def intToRoman(self, num: int) -> str:
        d = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX',
         10: 'X', 40: 'XL', 50: 'L', 90: 'XC',
         100: 'C', 400: 'CD', 500: 'D', 900: 'CM',
         1000: 'M'}

        o = ''
        u = num % 10
        te = (num - u) % 100
        h = (num - te - u) % 1000
        th = num - h - te - u

        te = int(te/10)
        h = int(h/100)
        th = int(th/1000)

        if th > 0:
            o += d[1000]*th

        if h == 9:
            o += d[900]
        elif h >= 5:
            o += d[500] + d[100]*(h-5)
        elif h == 4:
            o += d[400]
        elif h < 4:
            o += d[100]*h

        if te == 9:
            o += d[90]
        elif te >= 5:
            o += d[50] + d[10]*(te-5)
        elif te == 4:
            o += d[40]
        elif te < 4:
            o += d[10]*te

        if u == 9:
            o += d[9]
        elif u >= 5:
            o += d[5] + d[1]*(u-5)
        elif u == 4:
            o += d[4]
        elif u < 4:
            o += d[1]*u

        return o

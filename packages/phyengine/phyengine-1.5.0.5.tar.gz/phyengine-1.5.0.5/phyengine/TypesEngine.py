class LongInt:
    def __init__(self, value: str):
        self.value = str(value)

    def __str__(self):
        return self.value

    def __add__(self, other):
        val1, val2 = self.value[::-1], other.value[::-1]
        if val1 < val2:
            val1, val2 = val2, val1
        res = ""
        extra = 0
        for i in range(len(val1)):
            digit = 0
            if i <= len(val2) - 1:
                digit = int(val1[i]) + int(val2[i]) + extra
            else:
                digit = int(val1[i]) + extra
            extra = int((digit - digit % 10) / 10)
            res += str(digit % 10)
        return LongInt(res)

if __name__ == '__main__':
    print(LongInt("123456781234567812345678") + LongInt("876543218765432187654321"))
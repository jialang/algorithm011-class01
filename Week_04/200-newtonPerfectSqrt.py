    def isPerfectSquare(self, num):
        if num == 1:
            return True
        r = num
        while r * r > num:
            r = (r+num/r) // 2
        return (r*r == num)

class Isbn13():
    def csum(isbn):
        array = list()

        for i in list(isbn):
            if str(i).isnumeric():
                array.append(int(i))

        if(len(array) == 13):
            for i in range(0, 12):
                if(i%2 != 0):
                    array[i] *= 3
                elif(i%2 == 0):
                    array[i] *= 1
        else:
            return "Input must contain 13 digits!"
        
        s = sum(array[:12])

        r = s%10

        if(r == 0):
            s = 0
        else:
            s = 10-r
        
        if(s == array[12]):
            return s
        else:
            return False
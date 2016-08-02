class Unpacking:

    def unpack(self):

        p = (4,5)
        x,y = p
        print("%s, %s" % (x, y))

        p = ['foo', 'bar', 123, (2016,8,2)]
        a,b,c,d = p
        #if number of unpack item is not correct is will give ValueError
        print("%s,%s,%d,%d,%d,%d" % (a,b,c,d[0],d[1],d[2]))

        """
            unpack a string
        """
        p = 'Hello'
        a,b,c,d,e = p
        print(a)


        """
            disgard vaiable with _
        """
        p = ['foo', 'bar', 123, (2016,8,2)]
        _,b,c,_ = p
        print(b) #print _ return nothing

        """
            Using *
        """

        p = ['foo', 'bar', '234234213434', '3421342341324']
        a,c,*num=p
        print(a)
        print(*num)


        """
         unpacking dictionary
        """

        records = [
            ('foo', 1, 2),
            ('bar', 'hello'),
            ('foo', 3, 4),
        ]

        def do_foo(x,y):
            print('foo', x, y)

        def do_bar(s):
            print('bar', s)

        for tag, *args in records:
            if tag == 'foo':
                do_foo(*args)
            else:
                do_bar(*args)


        line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'

        name,*_,home,bin = line.split(':')
        print(name)
        print(home)
        print(bin)









if __name__ == '__main__':

    unpacking = Unpacking()
    unpacking.unpack()






# from collections import deque
#
# def search(lines, pattern, history=5):
#     previous_lines = deque(maxlen=history)
#     for line in lines:
#         if pattern in line:
#             yield line, previous_lines
#     previous_lines.append(line)
#
# # Example use on a file
# if __name__ == '__main__':
#
#     with open('/Users/tokluo/IdeaProjects/PysparkProject/sparky/dataFrame.py') as f:
#         for line, prevlines in search(f, 'parser', 5):
#             for pline in prevlines:
#                 print(pline)
#             print(line)
#             print('-'*20)


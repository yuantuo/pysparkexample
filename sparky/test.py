class Unpacking:

    def unpack(self):
        p = (4,5)
        x,y = p
        print("%s, %s" % (x, y))

        p = ['foo', 'bar', 123, (2016,8,2)]
        a,b,c,d = p
        #if number of unpack item is not correct is will give ValueError
        print("%s,%s,%d,%d,%d,%d" % (a,b,c,d[0],d[1],d[2]))

        #unpack a string
        p = 'Hello'
        a,b,c,d,e = p
        print(a)

        p = ['foo', 'bar', 123, (2016,8,2)]
        #disgard vaiable with _
        _,b,c,_ = p
        print(b) #print _ return nothing








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


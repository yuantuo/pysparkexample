class Unpacking:

    def unpack(self):

        p = (4,5)
        x,y = p
        print("%s, %s" % x, y)


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


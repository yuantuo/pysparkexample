class Structures:

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


    def queue(self):

        """
            using deque as a queued pipe
        """
        from collections import deque
        q = deque(maxlen=3)
        q.append(1)
        q.append(2)
        q.append(3)
        q.append(4)
        print(q)

    """
        find largest and smallest N items with heapq
    """

    def lagest_smallest(self):
        import heapq

        num = [1,3,4,5,6,24,-3,0,-5,34,5]

        print(heapq.nlargest(2,num))
        print(heapq.nsmallest(1,num))


        """
            some nested struc [{},{}]
        """
        stru = [
                    {'name': 'foo', 'price': 12},
                    {'name': 'bar', 'price': 23},
                    {'name': 'fred', 'price': 0.4},
                    {'name': 'wilma', 'price': -3},
                ]

        cheap = heapq.nsmallest(1, stru, key=lambda s:s['price'])
        expen = heapq.nlargest(1, stru, key=lambda s:s['price'])

        print("%f, %f" %  (cheap[0]['price'],expen[0]['price']))

        heap = list(num)
        heapq.heapify(heap)
        print(heap)
        print(heapq.heappop(heap))
        print(heapq.heappop(heap))
        print(heapq.heappop(heap))

        #or you can use min() or max() if you are only interested in 1
        print(min(num))
        print(max(num))

        a = []
        heapq.heappush(a,(3,0,'e'))
        heapq.heappush(a,(1,0,'H'))
        heapq.heappush(a,(4,0,'l'))
        heapq.heappush(a,(7,0,'0'))
        heapq.heappush(a,(6,0,'l'))

        print(heapq.heappop(a)[-1])
        print(heapq.heappop(a)[-1])
        print(heapq.heappop(a)[-1])
        print(heapq.heappop(a)[-1])
        print(heapq.heappop(a)[-1])


    def keys_maps(self):
        pass


if __name__ == '__main__':

    structure = Structures()
    structure.unpack()
    structure.queue()
    structure.lagest_smallest()
    structure.keys_maps()





class Structures:

    def __init__(self):
        self.string = 'Hello'
        self.tuple = (4,5)
        self.list = ['foo', 'bar', 123, (2016,8,2)]
        self.list2 = ['foo', 'bar', '234234213434', '3421342341324']
        self.records = [
            ('foo', 1, 2),
            ('bar', 'hello'),
            ('foo', 3, 4),
        ]
        self.line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
        self.num = [1,3,4,5,6,24,-3,0,-5,34,5]
        self.stru = [
            {'name': 'foo', 'price': 12},
            {'name': 'bar', 'price': 23},
            {'name': 'fred', 'price': 0.4},
            {'name': 'wilma', 'price': -3},
        ]
        self.dictionary = {
            'ACME': 45.23,
            'AAPL': 612.78,
            'IBM': 205.55,
            'HPQ': 37.20,
            'FB': 10.75
        }

        self.dictionary_a = {
            'x' : 1,
            'y' : 2,
            'z' : 3
        }
        self.dictionary_b = {
            'w' : 10,
            'x' : 11,
            'y' : 2
        }

        self.slicestr = '....................100          .......513.25     ..........'

        self.count = [
            'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
            'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
            'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
            'my', 'eyes', "you're", 'under'
        ]

    def unpack(self):

        x,y = self.tuple
        print("%s, %s" % (x, y))

        a,b,c,d = self.list
        #if number of unpack item is not correct is will give ValueError
        print("%s,%s,%d,%d,%d,%d" % (a,b,c,d[0],d[1],d[2]))

        """
            unpack a string
        """
        a,b,c,d,e = self.string
        print(a)


        """
            disgard vaiable with _
        """
        # p = ['foo', 'bar', 123, (2016,8,2)]
        _,b,c,_ = self.list
        print(b) #print _ return nothing

        """
            Using *
        """
        a,c,*num=self.list2
        print(a)
        print(*num)

        """
         unpacking dictionary
        """
        def do_foo(x,y):
            print('foo', x, y)

        def do_bar(s):
            print('bar', s)

        for tag, *args in self.records:
            if tag == 'foo':
                do_foo(*args)
            else:
                do_bar(*args)

        name,*_,home,bin = self.line.split(':')
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

        print(heapq.nlargest(2,self.num))
        print(heapq.nsmallest(1,self.num))


        """
            some nested struc [{},{}]
        """
        cheap = heapq.nsmallest(1, self.stru, key=lambda s:s['price'])
        expen = heapq.nlargest(1, self.stru, key=lambda s:s['price'])

        print("%f, %f" %  (cheap[0]['price'],expen[0]['price']))

        heap = list(self.num)
        heapq.heapify(heap)
        print(heap)
        print(heapq.heappop(heap))
        print(heapq.heappop(heap))
        print(heapq.heappop(heap))

        #or you can use min() or max() if you are only interested in 1
        print(min(self.num))
        print(max(self.num))

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


    def keys_and_dictionary(self):

        from collections import defaultdict
        d = defaultdict(list)
        d['a'].append('foo')
        d['a'].append('bar')
        d['b'].append('fred')
        d['b'].append(22.3)

        print(d)

        """
            ordered dictionary
        """
        from collections import OrderedDict
        d = OrderedDict()
        d['foo'] = 1
        d['bar'] = 3
        d['fred'] = 5
        d['wilma'] = 5

        print(d)

        """
            zip creates iterator can only be used once
        """
        min_price = min(zip(self.dictionary.values(), self.dictionary.keys()))
        print(min_price)

        max_price = max(zip(self.dictionary.values(), self.dictionary.keys()))
        print(max_price)

        sorted_price = sorted(zip(self.dictionary.values(), self.dictionary.keys()))
        print(sorted_price)


        print(min(self.dictionary.values()))
        print(min(self.dictionary, key=lambda k: self.dictionary[k]))

        """
            compare dictionary
        """

        print( self.dictionary_a.keys() & self.dictionary_b.keys())
        print( self.dictionary_a.keys() - self.dictionary_b.keys())
        print( self.dictionary_a.items() - self.dictionary_b.items())


    def slice(self):
        share = slice(20,32)
        cost = slice(40,48)

        cost = int(self.slicestr[share]) * float(self.slicestr[cost])
        print(cost)

    def counter(self):

        from collections import Counter
        word_count = Counter(self.count)
        print(word_count.most_common(3))
        print(word_count['eyes'])

        b = word_count + word_count
        print(b)


    

if __name__ == '__main__':

    structure = Structures()
    structure.unpack()
    structure.queue()
    structure.lagest_smallest()
    structure.keys_and_dictionary()
    structure.slice()
    structure.counter()




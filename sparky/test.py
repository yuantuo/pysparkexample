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

    """
        using deque as a queued pipe
        from collections import deque

    """
    def queue(self):

        from collections import deque
        q = deque(maxlen=3)
        q.append(1)
        q.append(2)
        q.append(3)
        q.append(4)
        print(q)

    """
        find largest and smallest N items with heapq
        import heapq
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


    """
        from collections import defaultdict
        from collections import OrderedDict

    """

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



    """
        slice
    """
    def slice(self):
        share = slice(20,32)
        cost = slice(40,48)

        cost = int(self.slicestr[share]) * float(self.slicestr[cost])
        print(cost)


    """
        from collections import Counter
    """
    def counter(self):

        from collections import Counter
        word_count = Counter(self.count)
        print(word_count.most_common(3))
        print(word_count['eyes'])

        b = word_count + word_count
        print(b)



    """
        Sorting a List of Dictionaries by a Common Key

        from operator import itemgetter
    """

    def sort_list(self):

        rows = [
            {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
            {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
            {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
            {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
        ]


        from operator import itemgetter

        rows_by_fname = sorted(rows, key=itemgetter('fname'))
        rows_by_uid = sorted(rows,key=itemgetter('uid'))

        print(rows_by_fname)
        print(rows_by_uid)

        rows_by_lname_fname = sorted(rows, key=itemgetter('lname', 'fname'))
        print(rows_by_lname_fname)

        vmin = min(rows, key=lambda s: s['uid'])
        print(vmin)

        vmax = max(rows, key=lambda s: s['uid'])
        print(vmax)

        #you can also sort by class field
        #see example on reference

    """
        group by

        from itertools import groupby
        from operator import itemgetter
    """
    def group_by(self):

        rows = [
            {'address': '5412 N CLARK', 'date': '07/01/2012'},
            {'address': '5148 N CLARK', 'date': '07/04/2012'},
            {'address': '5800 E 58TH', 'date': '07/02/2012'},
            {'address': '2122 N CLARK', 'date': '07/03/2012'},
            {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
            {'address': '1060 W ADDISON', 'date': '07/02/2012'},
            {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
            {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
        ]

        from operator import itemgetter
        from itertools import groupby


        rows.sort(key=itemgetter('date'))

        for date, items in groupby(rows, key=itemgetter('date')):
            print(date)
            for i in items:
                print(' '*10, i)

    def filtering(self):

        mylist = [1, 4, -5, 10, -7, 2, 3, -1]
        print([n for n in mylist if n > 0])
        print([n for n in mylist if n < 0])

        import math

        print([math.sqrt(n) for n in mylist if n > 0])

    def cool_stuff(self):

        mylist = [1, 4, -5, 10, -7, 2, 3, -1]
        print([n if n > 0 else 0 for n in mylist])
        print([n if n < 0 else 0 for n in mylist])


        mydict = {
            'ACME': 45.23,
            'AAPL': 612.78,
            'IBM': 205.55,
            'HPQ': 37.20,
            'FB': 10.75
        }

        print({key:value for key, value in mydict.items() if value > 200})

        p1 = {'FB', 'IBM'}
        print({key:value for key, value in mydict.items() if key in p1})

        print( dict((key, value) for key, value in mydict.items() if value > 200) )

        # if any(t < 0 for t in x):
        #     pass

    """
        named tuple ( less space )
        from collections import namedtuple

    """

    def named_tuple(self):

        from collections import namedtuple

        subscriber = namedtuple('Subscriber', ['addr', 'joined'])
        sub = subscriber('foo@bar.com', '08/02/2016')

        print(sub)
        print(sub.addr)
        print(sub.joined)

        ###########
        #replace
        ###########
        Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
        # Create a prototype instance
        stock_prototype = Stock('', 0, 0.0, None, None)

        s = {'name': 'ACME', 'shares': 100, 'price': 123.45}
        print(stock_prototype._replace(**s))

    """
        Combining Multiple Mappings into a Single
        from collections import ChainMap

    """
    def combin_maps(self):

        from collections import ChainMap

        a = {'x': 1, 'z': 3 }
        b = {'y': 2, 'z': 4 }

        c = ChainMap(a,b)
        print(c)
        print(c['z'])

        merge = dict(b)
        merge.update(a)

        print(merge)


class StringText:

    def __init__(self):
        self.line = 'asdf fjdk; afed, fjek,asdf, foo'
        self.line1 = 'spam.txt'
        self.line2 = 'http://www.python.org'
        self.arr_files = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
        self.addresses = [
            '5412 N CLARK ST',
            '1060 W ADDISON ST',
            '1039 W GRANVILLE AVE',
            '2122 N CLARK ST',
            '4802 N BROADWAY',
        ]

    """
        split line and using re

        import re
    """
    def split(self):
        import re
        print(re.split(r'[;,\s]\s*', self.line))

        #:r (none capture)
        print(re.split(r'(?:;|,|\s)\s*', self.line))


        # if any(t < 0 for t in x):

    def text_start_end_with(self):

        print(self.line1.endswith('.txt'))
        print(self.line2.startswith('http'))

        import os
        filenames = os.listdir('/Users/tokluo/IdeaProjects/PysparkProject/sparky/')
        print([ name for name in filenames if name.endswith('.py')])

        #or use match
        import re
        print(re.match('http:|https:|ftp:', self.line2))

    """
        Matching Strings Using Shell Wildcard Patterns
    """

    def match_wildcard(self):

        from fnmatch import fnmatch, fnmatchcase
        print(fnmatch('foo.txt', '*.txt'))
        print(fnmatch('foo.txt', '?oo.txt'))
        print(fnmatch('Dat45.txt', 'Dat[0-9]*'))

        print([ filename for filename in self.arr_files if fnmatch(filename, 'Dat*.csv')])

        print([address for address in self.addresses if fnmatch(address, '* ST')])

    """
        simple and complex string search/match
    """

    def string_match(self):

        str = 'hello world, this is an awesome string'
        print(str.find('awesome'))
        import re
        print( re.match(r'.+ world', str) )

        #if the pattern will be used more than once
        pattern = re.compile(r'.+ world')
        print(pattern.match(str))

        print(re.findall(r'awesome|this', str))

        #using group and match

        datapat = re.compile(r'(\d+)/(\d+)/(\d+)')
        m = datapat.match('11/27/2016')
        print(m.group(0))
        print(m.group(1))
        print(m.group(2))
        print(m.group(3))

        date, month, year = m.groups()
        print(date, month, year)

        str2 = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
        m = datapat.findall(str2)
        print(m)


    """
        search and replace
    """

    def search_replace(self):

        str = 'yeah, but no, but yeah, but no, but yeah'

        print( str.replace('yeah', 'ya'))

        text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
        import re
        print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\1-\2-\3', text))

        datapat = re.compile(r'(\d+)/(\d+)/(\d+)')
        print(datapat.sub(r'\1-\2-\3', text))

        #case insenstive flaf
        text = 'UPPER PYTHON, lower python, Mixed Python'
        print(re.findall('python', text, flags=re.IGNORECASE))
        print(re.sub('python', 'snake', text, flags=re.IGNORECASE))

        #match shortest
        text = 'Computer say "no" and phone says "yes"'
        datapat = re.compile(r'\"(.*?)\"')
        print( datapat.findall(text))

    """
        Normalizing unicode in text

        import unicodedata

        The first argument to normalize() specifies how you want the string normalized.
        NFC means that characters should be fully composed (i.e., use a single code point if possible).
        NFD means that characters should be fully decomposed with the use of combining char‐ acters.
    """

    def normalise(self):

        import unicodedata
        print(unicodedata.normalize('NFC', 'Spicy Jalape\u00f1o'))

        t1 = unicodedata.normalize('NFD', 'Spicy Jalape\u00f1o')
        print(''.join(c for c in t1 if not unicodedata.combining(c)))


    """
        Stripping Unwanted Characters from Strings
    """
    def striping_unwants(self):
        pass


if __name__ == '__main__':

    structure = Structures()
    structure.unpack()
    structure.queue()
    structure.lagest_smallest()
    structure.keys_and_dictionary()
    structure.slice()
    structure.counter()
    structure.sort_list()
    structure.group_by()
    structure.filtering()
    structure.cool_stuff()
    structure.named_tuple()
    structure.combin_maps()

    stringtext = StringText()
    stringtext.split()
    stringtext.text_start_end_with()
    stringtext.match_wildcard()
    stringtext.string_match()
    stringtext.search_replace()
    stringtext.normalise()


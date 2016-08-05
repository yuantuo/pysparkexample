from dateutil.rrule import *
from pprint import pprint

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

        a = 'pýtĥöñ is awesome\n'
        b = unicodedata.normalize('NFD', a)
        print(b.encode('ascii', 'ignore').decode('ascii'))


    """
        Stripping Unwanted Characters from Strings
    """
    def striping_unwants(self):

        import re
        s = '    hello world \n'
        print(s.strip())
        s = '--------hello world +++++++'
        print(s.strip('-+'))

        #stripping does not apply to any text in the middle of a string
        s = '** Hello     World----'
        print( re.sub('\s+', ' ', s.strip('*-').strip()))

        #################################
        ##string line with opening file
        #################################

        #with open(filename) as f:
        #    lines = (line.strip() for line in f)
        #    for line in lines:


    def aligning_text(self):

        text = 'hello world'
        print(text.ljust(20))
        print(text.rjust(20))
        print(text.center(20))
        print(text.rjust(20,'='))

        print(format(text, '>20'))
        print(format(text, '^20'))

        print(format(text, '=>20'))
        print(format(text, '*^20'))
        print('{:>10s} {:>10s}'.format('hello', 'world'))

        parts =  ['Is', 'Chicago', 'Not', 'Chicago?']
        print(' '.join(parts))
        print(','.join(parts))

        a = 'Is Chicago'
        b = 'Not Chicago?'

        print('{} {}'.format(a,b))

        #############################
        #join string mix with digits
        #############################
        data = ['ACME', 50, 9.4]
        print(' '.join(str(w) for w in data ))

        s = '{name} has {n} messages'
        print(s.format(name='foo', n=100))

    def byte_string(self):

        data = b'Hello world'
        print(data.split())
        print(data.replace(b'Hello', b'yoyooy'))

        data = b'FOO:BAR,SPAM'
        import re
        print( re.split(b'[:,]', data))
        print(data.decode('ascii'))

class Numbers:
    def __init__(self):
        pass

    def arounding(self):

        #around to even number
        print( round(1.15, 1))
        print( round(1.25, 1))
        print( round(1627731, -3))
        print(format(1.2343, '0.2f'))
        print( 'value is {:0.3f}'.format(1.23434))

    """
        using
        from decimal import Decimal
    """
    def decimals(self):
        from decimal import Decimal

        a = Decimal('4.2')
        b = Decimal('2.1')
        print(a + b)

    def sums(self):

        data = [1.23e+18, 1, -1.23e+18]
        print('error on small with large number')
        print(sum(data))

        print('To fix this use math module')
        import math
        print( math.fsum(data) )


    def formats(self):
        x = 1234.56789

        print(format(x, '0.2f'))
        print(format(x, '>10.1f'))
        print(format(x, '<10.1f'))
        print(format(x, '^10.1f'))

        print('convert into binary, octal, hex')
        x = 1234
        print( bin(x))
        print( oct(x))
        print( hex(x))

    def complexmath(self):
        a = complex(2,4)
        b = 3 - 5j

        import cmath
        print( cmath.sin(a))
        print( cmath.cos(b))


    """
        from fractions import Fractions
    """
    def fractionmath(self):

        from fractions import Fraction

        a = Fraction(5,4)
        b = Fraction(7, 16)
        print(float(a))

        c = a + b
        print(c)

        #inf, nan using float
        print( float('inf') )
        print( float('-inf') )
        print( float('nan') )


    """
        import numpy as np
    """
    def numarray(self):

        import numpy as np
        ax = np.array([1, 2, 3, 4])
        print( ax * 2 )
        print( ax + 10 )
        print( np.sqrt(ax) )

        a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

        print(a[0])
        print(a[1:3,1:4])

    """
        import random
    """
    def randomvalues(self):

        import random
        values = [1,2,3,4,5,6,7]

        print(random.choice(values))
        print(random.sample(values, 2))
        random.shuffle(values)
        print(values)
        print(random.randint(0,10))
        print(random.random())

    """
        from datetime import timedelta, datetime
    """

    def timeformat(self):
        from datetime import timedelta, datetime
        #days
        a = timedelta(2018,8,3)
        print(a)
        print(a.days)

        now = datetime.now()
        print(now)

        today = datetime.today()
        print(today)
        print(today + timedelta(minutes=10))

        #days
        a = timedelta(2018,8,3)
        b = timedelta(2016,8,1)
        print( (a-b).days)

        #datetime
        a = datetime(2018,8,3)
        b = datetime(2018,7,1)
        print( (a-b).days)

        #months
        from dateutil.relativedelta import relativedelta
        a = datetime.today()
        print( a + relativedelta(months=+1) )

        print(a + relativedelta(weekday=FR))
        print(a + relativedelta(weekday=FR(-1)))


        #string to datetime
        text = '2018-08-03'
        y = datetime.strptime(text, '%Y-%m-%d')
        print(y)

        print( datetime.strftime(y, '%A %B %d, %Y') )

        #timezone
        from pytz import timezone
        central = timezone('US/Central')
        print(central.localize(y))

class Iterors:
    def __init__(self):
        pass

    def custome_itr(self):

        root = Node(0)
        child1 = Node(1)
        child2 = Node(2)

        root.add_child(child1)
        root.add_child(child2)

        for ch in root:
            print(ch)


    def frange(self, start, stop, incr):
        x = start
        while x < stop:
            yield x
            x += incr

    """
        drop while
        from itertools import dropwhile
    """

    def dropwhile(self):

        from itertools import dropwhile

        with open('/etc/passwd') as f:
            for line in dropwhile(lambda line: line.startswith('#'), f):
                print(line)

    """
        permutations
        from itertools import permutations
    """

    def permutations_ltr(self):

        from itertools import permutations, combinations_with_replacement

        items = ['a', 'b', 'c']

        for p in permutations(items):
            print(p)

        for p in permutations(items,2):
            print(p)

        for p in combinations_with_replacement(items,3):
            print(p)

    def using_zip_ltr(self):

        xpts = [1,5,6,8,0]
        ypts = [101,78,96,45,74, 887]

        for x, y in zip(xpts, ypts):
            print(x,y)


        from itertools import zip_longest

        for i in zip_longest(xpts, ypts, fillvalue=0):
            print(i)

        c = ['x','y','z']

        for i in zip_longest(xpts, ypts, c, fillvalue=0):
            print(i)


        from itertools import chain

        for i in chain(xpts,ypts):
            print(i)

    def withindex(self):

        list = ['a', 'b', 'c']

        for idx, val in enumerate(list):
            print(idx, val)

class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

class FileIO:
    def __init__(self):
        pass

    def openfile(self):

        with open('/etc/passwd') as f:
            print(f.read())


        with open('/Users/tokluo/IdeaProjects/PysparkProject/bin/test.txt', 'rt', encoding='ascii', errors='ignore') as f:
            print(f.read())


        print('ACME', 50, 95.4, sep=',', end='@@')

        row = ('ACME', 50, 91.5)
        print(*row, sep='|')

        with open('/Users/tokluo/IdeaProjects/PysparkProject/bin/some.bin', 'wb') as f:
            f.write(b'hello world')

        #reading/writing binary
        with open('/Users/tokluo/IdeaProjects/PysparkProject/bin/some.bin', 'rb') as f:
            print(f.read())

        with open('/Users/tokluo/IdeaProjects/PysparkProject/bin/some.bin', 'rb') as f:
            data = f.read()
            print(data.decode('utf-8'))


        #writing to file not already exsits
        # with open('somefile', 'xt') as f:

    def usingIoString(self):
        import io
        s = io.StringIO()
        s.write('Io string hello world')

        print(s.getvalue())

    def compressed_file(self):
        import gzip
        import bz2

        with gzip.open('somefile.gz', 'rt') as f:
            text = f.read()

        with bz2.open('somefile.bz2', 'rt') as f:
            text = f.read()

    def read_parical(self):

        from functools import partial

        RECORD_SIZE = 32
        with open ('somefile.data', 'rb') as f:
            records = iter(partial(f.read, RECORD_SIZE), b'')
            for r in records:
                print(r)

    def do_path(self):

        import os
        import sys

        tempath = '/Users/tokluo/Data/data.csv'

        print(os.path.basename(tempath))
        print(os.path.dirname(tempath))

        print(os.path.join('tmp', 'data', os.path.basename(tempath)))

        tempath2 = '~/foobar/file'
        print (os.path.expanduser(tempath2))

        print(os.path.exists(tempath))
        print(os.path.isfile('/etc/passwd'))
        print(os.path.isdir('/etc/passwd'))

        import time
        print( time.ctime(os.path.getctime('/etc/passwd')))

        name = os.listdir('/usr/local')
        print(name)

        filenames = [filename for filename in os.listdir('/usr/local') if os.path.isfile(os.path.join('/usr', 'local', filename))]
        print(filenames)

        dirname = {filedir for filedir in os.listdir('/usr/local') if os.path.isdir(os.path.join('/usr', 'local', filedir))}
        print(dirname)

        print(sys.getfilesystemencoding())

    def temparyfile(self):

        from tempfile import TemporaryFile, NamedTemporaryFile

        with NamedTemporaryFile('w+t', prefix='toktmp_', suffix='.txt', dir='/tmp') as f:
            f.write('foobar')
            f.write('wilma')
            f.seek(0)
            print(f.name)
            print(f.read())

    def serializingobj(self):
        import pickle
        data = 'some cool stuff'
        data2= 'the morning is good'

        with open('/tmp/seri', 'wb') as f:
            pickle.dump(data, f)
            pickle.dump(data2, f)


        with open('/tmp/seri', 'rb') as f:
            data = pickle.load(f)
            data = pickle.load(f)
            print(data)

class Encodeing:

    def __init__(self):
        pass

    def openfile(self):

        from collections import namedtuple
        import os, csv
        path = os.path.join('/Users', 'tokluo', 'IdeaProjects', 'PysparkProject', 'bin', 'stock.csv')
        print(path)
        with open(path, 'rt') as f:
            f_csv = csv.reader(f)
            headings = next(f_csv)
            print(headings)
            Row = namedtuple('Row', headings)
            for r in f_csv:
                row =Row(*r)
                print(row)


        with open(path, 'rt') as f:
            f_csv = csv.DictReader(f)
            for r in f_csv:
                print(r)
                print(r['Date'])

    def writecsv(self):

        import os, csv

        path = os.path.join('/Users', 'tokluo', 'IdeaProjects', 'PysparkProject', 'bin', 'stock2.csv')

        headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
        rows = [{'Symbol':'AA', 'Price':39.48, 'Date':'6/11/2007',
                 'Time':'9:36am', 'Change':-0.18, 'Volume':181800},
                {'Symbol':'AIG', 'Price': 71.38, 'Date':'6/11/2007',
                 'Time':'9:36am', 'Change':-0.15, 'Volume': 195500},
                {'Symbol':'AXP', 'Price': 62.58, 'Date':'6/11/2007',
                 'Time':'9:36am', 'Change':-0.46, 'Volume': 935000}]

        with open (path, 'wt') as f:
            f_csv = csv.DictWriter(f, headers)
            f_csv.writeheader()
            f_csv.writerows(rows)

        #using panda is good module to convert csv pandas.read_csv()

    def readjson(self):

        import json
        data = {

            'name': 'ACME',
            'share': 100,
            'price': 542.34
        }

        json_str = json.dumps(data)
        pprint(json_str)

        json_obj = json.loads(json_str)
        pprint(json_obj)

        from urllib.request import urlopen
        import json

        u = urlopen('http://mysafeinfo.com/api/data?list=englishmonarchs&format=json')
        resp = json.loads(u.read().decode('utf-8'))
        # pprint(resp)

        # iteritems removed in python3 using items
        for i in resp:
            pprint(i['cty'])
            for attr, item in i.items():
                print(attr, item)

    def readingxml(self):
        from urllib.request import urlopen
        from xml.etree.ElementTree import parse

        u = urlopen('http://planet.python.org/rss20.xml')
        doc = parse(u)

        for item in doc.iterfind('channel/item'):
            title = item.findtext('title')
            date = item.findtext('pubDate')
            link = item.findtext('link')

            print(title)
            print(date)
            print(link)


    def parse_and_remove(self, filename, path):

        print('********')
        from xml.etree.ElementTree import iterparse

        path_parts = path.split('/')
        doc = iterparse(filename, ('start', 'end')) # Skip the root element
        print(path_parts)
        next(doc)
        tag_stack = []
        elem_stack = []
        for event, elem in doc:
            print(event)
            print(elem)
            if event == 'start':
                tag_stack.append(elem.tag)
                elem_stack.append(elem)
            elif event == 'end':
                if tag_stack == path_parts:
                    yield elem
                    elem_stack[-2].remove(elem)
                try:
                    tag_stack.pop()
                    elem_stack.pop()
                except IndexError as e:
                    print(e)
                    pass


    def writexml(self):

        s = {"foo":"bar", "fred":"wlima","num":123}

        from xml.etree.ElementTree import Element, tostring

        elem = Element('Tok')

        for key, value in s.items():

            child = Element(key)
            child.text = str(value)
            elem.append(child)
        elem.set('_id', 'thisid')
        pprint(tostring(elem))

    def hexadeimal(self):

        s = b'hello'
        import binascii
        h = binascii.b2a_hex(s)
        print(h)
        print(binascii.a2b_hex(h))

        import base64
        h = base64.b16encode(s)
        print(h)
        print(base64.b16decode(h))

class Functions:
    def __init__(self):
        pass

    def passargs(self,first, *rest):
        print((first + sum(rest)) / (1 + len(rest)))

    def keywords(self, *tuple, **args):
        print(tuple)
        print(args)
        print(args['foo'])


    def cooloneline(self):
        add = lambda x,y: x+y
        print(add(2,3))

        names = ['Foo', 'Bar', 'Fred', 'Wilma']

        print(sorted(names, key=lambda name: name.split()[-1].lower()))

        #using for loop in lambda

        func = [lambda x, n=n: x+n for n in range(5)]
        for f in func:
            print(f(1))


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
    stringtext.striping_unwants()
    stringtext.aligning_text()
    stringtext.byte_string()

    numbers = Numbers()
    numbers.arounding()
    numbers.decimals()
    numbers.sums()
    numbers.formats()
    numbers.complexmath()
    numbers.fractionmath()
    numbers.numarray()
    numbers.randomvalues()
    numbers.timeformat()


    itr = Iterors()
    itr.custome_itr()
    for x in itr.frange(0,5,0.5):
        print(x)

    print('************')
    a = itr.frange(0,5,0.5)
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))

    itr.dropwhile()
    itr.permutations_ltr()
    itr.using_zip_ltr()
    itr.withindex()


    fileio = FileIO()
    fileio.openfile()
    fileio.usingIoString()
    fileio.do_path()
    fileio.temparyfile()
    fileio.serializingobj()

    encoding = Encodeing()
    encoding.openfile()
    encoding.writecsv()
    encoding.readjson()
    encoding.readingxml()

    # from collections import Counter
    # potholes_by_zip = Counter()
    # data = encoding.parse_and_remove('/Users/tokluo/Desktop/rows.xml', 'row/row')
    # for pothole in data:
    #     potholes_by_zip[pothole.findtext('zip')] += 1
    #
    # for zipcode, num in potholes_by_zip.most_common():
    #     print(zipcode, num)
    #


    encoding.writexml()
    encoding.hexadeimal()

    func = Functions()
    func.passargs(1,2,3,4)
    func.keywords(1,2,3,4,foo='bar',fred='wilma')
    func.cooloneline()
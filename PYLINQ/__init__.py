class PYLINQ:
    _inerList = None
    def __init__(self, array: list):
        self._inerList = array

    def __iter__(self):
        '''
        Generating Iterative Method
        '''
        for item in self._inerList:
            yield item


    def toList(self):
        '''
        Converting goals into arrays
        '''
        return [x for x in self]

    def where(self, func=lambda x: x):
        '''
        func： return true for each item whicth want
        '''
        return WhereIterator(self, func)

    def first(self, func=lambda x: x):
        '''
        retrun one Which one do you do not want
        '''
        for item in self:
            if func(item):
                return item
        return None

    def select(self, func=lambda x: x):
        '''
        Projection of new type of items  
        '''
        return SelectIterator(self, func)

    def any(self):
        '''
        test they are any
        '''
        for _ in self:
            return True
        return False

    def exist(self, func=lambda x: x):
        '''
        item is is exist
        '''
        for item in self:
            if func(item):
                return True
        return False

    def take(self, count):
        '''
        Get some of elements 
        '''
        return TakeIterator(self, count)

    def contains(self, model):
        '''
        Does the array contain
        '''
        for item in self:
            if item == model:
                return True
        return False

    def remove(self, func=lambda x: x, count=1):
        '''
        Removing Elements
        '''
        return RemoveIterator(self, func, count)

    def removeAll(self, func=lambda x: x):
        '''
        Removing all Elements
        '''
        return RemoveIterator(self, func, 0)

    def count(self):
        '''
        Removing all Elements
        '''
        count = 0
        for _ in self:
            count += 1
        return count

    def orderBy(self, func=lambda x: x):
        '''
        order by 
        '''
        return OrderIterator(self, func)

    def orderByDesc(self, func=lambda x: x):
        '''
        order by desc
        '''
        return OrderIterator(self, func, True)


class WhereIterator(PYLINQ):
    '''
    Filtering eligible elements
    '''

    def __init__(self, array: list, func=lambda x: x):
        super(WhereIterator, self).__init__(array)
        self._func = func

    def __iter__(self):
        '''
        Generating Iterative Method
        '''
        for item in self._inerList:
            if self._func(item):
                yield item


class SelectIterator(PYLINQ):
    '''
    Projection of new items 
    '''

    def __init__(self, array: list, func=lambda x: x):
        super(SelectIterator, self).__init__(array)
        self._func = func

    def __iter__(self):
        '''
        Generating Iterative Method
        '''
        for item in self._inerList:
            yield self._func(item)

class TakeIterator(PYLINQ):
    '''
    Gets a specified number of items
    '''

    def __init__(self, array: list, count=1):
        super(TakeIterator, self).__init__(array)
        self._count = count

    def __iter__(self):
        '''
        Generating Iterative Method
        '''
        for item in self._inerList:
            if self._count > 0:
                self._count -= 1
                yield item
            else:
                break


class RemoveIterator(PYLINQ):
    '''
    Remove one or more elements
    func:retrun bool Which one do you do not want
    count:the quantity Which one do you want
    '''

    def __init__(self, array: list, func=lambda x: x, count=0):
        super(RemoveIterator, self).__init__(array)
        self._func = func
        self._count = count

    def __iter__(self):
        '''
        Generating Iterative Method
        '''
        for item in self._inerList:
            if not self._func(item):
                if self._count == 0 or self._count > 0:
                    self._count -= 1
                    yield item
                else:
                    break


class OrderIterator(PYLINQ):
    '''
    sort list
    '''

    def __init__(self, array: list, func=lambda x: x, reverse=False):
        super(OrderIterator, self).__init__(array)
        self._inerList = sorted(self._inerList, func, reverse)

from operator import itemgetter, attrgetter


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

    def groupBy(self, func=lambda x: x):
        '''
        order by desc
        '''
        return GroupByIterator(self, func)

    def sum(self, func=lambda x: x):
        '''
        sum 
        '''
        total = 0
        for item in self:
            total += func(item)
        return total

    def skip(self, size=0):
        '''
        skip:
        size:
        '''
        return SkipIterator(self, size)

    def max(self, func=lambda x: x):
        '''
        max of item
        '''
        maxModel = None
        for item in self:
            if maxModel is None:
                maxModel = item
            elif func(item) > func(maxModel):
                maxModel = item
        return maxModel

    def min(self, func=lambda x: x):
        '''
        max of item
        '''
        maxModel = None
        for item in self:
            if maxModel is None:
                maxModel = item
            elif func(item) < func(maxModel):
                maxModel = item
        return maxModel

    def forEach(self, func=lambda x: x):
        '''
        Cyclic processing of each element
        '''
        def _calculation():
            for item in self:
                yield func(item)
        return PYLINQ(_calculation())

    def distinct(self, func=lambda x: x):
        return DistinctIterator(self, func)


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


class SkipIterator(PYLINQ):
    '''
    Skip a specified number of items
    '''

    def __init__(self, array: list, count=1):
        super(SkipIterator, self).__init__(array)
        self._count = count

    def __iter__(self):
        '''
        Generating Iterative Method
        '''
        for item in self._inerList:
            if self._count > 0:
                self._count -= 1
                continue
            else:
                yield item


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

    def __init__(self, array: list, keyFunc=lambda x: x, reverse=False):
        super(OrderIterator, self).__init__(array)
        self._keyFunc = keyFunc
        self._keyFuncs = [keyFunc]
        self._reverse = reverse

    def __iter__(self):
        '''
        sort
        '''
        tmpList = []
        if len(self._keyFuncs) > 1:
            def orderKey(keyFuncs, model):
                for kf in keyFuncs:
                    yield kf(model)
            tmpList = sorted(self._inerList, key=lambda x: tuple([x for x in orderKey(self._keyFuncs, x)]),
                             reverse=self._reverse)
        else:
            tmpList = sorted(self._inerList, key=self._keyFunc,
                             reverse=self._reverse)
        for item in tmpList:
            yield item

    def thenBy(self, keyFunc=lambda x: x):
        '''
        the next order by
        '''
        def orderFunc(model):
            v = keyFunc(model)
            if self._reverse and (isinstance(v, int) or isinstance(v, float)):
                return -v
            return v
        self._keyFuncs.append(orderFunc)
        return self

    def thenByDesc(self, keyFunc=lambda x: x):
        '''
        the next order by desc
        '''
        def descOrderFunc(model):
            v = keyFunc(model)
            if not self._reverse and (isinstance(v, int) or isinstance(v, float)):
                return -v
            return v
        self._keyFuncs.append(descOrderFunc)
        return self


class GroupByIterator():

    def __init__(self, array: list, keyFunc=lambda x: x):
        self.inerList = array
        self.keyFunc = keyFunc
        self.grdoupCollection={}

    def __iter__(self):
        iremDir = {}
        for target in self.inerList:
            key = self.keyFunc(target)
            if key not in iremDir:
                iremDir[key] = True
                yield GroupByItemIterator(key, self)


class GroupByItemIterator():

    def __init__(self, key, groupModel):
        self.key = key
        self._groupModel = groupModel

    def __iter__(self):
        if self.key in self._groupModel.grdoupCollection:
            # 如果所在key没有，代表此数组从未循环过
            for target in self._groupModel.grdoupCollection[self.key]:
                yield target
        else:
            yield from self._forEachGroupItem()


    @property
    def value(self):
        return PYLINQ(self)

    def _forEachGroupItem(self):
        for item in self._groupModel.inerList:
            itemKey = self._groupModel.keyFunc(item)
            if itemKey not in self._groupModel.grdoupCollection:
                self._groupModel.grdoupCollection[itemKey] = [item]
            else:
                self._groupModel.grdoupCollection[itemKey].append(item)

            if self.key == itemKey:
                yield item


class DistinctIterator(PYLINQ):
    '''
    Distinct 
    '''

    def __init__(self, array: list, keyFunc=lambda x: x):
        super(DistinctIterator, self).__init__(array)
        self._keyFunc = keyFunc

    def __iter__(self):
        itemDic = {}
        for item in self._inerList:
            itemKey = self._keyFunc(item)
            if itemKey not in itemDic:
                itemDic[itemKey] = True
                yield item

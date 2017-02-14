#----------------------------------------------------------------------
# LList.py
# Karenna Maaser
# 02/13/2012
#----------------------------------------------------------------------

import sys

#----------------------------------------------------------------------

class LList:

    '''A single-linked structure'''
    
    #----------------------------------------------------------------------
    
    def __init__(self, item = None, link = None):

        '''creates a linked with the specified data value and link
        pre: None
        post: creates a linked with the specified data value and link'''
        
        self.item = item
        self.link = link
        self.head = None
        self.tail = None
        self.size = 0

#----------------------------------------------------------------------

    def __len__(self):

        '''returns number of items in the list
        pre: none
        post: returns number of items in the list'''

        return self.size

#----------------------------------------------------------------------

    def __iter__(self):

        '''iteration support using yield keyword
        pre: none
        post: '''

        node = self.head
        while node is not None:
            yield node.item
            node = node.link

#----------------------------------------------------------------------
    def _find(self, position):
        '''private method that returns node that is at location position
        in the list (0 is first item, size-1 is last item)
        pre: none
        post: returns the ListNode at the specified position in the list'''

        assert 0 <= position < self.size

        node = self.head
        # move forward until we reach the specified node
        for i in range(position):
            node = node.link
        return node

#----------------------------------------------------------------------
    def __getitem__(self, position):

        '''return data item at location position
        pre: 0 <= position < size
        post: returns data item at the specified position'''

        node = self._find(position)
        return node.item

#----------------------------------------------------------------------
    def __setitem__(self, position, value):

        '''set data item at location position to value
        pre: 0 <= position < self.size
        post: sets the data item at the specified position to value'''

        node = self._find(position)
        node.item = value

#----------------------------------------------------------------------
    def __delitem__(self, position):

        '''delete item at location position from the list
        pre: 0 <= position < self.size
        post: the item at the specified position is removed from the list'''

        assert 0 <= position < self.size

        self._delete(position)

#----------------------------------------------------------------------
    def _delete(self, position):

        '''private method to delete item at location position from the list
        pre: 0 <= position < self.size
        post: the item at the specified position is removed from the list'''

        if position == 0:
            # save item from the initial node
            item = self.head.item

            # change self.head to point "over" the deleted node
            self.head = self.head.link
        elif position == (self.size - 1):
            # find the node immediately before the one to delete
            pNode = self._find(position - 1)

             # save the item from the node to delete
            item = pNode.link.item

            # changes the tail to the predecessor
            pNode.link = None
            pNode = self.tail
        elif self.size == 1:
            self.head = None
            self.tail = None
        else:
            # find the node immediately before the one to delete
            prev_node = self._find(position -1)

            # save the item from the node to delete
            item = prev_node.link.item

            # change predecessor to point "over" the deleted node
            prev_node.link = prev_node.link.link
        self.size -= 1

#----------------------------------------------------------------------
    def append(self, x):

        '''appends x onto end of the list
        pre: none
        post: x is appended onto the end of the list'''

        # create a new node containing x
        newNode = LList(x)

        # link it into the end of the list
        if self.head is not None:
            # non-empty list
            self.tail.link = newNode
            newNode.link = None
            self.tail.link = newNode
        else:
            # empty list
            # set self.head to new node
            # set self.tail to new Node
            self.head = newNode
            self.tail = newNode
        self.size += 1

#----------------------------------------------------------------------
    def insert(self, i, x):

        '''inserts x before position i in the list
        pre: 0 <= i <= self.size
        post: x is inserted into the list before position i'''

        assert 0 <= i <= self.size

        if i == 0:
            # insert before position 0 requires updating self.head
            self.head = LList(x, self.head)
        elif i == (self.size - 1):
            newNode = LList(x)
            self.tail.link = newNode.item
            newNode.link = None
            newNode = self.tail
        else:
            # find item that node is to be inserted after
            prev = self._find(i -1)
            prev.link = LList(x, prev.link)
        self.size += 1

#----------------------------------------------------------------------
    def pop(self, i=None):

        '''returns and removes at position i from list; the default is to
        return and remove the last item
        pre: self.size > 0 and ((i is None or (0 <= i < self.size))
        post: if i is None, the last item in the list is removed and returned
        otherwise the item at position i is removed and returned'''

        assert self.size > 0 and (i is None or (0 <= i < self.size))

        # default is to delete the last item
        # i could be zero so need to compare to None
        if i is None:
            self.tail = self._find(i -1)
            i = self.size - 1
            self._delete(i)
        self.size -= 1

        return self._delete(i)

#----------------------------------------------------------------------
    def index(self, x, start=0):

        '''return position of first occurrence of x in the list starting
        at position start
        pre: start >= 0
        post: if x is in the list from position start to the end, the position
        it is located at is returned, otherwise a ValueError is raised'''

        start = 0
        for i in LList:
            start += 1
            if i == x:
                yield start
            else:
                return ValueError

#----------------------------------------------------------------------
    def remove(self, x):
        '''removes the first instance of x from the list
        pre: None
        post: if x is in the list, the first instance of x is removed from
        the list, otherwise a ValueError is raised'''
        for i in LList:
            if i == x:
                self._delete(x)
            else:
                return ValueError
        pass

#----------------------------------------------------------------------
    def extend(self, l):
        '''add each element of list l onto the list
        pre: none
        post: each item in the list l is appended onto the list'''

        l = LList()
        for i in l:
            LList.append(i)
            self.size += 1

#----------------------------------------------------------------------
    def __copy__(self):
        '''returns a new LList that contains the same items as self'''

        a = LList()
        for i in range(len(self)):
            a.append(self[i])
            if self[i] == 0:
                self.head = i
                self.tail = None

#----------------------------------------------------------------------

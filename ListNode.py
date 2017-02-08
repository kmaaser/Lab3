#----------------------------------------------------------------------
# ListNode.py
# Karenna Maaser
# 01/28/2012
#----------------------------------------------------------------------

import sys

#----------------------------------------------------------------------

class ListNode:

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

        pass

#----------------------------------------------------------------------
    def __setitem__(self, position, value):

        '''set data item at location position to value
        pre: 0 <= position < self.size
        post: sets the data item at the specified position to value'''

        pass

#----------------------------------------------------------------------
    def __delitem__(self, position):

        '''delete item at location position from the list
        pre: 0 <= position < self.size
        post: the item at the specified position is removed from the list'''

        pass

#----------------------------------------------------------------------
    def _delete(self, position):

        '''private method to delete item at location position from the list
        pre: 0 <= position < self.size
        post: the item at the specified position is removed from the list'''

        if position == 0:
            item = self.head.item
            self.head = self.head.link
        else:
            node = self._find(position -1)
            item = node.link.item
            node.link = node.link.link
        self.size -= 1

#----------------------------------------------------------------------
    def append(self, x):

        '''appends x onto end of the list
        pre: none
        post: x is appended onto the end of the list'''

        pass

#----------------------------------------------------------------------
    def insert(self, i, x):

        '''inserts x before position i in the list
        pre: 0 <= i <= self.size
        post: x is inserted into the list before position i'''

        newNode = ListNode(x)

        if self.size == 0:
            self.head = newNode
            self.tail = newNode
            self.size += 1
        else:
            node = self._find(i - 1)
            newNode.link = node.link
            node.link = newNode
            self.size +=1

#----------------------------------------------------------------------
    def pop(self, i=None):

        '''returns and removes at position i from list; the default is to
        return and remove the last item
        pre: self.size > 0 and ((i is None or (0 <= i < self.size))
        post: if i is None, the last item in the list is removed and returned
        otherwise the item at position i is removed and returned'''

        pass

#----------------------------------------------------------------------
    def index(self, x, start=0):

        '''return position of first occurrence of x in the list starting
        at position start
        pre: start >= 0
        post: if x is in the list from position start to the end, the position
        it is located at is returned, otherwise a ValueError is raised'''

        pass

#----------------------------------------------------------------------
    def remove(self, x):
        '''removes the first instance of x from the list
        pre: None
        post: if x is in the list, the first instance of x is removed from
        the list, otherwise a ValueError is raised'''

        pass

#----------------------------------------------------------------------
    def extend(self, l):
        '''add each element of list l onto the list
        pre: none
        post: each item in the list l is appended onto the list'''

        pass

#----------------------------------------------------------------------
    def __copy__(self):
        '''returns a new LList that contains the same items as self'''

        pass

#----------------------------------------------------------------------

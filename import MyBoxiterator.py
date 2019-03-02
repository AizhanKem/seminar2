from myboxiterator import MyBoxIterator

class MyBox:
  def__init__(self):
    self.theItems=list()
  def__len__(self):
    return len(self._theItems)
  def add(self, item):
    self._theItems.append(item)
  def remove(self, item):
    self._theItems.pop(item)
  def__contains__(self, item):
    return item in self._theItems
  def __iter__(self):
    return MyBoxIterator (self._theItems)
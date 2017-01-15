class arr_utils:
   'Common base class for manipulating arrays'


   def __init__(self, arr):
      self.arr = arr

   def index_based_extract(self,number):
       return self.arr[number]

# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 11:14:10 2021

@author: yujie
"""

def reverse(self, x):
      """
      :type x: int
      :rtype: int
      """
      sign = -1 if x < 0 else 1
      x *= sign
      # Remove leading zero in the reversed integer
      while x:
          if x % 10 == 0:
              x /= 10
          else:
              break
      # string manipulation
      x = str(x)
      lst = list(x)  # list('234') returns ['2', '3', '4']
      lst.reverse()
      x = "".join(lst)
      x = int(x)
      return sign*x

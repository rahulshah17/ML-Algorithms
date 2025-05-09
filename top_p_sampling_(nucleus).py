# -*- coding: utf-8 -*-
"""Top P Sampling (Nucleus).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WZEp-a57aqf5I_Cg_LtOfOR6OG8BmKux
"""

import numpy as np

def nucleusFun(next_word_list,p):
  next_word_list = sorted(next_word_list,key=lambda x:x[1],reverse=True)

  words = []
  probs = []

  for w,pr in next_word_list:
    if(p>=0):
      words.append(w)
      probs.append(pr)
      p-=pr

  probs = np.array(probs)
  probs/= probs.sum()

  ans = np.random.choice(words,p=probs)
  return ans

next_word_list = [('books',0.43),('laptops',0.37),('eyes',0.2)]
p = float(input("Enter the p value between 0 and 1 "))
nucleusFun(next_word_list,p)
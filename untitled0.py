# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1USnsUA98ao1j686DizDgDsXq_yKZ2VOR
"""

score = input().split()
countF = 0
for s in score:
  if s < 60:
    countF += 1

print(countF)
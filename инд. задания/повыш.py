#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Дано предложение. Найти длину его самого короткого слова..
if __name__ == '__main__':
    s = str(input('Введите предложение:\n'))
    s = s.split()
    k = (min(s, key = len))
    print(len(k))
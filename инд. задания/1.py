#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#дан текст. Сколько раз в нем встречается
#символ "+" и символ "*"
if __name__ == '__main__':
    s = str(input('Введите предложение:\n'))
    k = len(s)
    count1 = 0
    count2 = 0
    for i in range(0, k):
        if s[i] == "+":
            count1 +=1
        elif s[i] == "*":
            count2 +=1
    print(count1)
    print(count2)




#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Дано предложение. Заменить в нем все вхождения буквосочетания про на нет.
if __name__ == '__main__':
    s = str(input('Введите предложение:\n'))
    s = s.replace("про", "нет")
    print(s)
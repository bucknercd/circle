#!/usr/bin/python

import pygame
import sys
import math


class Circle(object):
    dic = {}

    def __init__(self, radius, name):
        self.radius = int(radius) * 3 / 4
        self.diam = self.radius * 2
        self.name = name
        self.point = (-1000, -1000)
        self.key = "center"

    def getRad(self):
        return self.radius

    def __str__(self):
        return "{0} : {1} : {2}->> {3}".format(self.name, self.radius, self.point, self.key)


def parse_line(line, clist):
    tokens = line.split(",")
    for i in range(0, len(tokens), 2):
        try:
            c1 = Circle(tokens[i], tokens[i + 1])
            clist.append(c1)
        except IndexError:
            break


def add(center_circ, circ, state, layer, ptDic, snum):
    mstates = ['e', 'w']
    key = str(layer) + state
    oldkey = ""
    old_diam = 0

    try:
        oldkey = str(layer - 1) + state
        old_diam = ptDic[oldkey].diam
    except KeyError:
        pass
    rad = center_circ.radius + circ.radius
    if layer == 1:
        rad += old_diam
    if layer > 1:
        for i in range(layer - 1):
            key = str(i) + state
            old_diam += ptDic[key].diam
        rad += old_diam
    p1 = center_circ.point

    cp2 = (0, 0)
    if state == 'e':
        cp2 = (p1[0] + rad, p1[1])
        circ.key = str(layer) + "e"
    if state == 'w':
        cp2 = (p1[0] - rad, p1[1])
        circ.key = str(layer) + "w"
    circ.point = cp2
    ptDic[key] = circ

    p20 = 0
    p21 = 0
    if state not in mstates:
        if layer == 0:
            a = center_circ.radius
            ppnt = center_circ.point
        elif layer > 0:
            prev = str(layer - 1) + state
            a = ptDic[prev].radius
            ppnt = ptDic[prev].point

        c = a + circ.radius
        b = c**2 - a**2
        b = int(math.sqrt(b))

        if state == 'ne':
            b *= -1
        if state == 'se':
            pass
        if state == 'nw':
            a *= -1
            b *= -1
        if state == 'sw':
            a *= -1
        p20 = ppnt[0] + a
        p21 = ppnt[1] + b
        key = str(layer) + state
        circ.point = (p20, p21)
        circ.key = key
        ptDic[key] = circ


wstart = 600
hstart = 400
win_len = 1200
win_height = 900

pygame.init()
green = (0, 255, 0)
darkBlue = (0, 0, 128)
screen = pygame.display.set_mode((win_len, win_height))
screen.fill(green)
pygame.display.update()
clist = []
ptDic = {}

while True:
    try:
        line = raw_input()
    except EOFError:
        break
    parse_line(line, clist)

sort_list = sorted(clist, key=Circle.getRad)
sort_list.reverse()
sort_list[0].point = (wstart, hstart)
states = ['w', 'e', 'sw', 'ne', 'se', 'nw']

layer = 0
state = 0
centerc = sort_list[0]
for i in range(1, len(sort_list)):
    if state > 5:
        state = 0
        layer += 1
    add(centerc, sort_list[i], states[state], layer, ptDic, state)
    state += 1
for i in sort_list:
    pygame.draw.circle(screen, darkBlue, i.point, i.radius, 2)
    pygame.display.update()
    print(i)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

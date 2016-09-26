#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import

import pwndbg.heap.dlmalloc
import pwndbg.heap.heap
import pwndbg.heap.ptmalloc

current = pwndbg.heap.heap.Heap()

@pwndbg.events.new_objfile
def update():
    global current


    if pwndbg.symbol.get('ptmalloc_init'):
      current = pwndbg.heap.ptmalloc.Heap()

    elif pwndbg.symbol.get('malloc_stats'):
      current = pwndbg.heap.dlmalloc.Heap()

#!/usr/bin/env python


def as_we_can(func):
    print(func.__name__)

@as_we_can
def fuck():
    print("oh_yeah")

fuck()

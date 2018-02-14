#!/bin/env python3
# Flask is our webserver. It handles serving and interacting with our
# web front-end. Socket the connection. 
import flask
from flask_socketio import SocketIO

# Rx (ReactiveX) gives us the ability to create asynchronous streams
# so our webpage can interact with events quickly
import rx
from rx import Observable, Observer

# Direct imports from python stdlib
import os
import sys
import argparse
import trace

# Add lib folder to python runtime path inorder to import desired algorithms
from sortlib import bubble_sort, quick_sort, merge_sort, selection_sort, heap_sort

def main():
    print("hello world!")

if __name__ == '__main__':
    main()

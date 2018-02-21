#!/bin/env python3
# Flask is our webserver. It handles serving and interacting with our
# web front-end. Socket the connection.
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

# Direct imports from python stdlib
# import os
# import sys
# import argparse
# import trace
import webbrowser

# Add lib folder to python runtime path inorder to import desired algorithms
# from sortlib import
#   bubble_sort, quick_sort, merge_sort, selection_sort, heap_sort


###############################################################################
# 1. We are going to define our flask main route to render our main page
#    template
# 2. We are going to setup socketed events for our application
# 4. Define default browser to open up our application
###############################################################################
app = Flask(__name__)
socketio = SocketIO(app)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@socketio.on('connect')
def connect_msg():
    print("The browser is now connected to me")
    emit('serverEvent', {'data': 'Server connected, so I emitted this data'})


@socketio.on('browserEvent')
def browser_event(eventMsg):
    print("The browser had an event!")
    print(eventMsg)


def main():
    print("hello world!")


if __name__ == '__main__':
    webbrowser.open("http://localhost:5000", 2, autoraise=True)
    socketio.run(app)

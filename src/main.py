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

import NumberList as nl #holds the data
import State as st #holds state of algorithm
import Algorithm as alg #holds algorithm 

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

algorithm = False
numberList = False
state = False

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@socketio.on('connect')
def connect_msg():
	print("The browser is now connected to me")
	
@socketio.on('startSorting')
def startSorting(data):
	global numberList
	global state
	global algorithm 

	algorithm=alg.Algorithm(True, data['choice'])
	
	if('file' in data.keys()):
		algorithm.importText(data['file']);
	else:
		algorithm.setRandomData(data['size'])

	state=algorithm.getState()

	emit('sorting', {'numbers':algorithm.getData(), 'compares':state.compares, 'swaps':state.swaps, 'memUsage':state.memUsage, 'runtime':state.runtime, 'currentLine':state.currentLine})


@socketio.on('step')
def step():
	global state

	if(not state.sorting):
		emit('doneSorting')
	else:
		algorithm.step()
		emit('sorting', {'numbers':algorithm.getData(), 'compares':state.compares, 'swaps':state.swaps, 'memUsage':state.memUsage, 'runtime':state.runtime, 'currentLine':state.currentLine, 'i':state.i, 'j':state.j})

@socketio.on('browserEvent')
def browser_event(eventMsg):
	print("The browser had an event!")
	print(eventMsg)


def main():
	print("hello world!")

if __name__ == '__main__':
	webbrowser.open("http://localhost:5500", 2, autoraise=True)
	socketio.run(app, port=5500)

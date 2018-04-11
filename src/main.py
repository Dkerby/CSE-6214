#!/bin/env python3

from flask import Flask, render_template
from flask_socketio import SocketIO, emit

# Direct imports from python stdlib
# import os
# import sys
# import argparse
# import trace
import webbrowser

# import NumberList as nl
# import State as st
import Algorithm as alg

app = Flask(__name__)
socketio = SocketIO(app)

algorithm = False
numberList = False
state = False


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@socketio.on('startSorting')
def startSorting(data):
    global state
    global algorithm

    algorithm = alg.Algorithm(True, data['choice'], data['speed'])

    if ('file' in data.keys()):
        algorithm.importText(data['file'])
    else:
        algorithm.setRandomData(data['size'])

    state = algorithm.getState()

    emit('sorting', {'numbers': algorithm.getData(),
                     'compares': state.compares,
                     'swaps': state.swaps,
                     'memUsage': state.memUsage,
                     'runtime': str("{0:.1f}".format(state.runtime)),
                     'currentLine': state.currentLine})


@socketio.on('startBenchmarks')
def startBenchmarks(data):
    global algorithm
    global state

    # pass State object into Algorithm along with the choice of algorithm
    algorithm = alg.Algorithm(True, 1, 0.0001, data['size'])

    state = algorithm.getState()
    algorithm.benchsetup(data['size'])
    runBenchmarks()


@socketio.on('benchmark')
def runBenchmarks():
    global algorithm
    global state
    if state.benchmarking:
        algorithm.benchstep()
        state = algorithm.getState()
        emit('benchmarks', {'compares': state.compares,
                            'swaps': state.swaps,
                            'memUsage': state.memUsage,
                            'runtime': state.runtime,
                            'sorting': state.sorting})
    else:
        emit('doneBenchmarking')


@socketio.on('step')
def step():
    global state
    if(not state.sorting):
            emit('doneSorting')
    else:
            algorithm.step()
            emit('sorting', {'numbers': algorithm.getData(),
                             'compares': state.compares,
                             'swaps': state.swaps,
                             'memUsage': state.memUsage,
                             'runtime': str("{0:.1f}".format(state.runtime)),
                             'currentLine': state.currentLine,
                             'i': state.i,
                             'j': state.j})


if __name__ == '__main__':
    webbrowser.open("http://localhost:5555", new=0, autoraise=True)
    socketio.run(app, port=5555)

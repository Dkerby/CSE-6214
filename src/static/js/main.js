

var socket = io.connect('http://' + document.domain + ':' + location.port);
socket.on('connect', function() { 
	console.log("Server connected");
	socket.emit('browserEvent', {data: 'Browser connected, so I emitted this data'});
});

socket.on('serverEvent', function(eventMsg) {
	console.log("Server event:");
	console.log(eventMsg);
});

socket.on('sorting', function(data) {
	step(data.numbers, data.i, data.j);
	updateState(data);
	highlightLine(data.currentLine);
	if (playing) socket.emit("step");
});

socket.on('doneSorting', function() {
	stop();
	highlightLine(-1);
});

var sort = "Merge";
var file = "";
var playing = false;

var psudocode = {
	"Merge": [
	"midpoint = length / 2</br>left_half = merge_sort(array[:midpoint])</br>right_half = merge_sort(array[midpoint:])",
	"i,j,k = 0</br>left_length = len(left_half)</br>right_length = len(right_half)",
	"while i < left_length and j < right_length:",
	"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if left_half[i] < right_half[j]:</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;array[k] = left_half[i]</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;i += 1",
	"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;else:</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;array[k] = right_half[j]</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;j += 1</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;k += 1",
	"while i < left_length:",
	"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;array[k] = left_half[i]</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;i += 1</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;k += 1",
	"while j < right_length:",
	"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;array[k] = right_half[j]</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;j += 1</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;k += 1"
	], "Bubble": [
	"for i in range(len(array)):",
	"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;for j in range(len(array)-1):",
	"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if array[j] > [j+1]:",
	"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;array[j], array[j+1] = array[j+1], array[j]"
	], "Insertion": [
	"</br>for i in range(1, len(array)):",
	"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;while 0 < index and array[index] < array[index - 1]:</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;array[index], array[index - 1] = array[index - 1], array[index]</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;index -= 1"
	], "Heap": [
	"Line of",
	"Psudocode for",
	"Heapsort"
	], "Quick": [
	"if( len(array) <= 1):</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return",
	"else:</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pivot = len(array)-1</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;i=0",
	"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;for j in array:",
	"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if j <= array[pivot]:",
	"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;i++</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;array[i], j = j, array[i]",
	"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;array[i+1], array[pivot] = array[pivot], array[i+1]",
	"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;QuickSort(array[:i+1])</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;QuickSort(array[i+2:])"
	],
}

function chooseAlgorithm(choice) {
	document.getElementById("algorithm").innerHTML = choice + " Sort";
	sort = choice;
	showPsudocode(choice);
}

var barChart;

function step(list, i, j) {
	var ctx = document.getElementById("numbers");
	
	var colors = [];
	for (var each in list) {
		if (each == i) colors.push('rgb(58, 94, 150)');
		else if (each == j) colors.push('rgb(72, 138, 242)');
		else colors.push('rgb(175, 203, 247)');
	}
	
	

	if(!barChart) {
		var data = {
label: 'Randomly Generated List',
data: list,
backgroundColor: colors
		};
		
		barChart = new Chart(ctx, {
type: 'bar',
data: {
labels: list,
datasets: [data]
			}, 
options: {
animation: {
duration: 0
				},
legend: {
display: false
				},
tooltips: {
callbacks: {
label: function(tooltipItem) {
							return tooltipItem.yLabel;
						}
					}
				}
			}, 
		});	
	} else {
		for (var i in list) {
			barChart.data.datasets[0].data[i] = list[i];
			barChart.data.datasets[0].backgroundColor[i] = colors[i];
		}
		barChart.data.labels = list;
		barChart.update();
	}
}

function fileUploaded(fileLoaded) {
	if(fileLoaded.name.substring(fileLoaded.name.length-4) != ".txt") {
		document.getElementById("error").innerHTML = "Only .txt files are supported";
		return;
	} else if (document.getElementById("error").innerHTML == "Only .txt files are supported") {
		document.getElementById("error").innerHTML = "";
	}
	
	file = fileLoaded;
}

function play() {
	if(barChart) {
		barChart.data.datasets[0].data = [];
		barChart.data.datasets[0].backgroundColor = [];
		barChart.data.labels = [];
	}
	
	document.getElementById("stats").style.opacity = "1";
	playing = true;
	var sortData = {};
	switch(sort) {
	case 'Merge':
		sortData.choice = 4;
		break;
	case 'Bubble':
		sortData.choice = 2;
		break;
	case 'Insertion':
		sortData.choice = 1;
		break;
	case 'Heap':
		sortData.choice = 5
		break;
	case 'Quick':
		sortData.choice = 3;
		break;
	}
	
	if (file) sortData.file = file;
	else sortData.size = parseInt(document.getElementById("sizeSlider").value);
	socket.emit('startSorting', sortData);
	document.getElementById('play').innerHTML = "Stop";
	document.getElementById('play').onclick = stop;
	document.getElementById('pause').style.opacity = "1";
	document.getElementById('pause').innerHTML = "Pause";
	showPsudocode(sort);
}

function showPsudocode(sort) {
	document.getElementById("psudocode").innerHTML = "";
	for(var line in psudocode[sort]) {
		var code = document.createElement("p");
		code.innerHTML = psudocode[sort][line];
		code.id = line;
		code.style.fontSize = "13px";
		code.style.lineHeight = "14px";
		document.getElementById("psudocode").appendChild(code);
	}
}

function highlightLine(line) {
	var children = document.getElementById("psudocode").children;
	for (var i in children) {
		if(i == "length") break;
		if (i == line) {
			children[i].style.backgroundColor = "yellow";
		} else {
			children[i].style.backgroundColor = "white";
		}
	}
}

function stop() {
	document.getElementById('play').innerHTML = "Play";
	document.getElementById('play').onclick = play;
	document.getElementById('pause').style.opacity = "0";
	playing = false;
}

function pause() {
	if(playing) {
		playing = false;
		document.getElementById('pause').innerHTML = "Play";
	} else {
		playing = true;
		socket.emit("step");
		document.getElementById('pause').innerHTML = "Pause";
	}
}

function updateSliderValue() {
	document.getElementById("sliderValue").innerHTML = document.getElementById("sizeSlider").value;
}

function updateState(state) {
	document.getElementById("compares").innerHTML = state.compares;
	document.getElementById("swaps").innerHTML = state.swaps;
	document.getElementById("memory").innerHTML = state.memUsage;
}

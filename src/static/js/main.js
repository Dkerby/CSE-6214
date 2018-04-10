var socket = io.connect('http://' + document.domain + ':' + location.port);

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

socket.on('benchmarks', function(state) {
    updateBenchmarkChart(state);
    document.getElementById("stats").style.opacity = 0;
    if(!state.sorting) {
        algorithm++; 
        algorithmName = algorithms[algorithm];
    }
    if (playing) socket.emit("benchmark");
});

var sort = "Merge";
var file = "";
var playing = false;
var algorithm = 1;
var algorithms = ["", "Insertion Sort", "Bubble Sort", "Quick Sort", "Merge Sort", "Heap Sort"];
var algorithmName = algorithms[algorithm];
var speed="Medium";

var psudocode = {
    "Merge Sort": [
        "midpoint = length / 2</br>left_half = merge_sort(array[:midpoint])</br>right_half = merge_sort(array[midpoint:])",
        "i,j,k = 0</br>left_length = len(left_half)</br>right_length = len(right_half)",
        "while i < left_length and j < right_length:",
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if left_half[i] < right_half[j]:</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;array[k] = left_half[i]</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;i += 1",
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;else:</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;array[k] = right_half[j]</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;j += 1</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;k += 1",
        "while i < left_length:",
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;array[k] = left_half[i]</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;i += 1</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;k += 1",
        "while j < right_length:",
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;array[k] = right_half[j]</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;j += 1</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;k += 1"
    ], "Bubble Sort": [
        "for i in range(len(array)):",
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;for j in range(len(array)-1):",
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if array[j] > [j+1]:",
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;array[j], array[j+1] = array[j+1], array[j]"
    ], "Insertion Sort": [
        "</br>for i in range(1, len(array)):",
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;while 0 < index and array[index] < array[index - 1]:</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;array[index], array[index - 1] = array[index - 1], array[index]</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;index -= 1"
    ], "Heap Sort": [
        "def heapify(array, index, heap_size):",
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;largest = index</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;left_index = 2 * index + 1</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;right_index = 2 * index + 2",
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if left_index < heap_size and array[left_index] > array[largest]:</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;largest = left_index</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if right_index < heap_size and array[right_index] > array[largest]:</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;largest = right_index</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if largest != index:</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;array[largest], array[index] = array[index], array[largest]</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;heapify(array, largest, heap_size)",
        "",
        "def heapsort(array):",
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;n = len(array)",
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;for i in range(n // 2 - 1, -1, -1):</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;heapify(array, i, n)",
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;for j in range(n - 1, 0, -1):</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;array[0], array[j] = array[j], array[0]</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;heapify(array, 0, j)",
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return array"
    ], "Quick Sort": [
        "if( len(array) <= 1):</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return",
        "else:</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pivot = len(array)-1</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;i=0",
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;for j in array:",
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if j <= array[pivot]:",
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;i++</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;array[i], j = j, array[i]",
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;array[i+1], array[pivot] = array[pivot], array[i+1]",
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;QuickSort(array[:i+1])</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;QuickSort(array[i+2:])"
    ], "Default": [
        "Lines of",
        "Psudocode for",
        "Sorting go here"
    ],
}

function setAlgorithm() {
    choice = document.getElementById('algorithm').value;
    sort = choice;
    showPsudocode(choice);
}

function setSpeed() {
    choice = document.getElementById('speed').value;
    speed = choice;
}

function setList(choice) {
    console.log(choice);
    switch(choice) {
        case "upload":
            document.getElementById("file-upload").style.display = "block";
            document.getElementById("generate-list").style.display = "none";
            break;
        case "generate":
            document.getElementById("file-upload").style.display = "none";
            document.getElementById("generate-list").style.display = "block";
            break;
    }
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


function updateBenchmarkChart(state) {
    var ctx = document.getElementById("numbers");
    if (!algorithmName) return;

    var colors = ["purple", "rgb(19, 54, 112)", "rgb(167, 184, 214)", "rgb(10, 22, 43)", "rgb(91, 125, 183)", "rgb(5, 69, 178)"];
    var color = colors[algorithm];

    if(!barChart) {
        var data = {
            label: algorithmName,
            data: [state.swaps, state.compares, state.memUsage, state.runtime],
            backgroundColor: color
        };

        barChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: ["swaps", "compares", "memory", "runtime"],
                datasets: [data]
            }, 
            options: {	
                animation: {
                    duration: 0
                },
                legend: {
                    display: true
                },
                scales: {
                    yAxes: [{
                        type: 'linear'
                    }]},
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
        var list = [state.swaps, state.compares, state.memUsage, state.runtime];
        var label = algorithmName;
        if (barChart.data.datasets.length-1 < algorithm-1) {
            barChart.data.datasets.push( {
                label: label,
                data: [state.swaps, state.compares, state.memUsage, state.runtime],
                backgroundColor: color
            });
        }

        for (var i in list) {
            barChart.data.datasets[algorithm-1].data[i] = list[i];
        }
        barChart.data.labels = ["swaps", "compares", "memory", "runtime"];

        barChart.update();
    }
}

function fileUploaded(fileLoaded) {
    if(fileLoaded.name.substring(fileLoaded.name.length-4) != ".txt") {
        alert("Only .txt files are supported");
    } else {
        file = fileLoaded;
    }
}

function play() {
    showPsudocode(sort);
    algorithm = 1;

    if(barChart) {
        barChart.destroy();
        barChart = false;
    }

    document.getElementById("stats").style.opacity = "1";
    playing = true;
    var sortData = {};
    switch(sort) {
        case 'Merge Sort':
            sortData.choice = 4;
            break;
        case 'Bubble Sort':
            sortData.choice = 2;
            break;
        case 'Insertion Sort':
            sortData.choice = 1;
            break;
        case 'Heap Sort':
            sortData.choice = 5
            break;
        case 'Quick Sort':
            sortData.choice = 3;
            break;
        case 'Run Benchmark':
            sortData.choice = -1;
            break;
    }

    switch(speed){
        case 'Slow':
            sortData.speed=0.05;
            break;
        case 'Medium':
            sortData.speed=0.025;
            break;
        case 'Fast':
            sortData.speed=0.001;
            break;
        case 'Ludicrous Speed':
            sortData.speed=0.0;
            break;
    }

    if (sortData.choice < 0) sortData.speed = 0.0;

    if (file) sortData.file = file;
    else sortData.size = parseInt(document.getElementById("sizeSlider").value);

    document.getElementById('playpause').innerText = "stop";
    document.getElementById('playpause').onclick = stop;
    if (sortData.choice > 0) {
        socket.emit('startSorting', sortData);
        document.getElementById('pause').style.opacity = "1";
        document.getElementById('pause').innerHTML = "Pause";
    } else {
        socket.emit('startBenchmarks', sortData);
    }
}

function showPsudocode(sort) {
    if (sort == "Run Benchmark") {
        document.getElementById("psudocode-container").style.display = "none";
        document.getElementById("pause").addAttribute("disabled");
        return;
    }

    document.getElementById("psudocode").innerHTML = "";
    document.getElementById("pause").disabled = false;

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
    document.getElementById('playpause').innerText = "play_arrow";
    document.getElementById('playpause').onclick = play;
    document.getElementById('pause').style.opacity = "0";
    playing = false;
}

function pause() {
    if(playing) {
        playing = false;
        document.getElementById('pause').innerHTML = '<i class="material-icons">play_arrow</i><span> Resume </span>';
        document.getElementById('step').style.opacity = "1";
    } else {
        playing = true;
        socket.emit("step");
        document.getElementById('pause').innerHTML = '<i class="material-icons">pause</i><span> Pause </span>';
        document.getElementById('step').style.opacity = "0";
    }
}

function updateSliderValue() {
    document.getElementById("sliderValue").innerHTML = document.getElementById("sizeSlider").value;
}

function updateState(state) {
    document.getElementById("compares").innerHTML = state.compares;
    document.getElementById("swaps").innerHTML = state.swaps;
    document.getElementById("memory").innerHTML = state.memUsage;
    document.getElementById("runtime").innerHTML = state.runtime;
}

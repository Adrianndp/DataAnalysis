function menu() {
    if (document.getElementById("mySidebar").style.display === "none") {
        document.getElementById("mySidebar").style.display = "block";
        document.getElementById("main").style.marginLeft = "300px";
    } else {
        document.getElementById("mySidebar").style.display = "none";
        document.getElementById("main").style.marginLeft = "0";
    }
}

function get_graph(data) {
    let options = {
        chart: {
            width: '100%',
            type: 'candlestick',
            animations: {
                enabled: false
            },
        },
        series: [{
            data: data
        }],
        title: {
            text: 'AAPL',
            align: 'left'
        },
        tooltip: {
            enabled: true,
        },
        xaxis: {
            type: 'datetime',
            valueFormatString: "MMM DD"
        },
        yaxis: {
            decimalsInFloat: 0,
            tooltip: {
                enabled: true
            }
        }
    }
    // -------------------------
    let chart = new ApexCharts(
        document.querySelector("#chart"),
        options
    );
    chart.render();

}

function handle_data(data) {
    let length = Object.keys(data.Date).length;
    let filtered_data = [];
    let object = {}
    for (let i = length; i > 0; i--) {
        object = {
            x: new Date(data.Date[i]),
            y: [data.Open[i], data.High[i], data.Low[i], data.Close[i]]
        };
        filtered_data.push(object);
        object = {};
    }
    get_graph(filtered_data);
}

function fetch_data(stock) {
    fetch(`http://localhost:5000/get_graph_api?stock=${stock}`)
        .then(response => response.json())
        .then(data => handle_data(data));
}




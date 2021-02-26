function menu() {
    if (document.getElementById("mySidebar").style.display === "none") {
        document.getElementById("mySidebar").style.display = "block";
        document.getElementById("main").style.marginLeft = "300px";
    } else {
        document.getElementById("mySidebar").style.display = "none";
        document.getElementById("main").style.marginLeft = "0";
    }
}

function get_graph(data, EMA, stock_title) {
    let options = {
        series: [
            {
                name: 'EMA',
                type: 'line',
                data: EMA
            },
            {
                name: 'candle',
                type: 'candlestick',
                data: data
            }],
        chart: {
            width: '100%',
            animations: {
                enabled: false
            },
            type: 'line',
        },
        stroke: {
            width: [3, 1]
        },
        title: {
            text: stock_title,
            align: 'left'
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
    document.getElementById("button").style.display = "block";
    document.getElementById("stock_image").style.display = "block";
    document.getElementById('stock').value = "";

}

function handle_data(data, stock_title, window_size) {
    let ema_window_size = window_size;
    let length = Object.keys(data.Date).length;
    let filtered_data = [];
    let EMA = [];
    let object = {};
    let ema_object = {};
    for (let i = ema_window_size; i < length + ema_window_size; i++) {
        object = {
            x: new Date(data.Date[i]),
            y: [data.Open[i], data.High[i], data.Low[i], data.Close[i]]
        };
        filtered_data.push(object);
        object = {};
        ema_object = {
            x: new Date(data.Date[i]),
            y: data.EMA[i]

        };
        EMA.push(ema_object);
        ema_object = {};
    }
    get_graph(filtered_data, EMA, stock_title);
}

function fetch_data(stock, window_size) {
    stock = stock.toUpperCase()
    fetch(`http://localhost:5000/get_graph_api?stock=${stock}`)
        .then(response => response.json())
        .then(data => handle_data(data, stock, window_size));
}


function show_prediction() {
     document.getElementById("stock_image").style.display = "none";
     document.getElementById("chart-container").style.display = "block";
     document.getElementById("link").style.display = "block";
}



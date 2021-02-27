function menu() {
    if (document.getElementById("mySidebar").style.display === "none") {
        document.getElementById("mySidebar").style.display = "block";
        document.getElementById("main").style.marginLeft = "300px";
    } else {
        document.getElementById("mySidebar").style.display = "none";
        document.getElementById("main").style.marginLeft = "0";
    }
}

function get_graph(data, SMA, stock_title) {
    let options = {
        series: [
            {
                name: 'SMA',
                type: 'line',
                data: SMA
            },
            {
                name: 'Price',
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
        tooltip: {
            enabled: true,
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
    get_RSI();
    document.getElementById("button").style.display = "block";
    document.getElementById("stock_image").style.display = "block";
    document.getElementById('stock').value = "";

}

function handle_data(data, stock_title, window_size) {
    let sma_window_size = window_size;
    let length = Object.keys(data.Date).length;
    let filtered_data = [];
    let SMA = [];
    let object = {};
    let sma_object = {};
    for (let i = sma_window_size; i < length + sma_window_size; i++) {
        object = {
            x: new Date(data.Date[i]),
            y: [data.Open[i], data.High[i], data.Low[i], data.Close[i]]
        };
        filtered_data.push(object);
        object = {};
        sma_object = {
            x: new Date(data.Date[i]),
            y: data.SMA[i]

        };
        SMA.push(sma_object);
        sma_object = {};
    }
    get_graph(filtered_data, SMA, stock_title);
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

function fetch_news_api(keyword) {
    fetch(`http://localhost:5000/get_news_api?keyword=${keyword}`)
        .then(response => response.json())
        .then(data => console.log(data));
}

function get_RSI() {
    let options = {
        chart: {
            height: 280,
            type: "area"
        },
        dataLabels: {
            enabled: false
        },
        title: {
            text: 'RSI',
            align: 'left',
        },
        series: [
            {
                name: "Series 1",
                data: [45, 52, 38, 45, 19, 23, 2]
            }
        ],
        fill: {
            type: "gradient",
            gradient: {
                shadeIntensity: 1,
                opacityFrom: 0.7,
                opacityTo: 0.9,
                stops: [0, 90, 100]
            }
        },
        xaxis: {
            categories: [
                "01 Jan",
                "02 Jan",
                "03 Jan",
                "04 Jan",
                "05 Jan",
                "06 Jan",
                "07 Jan"
            ]
        }
    };

    let chart = new ApexCharts(document.querySelector("#RSI"), options);
    chart.render();
}


function menu() {
    if (document.getElementById("mySidebar").style.display === "none") {
        document.getElementById("mySidebar").style.display = "block";
        document.getElementById("main").style.marginLeft = "300px";
    } else {
        document.getElementById("mySidebar").style.display = "none";
        document.getElementById("main").style.marginLeft = "0";
    }
}

function get_graph(data, EMA, stock_title, RSI, date_list) {
    let options = {
        series: [
            {
                name: 'EMA',
                type: 'line',
                data: EMA
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
            custom: function ({seriesIndex, dataPointIndex, w}) {
                const o = w.globals.seriesCandleO[seriesIndex][dataPointIndex]
                const h = w.globals.seriesCandleH[seriesIndex][dataPointIndex]
                const l = w.globals.seriesCandleL[seriesIndex][dataPointIndex]
                const c = w.globals.seriesCandleC[seriesIndex][dataPointIndex]
                return (
                    '<div class="apexcharts-tooltip-candlestick">' +
                    '<div>Open: <span class="value">' +
                    o +
                    '</span></div>' +
                    '<div>High: <span class="value">' +
                    h +
                    '</span></div>' +
                    '<div>Low: <span class="value">' +
                    l +
                    '</span></div>' +
                    '<div>Close: <span class="value">' +
                    c +
                    '</span></div>' +
                    '</div>'
                )
            }
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
        },
    }
    // -------------------------
    let chart = new ApexCharts(
        document.querySelector("#chart"),
        options
    );
    chart.render();
    get_RSI(RSI, date_list);
    document.getElementById("button").style.display = "block";
    document.getElementById("stock_image").style.display = "block";
    document.getElementById('stock').value = "";

}

function handle_data(data, stock_title, window_size) {
    let sma_window_size = window_size;
    let length = Object.keys(data.Date).length;
    let filtered_data = [];
    let EMA = [];
    let RSI = [];
    let object = {};
    let ema_object = {};
    let date_list = [];

    for (let i = sma_window_size; i < length + sma_window_size; i++) {
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
        RSI.push(data.RSI[i]);
        date_list.push(data.Date[i].getTime());


    }
    get_graph(filtered_data, EMA, stock_title, RSI, date_list);
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

function get_RSI(RSI, dates) {
    let options = {
        chart: {
            height: 280,
            type: "area",
             animations: {
                enabled: false
            },
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
                data: RSI,
                decimalsInFloat: 0,
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
            categories: dates
        }
    };

    let chart = new ApexCharts(document.querySelector("#RSI"), options);
    chart.render();
}


function menu() {
    if (document.getElementById("mySidebar").style.display === "none") {
        document.getElementById("mySidebar").style.display = "block";
        document.getElementById("main").style.marginLeft = "300px";
    } else {
        document.getElementById("mySidebar").style.display = "none";
        document.getElementById("main").style.marginLeft = "0";
    }
}

function get_graph(data, EMA, stock_title, RSI, range) {
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
            events: {
                beforeZoom: function (ctx) {
                    ctx.w.config.xaxis.range = undefined
                }
            }
        },
        tooltip: {
            enabled: true,
            custom: function ({dataPointIndex, w}) {
                const o = w.globals.seriesCandleO[1][dataPointIndex]
                const h = w.globals.seriesCandleH[1][dataPointIndex]
                const l = w.globals.seriesCandleL[1][dataPointIndex]
                const c = w.globals.seriesCandleC[1][dataPointIndex]
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
            valueFormatString: "MMM DD",
            range: range,
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
    get_RSI(RSI, range);
    document.getElementById("button").style.display = "block";
    document.getElementById("stock_image").style.display = "block";
    document.getElementById('stock').value = "";

}

function handle_data(data, stock_title, window_size) {
    let sma_window_size = window_size;
    let length = Object.keys(data.Date).length;
    let filtered_data = [], EMA = [], RSI = [];
    for (let i = sma_window_size; i < length + sma_window_size; i++) {
        filtered_data.push({x: new Date(data.Date[i]), y: [data.Open[i], data.High[i], data.Low[i], data.Close[i]]});
        EMA.push({x: new Date(data.Date[i]), y: data.EMA[i]});
        RSI.push({x: new Date(data.Date[i]), y: data.RSI[i]});
    }
    let max = new Date().getTime()
    let min = new Date(data.zoom_range).getTime()
    let range = max - min
    get_graph(filtered_data, EMA, stock_title, RSI, range);
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

function get_RSI(RSI, range) {
    let options = {
        chart: {
            height: 280,
            type: "area",
            animations: {
                enabled: false
            },
            events: {
                beforeZoom: function (ctx) {
                    ctx.w.config.xaxis.range = undefined
                }
            }
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
            type: 'datetime',
            tickAmount: 6,
            range: range,
        },
        yaxis: {
            decimalsInFloat: 0,
            tooltip: {
                enabled: true
            }
        },
        tooltip: {
            x: {
                format: 'dd MMM yyyy'
            }
        },

    };

    let chart = new ApexCharts(document.querySelector("#RSI"), options);
    chart.render();
}


$(document).ready(function ($) {
    $(document).on('submit', '#submit-form', function (event) {
        event.preventDefault();
    });
});

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
    console.log("graph")
    document.getElementById("stock_image").style.display = "none";
    document.getElementById('stock').value = "";
    let options = {
        series: [
            {
                name: 'EMA',
                type: 'line',
                data: EMA,
            },
            {
                name: 'Price',
                type: 'candlestick',
                data: data,
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
        colors: ["#026d63"],
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
            width: [3, 1],
            colors: ['#009688']

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
}

function handle_data(data, stock_title, window_size) {
    console.log("im handling")
    document.getElementById('stock_error').style.display = "none";
    document.getElementById('chart').style.display = "block";
    document.getElementById('RSI').style.display = "block";
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
    console.log("im fetching")
    stock = stock.toUpperCase()
    fetch(`http://localhost:5000/get_graph_api?stock=${stock}`)
        .then(response => {
            if (response.ok) {
                return response.json();
            } else {
                throw new Error(`No Data fetched for symbol: ${stock}`);
            }
        })
        .then(data => handle_data(data, stock, window_size))
        .catch((error) => {
            show_error(stock)
        });
}

function show_error(stock) {
    document.getElementById('RSI').style.display = "none";
    document.getElementById('chart').style.display = "none";
    document.getElementById('stock_image').style.display = "none";
    document.getElementById('stock_error').innerHTML = (`No Data fetched for symbol: ${stock}`);
    document.getElementById('stock_error').style.display = "block";

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
        colors: ["#026d63"],
        dataLabels: {
            enabled: false
        },
        title: {
            text: 'RSI',
            align: 'left',
        },
        series: [
            {
                name: "RSI Index",
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
            },
            colors: ['#009688']
        },
        stroke: {
            colors: ['#009688']
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

function show_table(id, tittle) {
    if (document.getElementById(id).style.display === "none") {
        document.getElementById(id).style.display = "block";
        document.getElementById(tittle).style.color = '#162f7a';
    } else {
        document.getElementById(id).style.display = "none";
        document.getElementById(tittle).style.color = '#99a5c8';
    }
}
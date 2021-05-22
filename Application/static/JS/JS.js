$(document).ready(function ($) {
    $(document).on('submit', '#submit-form', function (event) {
        event.preventDefault();
    });
});

function add_active(id) {
    let header = document.getElementById("menu_a_tags");
    let btns = header.getElementsByTagName("a");
    for (let i = 0; i < btns.length; i++) {
        btns[i].className = btns[i].className.replace(" blue", "");
        console.log(btns[i].className)
    }
    document.getElementById(id).className += " blue";
}


function menu() {
    if (document.getElementById("mySidebar").style.display === "none") {
        document.getElementById("mySidebar").style.display = "block";
        document.getElementById("main").style.marginLeft = "300px";
    } else {
        document.getElementById("mySidebar").style.display = "none";
        document.getElementById("main").style.marginLeft = "0";
    }
}


function fetch_data(stock, window_size) {
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

function fetch_stats(stock) {
    fetch(`http://localhost:5000/get_stats_api?stock=${stock}`)
        .then(response => {
            if (response.ok) {
                return response.json();
            } else {
                throw new Error(`No Data fetched for symbol: ${stock}`);
            }
        })
        .then(data => handle_stats(data, stock))
        .catch((error) => {
            show_error(stock, false)
        });
}

function handle_data(data, stock_title, window_size) {
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
    let EMA_title = `EMA_${window_size}`
    get_graph(filtered_data, EMA, stock_title, RSI, range, EMA_title);
}


function handle_stats(data, stock_tittle) {
    show_hide_stats_button();
    document.getElementById('stock_error').style.display = "none";
    document.getElementById('stats').innerHTML = "";
    let node = document.createElement("h1");
    node.style.color = '#0505af'
    let text_node = document.createTextNode(`Statistics of ${stock_tittle}`);
    node.appendChild(text_node);
    document.getElementById("stats").appendChild(node);
    for (let i in data) {
        if (data.hasOwnProperty(i)) {
            let node = document.createElement("h3");
            let text_data;
            if (i === 'Last Dividend') {
                text_data = `${i}:     ${data[i][1]} $`;
            } else {
                text_data = `${i}: ${data[i].toLocaleString()} $`
            }
            let text_node = document.createTextNode(text_data);
            node.appendChild(text_node);
            document.getElementById("stats").appendChild(node);
        }
    }
    document.getElementById('stock').value = "";
    document.getElementById('stats').style.display = 'block'
}


function show_error(stock, charts = true) {
    if (charts) {
        document.getElementById("stats_button").style.display = "none";
        document.getElementById("stats").style.display = "none";
        document.getElementById('RSI').style.display = "none";
        document.getElementById('chart').style.display = "none";
        document.getElementById('stock_image').style.display = "none";
    } else {
        document.getElementById('stats').style.display = 'none'
    }
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
        colors: ["#a152e5"],
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
        stroke: {
            colors: ['#a152e5']
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
    document.getElementById('stats').style.display = "none";
    show_hide_stats_button();
}

function append_element_to_store_id(stock_title) {
    if (document.getElementsByClassName("current_stock_1234").length) {
        document.getElementsByClassName("current_stock_1234")[0].id = stock_title;
    } else {
        let g = document.createElement('div');
        g.setAttribute("id", stock_title);
        g.setAttribute("class", "current_stock_1234");
        document.getElementById('empty_useless_div').appendChild(g);
    }
}

function get_graph(data, EMA, stock_title, RSI, range, EMA_TITLE) {
    append_element_to_store_id(stock_title)
    document.getElementById("stock_image").style.display = "none";
    document.getElementById('stock').value = "";
    let options = {
        series: [
            {
                name: EMA_TITLE,
                type: 'line',
                data: EMA,
            },
            {
                name: 'Price 1 d candles',
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
        colors: ["#005596"],
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
            colors: ['#005596']

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

function show_hide_stats_button() {
    let stats_button = document.getElementById("stats_button");
    if (stats_button.style.display === "none") {
        stats_button.style.display = "block";
    } else {
        stats_button.style.display = "none";
    }

}
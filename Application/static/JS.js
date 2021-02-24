function menu() {
    if (document.getElementById("mySidebar").style.display === "none") {
        document.getElementById("mySidebar").style.display = "block";
        document.getElementById("main").style.marginLeft = "300px";
    } else {
        document.getElementById("mySidebar").style.display = "none";
        document.getElementById("main").style.marginLeft = "0";
    }
}

function get_graph() {
    let options = {
        chart: {
            height: 350,
            type: 'candlestick',
        },
        series: [{
            data: [{
                x: "2020-02-01",
                y: [6629.81, 6650.5, 6623.04, 6633.33]
            },
                {
                    x: "2020-02-02",
                    y: [6632.01, 6643.59, 6620, 6630.11]
                },
                {
                    x: "2020-02-03",
                    y: [6630.71, 6648.95, 6623.34, 6635.65]
                },
                {
                    x: "2020-02-04",
                    y: [6635.65, 6651, 6629.67, 6638.24]
                },
                {
                    x: "2020-02-05",
                    y: [6638.24, 6640, 6620, 6624.47]
                },
                {
                    x: "2020-02-06",
                    y: [6624.53, 6636.03, 6621.68, 6624.31]
                }
            ]
        }],
        title: {
            text: 'AAPL',
            align: 'left'
        },
        xaxis: {
            interval: 1,
            valueFormatString: "MMM"
        },
        yaxis: {
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
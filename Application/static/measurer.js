const dataSource = {
    chart: {
        caption: "Prediction: \n Its a good moment to ...",
        lowerlimit: "0",
        upperlimit: "100",
        theme: "fusion",
        showValue: "0",
        showTickMarks: "0",
        showTickValues: "0",

    },
    colorrange: {
        color: [
            {
                minvalue: "0",
                maxvalue: "20",
                code: "#9b0f0b"
            },
            {
                minvalue: "20",
                maxvalue: "40",
                code: "#F2726F"
            },
            {
                minvalue: "40",
                maxvalue: "60",
                code: "#f2dc6f"
            },
            {
                minvalue: "60",
                maxvalue: "80",
                code: "#53a276"
            },
            {
                minvalue: "80",
                maxvalue: "100",
                code: "#0e753f"
            }
        ]
    },
    dials: {
        dial: [
            {
                value: "81",
            }
        ]
    },
    trendpoints: {
        point: [
            {
                startvalue: "0",
                displayvalue: "Sell",
                thickness: "0",
                color: "#f60909",
            },
            {
                startvalue: "100",
                displayvalue: "Buy",
                thickness: "0",
                color: "#072f03",
            }
        ]
    }
};

FusionCharts.ready(function () {
    var myChart = new FusionCharts({
        type: "angulargauge",
        renderAt: "chart-container",
        width: "30%",
        height: "80%",
        dataFormat: "json",
        dataSource
    }).render();
});
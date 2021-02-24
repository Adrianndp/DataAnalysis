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
                maxvalue: "50",
                code: "#F2726F"
            },
            {
                minvalue: "50",
                maxvalue: "75",
                code: "#FFC533"
            },
            {
                minvalue: "75",
                maxvalue: "100",
                code: "#62B58F"
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
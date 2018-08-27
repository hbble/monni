// Chart.js scripts
// -- Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

//my own charts
function charts(data){
    // -- Cat Pie Chart
    var ctx = document.getElementById("catPieChart");
    var catPieChart = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: data.pie_chart.categories,
            datasets: [{
            data: data.pie_chart.values,
            backgroundColor: ['#007bff', '#dc3545', '#ffc107', '#28a745', '#ff5107'],
            }],
        },
    });
    // -- Area Chart
    var ctx = document.getElementById("topAreaChart");
    var topLineChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: data.line_chart.labels,
            datasets: [{
                label: gettext('Incomes'),
                lineTension: 0.3,
                backgroundColor: "rgba(40, 167, 70,0.2)",
                borderColor: "rgba(40, 167, 70,1)",
                pointRadius: 5,
                pointBackgroundColor: "rgba(40, 167, 70,1)",
                pointBorderColor: "rgba(255,255,255,0.8)",
                pointHoverRadius: 6,
                pointHoverBackgroundColor: "rgba(40, 167, 70,1)",
                pointHitRadius: 20,
                pointBorderWidth: 2,
                data: data.line_chart.values_i,
                cubicInterpolationMode: 'monotone'
            },
            {
                label: gettext('Expenses'),
                lineTension: 0.3,
                backgroundColor: "rgba(244, 66, 66,0.4)",
                borderColor: "rgba(244, 66, 66,1)",
                pointRadius: 5,
                pointBackgroundColor: "rgba(244, 66, 66,1)",
                pointBorderColor: "rgba(255,255,255,0.8)",
                pointHoverRadius: 6,
                pointHoverBackgroundColor: "rgba(244, 66, 66,1)",
                pointHitRadius: 10,
                pointBorderWidth: 2,
                data: data.line_chart.values_e,
                cubicInterpolationMode: 'monotone'
            }],
        },
        options: {
            tooltips: {
                mode: 'index',
            },
            scales: {
            xAxes: [{
                time: {
                unit: 'date'
                },
                gridLines: {
                    display: false
                },
                ticks: {
                    maxTicksLimit: 7
                }
            }],
            yAxes: [{
                ticks: {
                min: 0,
                max: data.line_chart.max,
                maxTicksLimit: 5
                },
                gridLines: {
                color: "rgba(0, 0, 0, .125)",
                }
            }],
            },
            legend: {
            display: true
            },
            spanGaps: true,
        }
    });

    // -- Bar Chart
    var ctx = document.getElementById("myBarChart");
    var myBarChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: data.bar_chart.labels,
        datasets: data.bar_chart.datasets,
    },
    options: {
        scales: {
        xAxes: [{
            time: {
            unit: 'month'
            },
            gridLines: {
                display: false
            },
            ticks: {
                maxTicksLimit: 6
            }
        }],
        yAxes: [{
            ticks: {
                min: 0,
                max: data.bar_chart.max,
                maxTicksLimit: 5
            },
            gridLines: {
                display: true
            }
        }],
        },
        legend: {
            position: 'top',
        }
    }
    });

}

//getting data
$(document).ready(function(){
    var endpoint = $(".card-header").data("endpoint");
    $.ajax({
        method:"GET",
        url: endpoint,
        success: charts,
        error: function(error_data){
            console.log('error')
            console.log(error_data)
        }
    });
});


var ctx = document.getElementById('sales_chart').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday','Saturday'],
        datasets: [{
            label: 'Revenue',
            data: [12, 19, 3, 5, 2, 3,2],
            borderColor: 'rgba(66,155,227,1)',
            backgroundColor: 'rgba(0,0,0,0)',
            pointBackgroundColor: 'rgba(66,155,227,1)',
            pointRadius: 2,
            pointHoverRadius: 5,
            borderWidth: 2,
        },
        {
            label: 'Profit',
            data: [8, 12, 2, 3, 1, 2,1],
            borderColor: 'rgba(81,179,155,1)',
            backgroundColor: 'rgba(0,0,0,0)',
            pointBackgroundColor: 'rgba(81,179,155,1)',
            pointRadius: 2,
            pointHoverRadius: 5,
            borderWidth: 2,
        }]
    },
    options: {
        legend : {
            display: true,
            position: 'bottom',
            fillStyle:'rgba(66,155,227,1)',
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    }
});
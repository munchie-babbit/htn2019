var ctx = document.getElementById('operations_chart').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: ['Sun', 'Mon', 'Tues', 'Wed', 'Thurs', 'Fri','Sat'],
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
            label: 'Expenses',
            data: [8, 12, 2, 3, 1, 2,1],
            borderColor: 'rgba(224,127,127,1)',
            backgroundColor: 'rgba(0,0,0,0)',
            pointBackgroundColor: 'rgba(224,127,127,1)',
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
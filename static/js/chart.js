const ctx = document.getElementById('myChart').getContext('2d');
const myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['2019 Spring', '2019 Fall', '2020 Spring', '2020 Fall',
            '2022 Spring', '2022 Fall', '2023 Spring'],
        datasets: [{
            label: "A+",
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            data: [1, 1, 3, 1, 3, 3, 4],
        },{
            label: "A",
            backgroundColor:'rgba(255, 206, 86, 0.2)',
            data: [3, 2, 0, 2, 3, 3, 1],
        },{
            label: "B+",
            backgroundColor:'rgba(75, 192, 192, 0.2)',
            data: [2, 2, 3, 2, 1, 0, 0],
        },{
            label: "B",
            backgroundColor:'rgba(153, 102, 255, 0.2)',
            data: [1, 1, 1, 0, 0, 1, 0],
        },{
            label: "C+",
            backgroundColor: 'rgba(255, 159, 64, 0.2)',
            data: [1, 1, 0, 0, 0, 0, 0]
        },{
            label: "P",
            backgroundColor: 'rgba(99,255,64,0.2)',
            data: [2, 0, 1, 0, 1, 2, 2],
        }],

    },
    options: {
        scales: {
            x: {
                stacked: true,
            },
            y: {
                stacked: true,
                // beginAtZero: true
            }
        },
        indexAxis: 'y',
    }
});
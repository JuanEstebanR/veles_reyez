import { useState, useEffect } from 'react';
import Chart from 'chart.js/auto';

const InfoChart = ({title, labels, data}) => {
    const [chart, setChart] = useState(null);

    useEffect(() => {
        if (chart) {
            chart.destroy();
        }

        const ctx = document.getElementById('myChart').getContext('2d');
        const newChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [{
                    label: title,
                    data: data,
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.5)',
                        'rgba(54, 162, 235, 0.5)',
                        'rgba(255, 206, 86, 0.5)',
                        'rgba(75, 192, 192, 0.5)',
                        'rgba(153, 102, 255, 0.5)',
                        'rgba(255, 159, 64, 0.5)'
                    ],
                    borderColor: [
                        'rgba(255, 99, 132, 1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(255, 206, 86, 1)',
                        'rgba(75, 192, 192, 1)',
                        'rgba(153, 102, 255, 1)',
                        'rgba(255, 159, 64, 1)'
                    ],
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                indexAxis: 'y',
                scales: {
                    x: {
                        stacked: false,
                        beginAtZero: true,
                        ticks: {
                            autoSkip: false
                        }
                    },

                },
                plugins: {
                    legend: {
                        labels: {
                            // This more specific font property overrides the global property
                            font: {
                                size: 12
                            }
                        }
                    },
                },
                },
        });

        setChart(newChart);

        return () => {
            newChart.destroy();
        };
    }, []);

    return (
        <div style={{ display: "grid", gridTemplateColumns: "1fr 2fr", gap: "10px",alignItems: "start"}}>
            <div style={{ height: "600px", width:"800px", backgroundColor: "lightgray"}}>
                <canvas id="myChart"></canvas>
            </div>
        </div>
    );
};

export default InfoChart;
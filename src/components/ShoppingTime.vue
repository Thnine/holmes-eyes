<template>
  <div>
    <div id="ShoppingTime-canvas">
    </div>
  </div>
</template>

<script>
import * as echarts from 'echarts';
export default {
    name:'ShoppingTime',
    data(){
        return{

        }
    },
    methods:{

    },
    mounted(){
        let chartDom = document.getElementById('ShoppingTime-canvas');
        let myChart = echarts.init(chartDom);
        let option;

        option = {
        xAxis: {
            type: 'category',
            data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        },
        yAxis: {
            type: 'value'
        },
        series: [
            {
            data: [120, 200, 150, 80, 70, 110, 130],
            type: 'bar',
            showBackground: true,
            backgroundStyle: {
                color: 'rgba(180, 180, 180, 0.2)'
            }
            }
        ]
        };

        option && myChart.setOption(option);        
    },
}
</script>

<style>
    #ShoppingTime-canvas{
        height: 800px;
    }
</style>
<template>
  <div>
    <div id="map-container">
      <svg id="map-sketch-canvas"></svg>
      <svg id="map-path-canvas"></svg>
    </div>
    <div id="map-controller">
      <el-checkbox-group v-model="checkIdList" @change="drawSelectPath" id="path-select-box">
        <div v-for="item in idList" :key="item" style="display:flex;flex-direction:row">
          <el-checkbox  :label='item' size="medium" style="width:100px"></el-checkbox>
          <div :id='"select-legend-" + item' style="width:50px;margin:1px"></div>
        </div>
      </el-checkbox-group>

    </div>
  </div>
</template>

<script>
import * as d3 from 'd3'
import axios from 'axios'
import ElementUI from 'element-ui'
import Vue from 'vue'
import HistogramSlider from 'vue-histogram-slider';
import 'vue-histogram-slider/dist/histogram-slider.css';
Vue.use(ElementUI);
Vue.component(HistogramSlider.name, HistogramSlider);

export default {
  name: 'Mapshow',
  data () {
    return {
        geoData:null,
        height:1150,
        width:1600,
        checkIdList:[1],
        idList:[
          1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,101,104,105,106,107
        ],
        projection:null,
        colorScheme:{},
        timeRange:[new Date(2000, 10, 10, 10, 10), new Date(2000, 10, 11, 10, 10)],
    }
  },
  methods:{
    init(){
      axios.get('/static/data/GeoJson.json').then(req=>{
          //存储数据
          this.geoData = req.data;
          //初始化画布
          let sketch_svg = d3.select("#map-sketch-canvas");
          let path_svg = d3.select("#map-path-canvas");
          sketch_svg.attr("width",this.width).attr("height",this.height);
          path_svg.attr("width",this.width).attr("height",this.height);
          //初始化色彩
          for (let i = 0; i < this.idList.length; i++) {
          //生成颜色
            let hue = i * 360.0 / this.idList.length;
            let startuation = (90 + Math.random() * 10) / 100;
            let lightness = (50 + Math.random() * 10) / 100;
            let rgb_color = d3.rgb(d3.hsl(hue, startuation, lightness));
            this.colorScheme[this.idList[i]] = `rgb(${rgb_color.r},${rgb_color.g},${rgb_color.b})`;
            d3.select('#select-legend-'+ this.idList[i]).style("background-color",this.colorScheme[this.idList[i]])
          }
          //初始化图像
          this.drawSketch();
          this.drawPathbyId(1,this.colorScheme[1]);
      });
    },
    drawSketch(){
      //绘制街道轨迹图
        let svg = d3.select("#map-sketch-canvas");
        svg.attr("width",this.width).attr("height",this.height);
        this.projection = d3.geoMercator().fitSize([this.width, this.height], this.geoData);
        let path = d3.geoPath().projection(this.projection);
        let group = svg.append('g')
        group.selectAll("*")
            .data(this.geoData['features'])
            .enter()
            .append("path")
            .attr("stroke","#6b70bb")
            .attr("stroke-width",1)
            .attr("d", path )
            .attr("fill", 'black');
        svg.on("mousedown",() =>{
                console.log(this.projection.invert([event.clientX,event.clientY]))
            })
    },
    drawPathbyId(id,color){
      //绘制路径
      d3.csv('static/data/gps/'+id+'.csv').then(data=>{
        let svg = d3.select("#map-path-canvas");
        let group = svg.append('g')
        let pathString = ''
        data.forEach(element => {
          let result = this.projection([Number(element.long),Number(element.lat)])
          pathString = pathString + `${result[0]},${result[1]} `
        });
        group.append('polyline')
          .attr("points",pathString)
          .attr('fill','none')
          .attr('stroke',color)
          .attr('stroke-width','3px')
      })
    },
    drawSelectPath(){
      //绘制所有被选中的path
      let svg = d3.select("#map-path-canvas");
      svg.selectAll("*").remove();
      for (let i = 0; i < this.checkIdList.length; i++) {
          this.drawPathbyId(this.checkIdList[i],this.colorScheme[this.checkIdList[i]]);
      } 
    }
  },
  created(){
      this.init();
  },

}




</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  #map-controller{
      height: 1150px;
      width:500px;
      display: flex;
      flex-direction: column;
    }
  #map-container{
    height: 1150px;
    width: 1600px;
    background:url('http://localhost:8080/static/MC2-tourist.jpg');
    position:relative;
  }
  #map-sketch-canvas{
    position:absolute;
    left: 0;
    top:0;
  }
  #map-path-canvas{
    position:absolute;
    left: 0;
    top:0;    
  }
  #path-select-box{
    height:400px;
    width:200px;
    overflow-y:auto;
    border:1px solid black;
  }

</style>

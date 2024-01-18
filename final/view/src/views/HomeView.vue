<template>
  <v-chart class="chart" :option="option" autoresize />
</template>

<script lang="ts" setup>
import { use } from 'echarts/core';
import { CanvasRenderer } from 'echarts/renderers';
import { PieChart } from 'echarts/charts';
import {
  TitleComponent,
  TooltipComponent,
  LegendComponent,
} from 'echarts/components';
import VChart, { THEME_KEY } from 'vue-echarts';
//@ts-ignore
import axios from 'axios';
import { ref, provide, onMounted } from 'vue';

use([
  CanvasRenderer,
  PieChart,
  TitleComponent,
  TooltipComponent,
  LegendComponent,
]);

provide(THEME_KEY, 'dark');

const option = ref({
  title: {
    text: '热度词',
    left: 'center',
  },
  tooltip: {
    trigger: 'item',
    formatter: '{a} <br/>{b} : {c} ({d}%)',
  },
  legend: {
    orient: 'vertical',
    left: 'left',
    data: ['Direct', 'Email', 'Ad Networks', 'Video Ads', 'Search Engines'],
  },
  series: [
    {
      name: '热度词',
      type: 'pie',
      radius: '55%',
      center: ['50%', '60%'],
      data: [
        { value: 335, name: 'Direct' },
      ],
      emphasis: {
        itemStyle: {
          shadowBlur: 10,
          shadowOffsetX: 0,
          shadowColor: 'rgba(0, 0, 0, 0.5)',
        },
      },
    },
  ],
});
onMounted(async () => {
  try {
    // 使用axios发送GET请求获取数据
    const response = await axios.get('http://127.0.0.1:5000/api/data');
    const apiData = response.data;

    // 更新图表数据
    //@ts-ignore
    option.value.legend.data = apiData.map(item => item.word);
    //@ts-ignore
    option.value.series[0].data = apiData.map(item => ({
      value: item.tfidf, // 使用实际的字段名
      name: item.word,    // 使用实际的字段名
    }));

    // 强制刷新图表
    option.value = { ...option.value };
  } catch (error) {
    console.error('Error fetching data:', error);
  }
});


</script>

<style scoped>
.chart {
  height: 100vh;
}
</style>
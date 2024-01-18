<!--
 * @Description: 
 * @Author: 唐健峰
 * @Date: 2024-01-18 11:49:46
 * @LastEditors: ${author}
 * @LastEditTime: 2024-01-18 14:37:09
-->
<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <RouterLink to="/">全文章热度词 </RouterLink>
  <RouterLink to="/about">About</RouterLink>

  <RouterView />
</template>

<style scoped></style>

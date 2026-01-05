<script setup lang="ts">
import { useRoute } from 'vue-router'
import headnav from '@/components/headnav.vue'
import footnav from '@/components/footnav.vue'

const routeInfo = useRoute()
</script>

<template>
  <div style="min-height: 100vh; background-color: #f9fafb;">
    <component v-if="routeInfo.meta.hashead" :is="headnav" ref="headnavRef" />
    <RouterView />
    <component v-if="routeInfo.meta.hasfoot" :is="footnav" ref="footnavRef" />
  </div>
</template>

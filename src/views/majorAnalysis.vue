<script setup lang="ts">
import { ref, reactive, onMounted } from 'vue'
import sideTop from '@/components/sideTop.vue'
import * as api from '@/api/interfaceapi'

onMounted(() => {
  getZyCcQueryApi()
})

// 获取专业分类数据
const getZyCcQueryApi = async () => {
  const res = await api.ZyCcQueryApi({})
  if (res) {
    console.log(res);
  }
}

// 声明响应式变量
// 教育类型 - 可选值：'undergraduate', 'vocational-undergrad', 'vocational-college'
const selectedEducationType = ref('undergraduate')

// 教育类型点击事件处理函数
const handleEducationTypeClick = (type: string) => {
  selectedEducationType.value = type
  console.log(`选择了教育类型: ${type}`)
}

</script>

<template>
  <div class="major-analysis-page">
    <main class="container mx-auto px-6 py-8">
      <div class="bg-white rounded-lg shadow-sm">
        <!-- 内容标题 -->
        <div class="px-6 py-4 border-b">
          <h1 class="text-2xl font-bold text-secondary">大学专业信息库</h1>
          <p class="text-info mt-2">全面解析专业门类、培养方向与就业前景</p>
        </div>
        <!-- 分类按钮区域 -->
        <div class="px-6 py-4 flex items-center justify-between border-b">
          <div class="flex space-x-3">
            <button @click="handleEducationTypeClick('undergraduate')" :class="[
              'px-4 py-2 rounded-full education-type-btn',
              selectedEducationType === 'undergraduate' ? 'bg-blue-600 text-white border-blue-600' : 'border',
            ]" data-type="undergraduate">
              本科（普通教育）
            </button>
            <button @click="handleEducationTypeClick('vocational-undergrad')" :class="[
              'px-4 py-2 rounded-full education-type-btn',
              selectedEducationType === 'vocational-undergrad'
                ? 'bg-blue-600 text-white border-blue-600'
                : 'border',
            ]" data-type="vocational-undergrad">
              本科（职业教育）
            </button>
            <button @click="handleEducationTypeClick('vocational-college')" :class="[
              'px-4 py-2 rounded-full education-type-btn',
              selectedEducationType === 'vocational-college' ? 'bg-blue-600 text-white border-blue-600' : 'border',
            ]" data-type="vocational-college">
              高职（专科）
            </button>
          </div>
        </div>
      </div>
    </main>
    <sideTop />
  </div>
</template>

<style lang="scss" scoped>
.major-analysis-page {
  max-width: 80vw;
  min-width: 1200px;
  min-height: calc(100vh - 428px);
  margin: 0 auto;
  background-color: #fff;
  box-shadow:
    0 10px 15px -3px rgb(0 0 0 / 0.1),
    0 4px 6px -4px rgb(0 0 0 / 0.1);
  border-top: 1px solid #e5e7eb;
}
</style>

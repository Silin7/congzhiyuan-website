<script setup lang="ts">
import { ref, reactive, onMounted } from 'vue'
import sideTop from '@/components/sideTop.vue'
import * as api from '@/api/interfaceapi'

onMounted(() => {
  getZyCcQueryApi()
})

// 获取专业分类数据
const selectedEducationType: any = ref('')
const educationTypeList: any = ref([])
const getZyCcQueryApi = async () => {
  const res: any = await api.ZyCcQueryApi({})
  if (res) {
    educationTypeList.value = res.data || []
    selectedEducationType.value = educationTypeList.value[0]?.ccdm || ''
    getZyListQueryApi()
  }
}

const handleEducationTypeClick = (type: string) => {
  selectedEducationType.value = type
  getZyListQueryApi()
}

// 获取专业列表数据
const majorTypeList: any = ref([])
const getZyListQueryApi = async () => {
  const res: any = await api.ZyListQueryApi({
    ccdm: selectedEducationType.value,
  })
  if (res) {
    majorTypeList.value = res.data.Rs || []
  }
}

const defaultProps = {
  children: 'children',
  label: 'label',
}


const handleNodeClick = (data: any) => {
  if (!data.children) {
    console.log('-------->', '最后一层', data.id)
    window.open(`/#/majorDetail?zydm=${data.id}`)
  }
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
            <button v-for="(item, index) in educationTypeList" :key="index" @click="handleEducationTypeClick(item.ccdm)"
              :class="[
                'px-4 py-2 rounded-full education-type-btn',
                selectedEducationType === item.ccdm ? 'bg-blue-600 text-white border-blue-600' : 'border',
              ]" data-type="undergraduate">
              {{ item.ccmc }}
            </button>
          </div>
        </div>
        <div class="">
          <el-tree style="max-width: 600px" :data="majorTypeList" :props="defaultProps" @node-click="handleNodeClick" />
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

<script setup lang="ts">
import * as api from '@/api/interfaceapi'
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()

onMounted(() => {
  getSchoolDetail()
})

// 院校详情
const schoolDetail = ref<any>({})
const getSchoolDetail = async () => {
  const res: any = await api.YxDetailsQuery({
    yxid: route.query.yxid,
  })
  if (res) {
    schoolDetail.value = res.data || {}
    if (schoolDetail.value.yxts) {
      schoolDetail.value.yxts = schoolDetail.value.yxts.split(' | ')
    }
    if (schoolDetail.value.yxpg) {
      schoolDetail.value.yxpg = JSON.parse(`[${schoolDetail.value.yxpg}]`)
    }
    if (schoolDetail.value.yxgts) {
      schoolDetail.value.yxgts = schoolDetail.value.yxgts.split(';')
    }
    if (schoolDetail.value.yxsts) {
      schoolDetail.value.yxsts = schoolDetail.value.yxsts.split(';')
    }
  }
}
</script>

<template>
  <div class="school-detail">
    <div
      class="bg-gradient-to-r from-blue-50 to-blue-100 border border-blue-300 rounded-xl shadow-sm p-8 mb-8 relative overflow-hidden">
      <div class="absolute inset-0 opacity-10">
        <div class="pattern-dots pattern-amber-500 pattern-bg-transparent pattern-opacity-100 pattern-size-4" style="
            background-image: radial-gradient(#d97706 1px, transparent 1px);
            background-size: 15px 15px;
          "></div>
      </div>
      <div class="relative z-10">
        <div class="flex items-start justify-between">
          <div>
            <h1 class="text-4xl font-bold text-blue-800 mb-2">{{ schoolDetail.yxmc }}</h1>
            <div class="flex items-center text-lg">
              <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em"
                viewBox="0 0 24 24" data-icon="mdi:map-marker" class="iconify mr-2 text-blue-700 iconify--mdi">
                <path fill="currentColor"
                  d="M12 11.5A2.5 2.5 0 0 1 9.5 9A2.5 2.5 0 0 1 12 6.5A2.5 2.5 0 0 1 14.5 9a2.5 2.5 0 0 1-2.5 2.5M12 2a7 7 0 0 0-7 7c0 5.25 7 13 7 13s7-7.75 7-13a7 7 0 0 0-7-7">
                </path>
              </svg>
              <span class="text-gray-700">{{ schoolDetail.provcity }}</span>
            </div>
          </div>
          <div class="bg-blue-50 border border-blue-300 rounded-full p-2 flex items-center">
            <div style="margin-left: 10px;"
              class="h-12 w-12 bg-blue-100 border border-blue-300 rounded-full flex items-center justify-center mr-4">
              <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em"
                viewBox="0 0 24 24" data-icon="mdi:school" class="iconify text-3xl text-blue-700 iconify--mdi">
                <path fill="currentColor" d="M12 3L1 9l11 6l9-4.91V17h2V9M5 13.18v4L12 21l7-3.82v-4L12 17z"></path>
              </svg>
            </div>
            <div style="padding-right: 20px;">
              <div class="text-blue-600">综合排名</div>
              <div class="text-xl font-bold text-gray-900">第{{ schoolDetail.yxrankNum }}位</div>
            </div>
          </div>
        </div>
        <!-- 标签区域 -->
        <div class="mt-6 flex flex-wrap gap-3">
          <div v-for="(tag, index) in schoolDetail.yxts" :key="index">
            <span v-if="tag" class="px-3 py-1 bg-blue-100 border border-blue-300 rounded-full text-blue-700">
              {{ tag }}
            </span>
          </div>
        </div>
      </div>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-8 mb-8">
      <!-- 基础信息 -->
      <div class="bg-white border border-gray-200 rounded-xl shadow-sm p-6">
        <h2 class="text-xl font-bold text-blue-800 mb-4 border-b border-gray-200 pb-2">基础信息</h2>
        <div class="space-y-4">
          <div>
            <div class="text-sm text-blue-600">
              所在省市：
              <span class="font-medium text-gray-900">{{ schoolDetail.provcity }}</span>
            </div>
          </div>
          <div>
            <div class="text-sm text-blue-600">
              院校性质：
              <span class="font-medium text-gray-900">{{ schoolDetail.yxxz }}</span>
            </div>
          </div>
          <div>
            <div class="text-sm text-blue-600">
              隶属单位：
              <span class="font-medium text-gray-900">{{ schoolDetail.yxzgbm }}</span>
            </div>
          </div>
          <div>
            <div class="text-sm text-blue-600">
              成立时间：
              <span class="font-medium text-gray-900">{{ schoolDetail.yxbr }}年</span>
            </div>
          </div>
          <div>
            <div class="text-sm text-blue-600">
              男女比例：
              <span class="font-medium text-gray-900">{{ schoolDetail.yxsexbl }}</span>
            </div>
          </div>
          <div>
            <div class="text-sm text-blue-600">
              保研率：
              <span class="font-medium text-gray-900">{{ schoolDetail.byly }}</span>
            </div>
          </div>
        </div>
      </div>
      <!-- 联系方式 -->
      <div class="bg-white border border-gray-200 rounded-xl shadow-sm p-6">
        <h2 class="text-xl font-bold text-blue-800 mb-4 border-b border-gray-200 pb-2">联系方式</h2>
        <div class="space-y-4">
          <div>
            <div class="flex items-center">
              <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em"
                viewBox="0 0 24 24" data-icon="mdi:earth" class="iconify mr-2 text-blue-700 iconify--mdi">
                <path fill="currentColor"
                  d="M17.9 17.39c-.26-.8-1.01-1.39-1.9-1.39h-1v-3a1 1 0 0 0-1-1H8v-2h2a1 1 0 0 0 1-1V7h2a2 2 0 0 0 2-2v-.41a7.984 7.984 0 0 1 2.9 12.8M11 19.93c-3.95-.49-7-3.85-7-7.93c0-.62.08-1.22.21-1.79L9 15v1a2 2 0 0 0 2 2m1-16A10 10 0 0 0 2 12a10 10 0 0 0 10 10a10 10 0 0 0 10-10A10 10 0 0 0 12 2">
                </path>
              </svg>
              <div>
                <div class="text-sm text-blue-600">官网</div>
                <div class="font-medium text-gray-900">{{ schoolDetail.yxurl }}</div>
              </div>
            </div>
          </div>
          <div>
            <div class="flex items-center">
              <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em"
                viewBox="0 0 24 24" data-icon="mdi:phone" class="iconify mr-2 text-blue-700 iconify--mdi">
                <path fill="currentColor"
                  d="M6.62 10.79c1.44 2.83 3.76 5.15 6.59 6.59l2.2-2.2c.28-.28.67-.36 1.02-.25c1.12.37 2.32.57 3.57.57a1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57c.11.35.03.74-.25 1.02z">
                </path>
              </svg>
              <div>
                <div class="text-sm text-blue-600">招办电话</div>
                <div class="font-medium text-gray-900">{{ schoolDetail.yxphone }}</div>
              </div>
            </div>
          </div>
          <div>
            <div class="flex items-center">
              <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em"
                viewBox="0 0 24 24" data-icon="mdi:map-marker" class="iconify mr-2 text-blue-700 iconify--mdi">
                <path fill="currentColor"
                  d="M12 11.5A2.5 2.5 0 0 1 9.5 9A2.5 2.5 0 0 1 12 6.5A2.5 2.5 0 0 1 14.5 9a2.5 2.5 0 0 1-2.5 2.5M12 2a7 7 0 0 0-7 7c0 5.25 7 13 7 13s7-7.75 7-13a7 7 0 0 0-7-7">
                </path>
              </svg>
              <div>
                <div class="text-sm text-blue-600">通讯地址</div>
                <div class="font-medium text-gray-900">{{ schoolDetail.yxaddress }}</div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- 特色专业 -->
      <div class="bg-white border border-gray-200 rounded-xl shadow-sm p-6">
        <h2 class="text-xl font-bold text-blue-800 mb-4 border-b border-gray-200 pb-2">特色专业</h2>
        <div v-if="schoolDetail.yxgts?.length > 0" class="mb-4">
          <div class="text-sm text-blue-600 mb-2">国家特色专业</div>
          <div class="flex flex-wrap gap-2">
            <span v-for="(item, index) in schoolDetail.yxgts" :key="index">
              <span v-if="item" class="px-2 py-1 bg-blue-100 text-blue-800 rounded-md text-sm">{{
                item
              }}</span>
            </span>
          </div>
        </div>
        <div v-if="schoolDetail.yxsts?.length > 0">
          <div class="text-sm text-blue-600 mb-2">省特色专业</div>
          <div class="flex flex-wrap gap-2">
            <span v-for="(item, index) in schoolDetail.yxsts" :key="index">
              <span v-if="item" class="px-2 py-1 bg-gray-100 text-gray-800 rounded-md text-sm">{{
                item
              }}</span>
            </span>
          </div>
        </div>
      </div>
    </div>
    <div class="bg-white border border-gray-200 rounded-xl shadow-sm p-6 mb-8">
      <h2 v-if="schoolDetail.yxpg" class="text-xl font-bold text-blue-800 mb-4 border-b border-gray-200 pb-2">
        评估结果
      </h2>
      <div v-if="schoolDetail.yxpg" class="mb-8" style="display: flex;flex-wrap: wrap;">
        <span v-for="(item, index) in schoolDetail.yxpg" :key="index"
          class="px-3 py-1 bg-blue-100 border border-blue-300 rounded-full text-blue-700"
          style="margin-right: 10px; margin-bottom: 10px;">
          {{ item.name }} {{ item.value }}
        </span>
      </div>
      <h2 class="text-xl font-bold text-blue-800 mb-4 border-b border-gray-200 pb-2">大学简介</h2>
      <div class="prose max-w-none">
        <p class="text-gray-800 leading-relaxed">
          {{ schoolDetail.yxmemo }}
        </p>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.school-detail {
  max-width: 80vw;
  min-width: 1200px;
  min-height: calc(100vh - 428px);
  margin: 0 auto;
  padding: 2rem;
  background-color: #fff;
  box-shadow:
    0 10px 15px -3px rgb(0 0 0 / 0.1),
    0 4px 6px -4px rgb(0 0 0 / 0.1);
  border-top: 1px solid #e5e7eb;
}
</style>

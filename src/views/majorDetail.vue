<script setup lang="ts">
import * as api from '@/api/interfaceapi'
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()

onMounted(() => {
  getMajorDetail()
})

const majorDetail: any = ref({})
const getMajorDetail = async () => {
  const res: any = await api.ZyDetailsQueryApi({
    zydm: route.query.zydm,
  })
  if (res) {
    majorDetail.value = res.data || {}
  }
}
</script>

<template>
  <main class="max-w-6xl mx-auto px-6 py-10 space-y-8">
    <!-- 1. 专业头部卡片 -->
    <header class="bg-white rounded-3xl p-8 border border-slate-200 shadow-sm animate-slide-up">
      <div class="flex flex-col md:flex-row md:items-center justify-between gap-6">
        <div class="space-y-4">
          <div class="flex items-center space-x-3">
            <span class="bg-blue-50 text-blue-600 px-3 py-1 rounded-full text-xs font-bold tracking-wider uppercase">{{
              majorDetail.zydm }}</span>

          </div>
          <h1 class="text-4xl md:text-5xl font-extrabold text-slate-900">{{ majorDetail.zymc }}</h1>
          <p class="text-slate-500 text-lg flex items-center gap-2">
            <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em"
              viewBox="0 0 24 24" data-icon="lucide:award" class="iconify iconify--lucide">
              <g fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2">
                <path
                  d="m15.477 12.89l1.515 8.526a.5.5 0 0 1-.81.47l-3.58-2.687a1 1 0 0 0-1.197 0l-3.586 2.686a.5.5 0 0 1-.81-.469l1.514-8.526">
                </path>
                <circle cx="12" cy="8" r="6"></circle>
              </g>
            </svg>
            授予学位：{{ majorDetail.syxw || '无' }}
          </p>
        </div>
        <div class="flex gap-4">
          <div class="bg-slate-50 p-4 rounded-2xl border border-slate-100 text-center min-w-[120px]">
            <p class="text-slate-400 text-xs mb-1">修业年限</p>
            <p class="text-xl font-bold text-slate-800">{{ majorDetail.xynx }}</p>
          </div>
          <div class="bg-slate-50 p-4 rounded-2xl border border-slate-100 text-center min-w-[120px]">
            <p class="text-slate-400 text-xs mb-1">推荐指数</p>
            <p class="text-xl font-bold text-amber-500">
              <el-rate v-model="majorDetail.tjzs" disabled />
            </p>
          </div>
        </div>
      </div>
    </header>
    <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
      <!-- 左侧内容列 -->
      <div class="lg:col-span-2 space-y-8">
        <!-- 2. 专业简介 -->
        <section class="bg-white rounded-3xl p-8 border border-slate-200 shadow-sm space-y-8 animate-slide-up"
          style="animation-delay: 0.1s">
          <div class="flex items-center space-x-2 border-l-4 border-blue-600 pl-4">
            <h2 class="text-2xl font-bold text-slate-800">专业详解</h2>
          </div>
          <div class="grid grid-cols-1 gap-6">
            <!-- 专业是什么 -->
            <div class="space-y-3">
              <h3 class="text-lg font-bold text-slate-800 flex items-center gap-2">
                <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em"
                  viewBox="0 0 24 24" data-icon="lucide:help-circle" class="iconify text-blue-600 iconify--lucide">
                  <g fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2">
                    <circle cx="12" cy="12" r="10"></circle>
                    <path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3m.08 4h.01"></path>
                  </g>
                </svg>专业是什么
              </h3>
              <p class="text-slate-600 leading-relaxed text-base">
                {{ majorDetail.zyMemo1 }}
              </p>
            </div>
            <!-- 专业学什么 -->
            <div class="space-y-3">
              <h3 class="text-lg font-bold text-slate-800 flex items-center gap-2">
                <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em"
                  viewBox="0 0 24 24" data-icon="lucide:book-open" class="iconify text-indigo-600 iconify--lucide">
                  <path fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"
                    stroke-width="2"
                    d="M12 7v14m-9-3a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1h5a4 4 0 0 1 4 4a4 4 0 0 1 4-4h5a1 1 0 0 1 1 1v13a1 1 0 0 1-1 1h-6a3 3 0 0 0-3 3a3 3 0 0 0-3-3z">
                  </path>
                </svg>专业学什么
              </h3>
              <div class="grid grid-cols-1 md:grid-cols-1 gap-4">
                <div class="bg-blue-50/50 p-4 rounded-xl border border-blue-100">
                  <div class="space-y-1.5 text-slate-700">
                    {{ majorDetail.zyMemo2 }}
                  </div>
                </div>
              </div>
            </div>
            <!-- 专业干什么 -->
            <div class="space-y-3">
              <h3 class="text-lg font-bold text-slate-800 flex items-center gap-2">
                <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em"
                  viewBox="0 0 24 24" data-icon="lucide:briefcase" class="iconify text-emerald-600 iconify--lucide">
                  <g fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2">
                    <path d="M16 20V4a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path>
                    <rect width="20" height="14" x="2" y="6" rx="2"></rect>
                  </g>
                </svg>专业干什么
              </h3>
              <p class="text-slate-600 leading-relaxed text-base">
                {{ majorDetail.zyMemo3 }}
              </p>
            </div>
          </div>
        </section>

      </div>
      <!-- 右侧侧边栏 -->
      <div class="lg:col-span-1 space-y-8">
        <!-- 4. 男女比例 -->
        <section class="bg-white rounded-3xl p-8 border border-slate-200 shadow-sm space-y-6 animate-slide-up"
          style="animation-delay: 0.3s">
          <div class="flex items-center space-x-2 border-l-4 border-emerald-500 pl-4">
            <h2 class="text-xl font-bold text-slate-800">性别比例</h2>
          </div>
          <div class="py-4 space-y-8">
            <div class="space-y-3">
              <div class="flex justify-between items-end">
                <div class="flex items-center gap-2">
                  <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em"
                    viewBox="0 0 24 24" data-icon="lucide:user" class="iconify text-blue-500 iconify--lucide">
                    <g fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"
                      stroke-width="2">
                      <path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"></path>
                      <circle cx="12" cy="7" r="4"></circle>
                    </g>
                  </svg>
                  <span class="text-sm font-bold text-slate-700">男生 {{ majorDetail.sexblman }}%</span>
                </div>
              </div>
              <div class="w-full bg-slate-100 h-4 rounded-full overflow-hidden flex">
                <div class="bg-blue-500 h-full transition-all duration-1000"
                  :style="{ width: majorDetail.sexblman + '%' }"></div>
              </div>
            </div>
            <div class="space-y-3">
              <div class="flex justify-between items-end">
                <div class="flex items-center gap-2">
                  <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em"
                    viewBox="0 0 24 24" data-icon="lucide:user-round" class="iconify text-rose-400 iconify--lucide">
                    <g fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"
                      stroke-width="2">
                      <circle cx="12" cy="8" r="5"></circle>
                      <path d="M20 21a8 8 0 0 0-16 0"></path>
                    </g>
                  </svg>
                  <span class="text-sm font-bold text-slate-700">女生 {{ majorDetail.sexblwoman }}%</span>
                </div>
              </div>
              <div class="w-full bg-slate-100 h-4 rounded-full overflow-hidden flex">
                <div class="bg-rose-400 h-full transition-all duration-1000"
                  :style="{ width: majorDetail.sexblwoman + '%' }"></div>
              </div>
            </div>
            <div class="pt-4 border-t border-slate-100 flex justify-around text-center">

            </div>
          </div>
        </section>
      </div>
    </div>
  </main>
</template>

<style lang="scss" scoped></style>
<script setup lang="ts">
import { ref } from 'vue'
import sideTop from '@/components/sideTop.vue'

// 声明响应式变量
// 院校省份 - 可选值：'all' 或省份代码
const selectedProvince = ref('all')
// 办学层次 - 可选值：'all', 'bachelor', 'college'
const selectedLevel = ref('all')
// 院校名称
const schoolName = ref('')

// 省份按钮点击事件处理函数
const handleProvinceClick = (province: string) => {
  selectedProvince.value = province
  console.log(`选择了省份: ${province}`)
}

// 办学层次点击事件处理函数
const handleLevelClick = (level: string) => {
  selectedLevel.value = level
  console.log(`选择了办学层次: ${level}`)
}

// 查询按钮点击事件处理函数
const handleSearch = () => {
  // 收集查询条件
  const searchParams = {
    province: selectedProvince.value,
    level: selectedLevel.value,
    schoolName: schoolName.value,
  }
  console.log('查询条件:', searchParams)
  // 这里可以添加实际的查询逻辑，比如调用API
}
</script>

<template>
  <div class="school-search-page">
    <main class="flex-grow container mx-auto px-6 py-8">
      <div class="bg-white rounded-lg shadow-sm p-8 mb-8">
        <h2 class="text-2xl font-bold text-gray-800 mb-6">院校查询</h2>
        <!-- 查询表单 -->
        <div class="bg-gray-50 rounded-lg p-6 mb-8">
          <div class="grid grid-cols-1 gap-4">
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">院校省份</label>
              <div class="grid grid-cols-4 md:grid-cols-8 gap-2">
                <button @click="handleProvinceClick('all')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedProvince === 'all'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]" data-province="all" type="button">
                  全部
                </button>
                <button @click="handleProvinceClick('beijing')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedProvince === 'beijing'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]" data-province="beijing" type="button">
                  北京
                </button>
                <button @click="handleProvinceClick('tianjin')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedProvince === 'tianjin'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]" data-province="tianjin" type="button">
                  天津
                </button>
                <button @click="handleProvinceClick('hebei')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedProvince === 'hebei'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]" data-province="hebei" type="button">
                  河北
                </button>
                <button @click="handleProvinceClick('shanxi')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedProvince === 'shanxi'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]" data-province="shanxi" type="button">
                  山西
                </button>
                <button @click="handleProvinceClick('neimenggu')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedProvince === 'neimenggu'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]" data-province="neimenggu" type="button">
                  内蒙古
                </button>
                <button @click="handleProvinceClick('liaoning')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedProvince === 'liaoning'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]" data-province="liaoning" type="button">
                  辽宁
                </button>
                <button @click="handleProvinceClick('jilin')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedProvince === 'jilin'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]" data-province="jilin" type="button">
                  吉林
                </button>
                <button @click="handleProvinceClick('heilongjiang')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedProvince === 'heilongjiang'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]" data-province="heilongjiang" type="button">
                  黑龙江
                </button>
                <button @click="handleProvinceClick('shanghai')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedProvince === 'shanghai'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]" data-province="shanghai" type="button">
                  上海
                </button>
                <button @click="handleProvinceClick('jiangsu')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedProvince === 'jiangsu'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]" data-province="jiangsu" type="button">
                  江苏
                </button>
                <button @click="handleProvinceClick('zhejiang')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedProvince === 'zhejiang'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]" data-province="zhejiang" type="button">
                  浙江
                </button>
                <button @click="handleProvinceClick('anhui')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedProvince === 'anhui'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]" data-province="anhui" type="button">
                  安徽
                </button>
                <button @click="handleProvinceClick('fujian')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedProvince === 'fujian'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]" data-province="fujian" type="button">
                  福建
                </button>
                <button @click="handleProvinceClick('jiangxi')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedProvince === 'jiangxi'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]" data-province="jiangxi" type="button">
                  江西
                </button>
                <button @click="handleProvinceClick('shandong')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedProvince === 'shandong'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]" data-province="shandong" type="button">
                  山东
                </button>
                <button @click="handleProvinceClick('henan')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedProvince === 'henan'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]" data-province="henan" type="button">
                  河南
                </button>
                <button @click="handleProvinceClick('hubei')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedProvince === 'hubei'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]" data-province="hubei" type="button">
                  湖北
                </button>
                <button @click="handleProvinceClick('hunan')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedProvince === 'hunan'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]" data-province="hunan" type="button">
                  湖南
                </button>
                <button @click="handleProvinceClick('guangdong')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedProvince === 'guangdong'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]" data-province="guangdong" type="button">
                  广东
                </button>
                <button @click="handleProvinceClick('guangxi')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedProvince === 'guangxi'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]" data-province="guangxi" type="button">
                  广西
                </button>
                <button @click="handleProvinceClick('hainan')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedProvince === 'hainan'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]" data-province="hainan" type="button">
                  海南
                </button>
                <button @click="handleProvinceClick('chongqing')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedProvince === 'chongqing'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]" data-province="chongqing" type="button">
                  重庆
                </button>
                <button @click="handleProvinceClick('sichuan')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedProvince === 'sichuan'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]" data-province="sichuan" type="button">
                  四川
                </button>
                <button @click="handleProvinceClick('guizhou')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedProvince === 'guizhou'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]" data-province="guizhou" type="button">
                  贵州
                </button>
                <button @click="handleProvinceClick('yunnan')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedProvince === 'yunnan'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]" data-province="yunnan" type="button">
                  云南
                </button>
                <button @click="handleProvinceClick('xizang')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedProvince === 'xizang'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]" data-province="xizang" type="button">
                  西藏
                </button>
                <button @click="handleProvinceClick('shaanxi')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedProvince === 'shaanxi'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]" data-province="shaanxi" type="button">
                  陕西
                </button>
                <button @click="handleProvinceClick('gansu')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedProvince === 'gansu'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]" data-province="gansu" type="button">
                  甘肃
                </button>
                <button @click="handleProvinceClick('qinghai')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedProvince === 'qinghai'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]" data-province="qinghai" type="button">
                  青海
                </button>
                <button @click="handleProvinceClick('ningxia')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedProvince === 'ningxia'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]" data-province="ningxia" type="button">
                  宁夏
                </button>
                <button @click="handleProvinceClick('xinjiang')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedProvince === 'xinjiang'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]" data-province="xinjiang" type="button">
                  新疆
                </button>
              </div>
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-2">办学层次</label>
              <div class="flex gap-4">
                <button @click="handleLevelClick('all')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedLevel === 'all'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]" data-level="all">不限</button>
                <button @click="handleLevelClick('bachelor')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedLevel === 'bachelor'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]" data-level="bachelor">本科</button>
                <button @click="handleLevelClick('college')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedLevel === 'college'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]" data-level="college">专科</button>
              </div>
            </div>
            <div class="flex items-end gap-4">
              <div class="w-1/2">
                <label class="block text-sm font-medium text-gray-700 mb-2">院校名称</label>
                <input v-model="schoolName"
                  class="w-full px-4 py-2 border border-gray-300 rounded-md focus:border-blue-500 focus:ring-1 focus:ring-blue-500"
                  placeholder="请输入院校名称" type="text" />
              </div>
            </div>
            <div>
              <button @click="handleSearch"
                class="w-full bg-blue-700 hover:bg-blue-800 text-white py-2 px-4 rounded-md font-medium">
                查询
              </button>
            </div>
          </div>
        </div>
        <!-- 查询结果表格 -->
        <div class="overflow-x-auto">
          <table class="min-w-full divide-y divide-gray-200">
            <thead class="bg-gray-50">
              <tr>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-700 uppercase tracking-wider" scope="col">
                  院校名称
                </th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-700 uppercase tracking-wider" scope="col">
                  所在省份
                </th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-700 uppercase tracking-wider" scope="col">
                  城市
                </th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-700 uppercase tracking-wider" scope="col">
                  办学层次
                </th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-700 uppercase tracking-wider" scope="col">
                  院校性质
                </th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-700 uppercase tracking-wider" scope="col">
                  特色专业
                </th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-700 uppercase tracking-wider" scope="col">
                  保研率
                </th>
              </tr>
            </thead>
            <tbody class="bg-white divide-y divide-gray-200">
              <tr>
                <td class="px-6 py-4 whitespace-nowrap">
                  <div class="text-sm font-medium text-gray-900">
                    <a href="院校简介.html">北京大学</a>
                  </div>
                </td>
                <td class="px-6 py-4 whitespace-nowrap">
                  <div class="text-sm text-gray-700">北京</div>
                </td>
                <td class="px-6 py-4 whitespace-nowrap">
                  <div class="text-sm text-gray-700">北京市</div>
                </td>
                <td class="px-6 py-4 whitespace-nowrap">
                  <span
                    class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800">本科</span>
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-700">公办</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-700">
                  <span class="mr-2 px-2 py-1 text-xs bg-blue-100 text-blue-800 rounded-full">双一流</span>
                  <span class="px-2 py-1 text-xs bg-purple-100 text-purple-800 rounded-full">国家级优势</span>
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-700">56%</td>
              </tr>
              <tr class="bg-gray-50">
                <td class="px-6 py-4 whitespace-nowrap">
                  <div class="text-sm font-medium text-gray-900">清华大学</div>
                </td>
                <td class="px-6 py-4 whitespace-nowrap">
                  <div class="text-sm text-gray-700">北京</div>
                </td>
                <td class="px-6 py-4 whitespace-nowrap">
                  <div class="text-sm text-gray-700">北京市</div>
                </td>
                <td class="px-6 py-4 whitespace-nowrap">
                  <span
                    class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800">本科</span>
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-700">公办</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-700">
                  <span class="mr-2 px-2 py-1 text-xs bg-blue-100 text-blue-800 rounded-full">双一流</span>
                  <span class="px-2 py-1 text-xs bg-yellow-100 text-yellow-800 rounded-full">重点学科</span>
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-700">58%</td>
              </tr>
              <tr>
                <td class="px-6 py-4 whitespace-nowrap">
                  <div class="text-sm font-medium text-gray-900">复旦大学</div>
                </td>
                <td class="px-6 py-4 whitespace-nowrap">
                  <div class="text-sm text-gray-700">上海</div>
                </td>
                <td class="px-6 py-4 whitespace-nowrap">
                  <div class="text-sm text-gray-700">上海市</div>
                </td>
                <td class="px-6 py-4 whitespace-nowrap">
                  <span
                    class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800">本科</span>
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-700">公办</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-700">
                  <span class="mr-2 px-2 py-1 text-xs bg-blue-100 text-blue-800 rounded-full">双一流</span>
                  <span class="px-2 py-1 text-xs bg-red-100 text-red-800 rounded-full">特色专业</span>
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-700">54%</td>
              </tr>
            </tbody>
          </table>
        </div>
        <!-- 分页控件 -->
        <div class="flex items-center justify-between border-t border-gray-200 pt-6">
          <div class="text-sm text-gray-700">
            共 <span class="font-medium">3</span> 条结果 | 第
            <span class="font-medium">1</span> 页，共 <span class="font-medium">1</span> 页
          </div>
          <div class="flex space-x-2">
            <button
              class="px-3 py-1 border border-gray-300 rounded-md text-gray-700 bg-white hover:bg-gray-50 disabled:opacity-50">
              &lt; 上一页
            </button>
            <button class="px-3 py-1 bg-blue-700 text-white rounded-md font-medium">1</button>
            <button
              class="px-3 py-1 border border-gray-300 rounded-md text-gray-700 bg-white hover:bg-gray-50 disabled:opacity-50">
              下一页 &gt;
            </button>
          </div>
        </div>
      </div>
    </main>
    <sideTop />
  </div>
</template>

<style lang="scss" scoped>
.school-search-page {
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

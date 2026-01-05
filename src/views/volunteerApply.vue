<script setup lang="ts">
import { ref } from 'vue'
import { Icon } from '@iconify/vue'

// 声明院校层次响应式变量 - 可选值：'不限', '本科', '专科'
const selectedSchoolLevel = ref('本科')
const handleSchoolLevelClick = (level: string) => {
  selectedSchoolLevel.value = level
  console.log(`选择了院校层次: ${level}`)
}

// 声明录取批次响应式变量 - 可选值：'不限', '提前批A', '提前批B', '本科批', '专科批'
const selectedAdmissionBatch = ref('')
const handleAdmissionBatchClick = (batch: string) => {
  selectedAdmissionBatch.value = batch
  console.log(`选择了录取批次: ${batch}`)
}

// 声明录取类型响应式变量
const selectedAdmissionType = ref('不限')
const handleAdmissionTypeChange = (event: Event) => {
  const value = (event.target as HTMLSelectElement).value
  selectedAdmissionType.value = value
  console.log(`选择了录取类型: ${value}`)
}

// 声明院校性质响应式变量 - 可选值：'公办', '民办', '中外合作'
const selectedSchoolNature = ref('')
const handleSchoolNatureClick = (nature: string) => {
  selectedSchoolNature.value = nature
  console.log(`选择了院校性质: ${nature}`)
}

// 声明院校省份响应式变量
const selectedProvince = ref('')
const handleProvinceClick = (province: string) => {
  selectedProvince.value = province
  console.log(`选择了省份: ${province}`)
}

// 声明专业特色响应式变量 - 可选值：'双一流', '特色专业', '重点学科', '国家级优势'
const selectedMajorFeature = ref('')
const handleMajorFeatureClick = (feature: string) => {
  selectedMajorFeature.value = feature
  console.log(`选择了专业特色: ${feature}`)
}

// 声明院校名称响应式变量
const schoolName = ref('')

// 声明专业名称响应式变量
const majorName = ref('')

// 声明录取范围响应式变量
const admissionRange = ref('全部')
const handleAdmissionRangeChange = (event: Event) => {
  const value = (event.target as HTMLInputElement).value
  admissionRange.value = value
  console.log(`选择了录取范围: ${value}`)
}
</script>

<template>
  <div class="volunteer-apply-page">
    <main class="max-w-7xl mx-auto px-4 py-8">
      <section class="mb-10">
        <h2 class="text-2xl font-bold text-center mb-6">志愿填报查询</h2>
        <div class="bg-gray-50 rounded-2xl shadow-lg p-6 border border-gray-200">
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            <!-- 院校层次 -->
            <div>
              <label class="block text-sm font-medium mb-2 text-gray-800">院校层次</label>
              <div class="grid grid-cols-3 gap-2">
                <button @click="handleSchoolLevelClick('不限')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedSchoolLevel === '不限'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]">
                  不限
                </button>
                <button @click="handleSchoolLevelClick('本科')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedSchoolLevel === '本科'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]">
                  本科
                </button>
                <button @click="handleSchoolLevelClick('专科')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedSchoolLevel === '专科'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]">
                  专科
                </button>
              </div>
            </div>
            <!-- 录取批次 -->
            <div>
              <label class="block text-sm font-medium mb-2 text-gray-800">录取批次</label>
              <div class="grid grid-cols-3 gap-2">
                <button @click="handleAdmissionBatchClick('不限')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedAdmissionBatch === '不限'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]">
                  不限
                </button>
                <button @click="handleAdmissionBatchClick('提前批A')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedAdmissionBatch === '提前批A'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]">
                  提前批A
                </button>
                <button @click="handleAdmissionBatchClick('提前批B')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedAdmissionBatch === '提前批B'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]">
                  提前批B
                </button>
                <button @click="handleAdmissionBatchClick('本科批')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedAdmissionBatch === '本科批'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]">
                  本科批
                </button>
                <button @click="handleAdmissionBatchClick('专科批')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedAdmissionBatch === '专科批'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]">
                  专科批
                </button>
              </div>
            </div>
            <!-- 录取类型 -->
            <div>
              <label class="block text-sm font-medium mb-2 text-gray-800">录取类型</label>
              <select v-model="selectedAdmissionType" @change="handleAdmissionTypeChange"
                class="w-full bg-white text-gray-900 border border-gray-300 rounded-md py-2 px-3 focus:border-blue-500 focus:ring-2 focus:ring-blue-500/50 transition outline-none">
                <option>不限</option>
                <option>录取类型1</option>
                <option>录取类型2</option>
                <option>录取类型3</option>
              </select>
            </div>
          </div>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mt-6">
            <!-- 院校名称 -->
            <div>
              <label class="block text-sm font-medium mb-2 text-gray-800">院校名称</label>
              <input v-model="schoolName"
                class="w-full bg-white text-gray-900 border border-gray-300 rounded-md py-2 px-3 focus:border-blue-500 focus:ring-2 focus:ring-blue-500/50 transition outline-none"
                placeholder="输入院校名称" type="text" />
            </div>
            <!-- 院校性质 -->
            <div>
              <label class="block text-sm font-medium mb-2 text-gray-800">院校性质</label>
              <div class="grid grid-cols-3 gap-2">
                <button @click="handleSchoolNatureClick('公办')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedSchoolNature === '公办'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]">
                  公办
                </button>
                <button @click="handleSchoolNatureClick('民办')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedSchoolNature === '民办'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]">
                  民办
                </button>
                <button @click="handleSchoolNatureClick('中外合作')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedSchoolNature === '中外合作'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]">
                  中外合作
                </button>
              </div>
            </div>
          </div>
          <!-- 院校省份 - 单独一行 -->
          <div class="mt-6">
            <label class="block text-sm font-medium mb-2 text-gray-800">院校省份</label>
            <div class="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-2">
              <button @click="handleProvinceClick('北京')" :class="[
                'text-sm py-2 px-3 rounded-md border transition',
                selectedProvince === '北京'
                  ? 'bg-blue-600 text-white border-blue-600'
                  : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
              ]">
                北京
              </button>
              <button @click="handleProvinceClick('天津')" :class="[
                'text-sm py-2 px-3 rounded-md border transition',
                selectedProvince === '天津'
                  ? 'bg-blue-600 text-white border-blue-600'
                  : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
              ]">
                天津
              </button>
              <button @click="handleProvinceClick('河北')" :class="[
                'text-sm py-2 px-3 rounded-md border transition',
                selectedProvince === '河北'
                  ? 'bg-blue-600 text-white border-blue-600'
                  : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
              ]">
                河北
              </button>
              <button @click="handleProvinceClick('山西')" :class="[
                'text-sm py-2 px-3 rounded-md border transition',
                selectedProvince === '山西'
                  ? 'bg-blue-600 text-white border-blue-600'
                  : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
              ]">
                山西
              </button>
              <button @click="handleProvinceClick('内蒙古')" :class="[
                'text-sm py-2 px-3 rounded-md border transition',
                selectedProvince === '内蒙古'
                  ? 'bg-blue-600 text-white border-blue-600'
                  : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
              ]">
                内蒙古
              </button>
              <button @click="handleProvinceClick('辽宁')" :class="[
                'text-sm py-2 px-3 rounded-md border transition',
                selectedProvince === '辽宁'
                  ? 'bg-blue-600 text-white border-blue-600'
                  : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
              ]">
                辽宁
              </button>
              <button @click="handleProvinceClick('吉林')" :class="[
                'text-sm py-2 px-3 rounded-md border transition',
                selectedProvince === '吉林'
                  ? 'bg-blue-600 text-white border-blue-600'
                  : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
              ]">
                吉林
              </button>
              <button @click="handleProvinceClick('黑龙江')" :class="[
                'text-sm py-2 px-3 rounded-md border transition',
                selectedProvince === '黑龙江'
                  ? 'bg-blue-600 text-white border-blue-600'
                  : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
              ]">
                黑龙江
              </button>
              <button @click="handleProvinceClick('上海')" :class="[
                'text-sm py-2 px-3 rounded-md border transition',
                selectedProvince === '上海'
                  ? 'bg-blue-600 text-white border-blue-600'
                  : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
              ]">
                上海
              </button>
              <button @click="handleProvinceClick('江苏')" :class="[
                'text-sm py-2 px-3 rounded-md border transition',
                selectedProvince === '江苏'
                  ? 'bg-blue-600 text-white border-blue-600'
                  : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
              ]">
                江苏
              </button>
              <button @click="handleProvinceClick('浙江')" :class="[
                'text-sm py-2 px-3 rounded-md border transition',
                selectedProvince === '浙江'
                  ? 'bg-blue-600 text-white border-blue-600'
                  : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
              ]">
                浙江
              </button>
              <button @click="handleProvinceClick('安徽')" :class="[
                'text-sm py-2 px-3 rounded-md border transition',
                selectedProvince === '安徽'
                  ? 'bg-blue-600 text-white border-blue-600'
                  : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
              ]">
                安徽
              </button>
              <button @click="handleProvinceClick('福建')" :class="[
                'text-sm py-2 px-3 rounded-md border transition',
                selectedProvince === '福建'
                  ? 'bg-blue-600 text-white border-blue-600'
                  : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
              ]">
                福建
              </button>
              <button @click="handleProvinceClick('江西')" :class="[
                'text-sm py-2 px-3 rounded-md border transition',
                selectedProvince === '江西'
                  ? 'bg-blue-600 text-white border-blue-600'
                  : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
              ]">
                江西
              </button>
              <button @click="handleProvinceClick('山东')" :class="[
                'text-sm py-2 px-3 rounded-md border transition',
                selectedProvince === '山东'
                  ? 'bg-blue-600 text-white border-blue-600'
                  : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
              ]">
                山东
              </button>
              <button @click="handleProvinceClick('河南')" :class="[
                'text-sm py-2 px-3 rounded-md border transition',
                selectedProvince === '河南'
                  ? 'bg-blue-600 text-white border-blue-600'
                  : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
              ]">
                河南
              </button>
              <button @click="handleProvinceClick('湖北')" :class="[
                'text-sm py-2 px-3 rounded-md border transition',
                selectedProvince === '湖北'
                  ? 'bg-blue-600 text-white border-blue-600'
                  : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
              ]">
                湖北
              </button>
              <button @click="handleProvinceClick('湖南')" :class="[
                'text-sm py-2 px-3 rounded-md border transition',
                selectedProvince === '湖南'
                  ? 'bg-blue-600 text-white border-blue-600'
                  : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
              ]">
                湖南
              </button>
              <button @click="handleProvinceClick('广东')" :class="[
                'text-sm py-2 px-3 rounded-md border transition',
                selectedProvince === '广东'
                  ? 'bg-blue-600 text-white border-blue-600'
                  : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
              ]">
                广东
              </button>
              <button @click="handleProvinceClick('广西')" :class="[
                'text-sm py-2 px-3 rounded-md border transition',
                selectedProvince === '广西'
                  ? 'bg-blue-600 text-white border-blue-600'
                  : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
              ]">
                广西
              </button>
              <button @click="handleProvinceClick('海南')" :class="[
                'text-sm py-2 px-3 rounded-md border transition',
                selectedProvince === '海南'
                  ? 'bg-blue-600 text-white border-blue-600'
                  : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
              ]">
                海南
              </button>
              <button @click="handleProvinceClick('重庆')" :class="[
                'text-sm py-2 px-3 rounded-md border transition',
                selectedProvince === '重庆'
                  ? 'bg-blue-600 text-white border-blue-600'
                  : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
              ]">
                重庆
              </button>
              <button @click="handleProvinceClick('四川')" :class="[
                'text-sm py-2 px-3 rounded-md border transition',
                selectedProvince === '四川'
                  ? 'bg-blue-600 text-white border-blue-600'
                  : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
              ]">
                四川
              </button>
              <button @click="handleProvinceClick('贵州')" :class="[
                'text-sm py-2 px-3 rounded-md border transition',
                selectedProvince === '贵州'
                  ? 'bg-blue-600 text-white border-blue-600'
                  : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
              ]">
                贵州
              </button>
              <button @click="handleProvinceClick('云南')" :class="[
                'text-sm py-2 px-3 rounded-md border transition',
                selectedProvince === '云南'
                  ? 'bg-blue-600 text-white border-blue-600'
                  : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
              ]">
                云南
              </button>
              <button @click="handleProvinceClick('西藏')" :class="[
                'text-sm py-2 px-3 rounded-md border transition',
                selectedProvince === '西藏'
                  ? 'bg-blue-600 text-white border-blue-600'
                  : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
              ]">
                西藏
              </button>
              <button @click="handleProvinceClick('陕西')" :class="[
                'text-sm py-2 px-3 rounded-md border transition',
                selectedProvince === '陕西'
                  ? 'bg-blue-600 text-white border-blue-600'
                  : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
              ]">
                陕西
              </button>
              <button @click="handleProvinceClick('甘肃')" :class="[
                'text-sm py-2 px-3 rounded-md border transition',
                selectedProvince === '甘肃'
                  ? 'bg-blue-600 text-white border-blue-600'
                  : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
              ]">
                甘肃
              </button>
              <button @click="handleProvinceClick('青海')" :class="[
                'text-sm py-2 px-3 rounded-md border transition',
                selectedProvince === '青海'
                  ? 'bg-blue-600 text-white border-blue-600'
                  : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
              ]">
                青海
              </button>
              <button @click="handleProvinceClick('宁夏')" :class="[
                'text-sm py-2 px-3 rounded-md border transition',
                selectedProvince === '宁夏'
                  ? 'bg-blue-600 text-white border-blue-600'
                  : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
              ]">
                宁夏
              </button>
              <button @click="handleProvinceClick('新疆')" :class="[
                'text-sm py-2 px-3 rounded-md border transition',
                selectedProvince === '新疆'
                  ? 'bg-blue-600 text-white border-blue-600'
                  : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
              ]">
                新疆
              </button>
            </div>
          </div>
          <div class="grid grid-cols-1 gap-6 mt-6">
            <!-- 专业名称和专业特色 -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div>
                <label class="block text-sm font-medium mb-2 text-gray-800">专业名称</label>
                <input v-model="majorName"
                  class="w-full bg-white text-gray-900 border border-gray-300 rounded-md py-2 px-3 focus:border-blue-500 focus:ring-2 focus:ring-blue-500/50 transition outline-none"
                  placeholder="输入专业名称" type="text" />
              </div>
              <div>
                <label class="block text-sm font-medium mb-2 text-gray-800">专业特色</label>
                <div class="grid grid-cols-2 gap-2">
                  <button @click="handleMajorFeatureClick('双一流')" :class="[
                    'text-sm py-2 px-3 rounded-md border transition',
                    selectedMajorFeature === '双一流'
                      ? 'bg-blue-600 text-white border-blue-600'
                      : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                  ]">
                    双一流
                  </button>
                  <button @click="handleMajorFeatureClick('特色专业')" :class="[
                    'text-sm py-2 px-3 rounded-md border transition',
                    selectedMajorFeature === '特色专业'
                      ? 'bg-blue-600 text-white border-blue-600'
                      : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                  ]">
                    特色专业
                  </button>
                  <button @click="handleMajorFeatureClick('重点学科')" :class="[
                    'text-sm py-2 px-3 rounded-md border transition',
                    selectedMajorFeature === '重点学科'
                      ? 'bg-blue-600 text-white border-blue-600'
                      : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                  ]">
                    重点学科
                  </button>
                  <button @click="handleMajorFeatureClick('国家级优势')" :class="[
                    'text-sm py-2 px-3 rounded-md border transition',
                    selectedMajorFeature === '国家级优势'
                      ? 'bg-blue-600 text-white border-blue-600'
                      : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                  ]">
                    国家级优势
                  </button>
                </div>
              </div>
            </div>
            <!-- 录取范围 - 单独一行 -->
            <div>
              <label class="block text-sm font-medium mb-2 text-gray-800">录取范围</label>
              <div class="flex flex-wrap bg-white border border-gray-300 rounded-md p-3 gap-4">
                <label class="flex items-center space-x-2 text-sm">
                  <input v-model="admissionRange" @change="handleAdmissionRangeChange"
                    class="h-4 w-4 text-blue-600 bg-white" name="admission_range" type="radio" value="全部" />
                  <span class="text-gray-700">全部</span>
                </label>
                <label class="flex items-center space-x-2 text-sm">
                  <input v-model="admissionRange" @change="handleAdmissionRangeChange"
                    class="h-4 w-4 text-blue-600 bg-white" name="admission_range" type="radio" value="可冲击" />
                  <span class="text-gray-700">可冲击</span>
                </label>
                <label class="flex items-center space-x-2 text-sm">
                  <input v-model="admissionRange" @change="handleAdmissionRangeChange"
                    class="h-4 w-4 text-blue-600 bg-white" name="admission_range" type="radio" value="较稳妥" />
                  <span class="text-gray-700">较稳妥</span>
                </label>
                <label class="flex items-center space-x-2 text-sm">
                  <input v-model="admissionRange" @change="handleAdmissionRangeChange"
                    class="h-4 w-4 text-blue-600 bg-white" name="admission_range" type="radio" value="可保底" />
                  <span class="text-gray-700">可保底</span>
                </label>
              </div>
            </div>
            <div class="mt-8 flex justify-center">
              <button
                class="bg-gradient-to-r from-blue-600 to-purple-600 text-white px-8 py-3 rounded-lg font-medium hover:from-blue-500 hover:to-purple-500 transition-all duration-300 shadow-lg">
                查询
              </button>
            </div>
          </div>
        </div>
      </section>
      <section>
        <div class="flex justify-between items-center mb-6">
          <h2 class="text-2xl font-bold">结果信息</h2>
          <div class="flex items-center gap-3">
            <button
              class="bg-gradient-to-r from-green-600 to-teal-600 text-white px-6 py-2 rounded-lg hover:from-green-500 hover:to-teal-500 transition">
              <span class="flex items-center space-x-2">
                <Icon class="text-lg" icon="material-symbols:add" />
                <span>批量填报</span>
              </span>
            </button>
            <button
              class="bg-gradient-to-r from-blue-600 to-purple-600 text-white px-6 py-2 rounded-lg hover:from-blue-500 hover:to-purple-500 transition"
              id="openWishesBtn">
              <span class="flex items-center space-x-2">
                <Icon class="text-lg" icon="mdi:heart" />
                <span>我的志愿</span>
              </span>
            </button>
          </div>
        </div>
        <div class="bg-white rounded-2xl shadow-lg overflow-hidden border border-gray-200">
          <div class="overflow-x-auto">
            <table class="min-w-full">
              <colgroup>
                <col class="min-w-[50px]" width="5%" />
                <col class="min-w-[60px]" width="8%" />
                <col class="min-w-[80px]" width="15%" />
                <col class="min-w-[80px]" width="15%" />
                <col class="min-w-[70px]" width="10%" />
                <col class="min-w-[60px]" width="8%" />
                <col class="min-w-[130px]" width="27%" />
                <col class="min-w-[60px]" width="7%" />
                <col class="min-w-[50px]" width="5%" />
              </colgroup>
              <thead class="bg-gray-100 text-sm text-left">
                <tr>
                  <th class="px-2 py-3 whitespace-nowrap">选择</th>
                  <th class="px-2 py-3 whitespace-nowrap">招生院校</th>
                  <th class="px-2 py-3 whitespace-nowrap">招生专业</th>
                  <th class="px-2 py-3">备注</th>
                  <th class="px-2 py-3 whitespace-nowrap">批次类型</th>
                  <th class="px-2 py-3 whitespace-nowrap">本年计划</th>
                  <th class="px-2 py-3 whitespace-nowrap">成绩分析</th>
                  <th class="px-2 py-3 whitespace-nowrap">录取概率</th>
                  <th class="px-2 py-3 whitespace-nowrap">填报操作</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-gray-200 text-sm">
                <tr>
                  <td class="px-2 py-4 text-center">
                    <input class="w-4 h-4" type="checkbox" />
                  </td>
                  <td class="px-2 py-4 whitespace-nowrap">
                    <div class="font-medium">山东大学</div>
                    <div class="text-xs text-gray-500">山东省 济南市 公办</div>
                    <div class="text-xs text-gray-500">院校代码：A422</div>
                    <div class="text-xs text-gray-500">一流大学 一流学科建设高校 211 985</div>
                  </td>
                  <td class="px-2 py-4 whitespace-nowrap">
                    <div>人工智能</div>
                    <div class="text-xs text-gray-500">物理和化学</div>
                    <div class="text-xs text-gray-500">代号:34 学费:6600</div>
                    <div class="text-xs text-gray-500">学科评估:B</div>
                  </td>
                  <td class="px-2 py-4 whitespace-nowrap">
                    <div class="text-xs text-gray-500">国家级特色专业</div>
                  </td>
                  <td class="px-2 py-4 whitespace-nowrap">
                    <div>批次：常规批</div>
                    <div>类型：普通类</div>
                  </td>
                  <td class="px-2 py-4 whitespace-nowrap">
                    <div>120人</div>
                  </td>
                  <td class="px-2 py-4 whitespace-nowrap">
                    <div>精确:25年最低位:62，最低分:620，录取数:120</div>
                    <div>精确:24年最低位:71，最低分:625，录取数:115</div>
                    <div>精确:23年最低位:59，最低分:624，录取数:110</div>
                  </td>
                  <td class="px-2 py-4 whitespace-nowrap">
                    <div class="bg-blue-100 text-blue-800 px-2 py-1 rounded-full text-center">
                      75%
                    </div>
                    <div class="text-center">可冲击</div>
                  </td>
                  <td class="px-2 py-4 text-center">
                    <button class="text-blue-600 font-medium">填报</button>
                  </td>
                </tr>
                <tr>
                  <td class="px-2 py-4 text-center">
                    <input class="w-4 h-4" type="checkbox" />
                  </td>
                  <td class="px-2 py-4 whitespace-nowrap">
                    <div class="font-medium">中国海洋大学</div>
                    <div class="text-xs text-gray-500">山东省 青岛市 公办</div>
                    <div class="text-xs text-gray-500">院校代码：A423</div>
                    <div class="text-xs text-gray-500">一流大学 211 985</div>
                  </td>
                  <td class="px-2 py-4 whitespace-nowrap">
                    <div>法学</div>
                    <div class="text-xs text-gray-500">不限</div>
                    <div class="text-xs text-gray-500">代号:49 学费:5280</div>
                    <div class="text-xs text-gray-500">学科评估:B</div>
                  </td>
                  <td class="px-2 py-4">
                    <div class="text-xs text-gray-500">教育部涉外法治人才协同培养创新基地</div>
                  </td>
                  <td class="px-2 py-4 whitespace-nowrap">
                    <div>批次：常规批</div>
                    <div>类型：普通类</div>
                  </td>
                  <td class="px-2 py-4 whitespace-nowrap">
                    <div>80人</div>
                  </td>
                  <td class="px-2 py-4 whitespace-nowrap">
                    <div>精确:25年最低位:621，最低分:610，录取数:80</div>
                    <div>精确:24年最低位:711，最低分:611，录取数:90</div>
                    <div>精确:23年最低位:519，最低分:615，录取数:90</div>
                  </td>
                  <td class="px-2 py-4 whitespace-nowrap">
                    <div class="bg-green-100 text-green-800 px-2 py-1 rounded-full text-center">
                      82%
                    </div>
                    <div class="text-center">较稳妥</div>
                  </td>
                  <td class="px-2 py-4 text-center">
                    <button class="text-blue-600 font-medium">填报</button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
          <!-- 分页信息和翻页按钮 -->
          <div class="bg-gray-50 border-t border-gray-200 px-6 py-4">
            <div class="flex flex-col md:flex-row justify-between items-center gap-4">
              <!-- 结果总数显示 -->
              <div class="text-sm text-gray-600">
                <span>共 <span class="font-semibold text-gray-900">3</span> 条结果 | 第
                  <span class="font-semibold text-gray-900">1</span> 页，共
                  <span class="font-semibold text-gray-900">1</span> 页</span>
              </div>
              <!-- 翻页按钮 -->
              <div class="flex items-center gap-2">
                <button
                  class="bg-white border border-gray-300 text-gray-700 px-3 py-2 rounded-md hover:bg-gray-100 transition disabled:opacity-50 disabled:cursor-not-allowed">
                  <span class="flex items-center gap-1">
                    <iconify-icon class="text-lg" icon="mdi:chevron-left"></iconify-icon>
                    上一页
                  </span>
                </button>
                <!-- 页码显示 -->
                <div class="flex items-center gap-1">
                  <button class="bg-blue-600 text-white px-3 py-2 rounded-md font-medium">1</button>
                </div>
                <button
                  class="bg-white border border-gray-300 text-gray-700 px-3 py-2 rounded-md hover:bg-gray-100 transition disabled:opacity-50 disabled:cursor-not-allowed">
                  <span class="flex items-center gap-1">
                    下一页
                    <iconify-icon class="text-lg" icon="mdi:chevron-right"></iconify-icon>
                  </span>
                </button>
              </div>
              <!-- 页码跳转 -->
              <div class="flex items-center gap-2">
                <label class="text-sm text-gray-600">跳转到第</label>
                <input class="w-12 border border-gray-300 rounded-md px-2 py-1 text-sm text-gray-900" max="1" min="1"
                  type="number" value="1" />
                <label class="text-sm text-gray-600">页</label>
                <button class="bg-blue-600 text-white px-4 py-1 rounded-md text-sm hover:bg-blue-700 transition">
                  跳转
                </button>
              </div>
            </div>
          </div>
        </div>
      </section>
    </main>
    <sideTop />
  </div>
</template>

<style lang="scss" scoped>
.volunteer-apply-page {
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

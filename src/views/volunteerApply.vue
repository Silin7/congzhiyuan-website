<script setup lang="ts">
import { ref } from 'vue'
import { Icon } from '@iconify/vue'

// 声明院校层次响应式变量 - 可选值：'本科', '专科'
const selectedSchoolLevel = ref('')
const handleSchoolLevelClick = (level: string) => {
  selectedSchoolLevel.value = level
  console.log(`选择了院校层次: ${level}`)
}

// 声明录取批次响应式变量 - 可选值：'本科提前批', '本科常规批', '专科批次'
const selectedAdmissionBatch = ref('')
const handleAdmissionBatchClick = (batch: string) => {
  selectedAdmissionBatch.value = batch
  console.log(`选择了录取批次: ${batch}`)
}

// 声明录取类型响应式变量 - 可选值：'普通类', '地方专项', '中外合作'
const selectedAdmissionType = ref('')
const handleAdmissionTypeChange = (value: string) => {
  selectedAdmissionType.value = value
  console.log(`选择了录取类型: ${value}`)
}

// 声明院校性质响应式变量 - 可选值：'公办', '民办'
const selectedSchoolNature = ref('')
const handleSchoolNatureClick = (nature: string) => {
  selectedSchoolNature.value = nature
  console.log(`选择了院校性质: ${nature}`)
}

// 声明院校省份响应式变量 - 支持多选
const selectedProvince = ref<string[]>([])
const handleProvinceClick = (province: string) => {
  // 切换省份选中状态
  const index = selectedProvince.value.indexOf(province)
  if (index > -1) {
    selectedProvince.value.splice(index, 1)
  } else {
    selectedProvince.value.push(province)
  }
  console.log(`选择了省份: ${province}, 当前选中: ${selectedProvince.value.join(', ')}`)
}

// 声明学科类型响应式变量
const disciplineCategories = ref('')
const disciplineCategoriesChange = (value: string) => {
  disciplineCategories.value = value
  console.log(`选择了学科类型: ${value}`)
}

// 声明一级学科响应式变量
const firstDiscipline = ref('')
const firstDisciplineChange = (value: string) => {
  firstDiscipline.value = value
  console.log(`选择了录取类型: ${value}`)
}

// 声明二级学科响应式变量
const subDiscipline = ref('')
const subDisciplineChange = (value: string) => {
  subDiscipline.value = value
  console.log(`选择了二级学科: ${value}`)
}

// 声明院校特色响应式变量 - 可选值：'双万计划', '卓越计划', '强基示范', '国家级优势'
const selectedMajorFeature = ref('')
const handleMajorFeatureClick = (feature: string) => {
  selectedMajorFeature.value = feature
  console.log(`选择了院校特色: ${feature}`)
}

// 声明院校名称响应式变量
const schoolName = ref('')

// 声明专业名称响应式变量
const majorName = ref('')

// “冲” 风险阈值响应式变量
const riskThreshold = ref(15)

// “冲” “保” 安全阈值响应式变量
const safeThreshold = ref(85)
</script>

<template>
  <div class="volunteer-apply-page">
    <main class="max-w-7xl mx-auto px-4 py-8">
      <section class="mb-10">
        <h2 class="text-2xl font-bold text-center mb-6">志愿填报查询</h2>
        <div class="bg-gray-50 rounded-2xl shadow-lg p-6 border border-gray-200">
          <!-- 院校层次  录取批次 录取类型 -->
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            <div>
              <label class="block text-sm font-medium mb-2 text-gray-800">院校层次</label>
              <div class="grid grid-cols-3 gap-2">
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
            <div>
              <label class="block text-sm font-medium mb-2 text-gray-800">录取批次</label>
              <div class="grid grid-cols-3 gap-2">
                <button @click="handleAdmissionBatchClick('本科提前批')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedAdmissionBatch === '本科提前批'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]">
                  本科提前批
                </button>
                <button @click="handleAdmissionBatchClick('本科常规批')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedAdmissionBatch === '本科常规批'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]">
                  本科常规批
                </button>
                <button @click="handleAdmissionBatchClick('专科批次')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedAdmissionBatch === '专科批次'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]">
                  专科批次
                </button>
              </div>
            </div>
            <div>
              <label class="block text-sm font-medium mb-2 text-gray-800">录取类型</label>
              <div class="grid grid-cols-3 gap-2">
                <button @click="handleAdmissionTypeChange('普通类')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedAdmissionType === '普通类'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]">
                  普通类
                </button>
                <button @click="handleAdmissionTypeChange('地方专项')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedAdmissionType === '地方专项'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]">
                  地方专项
                </button>
                <button @click="handleAdmissionTypeChange('中外合作')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedAdmissionType === '中外合作'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]">
                  中外合作
                </button>
              </div>
            </div>
          </div>
          <!-- 院校名称 院校性质 -->
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mt-6">
            <div>
              <label class="block text-sm font-medium mb-2 text-gray-800">院校名称</label>
              <input v-model="schoolName"
                class="w-full bg-white text-gray-900 border border-gray-300 rounded-md text-sm py-2 px-3 focus:border-blue-500 transition outline-none"
                placeholder="输入院校名称" type="text" />
            </div>
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
              </div>
            </div>
          </div>
          <!-- 院校省份（可多选）-->
          <div class="mt-6">
            <label class="block text-sm font-medium mb-2 text-gray-800">院校省份（可多选）</label>
            <div class="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-2">
              <button @click="handleProvinceClick('北京')" :class="[
                'text-sm py-2 px-3 rounded-md border transition',
                selectedProvince.includes('北京')
                  ? 'bg-blue-600 text-white border-blue-600'
                  : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
              ]">
                北京
              </button>
              <button @click="handleProvinceClick('天津')" :class="[
                'text-sm py-2 px-3 rounded-md border transition',
                selectedProvince.includes('天津')
                  ? 'bg-blue-600 text-white border-blue-600'
                  : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
              ]">
                天津
              </button>
              <button @click="handleProvinceClick('河北')" :class="[
                'text-sm py-2 px-3 rounded-md border transition',
                selectedProvince.includes('河北')
                  ? 'bg-blue-600 text-white border-blue-600'
                  : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
              ]">
                河北
              </button>
              <button @click="handleProvinceClick('山西')" :class="[
                'text-sm py-2 px-3 rounded-md border transition',
                selectedProvince.includes('山西')
                  ? 'bg-blue-600 text-white border-blue-600'
                  : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
              ]">
                山西
              </button>
              <button @click="handleProvinceClick('内蒙古')" :class="[
                'text-sm py-2 px-3 rounded-md border transition',
                selectedProvince.includes('内蒙古')
                  ? 'bg-blue-600 text-white border-blue-600'
                  : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
              ]">
                内蒙古
              </button>
              <button @click="handleProvinceClick('辽宁')" :class="[
                'text-sm py-2 px-3 rounded-md border transition',
                selectedProvince.includes('辽宁')
                  ? 'bg-blue-600 text-white border-blue-600'
                  : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
              ]">
                辽宁
              </button>
              <button @click="handleProvinceClick('吉林')" :class="[
                'text-sm py-2 px-3 rounded-md border transition',
                selectedProvince.includes('吉林')
                  ? 'bg-blue-600 text-white border-blue-600'
                  : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
              ]">
                吉林
              </button>
              <button @click="handleProvinceClick('黑龙江')" :class="[
                'text-sm py-2 px-3 rounded-md border transition',
                selectedProvince.includes('黑龙江')
                  ? 'bg-blue-600 text-white border-blue-600'
                  : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
              ]">
                黑龙江
              </button>
              <button @click="handleProvinceClick('上海')" :class="[
                'text-sm py-2 px-3 rounded-md border transition',
                selectedProvince.includes('上海')
                  ? 'bg-blue-600 text-white border-blue-600'
                  : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
              ]">
                上海
              </button>
              <button @click="handleProvinceClick('江苏')" :class="[
                'text-sm py-2 px-3 rounded-md border transition',
                selectedProvince.includes('江苏')
                  ? 'bg-blue-600 text-white border-blue-600'
                  : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
              ]">
                江苏
              </button>
              <button @click="handleProvinceClick('浙江')" :class="[
                'text-sm py-2 px-3 rounded-md border transition',
                selectedProvince.includes('浙江')
                  ? 'bg-blue-600 text-white border-blue-600'
                  : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
              ]">
                浙江
              </button>
              <button @click="handleProvinceClick('安徽')" :class="[
                'text-sm py-2 px-3 rounded-md border transition',
                selectedProvince.includes('安徽')
                  ? 'bg-blue-600 text-white border-blue-600'
                  : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
              ]">
                安徽
              </button>
              <button @click="handleProvinceClick('福建')" :class="[
                'text-sm py-2 px-3 rounded-md border transition',
                selectedProvince.includes('福建')
                  ? 'bg-blue-600 text-white border-blue-600'
                  : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
              ]">
                福建
              </button>
              <button @click="handleProvinceClick('江西')" :class="[
                'text-sm py-2 px-3 rounded-md border transition',
                selectedProvince.includes('江西')
                  ? 'bg-blue-600 text-white border-blue-600'
                  : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
              ]">
                江西
              </button>
              <button @click="handleProvinceClick('山东')" :class="[
                'text-sm py-2 px-3 rounded-md border transition',
                selectedProvince.includes('山东')
                  ? 'bg-blue-600 text-white border-blue-600'
                  : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
              ]">
                山东
              </button>
              <button @click="handleProvinceClick('河南')" :class="[
                'text-sm py-2 px-3 rounded-md border transition',
                selectedProvince.includes('河南')
                  ? 'bg-blue-600 text-white border-blue-600'
                  : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
              ]">
                河南
              </button>
              <button @click="handleProvinceClick('湖北')" :class="[
                'text-sm py-2 px-3 rounded-md border transition',
                selectedProvince.includes('湖北')
                  ? 'bg-blue-600 text-white border-blue-600'
                  : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
              ]">
                湖北
              </button>
              <button @click="handleProvinceClick('湖南')" :class="[
                'text-sm py-2 px-3 rounded-md border transition',
                selectedProvince.includes('湖南')
                  ? 'bg-blue-600 text-white border-blue-600'
                  : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
              ]">
                湖南
              </button>
              <button @click="handleProvinceClick('广东')" :class="[
                'text-sm py-2 px-3 rounded-md border transition',
                selectedProvince.includes('广东')
                  ? 'bg-blue-600 text-white border-blue-600'
                  : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
              ]">
                广东
              </button>
              <button @click="handleProvinceClick('广西')" :class="[
                'text-sm py-2 px-3 rounded-md border transition',
                selectedProvince.includes('广西')
                  ? 'bg-blue-600 text-white border-blue-600'
                  : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
              ]">
                广西
              </button>
              <button @click="handleProvinceClick('海南')" :class="[
                'text-sm py-2 px-3 rounded-md border transition',
                selectedProvince.includes('海南')
                  ? 'bg-blue-600 text-white border-blue-600'
                  : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
              ]">
                海南
              </button>
              <button @click="handleProvinceClick('重庆')" :class="[
                'text-sm py-2 px-3 rounded-md border transition',
                selectedProvince.includes('重庆')
                  ? 'bg-blue-600 text-white border-blue-600'
                  : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
              ]">
                重庆
              </button>
              <button @click="handleProvinceClick('四川')" :class="[
                'text-sm py-2 px-3 rounded-md border transition',
                selectedProvince.includes('四川')
                  ? 'bg-blue-600 text-white border-blue-600'
                  : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
              ]">
                四川
              </button>
              <button @click="handleProvinceClick('贵州')" :class="[
                'text-sm py-2 px-3 rounded-md border transition',
                selectedProvince.includes('贵州')
                  ? 'bg-blue-600 text-white border-blue-600'
                  : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
              ]">
                贵州
              </button>
              <button @click="handleProvinceClick('云南')" :class="[
                'text-sm py-2 px-3 rounded-md border transition',
                selectedProvince.includes('云南')
                  ? 'bg-blue-600 text-white border-blue-600'
                  : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
              ]">
                云南
              </button>
              <button @click="handleProvinceClick('西藏')" :class="[
                'text-sm py-2 px-3 rounded-md border transition',
                selectedProvince.includes('西藏')
                  ? 'bg-blue-600 text-white border-blue-600'
                  : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
              ]">
                西藏
              </button>
              <button @click="handleProvinceClick('陕西')" :class="[
                'text-sm py-2 px-3 rounded-md border transition',
                selectedProvince.includes('陕西')
                  ? 'bg-blue-600 text-white border-blue-600'
                  : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
              ]">
                陕西
              </button>
              <button @click="handleProvinceClick('甘肃')" :class="[
                'text-sm py-2 px-3 rounded-md border transition',
                selectedProvince.includes('甘肃')
                  ? 'bg-blue-600 text-white border-blue-600'
                  : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
              ]">
                甘肃
              </button>
              <button @click="handleProvinceClick('青海')" :class="[
                'text-sm py-2 px-3 rounded-md border transition',
                selectedProvince.includes('青海')
                  ? 'bg-blue-600 text-white border-blue-600'
                  : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
              ]">
                青海
              </button>
              <button @click="handleProvinceClick('宁夏')" :class="[
                'text-sm py-2 px-3 rounded-md border transition',
                selectedProvince.includes('宁夏')
                  ? 'bg-blue-600 text-white border-blue-600'
                  : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
              ]">
                宁夏
              </button>
              <button @click="handleProvinceClick('新疆')" :class="[
                'text-sm py-2 px-3 rounded-md border transition',
                selectedProvince.includes('新疆')
                  ? 'bg-blue-600 text-white border-blue-600'
                  : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
              ]">
                新疆
              </button>
            </div>
          </div>
          <div class="grid grid-cols-1 gap-6 mt-6">
            <!-- 专业名称 院校特色 -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div>
                <label class="block text-sm font-medium mb-2 text-gray-800">专业名称</label>
                <input v-model="majorName"
                  class="w-full bg-white text-gray-900 border border-gray-300 rounded-md text-sm py-2 px-3 focus:border-blue-500 transition outline-none"
                  placeholder="输入专业名称" type="text" />
              </div>
              <div>
                <label class="block text-sm font-medium mb-2 text-gray-800">院校特色</label>
                <div class="grid grid-cols-3 gap-2">
                  <button @click="handleMajorFeatureClick('双万计划')" :class="[
                    'text-sm py-2 px-3 rounded-md border transition',
                    selectedMajorFeature === '双万计划'
                      ? 'bg-blue-600 text-white border-blue-600'
                      : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                  ]">
                    双万计划
                  </button>
                  <button @click="handleMajorFeatureClick('卓越计划')" :class="[
                    'text-sm py-2 px-3 rounded-md border transition',
                    selectedMajorFeature === '卓越计划'
                      ? 'bg-blue-600 text-white border-blue-600'
                      : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                  ]">
                    卓越计划
                  </button>
                  <button @click="handleMajorFeatureClick('强基示范')" :class="[
                    'text-sm py-2 px-3 rounded-md border transition',
                    selectedMajorFeature === '强基示范'
                      ? 'bg-blue-600 text-white border-blue-600'
                      : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                  ]">
                    强基示范
                  </button>
                </div>
              </div>
            </div>
            <!-- 学科门类 一级学科 二级学科 -->
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
              <div>
                <div>
                  <label class="block text-sm font-medium mb-2 text-gray-800">学科门类</label>
                  <el-select v-model="disciplineCategories" placeholder="请选择学科门类" class="select-tall38px"
                    @change="disciplineCategoriesChange">
                    <el-option value="工学">工学</el-option>
                    <el-option value="理学">理学</el-option>
                    <el-option value="医学">医学</el-option>
                    <el-option value="文学">文学</el-option>
                  </el-select>
                </div>
              </div>
              <div>
                <label class="block text-sm font-medium mb-2 text-gray-800">一级学科</label>
                <el-select v-model="firstDiscipline" placeholder="请选择一级学科" class="select-tall38px"
                  @change="firstDisciplineChange">
                  <el-option value="计算机科学与技术">计算机科学与技术</el-option>
                  <el-option value="电子信息">电子信息</el-option>
                  <el-option value="软件工程">软件工程</el-option>
                </el-select>
              </div>
              <div>
                <label class="block text-sm font-medium mb-2 text-gray-800">二级学科</label>
                <el-select v-model="subDiscipline" placeholder="请选择二级学科" class="select-tall38px"
                  @change="subDisciplineChange">
                  <el-option value="人工智能">人工智能</el-option>
                  <el-option value="数据科学">数据科学</el-option>
                  <el-option value="网络安全">网络安全</el-option>
                </el-select>
              </div>
            </div>
            <!-- 录取概率范围预警 -->
            <section class="bg-blue-50/50 p-6 rounded-2xl space-y-8">
              <div>
                <div class="flex items-center space-x-2 text-slate-700 font-semibold mb-3 text-sm">
                  <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em"
                    viewBox="0 0 24 24" data-icon="solar:chart-square-bold-duotone"
                    class="iconify text-blue-600 iconify--solar">
                    <path fill="currentColor"
                      d="M12 22c-4.714 0-7.071 0-8.536-1.465C2 19.072 2 16.714 2 12s0-7.071 1.464-8.536C4.93 2 7.286 2 12 2s7.071 0 8.535 1.464C22 4.93 22 7.286 22 12s0 7.071-1.465 8.535C19.072 22 16.714 22 12 22"
                      opacity=".5"></path>
                    <path fill="currentColor"
                      d="M12 5.25a.75.75 0 0 1 .75.75v12a.75.75 0 0 1-1.5 0V6a.75.75 0 0 1 .75-.75m-5 3a.75.75 0 0 1 .75.75v9a.75.75 0 0 1-1.5 0V9A.75.75 0 0 1 7 8.25m10 4a.75.75 0 0 1 .75.75v5a.75.75 0 0 1-1.5 0v-5a.75.75 0 0 1 .75-.75">
                    </path>
                  </svg>
                  <span>录取概率范围预警</span>
                </div>
                <div class="flex gap-4">
                  <label class="cursor-pointer">
                    <input class="peer sr-only" name="range" type="radio">
                    <span
                      class="block px-4 py-2 rounded-lg bg-white border border-slate-200 text-slate-600 text-sm font-medium peer-checked:border-red-500 peer-checked:text-red-600 transition-all">冲一冲</span>
                  </label>
                  <label class="cursor-pointer">
                    <input class="peer sr-only" name="range" type="radio">
                    <span
                      class="block px-4 py-2 rounded-lg bg-white border border-slate-200 text-slate-600 text-sm font-medium peer-checked:border-orange-500 peer-checked:text-orange-600 transition-all">稳一稳</span>
                  </label>
                  <label class="cursor-pointer">
                    <input class="peer sr-only" name="range" type="radio">
                    <span
                      class="block px-4 py-2 rounded-lg bg-white border border-slate-200 text-slate-600 text-sm font-medium peer-checked:border-green-600 peer-checked:text-green-600 transition-all">保一保</span>
                  </label>
                </div>
              </div>
              <div class="grid grid-cols-1 md:grid-cols-2 gap-12">
                <div class="space-y-4">
                  <div class="flex justify-between items-center">
                    <label class="text-sm font-semibold text-slate-700">“冲” 风险阈值</label>
                    <span class="text-red-500 font-bold" id="val-chong">{{ riskThreshold }}%</span>
                  </div>
                  <input class="w-full" max="30" min="0" type="range" v-model="riskThreshold">
                  <p class="text-xs text-slate-400 text-center">风险越高，录取可能性越低，建议作为前置志愿</p>
                </div>
                <div class="space-y-4">
                  <div class="flex justify-between items-center">
                    <label class="text-sm font-semibold text-slate-700">“保” 安全阈值</label>
                    <span class="text-green-600 font-bold" id="val-bao">{{ safeThreshold }}%</span>
                  </div>
                  <input class="w-full" max="100" min="70" type="range" v-model="safeThreshold">
                  <p class="text-xs text-slate-400 text-center">安全越高，录取稳定性越强，建议作为保底志愿</p>
                </div>
              </div>
            </section>
            <!-- 立即开始智能检索 -->
            <div class="mt-8 flex justify-center">
              <button
                class="w-full md:w-64 py-4 px-8 bg-blue-600 text-white rounded-2xl font-bold text-lg shadow-lg shadow-blue-200 hover:bg-blue-700 active:scale-95 transition-all flex items-center justify-center space-x-3">
                <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em"
                  viewBox="0 0 24 24" data-icon="solar:minimalistic-magnifer-zoom-in-bold"
                  class="iconify text-2xl iconify--solar">
                  <defs>
                    <mask id="IconifyId19b962244b31ed2cc0">
                      <g fill="none">
                        <path fill="#fff" d="M20.313 11.157a9.157 9.157 0 1 1-18.313 0a9.157 9.157 0 0 1 18.313 0">
                        </path>
                        <path fill="#000" fill-rule="evenodd"
                          d="M11.157 8.024c.399 0 .723.324.723.723v1.687h1.686a.723.723 0 0 1 0 1.446H11.88v1.686a.723.723 0 1 1-1.445 0V11.88H8.747a.723.723 0 1 1 0-1.445h1.687V8.747c0-.4.323-.723.723-.723"
                          clip-rule="evenodd"></path>
                        <path fill="#fff" fill-rule="evenodd"
                          d="M18.838 18.838a.723.723 0 0 1 1.023 0l1.927 1.928a.723.723 0 0 1-1.022 1.022l-1.928-1.927a.723.723 0 0 1 0-1.023"
                          clip-rule="evenodd"></path>
                      </g>
                    </mask>
                  </defs>
                  <path fill="currentColor" d="M0 0h24v24H0z" mask="url(#IconifyId19b962244b31ed2cc0)"></path>
                </svg>
                <span>立即开始智能检索</span>
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
                    <div class="text-xs text-gray-500">国家级卓越计划</div>
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

<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { Icon } from '@iconify/vue'
import { ElTable, ElTableColumn, ElCheckbox, ElButton, ElPagination, ElMessage } from 'element-plus'
import * as api from '@/api/interfaceapi'

onMounted(() => {
  getGenListQuery()
})

// 声明院校层次响应式变量 - 可选值：'本科', '专科'
const selectedSchoolLevel = ref('')
const handleSchoolLevelClick = (level: string) => {
  selectedSchoolLevel.value = level
  selectedAdmissionBatch.value = ''
  selectedAdmissionType.value = ''
  getPcList()
  getDisciplineCategoriesList()
}

// 志愿填报页批次查询
function getPcList() {
  api.pcListApi({
    token: window.localStorage.getItem('token') || '',
    ccdm: selectedSchoolLevel.value
  }).then(res => {
    admissionBatch.value = res.data.Rs || []
  })
}

// 声明录取批次响应式变量 - 可选值：'本科提前批', '本科常规批', '专科批次'
const admissionBatch: any = ref([{ pcdm: '1', pcmc: '本科提前批' }, { pcdm: '2', pcmc: '本科常规批' }, { pcdm: '3', pcmc: '专科批次' }])
const selectedAdmissionBatch = ref('')
const handleAdmissionBatchClick = (batch: string) => {
  if (selectedSchoolLevel.value === '') {
    ElMessage.error('请先选择院校层次')
    return
  }
  selectedAdmissionBatch.value = batch
  selectedAdmissionType.value = ''
  getTddwList()
}
function getTddwList() {
  api.tddwListApi({
    token: window.localStorage.getItem('token') || '',
    ccdm: selectedSchoolLevel.value,
    pcdm: selectedAdmissionBatch.value
  }).then(res => {
    admissionTypes.value = res.data.Rs || []
  })
}

// 声明录取类型响应式变量 - 可选值：'普通计划', '地方专项', '中外合作'
const admissionTypes: any = ref([{ dddw: '1', tdmc: '普通计划' }, { dddw: '2', tdmc: '地方专项' }, { dddw: '3', tdmc: '中外合作' }])
const selectedAdmissionType = ref('')
const handleAdmissionTypeChange = (value: string) => {
  if (selectedSchoolLevel.value === '' || selectedAdmissionBatch.value === '') {
    ElMessage.error('请先选择院校层次和录取批次')
    return
  }
  selectedAdmissionType.value = value
  console.log(`选择了录取类型: ${value}`)
}

// 声明院校性质响应式变量 - 可选值：'公办', '民办'
const schoolNatures: any = ref([])
function getGenListQuery() {
  api.genListQueryApi({
    token: window.localStorage.getItem('token') || '',
    genType: 'zyts'
  }).then(res => {
    schoolNatures.value = res.data.Rs || []
  })
}
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
const disciplineCategoriesList: any = ref([])
function getDisciplineCategoriesList() {
  api.xkmllistApi({
    token: window.localStorage.getItem('token') || '',
    ccdm: selectedSchoolLevel.value
  }).then(res => {
    disciplineCategoriesList.value = res.data.Rs || []
  })
}
const disciplineCategories = ref('')
const disciplineCategoriesChange = (value: string) => {
  disciplineCategories.value = value
  firstDiscipline.value = ''
  subDiscipline.value = ''
  getFirstDisciplineList()
}

// 声明一级学科响应式变量
const firstDisciplineList: any = ref([])
function getFirstDisciplineList() {
  api.yjxklistApi({
    token: window.localStorage.getItem('token') || '',
    xkml: disciplineCategories.value
  }).then(res => {
    firstDisciplineList.value = res.data.Rs || []
  })
}
const firstDiscipline = ref('')
const firstDisciplineChange = (value: string) => {
  firstDiscipline.value = value
  subDiscipline.value = ''
  getSubDisciplineList()
}

// 声明二级学科响应式变量
const subDisciplineList: any = ref([])
function getSubDisciplineList() {
  api.ejxklistApi({
    token: window.localStorage.getItem('token') || '',
    yjxk: firstDiscipline.value
  }).then(res => {
    subDisciplineList.value = res.data || []
  })
}
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
const getSchoolNameLoading = ref(false)
const schoolNameOptions: any = ref([])
function getSchoolNameOptions() {
  getSchoolNameLoading.value = true
  api.yxqueryBymcApi({
    token: window.localStorage.getItem('token') || '',
    yxmc: schoolName.value
  }).then(res => {
    schoolNameOptions.value = res.data.Rs || []
  }).finally(() => {
    getSchoolNameLoading.value = false
  })
}

// 声明专业名称响应式变量
const majorName = ref('')
const getMajorNameLoading = ref(false)
const majorNameOptions: any = ref([])
function getMajorNameOptions() {
  getMajorNameLoading.value = true
  api.zyqueryBymcApi({
    token: window.localStorage.getItem('token') || '',
    zymc: majorName.value
  }).then(res => {
    majorNameOptions.value = res.data.Rs || []
  }).finally(() => {
    getMajorNameLoading.value = false
  })
}



// “冲” 风险阈值响应式变量
const riskThreshold = ref(15)

// “冲” “保” 安全阈值响应式变量
const safeThreshold = ref(85)

// 声明表格数据响应式变量
const tableData = ref([
  {
    id: 1,
    schoolName: '山东大学',
    schoolInfo: '山东省 济南市 公办',
    schoolCode: 'A422',
    schoolTags: '一流大学 一流学科建设高校 211 985',
    majorName: '人工智能',
    majorRequirements: '物理和化学',
    majorCode: '34',
    tuition: '6600',
    disciplineEvaluation: 'B',
    remark: '国家级卓越计划',
    batch: '常规批',
    type: '普通计划',
    plan: '120人',
    scoreAnalysis: [
      '精确:25年最低位:62，最低分:620，录取数:120',
      '精确:24年最低位:71，最低分:625，录取数:115',
      '精确:23年最低位:59，最低分:624，录取数:110'
    ],
    admissionProbability: '75%',
    probabilityLevel: '可冲击',
    probabilityColor: 'bg-blue-100 text-blue-800'
  },
  {
    id: 2,
    schoolName: '中国海洋大学',
    schoolInfo: '山东省 青岛市 公办',
    schoolCode: 'A423',
    schoolTags: '一流大学 211 985',
    majorName: '法学',
    majorRequirements: '不限',
    majorCode: '49',
    tuition: '5280',
    disciplineEvaluation: 'B',
    remark: '教育部涉外法治人才协同培养创新基地',
    batch: '常规批',
    type: '普通计划',
    plan: '80人',
    scoreAnalysis: [
      '精确:25年最低位:621，最低分:610，录取数:80',
      '精确:24年最低位:711，最低分:611，录取数:90',
      '精确:23年最低位:519，最低分:615，录取数:90'
    ],
    admissionProbability: '82%',
    probabilityLevel: '较稳妥',
    probabilityColor: 'bg-green-100 text-green-800'
  }
])

// 声明分页相关变量
const currentPage = ref(1)
const pageSize = ref(10)
const total = ref(tableData.value.length)

// 声明排序相关变量
const sortField = ref('')
const sortOrder = ref('')

// 处理选择事件
const handleSelectionChange = (selection: any[]) => {
  console.log('选中的数据:', selection)
}

// 处理分页变化
const handlePageChange = (page: number) => {
  currentPage.value = page
  console.log(`当前页码: ${page}`)
}

// 处理排序变化
const handleSortChange = (column: any) => {
  console.log('-------->', column)
  sortField.value = column.prop
  sortOrder.value = column.order
  console.log(`排序字段: ${column.prop}, 排序顺序: ${column.order}`)
}

// 处理填报操作
const handleApply = (row: any) => {
  console.log(`填报院校: ${row.schoolName}, 专业: ${row.majorName}`)
}
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
                <button @click="handleSchoolLevelClick('1')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedSchoolLevel === '1'
                    ? 'bg-blue-600 text-white border-blue-600'
                    : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                ]">
                  本科
                </button>
                <button @click="handleSchoolLevelClick('2')" :class="[
                  'text-sm py-2 px-3 rounded-md border transition',
                  selectedSchoolLevel === '2'
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
                <button v-for="(item, index) in admissionBatch" :key="index"
                  @click="handleAdmissionBatchClick(item.pcdm)" :class="[
                    'text-sm py-2 px-3 rounded-md border transition',
                    selectedAdmissionBatch === item.pcdm
                      ? 'bg-blue-600 text-white border-blue-600'
                      : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                  ]">
                  {{ item.pcmc }}
                </button>
              </div>
            </div>
            <div>
              <label class="block text-sm font-medium mb-2 text-gray-800">录取类型</label>
              <div class="grid grid-cols-3 gap-2">
                <button v-for="(item, index) in admissionTypes" :key="index"
                  @click="handleAdmissionTypeChange(item.tddw)" :class="[
                    'text-sm py-2 px-3 rounded-md border transition',
                    selectedAdmissionType === item.tddw
                      ? 'bg-blue-600 text-white border-blue-600'
                      : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                  ]">
                  {{ item.tdmc }}
                </button>
              </div>
            </div>
          </div>
          <!-- 院校名称 院校性质 -->
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mt-6">
            <div>
              <label class="block text-sm font-medium mb-2 text-gray-800">院校名称</label>
              <el-select v-model="schoolName" filterable remote reserve-keyword placeholder="输入院校名称"
                :remote-method="getSchoolNameOptions" :loading="getSchoolNameLoading" class="select-tall38px">
                <el-option v-for="(item, index) in schoolNameOptions" :key="index" :label="item.yxmc"
                  :value="item.id" />
              </el-select>
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
                <el-select v-model="majorName" filterable remote reserve-keyword placeholder="输入专业名称"
                  :remote-method="getMajorNameOptions" :loading="getMajorNameLoading" class="select-tall38px">
                  <el-option v-for="(item, index) in majorNameOptions" :key="index" :label="item.zymc"
                    :value="item.zydm" />
                </el-select>
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
                    <el-option v-for="(item, index) in disciplineCategoriesList" :key="index" :value="item.zydm"
                      :label="item.zymc" />
                  </el-select>
                </div>
              </div>
              <div>
                <label class="block text-sm font-medium mb-2 text-gray-800">一级学科</label>
                <el-select v-model="firstDiscipline" placeholder="请选择一级学科" class="select-tall38px"
                  @change="firstDisciplineChange">
                  <el-option v-for="(item, index) in firstDisciplineList" :key="index" :value="item.zydm"
                    :label="item.zymc" />
                </el-select>
              </div>
              <div>
                <label class="block text-sm font-medium mb-2 text-gray-800">二级学科</label>
                <el-select v-model="subDiscipline" placeholder="请选择二级学科" class="select-tall38px"
                  @change="subDisciplineChange">
                  <el-option v-for="(item, index) in subDisciplineList" :key="index" :value="item.zydm"
                    :label="item.zymc" />
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
        <div>
          <!--  class="bg-white rounded-2xl shadow-lg overflow-hidden border border-gray-200" -->
          <!-- Element Plus 表格 -->
          <el-table v-loading="false" :data="tableData" style="width: 100%" @selection-change="handleSelectionChange"
            @sort-change="handleSortChange" stripe border size="small" class="custom-table">
            <!-- 选择列 -->
            <el-table-column type="selection" width="40" align="center"></el-table-column>
            <!-- 招生院校列 -->
            <el-table-column prop="schoolName" label="招生院校" min-width="180" align="left">
              <template #default="scope">
                <div class="font-medium">{{ scope.row.schoolName }}</div>
                <div class="text-xs text-gray-500">{{ scope.row.schoolInfo }}</div>
                <div class="text-xs text-gray-500">院校代码：{{ scope.row.schoolCode }}</div>
                <div class="text-xs text-gray-500">{{ scope.row.schoolTags }}</div>
              </template>
            </el-table-column>

            <!-- 招生专业列 -->
            <el-table-column prop="majorName" label="招生专业" min-width="180" align="left">
              <template #default="scope">
                <div class="font-medium">{{ scope.row.majorName }}</div>
                <div class="text-xs text-gray-500">{{ scope.row.majorRequirements }}</div>
                <div class="text-xs text-gray-500">代号:{{ scope.row.majorCode }} 学费:{{ scope.row.tuition }}</div>
                <div class="text-xs text-gray-500">学科评估:{{ scope.row.disciplineEvaluation }}</div>
              </template>
            </el-table-column>

            <!-- 备注列 -->
            <el-table-column prop="remark" label="备注" min-width="120" align="left">
              <template #default="scope">
                <div class="text-xs text-gray-500">{{ scope.row.remark }}</div>
              </template>
            </el-table-column>

            <!-- 批次类型列 -->
            <el-table-column prop="batch" label="批次类型" min-width="120" align="left">
              <template #default="scope">
                <div class="text-xs">批次：{{ scope.row.batch }}</div>
                <div class="text-xs">类型：{{ scope.row.type }}</div>
              </template>
            </el-table-column>

            <!-- 本年计划列 -->
            <el-table-column prop="plan" label="本年计划" min-width="100" align="center"></el-table-column>

            <!-- 成绩分析列 -->
            <el-table-column prop="scoreAnalysis" label="成绩分析" min-width="240" align="left">
              <template #default="scope">
                <div v-for="(item, index) in scope.row.scoreAnalysis" :key="index" class="text-xs">
                  {{ item }}
                </div>
              </template>
            </el-table-column>

            <!-- 录取概率列 -->
            <el-table-column prop="admissionProbability" label="录取概率" min-width="100" sortable align="center">
              <template #default="scope">
                <div :class="[scope.row.probabilityColor, 'px-2 py-1 rounded-full text-center text-xs']">
                  {{ scope.row.admissionProbability }}
                </div>
                <div class="text-center text-xs mt-1">{{ scope.row.probabilityLevel }}</div>
              </template>
            </el-table-column>

            <!-- 填报操作列 -->
            <el-table-column label="填报操作" width="80" align="center">
              <template #default="scope">
                <el-button type="text" size="small" class="text-blue-600" @click="handleApply(scope.row)">
                  填报
                </el-button>
              </template>
            </el-table-column>
          </el-table>

          <!-- Element Plus 分页 -->
          <div class="bg-gray-50 border-t border-gray-200 px-6 py-4">
            <div class="flex flex-col md:flex-row justify-between items-center gap-4">
              <!-- 结果总数显示 -->
              <div class="text-sm text-gray-600">
                <span>共 <span class="font-semibold text-gray-900">{{ total }}</span> 条结果 | 第
                  <span class="font-semibold text-gray-900">{{ currentPage }}</span> 页，共
                  <span class="font-semibold text-gray-900">{{ Math.ceil(total / pageSize) }}</span> 页</span>
              </div>

              <!-- Element Plus 分页组件 -->
              <el-pagination v-model:current-page="currentPage" v-model:page-size="pageSize"
                :page-sizes="[10, 20, 50, 100]" :total="total" layout="sizes, prev, pager, next, jumper"
                :prev-text="'上一页'" :next-text="'下一页'" @size-change="(size) => pageSize = size"
                @current-change="handlePageChange"></el-pagination>
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

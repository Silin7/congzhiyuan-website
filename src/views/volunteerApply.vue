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
  var params = new FormData();
  params.append('token', window.localStorage.getItem('token') || '');
  params.append('genType', 'yxxz');
  // axios.post(`${baseURL}/mod/zhiYuan/GenListQuery.ajax.php`, params)
  //   .then((res: any) => {
  //     schoolNatures.value = res.data.Rs || []
  //   }).catch((error: any) => {
  //     return Promise.reject(error)
  //   })
  api.genListQueryApi({
    token: window.localStorage.getItem('token') || '',
    genType: 'yxxz'
  }).then((res: any) => {
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
const selectedSchool = ref('')
// 院校名称选择变化时触发
const handleSchoolNameChange = (value: string) => {
  selectedSchool.value = value
  console.log(`选择了院校名称: ${value}`)
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
const selectedMajor = ref('')
// 专业名称选择变化时触发
const handleMajorNameChange = (value: string) => {
  selectedMajor.value = value
  console.log(`选择了专业名称: ${value}`)
}

// 声明风险等级响应式变量 - 用于控制录取概率范围选择
// 可选值：'high'（冲一冲 - 高风险，低录取概率）, 'medium'（稳一稳 - 中等风险，中等录取概率）, 'low'（保一保 - 低风险，高录取概率）
const selectedRiskLevel = ref<'high' | 'medium' | 'low'>('medium') // 默认选择'稳一稳'
// 监听风险等级变化，根据不同等级设置默认阈值
const handleRiskLevelChange = () => {
  // 根据风险等级调整默认阈值
  switch (selectedRiskLevel.value) {
    case 'high': // 冲一冲 - 高风险
      riskThreshold.value = 25 // 较高风险阈值
      safeThreshold.value = 75 // 保持较高安全阈值
      break
    case 'medium': // 稳一稳 - 中等风险
      riskThreshold.value = 15 // 中等风险阈值
      safeThreshold.value = 85 // 中等安全阈值
      break
    case 'low': // 保一保 - 低风险
      riskThreshold.value = 10 // 较低风险阈值
      safeThreshold.value = 90 // 较高安全阈值
      break
  }
  console.log(`风险等级已切换为: ${selectedRiskLevel.value}, 风险阈值: ${riskThreshold.value}%, 安全阈值: ${safeThreshold.value}%`)
}
// “冲” 风险阈值响应式变量
const riskThreshold = ref(15)
// “保” 安全阈值响应式变量
const safeThreshold = ref(85)

// 声明表格数据响应式变量
const queryState = ref('')
const currentPage = ref(1)
const pageSize = ref(10)
const total = ref(0)
const tableData: any = ref([])

// 专业模式 - 志愿查询
function lqInfoZyQuery() {
  const data = {
    token: window.localStorage.getItem('token') || '',
    ccdm: selectedSchoolLevel.value,
    pcdm: selectedAdmissionBatch.value,
    tddw: selectedAdmissionType.value,
    yxxz: selectedSchoolNature.value,
    yxid: selectedSchool.value,
    // g.genList通用列表项查询字段拼接字符串,格式{"Rs":[{"id":11,"genType":"yxxz"},{"id":23,"genType":"yxxz"}]}
    zydm: selectedMajor.value,
    lqdc: selectedRiskLevel.value === 'high' ? '4' : selectedRiskLevel.value === 'medium' ? '3' : '2',
    startrow: currentPage.value,
    pagesize: pageSize.value,
    progressChong: riskThreshold.value,
    progressBao: safeThreshold.value,
  }
  api.lqInfoZyQueryApi(data).then((res: any) => {
    console.log(res)
    queryState.value = 'zyQuery'
    tableData.value = res.data.Rs || []
    total.value = res.recordsTotal || 0
  })
}

// 专业模式 - 填报
const zyHandleApply = (row: any) => {
  api.myChioesAddApi({
    token: window.localStorage.getItem('token') || '',
    zyId: row.zyid,
    lqdc: row.lqdc,
    lqbl: row.bl,
  }).then(res => {
    console.log(res)
  })
}

// 专业模式 - 批量填报
const handleBatchAdd = async () => {
  if (selectedRows.value.length === 0) {
    ElMessage.warning('请选择要填报的专业')
    return
  }
  try {
    const datas: any = ref([])
    await selectedRows.value.forEach((item: any) => {
      datas.value.push({
        zyid: item.zyid,
        lqdc: item.lqdc,
        lqbl: item.bl,
      })
    })
    const data = {
      token: window.localStorage.getItem('token') || '',
      jsonStr: JSON.stringify({ Rs: datas.value }),
    }
    const res = await api.myChioesBatchAddApi(data)
    console.log('-------->', res)
  } catch (error) {
    console.log(error)
    ElMessage.error('批量填报失败')
  }
}

// 专业模式 - 收藏
const zyHandleCollect = (row: any) => {
  api.zyChoicesQueryApi({
    token: window.localStorage.getItem('token') || '',
    chGroupId: row.chId,
  }).then(res => {
    console.log(res)
  })
}

// 专业组模式志愿查询
function lqInfoZyGroupQuery() {
  const data = {
    token: window.localStorage.getItem('token') || '',
    ccdm: selectedSchoolLevel.value,
    pcdm: selectedAdmissionBatch.value,
    tddw: selectedAdmissionType.value,
    yxxz: selectedSchoolNature.value,
    yxid: selectedSchool.value,
    // g.genList通用列表项查询字段拼接字符串,格式{"Rs":[{"id":11,"genType":"yxxz"},{"id":23,"genType":"yxxz"}]}
    zydm: selectedMajor.value,
    lqdc: selectedRiskLevel.value === 'high' ? '4' : selectedRiskLevel.value === 'medium' ? '3' : '2',
    startrow: currentPage.value,
    pagesize: pageSize.value,
    progressChong: riskThreshold.value,
    progressBao: safeThreshold.value,
  }
  api.lqInfoZyGroupQueryApi(data).then((res: any) => {
    console.log(res)
    queryState.value = 'zyGroupQuery'
    tableData.value = res.data.Rs || []
    total.value = res.recordsTotal || 0
  })
}

// 专业组模式收藏查询
const zyGroupHandleCollect = (row: any) => {
  api.zyGroupChoicesQueryApi({
    token: window.localStorage.getItem('token') || '',
    chGroupId: row.chId,
  }).then(res => {
    console.log(res)
  })
}

// 合并表格
const objectSpanMethod = ({ row, rowIndex, columnIndex }: any) => {
  console.log('-------->', row, rowIndex, columnIndex)
}

// 处理选择事件 - 多选
const selectedRows = ref<any[]>([])
const handleSelectionChange = (selection: any[]) => {
  selectedRows.value = selection
}

// 处理分页变化
const handlePageChange = (page: number) => {
  currentPage.value = page
  console.log(`当前页码: ${page}`)
}

// 批量处置
const handleBatchBtn = () => {
  if (selectedRows.value.length === 0) {
    ElMessage.warning('请选择要处置的专业')
    return
  }
  if (queryState.value === 'zyQuery') {
    handleBatchAdd()
  } else if (queryState.value === 'zyGroupQuery') {
    // handleBatchAdd()
  }
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
                :remote-method="getSchoolNameOptions" :loading="getSchoolNameLoading" @change="handleSchoolNameChange"
                class="select-tall38px">
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
                  :remote-method="getMajorNameOptions" :loading="getMajorNameLoading" @change="handleMajorNameChange"
                  class="select-tall38px">
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
                  <!-- 冲一冲选项 - 高风险 -->
                  <label class="cursor-pointer">
                    <input class="peer sr-only" name="range" type="radio" v-model="selectedRiskLevel" value="high"
                      @change="handleRiskLevelChange">
                    <span
                      class="block px-4 py-2 rounded-lg bg-white border border-slate-200 text-slate-600 text-sm font-medium peer-checked:border-red-500 peer-checked:text-red-600 transition-all">冲一冲</span>
                  </label>
                  <!-- 稳一稳选项 - 中等风险 -->
                  <label class="cursor-pointer">
                    <input class="peer sr-only" name="range" type="radio" v-model="selectedRiskLevel" value="medium"
                      @change="handleRiskLevelChange">
                    <span
                      class="block px-4 py-2 rounded-lg bg-white border border-slate-200 text-slate-600 text-sm font-medium peer-checked:border-orange-500 peer-checked:text-orange-600 transition-all">稳一稳</span>
                  </label>
                  <!-- 保一保选项 - 低风险 -->
                  <label class="cursor-pointer">
                    <input class="peer sr-only" name="range" type="radio" v-model="selectedRiskLevel" value="low"
                      @change="handleRiskLevelChange">
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
                class="w-full md:w-64 py-4 px-8 bg-blue-600 text-white rounded-2xl font-bold text-lg shadow-lg shadow-blue-200 hover:bg-blue-700 active:scale-95 transition-all flex items-center justify-center space-x-3"
                @click="lqInfoZyQuery" style="margin-right: 100px;">
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
                <!-- <span>立即开始智能检索</span> -->
                <span>专业模式查询</span>
              </button>
              <button
                class="w-full md:w-64 py-4 px-8 bg-blue-600 text-white rounded-2xl font-bold text-lg shadow-lg shadow-blue-200 hover:bg-blue-700 active:scale-95 transition-all flex items-center justify-center space-x-3"
                @click="lqInfoZyGroupQuery">
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
                <!-- <span>立即开始智能检索</span> -->
                <span>专业组模式查询</span>
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
              class="bg-gradient-to-r from-green-600 to-teal-600 text-white px-6 py-2 rounded-lg hover:from-green-500 hover:to-teal-500 transition"
              @click="handleBatchBtn">
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
          <!-- 专业模式查询结果表格 -->
          <el-table v-if="queryState === 'zyQuery' && tableData.length > 0" v-loading="false" :data="tableData"
            @span-method="objectSpanMethod" @selection-change="handleSelectionChange" stripe border size="small"
            class="custom-table" style="width: 100%">
            <!-- 选择列 -->
            <el-table-column type="selection" width="40" align="center"></el-table-column>
            <!-- 招生院校列 -->
            <el-table-column prop="schoolName" label="招生院校" min-width="180" align="left">
              <template #default="scope">
                <div class="font-medium yxmc">
                  {{ scope.row.yxmc }}
                  <span v-if="scope.row.lqdcstr.includes('稳')" class="lqdcstr bg2">{{ scope.row.lqdcstr }}</span>
                  <span v-else-if="scope.row.lqdcstr.includes('冲')" class="lqdcstr bg1">{{ scope.row.lqdcstr }}</span>
                  <span v-else class="lqdcstr bg3">{{ scope.row.lqdcstr }}</span>
                </div>
                <div class="text-xs text-gray-500">
                  {{ scope.row.provice }}/{{ scope.row.city }}
                  {{ scope.row.sylyx === 1 ? ' 一流大学 | ' : '' }}
                  {{ scope.row.sylxk === 1 ? '一流学科建设高校 | ' : '' }}
                  {{ scope.row.sf211 === 1 ? '211高校 |' : '' }}
                  {{ scope.row.sf985 === 1 ? '985高校' : '' }}
                  <span v-if="scope.row.byly">保研率：{{ scope.row.byly }}% |</span>
                  <span v-if="scope.row.xkkm">对应选考科目：{{ scope.row.xkkm }}</span>
                </div>
              </template>
            </el-table-column>
            <el-table-column label="招生专业" min-width="120" align="left">
              <template #default="scope">
                <div class="text-xs text-gray-500">当年计划人数：{{ scope.row.jhrs }}</div>
                <div class="text-xs text-gray-500">是否新增专业：{{ scope.row.isNew === 1 ? '是' : '否' }}</div>
                <div class="text-xs text-gray-500">专业代号：{{ scope.row.zydh }}</div>
                <div class="text-xs text-gray-500">专业名称：{{ scope.row.zymc }}</div>
                <div class="text-xs text-gray-500">学制：{{ scope.row.zymc }}</div>
                <div class="text-xs text-gray-500">学费：{{ scope.row.xzdm }}</div>
                <div class="text-xs text-gray-500">批次：{{ scope.row.pcmc }}</div>
                <div class="text-xs text-gray-500">投档单位：{{ scope.row.tddwmc }}</div>
              </template>
            </el-table-column>
            <el-table-column min-width="120" align="left">
              <template #header>
                {{ tableData[0].match1Year ?? '历年' }}
              </template>
              <template #default="scope">
                <div class="text-xs text-gray-500">
                  成绩类型：{{ scope.row.match1Type === 1 ? '精确' : scope.row.match1Type === 2 ? '近似' : '其他' }}
                </div>
                <div class="text-xs text-gray-500">位次：{{ scope.row.minwc1 }}</div>
                <div class="text-xs text-gray-500">分数：{{ scope.row.mincj1 }}</div>
                <div class="text-xs text-gray-500">录取人数：{{ scope.row.lqrs1 }}</div>
              </template>
            </el-table-column>
            <el-table-column min-width="120" align="left">
              <template #header>
                {{ tableData[0].match2Year ?? '历年' }}
              </template>
              <template #default="scope">
                <div class="text-xs text-gray-500">
                  成绩类型：{{ scope.row.match2Type === 1 ? '精确' : scope.row.match2Type === 2 ? '近似' : '其他' }}
                </div>
                <div class="text-xs text-gray-500">位次：{{ scope.row.minwc2 }}</div>
                <div class="text-xs text-gray-500">分数：{{ scope.row.mincj2 }}</div>
                <div class="text-xs text-gray-500">录取人数：{{ scope.row.lqrs2 }}</div>
              </template>
            </el-table-column>
            <el-table-column min-width="120" align="left">
              <template #header>
                {{ tableData[0].match3Year ?? '历年' }}
              </template>
              <template #default="scope">
                <div class="text-xs text-gray-500">
                  成绩类型：{{ scope.row.match3Type === 1 ? '精确' : scope.row.match3Type === 2 ? '近似' : '其他' }}
                </div>
                <div class="text-xs text-gray-500">位次：{{ scope.row.minwc3 }}</div>
                <div class="text-xs text-gray-500">分数：{{ scope.row.mincj3 }}</div>
                <div class="text-xs text-gray-500">录取人数：{{ scope.row.lqrs3 }}</div>
              </template>
            </el-table-column>
            <el-table-column prop="remark" label="备注" min-width="120" align="left">
              <template #default="scope">
                <div class="text-xs text-gray-500">{{ scope.row.jhbz }}</div>
              </template>
            </el-table-column>
            <el-table-column prop="bl" label="录取比例" min-width="80" sortable align="center">
              <template #default="scope">
                <div class="text-center text-xs mt-1">{{ scope.row.bl }}%</div>
              </template>
            </el-table-column>
            <el-table-column label="填报操作" width="120" align="center">
              <template #default="scope">
                <el-button text type="primary" size="small" @click="zyHandleApply(scope.row)">
                  填报
                </el-button>
                <el-button text type="warning" size="small" style="margin-left: 0 !important;"
                  @click="zyHandleCollect(scope.row)">
                  收藏
                </el-button>
              </template>
            </el-table-column>
          </el-table>
          <!-- 专业组模式查询结果表格 -->
          <el-table v-if="queryState === 'zyGroupQuery' && tableData.length > 0" v-loading="false" :data="tableData"
            @span-method="objectSpanMethod" @selection-change="handleSelectionChange" stripe border size="small"
            class="custom-table" style="width: 100%">
            <el-table-column type="expand">
              <template #default="props">
                <el-table :data="props.row.zyRs" border>
                  <el-table-column label="专业名称" prop="zymc" />
                  <el-table-column label="学制" prop="xzdm" />
                  <el-table-column label="学费" prop="sfbz" />
                  <el-table-column label="选考科目" prop="xkkm" />
                  <el-table-column label="计划招生人数" prop="jhrs" />
                  <el-table-column label="备注" prop="jhbz" />
                </el-table>
              </template>
            </el-table-column>
            <!-- 选择列 -->
            <el-table-column type="selection" width="40" align="center"></el-table-column>
            <!-- 招生院校列 -->
            <el-table-column prop="schoolName" label="招生院校" min-width="180" align="left">
              <template #default="scope">
                <div class="font-medium yxmc">
                  {{ scope.row.yxmc }}
                  <span v-if="scope.row.lqdcstr.includes('稳')" class="lqdcstr bg2">{{ scope.row.lqdcstr }}</span>
                  <span v-else-if="scope.row.lqdcstr.includes('冲')" class="lqdcstr bg1">{{ scope.row.lqdcstr }}</span>
                  <span v-else class="lqdcstr bg3">{{ scope.row.lqdcstr }}</span>
                </div>
                <div class="text-xs text-gray-500">
                  {{ scope.row.provice }}/{{ scope.row.city }}
                  {{ scope.row.sylyx === 1 ? ' 一流大学 | ' : '' }}
                  {{ scope.row.sylxk === 1 ? '一流学科建设高校 | ' : '' }}
                  {{ scope.row.sf211 === 1 ? '211高校 |' : '' }}
                  {{ scope.row.sf985 === 1 ? '985高校' : '' }}
                  <span v-if="scope.row.byly">保研率：{{ scope.row.byly }}% |</span>
                  <span v-if="scope.row.xkkm">对应选考科目：{{ scope.row.xkkm }}</span>
                </div>
              </template>
            </el-table-column>
            <el-table-column label="招生专业" min-width="120" align="left">
              <template #default="scope">
                <div class="text-xs text-gray-500">当年计划人数：{{ scope.row.jhrs }}</div>
                <div class="text-xs text-gray-500">是否新增专业：{{ scope.row.isNew === 1 ? '是' : '否' }}</div>
                <div class="text-xs text-gray-500">专业代号：{{ scope.row.zydh }}</div>
                <div class="text-xs text-gray-500">专业名称：{{ scope.row.zymc }}</div>
                <div class="text-xs text-gray-500">学制：{{ scope.row.zymc }}</div>
                <div class="text-xs text-gray-500">学费：{{ scope.row.xzdm }}</div>
                <div class="text-xs text-gray-500">批次：{{ scope.row.pcmc }}</div>
                <div class="text-xs text-gray-500">投档单位：{{ scope.row.tddwmc }}</div>
              </template>
            </el-table-column>
            <el-table-column min-width="120" align="left">
              <template #header>
                {{ tableData[0].match1Year ?? '历年' }}
              </template>
              <template #default="scope">
                <div class="text-xs text-gray-500">
                  成绩类型：{{ scope.row.match1Type === 1 ? '精确' : scope.row.match1Type === 2 ? '近似' : '其他' }}
                </div>
                <div class="text-xs text-gray-500">位次：{{ scope.row.minwc1 }}</div>
                <div class="text-xs text-gray-500">分数：{{ scope.row.mincj1 }}</div>
                <div class="text-xs text-gray-500">录取人数：{{ scope.row.lqrs1 }}</div>
              </template>
            </el-table-column>
            <el-table-column min-width="120" align="left">
              <template #header>
                {{ tableData[0].match2Year ?? '历年' }}
              </template>
              <template #default="scope">
                <div class="text-xs text-gray-500">
                  成绩类型：{{ scope.row.match2Type === 1 ? '精确' : scope.row.match2Type === 2 ? '近似' : '其他' }}
                </div>
                <div class="text-xs text-gray-500">位次：{{ scope.row.minwc2 }}</div>
                <div class="text-xs text-gray-500">分数：{{ scope.row.mincj2 }}</div>
                <div class="text-xs text-gray-500">录取人数：{{ scope.row.lqrs2 }}</div>
              </template>
            </el-table-column>
            <el-table-column min-width="120" align="left">
              <template #header>
                {{ tableData[0].match3Year ?? '历年' }}
              </template>
              <template #default="scope">
                <div class="text-xs text-gray-500">
                  成绩类型：{{ scope.row.match3Type === 1 ? '精确' : scope.row.match3Type === 2 ? '近似' : '其他' }}
                </div>
                <div class="text-xs text-gray-500">位次：{{ scope.row.minwc3 }}</div>
                <div class="text-xs text-gray-500">分数：{{ scope.row.mincj3 }}</div>
                <div class="text-xs text-gray-500">录取人数：{{ scope.row.lqrs3 }}</div>
              </template>
            </el-table-column>
            <el-table-column prop="remark" label="备注" min-width="120" align="left">
              <template #default="scope">
                <div class="text-xs text-gray-500">{{ scope.row.jhbz }}</div>
              </template>
            </el-table-column>
            <el-table-column prop="bl" label="录取比例" min-width="80" sortable align="center">
              <template #default="scope">
                <div class="text-center text-xs mt-1">{{ scope.row.bl }}%</div>
              </template>
            </el-table-column>
            <el-table-column label="填报操作" width="120" align="center">
              <template #default="scope">
                <el-button text type="primary" size="small" @click="zyHandleApply(scope.row)">
                  填报
                </el-button>
                <el-button text type="warning" size="small" style="margin-left: 0 !important;"
                  @click="zyGroupHandleCollect(scope.row)">
                  收藏
                </el-button>
              </template>
            </el-table-column>
          </el-table>
          <!-- Element Plus 分页 -->
          <div v-if="tableData.length > 0" class="bg-gray-50 border-t border-gray-200 px-6 py-4">
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

  .yxmc {
    margin-bottom: 10px;
    font-size: 18px;
    color: #000;
    font-weight: bold;

    .lqdcstr {
      display: inline-block;
      margin-left: 8px;
      height: 20px;
      line-height: 20px;
      font-size: 14px;
      color: #fff;
      padding: 0 10px;
      border-radius: 4px;
    }

    .bg1 {
      background-color: #FA8E23;
    }

    .bg2 {
      background-color: #15C496;
    }

    .bg3 {
      background-color: #007AFF;
    }
  }
}
</style>

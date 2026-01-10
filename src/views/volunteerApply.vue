<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { Icon } from '@iconify/vue'
import { ElTable, ElTableColumn, ElCheckbox, ElButton, ElPagination, ElMessage } from 'element-plus'
import * as api from '@/api/interfaceapi'
import { useRouter } from 'vue-router'


onMounted(() => {
  getSchoolNatures()
  getProvinceList()
  getMajorFeatureList()
})

// 院校层次
const selectedSchoolLevel = ref('')
const handleSchoolLevelClick = (level: string) => {
  selectedSchoolLevel.value = level
  selectedAdmissionBatch.value = ''
  selectedAdmissionType.value = ''
  getPcList()
  getDisciplineCategoriesList()
}

// 录取批次
const admissionBatch: any = ref([{ pcdm: '1', pcmc: '本科提前批' }, { pcdm: '2', pcmc: '本科常规批' }, { pcdm: '3', pcmc: '专科批次' }])
const getPcList = async () => {
  try {
    const res = await api.pcListApi({
      token: window.localStorage.getItem('token') || '',
      ccdm: selectedSchoolLevel.value
    })
    if (res.data.code === 0) {
      admissionBatch.value = res.data.data.Rs || []
    } else {
      ElMessage.error(res.data.message || '获取批次列表失败')
    }
  } catch (error) {
    ElMessage.error('获取批次列表失败')
  }
}
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

// 录取类型
const admissionTypes: any = ref([{ dddw: '1', tdmc: '普通计划' }, { dddw: '2', tdmc: '地方专项' }, { dddw: '3', tdmc: '中外合作' }])
const getTddwList = async () => {
  try {
    const res = await api.tddwListApi({
      token: window.localStorage.getItem('token') || '',
      ccdm: selectedSchoolLevel.value,
      pcdm: selectedAdmissionBatch.value
    })
    if (res.data.code === 0) {
      admissionTypes.value = res.data.data.Rs || []
    } else {
      ElMessage.error(res.data.message || '获取录取类型列表失败')
    }
  } catch (error) {
    ElMessage.error('获取录取类型列表失败')
  }
}
const selectedAdmissionType = ref('')
const handleAdmissionTypeChange = (value: string) => {
  if (selectedSchoolLevel.value === '' || selectedAdmissionBatch.value === '') {
    ElMessage.error('请先选择院校层次和录取批次')
    return
  }
  selectedAdmissionType.value = value
  console.log(`选择了录取类型: ${value}`)
}

// 院校名称
const schoolName = ref('')
const getSchoolNameLoading = ref(false)
const schoolNameOptions: any = ref([])
const getSchoolNameOptions = async () => {
  getSchoolNameLoading.value = true
  try {
    const res = await api.yxqueryBymcApi({
      token: window.localStorage.getItem('token') || '',
      yxmc: schoolName.value
    })
    if (res.data.code === 0) {
      schoolNameOptions.value = res.data.data.Rs || []
    } else {
      ElMessage.error(res.data.message || '获取院校名称列表失败')
    }
  } catch (error) {
    ElMessage.error('获取院校名称列表失败')
  } finally {
    getSchoolNameLoading.value = false
  }
}
const selectedSchool = ref('')
const handleSchoolNameChange = (value: string) => {
  selectedSchool.value = value
  console.log(`选择了院校名称: ${value}`)
}

// 院校性质
const schoolNatures: any = ref([])
const getSchoolNatures = async () => {
  try {
    const res = await api.genListQueryApi({
      token: window.localStorage.getItem('token') || '',
      genType: 'yxxz'
    })
    if (res.data.code === 0) {
      schoolNatures.value = res.data.data.Rs || []
    } else {
      ElMessage.error(res.data.message || '获取院校性质列表失败')
    }
  } catch (error) {
    ElMessage.error('获取院校性质列表失败')
  }
}
const selectedSchoolNature = ref('')
const handleSchoolNatureClick = (nature: string) => {
  selectedSchoolNature.value = nature
  console.log(`选择了院校性质: ${nature}`)
}

// 院校省份
const provinceList = ref<any>([])
const getProvinceList = async () => {
  try {
    const res = await api.genListQueryApi({
      token: window.localStorage.getItem('token') || '',
      genType: 'prov'
    })
    if (res.data.code == 0) {
      provinceList.value = res.data.data.Rs || []
    } else {
      ElMessage.error(res.data.message || '获取省份列表失败')
    }
  } catch (error) {
    ElMessage.error('获取省份列表失败')
  }
}
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

// 专业名称
const majorName = ref('')
const getMajorNameLoading = ref(false)
const majorNameOptions: any = ref([])
const getMajorNameOptions = async () => {
  getMajorNameLoading.value = true
  try {
    const res = await api.zyqueryBymcApi({
      token: window.localStorage.getItem('token') || '',
      zymc: majorName.value
    })
    if (res.data.code === 0) {
      majorNameOptions.value = res.data.data.Rs || []
    } else {
      ElMessage.error(res.data.message || '获取专业名称列表失败')
    }
  } catch (error) {
    ElMessage.error('获取专业名称列表失败')
  } finally {
    getMajorNameLoading.value = false
  }
}
const selectedMajor = ref('')
const handleMajorNameChange = (value: string) => {
  selectedMajor.value = value
  console.log(`选择了专业名称: ${value}`)
}

// 院校特色
const selectedMajorFeatureList = ref<any>([])
const getMajorFeatureList = async () => {
  try {
    const res = await api.genListQueryApi({
      token: window.localStorage.getItem('token') || '',
      genType: 'yxts'
    })
    if (res.data.code == 0) {
      selectedMajorFeatureList.value = res.data.data.Rs || []
    } else {
      ElMessage.error(res.data.message || '获取省份列表失败')
    }
  } catch (error) {
    ElMessage.error('获取省份列表失败')
  }
}
const selectedMajorFeature = ref('')
const handleMajorFeatureClick = (feature: string) => {
  selectedMajorFeature.value = feature
  console.log(`选择了院校特色: ${feature}`)
}

// 学科门类
const disciplineCategoriesList: any = ref([])
const getDisciplineCategoriesList = async () => {
  try {
    const res = await api.xkmllistApi({
      token: window.localStorage.getItem('token') || '',
      ccdm: selectedSchoolLevel.value
    })
    if (res.data.code == 0) {
      disciplineCategoriesList.value = res.data.data.Rs || []
    } else {
      ElMessage.error(res.data.message || '获取学科门类列表失败')
    }
  } catch (error) {
    ElMessage.error('获取学科门类列表失败')
  }
}
const disciplineCategories = ref('')
const disciplineCategoriesChange = (value: string) => {
  disciplineCategories.value = value
  firstDiscipline.value = ''
  subDiscipline.value = ''
  getFirstDisciplineList()
}

// 一级学科
const firstDisciplineList: any = ref([])
const getFirstDisciplineList = async () => {
  try {
    const res = await api.yjxklistApi({
      token: window.localStorage.getItem('token') || '',
      xkml: disciplineCategories.value
    })
    if (res.data.code == 0) {
      firstDisciplineList.value = res.data.data.Rs || []
    } else {
      ElMessage.error(res.data.message || '获取一级学科列表失败')
    }
  } catch (error) {
    ElMessage.error('获取一级学科列表失败')
  }
}
const firstDiscipline = ref('')
const firstDisciplineChange = (value: string) => {
  firstDiscipline.value = value
  subDiscipline.value = ''
  getSubDisciplineList()
}

// 二级学科
const subDisciplineList: any = ref([])
const getSubDisciplineList = async () => {
  try {
    const res = await api.ejxklistApi({
      token: window.localStorage.getItem('token') || '',
      yjxk: firstDiscipline.value
    })
    if (res.data.code == 0) {
      subDisciplineList.value = res.data.data || []
    } else {
      ElMessage.error(res.data.message || '获取二级学科列表失败')
    }
  } catch (error) {
    ElMessage.error('获取二级学科列表失败')
  }
}
const subDiscipline = ref('')
const subDisciplineChange = (value: string) => {
  subDiscipline.value = value
  console.log(`选择了二级学科: ${value}`)
}

// 录取概率范围预警 默认选择'稳一稳'
const selectedRiskLevel = ref<'high' | 'medium' | 'low'>('medium')
// 监听风险等级变化，根据不同等级设置默认阈值
const handleRiskLevelChange = () => {
  switch (selectedRiskLevel.value) {
    case 'high':
      riskThreshold.value = 25 // 较高风险阈值
      safeThreshold.value = 75 // 保持较高安全阈值
      break
    case 'medium':
      riskThreshold.value = 15 // 中等风险阈值
      safeThreshold.value = 85 // 中等安全阈值
      break
    case 'low':
      riskThreshold.value = 10 // 较低风险阈值
      safeThreshold.value = 90 // 较高安全阈值
      break
  }
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
const lqInfoZyQuery = async () => {
  const data = {
    token: window.localStorage.getItem('token') || '',
    ccdm: selectedSchoolLevel.value,
    pcdm: selectedAdmissionBatch.value,
    tddw: selectedAdmissionType.value,
    yxxz: selectedSchoolNature.value,
    yxid: selectedSchool.value,
    genList: JSON.stringify({ Rs: [{ id: selectedSchoolNature.value, genType: 'yxxz' }, { id: selectedMajorFeature.value, genType: 'yxts' }, { id: selectedProvince.value.join(','), genType: 'prov' }] }),
    // g.genList通用列表项查询字段拼接字符串,格式{"Rs":[{"id":11,"genType":"yxxz"},{"id":23,"genType":"yxxz"}]}
    zydm: selectedMajor.value,
    lqdc: selectedRiskLevel.value === 'high' ? '4' : selectedRiskLevel.value === 'medium' ? '3' : '2',
    startrow: currentPage.value,
    pagesize: pageSize.value,
    progressChong: riskThreshold.value,
    progressBao: safeThreshold.value,
  }
  console.log('专业模式 - 志愿查询 -------->', data, data.genList)
  try {
    const res = await api.lqInfoZyQueryApi(data)
    if (res.data.code == 0) {
      queryState.value = 'zyQuery'
      tableData.value = res.data.data.Rs || []
      total.value = res.data.recordsTotal || 0
    } else {
      ElMessage.error(res.data.message || '志愿查询失败')
    }
  } catch (error) {
    ElMessage.error('志愿查询失败')
  }
}

// 专业模式 - 填报
const zyHandleApply = async (row: any) => {
  try {
    const res = await api.myChioesAddApi({
      token: window.localStorage.getItem('token') || '',
      zyId: row.zyid,
      lqdc: row.lqdc,
      lqbl: row.bl,
    })
    if (res.data.code == 0) {
      ElMessage.success('填报成功')
    } else {
      ElMessage.error(res.data.message || '填报失败')
    }
  } catch (error) {
    ElMessage.error('填报失败')
  }
}

// 专业模式 - 批量填报
const selectedRows = ref<any[]>([])
const handleSelectionChange = (selection: any[]) => {
  selectedRows.value = selection
}
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
    if (res.data.code == 0) {
      ElMessage.success('批量填报成功')
    } else {
      ElMessage.error(res.data.message || '批量填报失败')
    }
  } catch (error) {
    console.log(error)
    ElMessage.error('批量填报失败')
  }
}

// 专业模式 - 收藏
const zyHandleCollect = async (row: any) => {
  try {
    const res = await api.zyChoicesQueryApi({
      token: window.localStorage.getItem('token') || '',
      chGroupId: row.chId,
    })
    if (res.data.code == 0) {
      ElMessage.success('收藏成功')
    } else {
      ElMessage.error(res.data.message || '收藏失败')
    }
  } catch (error) {
    ElMessage.error('收藏失败')
  }
}

// 专业组模式志愿查询
const lqInfoZyGroupQuery = async () => {
  const data = {
    token: window.localStorage.getItem('token') || '',
    ccdm: selectedSchoolLevel.value,
    pcdm: selectedAdmissionBatch.value,
    tddw: selectedAdmissionType.value,
    yxxz: selectedSchoolNature.value,
    yxid: selectedSchool.value,
    genList: JSON.stringify({ Rs: [{ id: selectedSchoolNature.value, genType: 'yxxz' }, { id: selectedMajorFeature.value, genType: 'yxts' }, { id: selectedProvince.value.join(','), genType: 'prov' }] }),
    // g.genList通用列表项查询字段拼接字符串,格式{"Rs":[{"id":11,"genType":"yxxz"},{"id":23,"genType":"yxxz"}]}
    zydm: selectedMajor.value,
    lqdc: selectedRiskLevel.value === 'high' ? '4' : selectedRiskLevel.value === 'medium' ? '3' : '2',
    startrow: currentPage.value,
    pagesize: pageSize.value,
    progressChong: riskThreshold.value,
    progressBao: safeThreshold.value,
  }
  console.log('专业组模式 - 志愿查询 -------->', data, data.genList)
  try {
    const res = await api.lqInfoZyGroupQueryApi(data)
    if (res.data.code == 0) {
      queryState.value = 'zyGroupQuery'
      tableData.value = res.data.data.Rs || []
      total.value = res.data.recordsTotal || 0
    } else {
      ElMessage.error(res.data.message || '志愿查询失败')
    }
  } catch (error) {
    ElMessage.error('志愿查询失败')
  }
}

// 专业组模式收藏查询
const zyGroupHandleCollect = async (row: any) => {
  try {
    const res = await api.zyGroupChoicesQueryApi({
      token: window.localStorage.getItem('token') || '',
      chGroupId: row.chId,
    })
    if (res.data.code == 0) {
      ElMessage.success('收藏成功')
    } else {
      ElMessage.error(res.data.message || '收藏失败')
    }
  } catch (error) {
    ElMessage.error('收藏失败')
  }
}

// 合并表格
const objectSpanMethod = ({ row, rowIndex, columnIndex }: any) => {
  console.log('-------->', row, rowIndex, columnIndex)
}

// 处理分页变化
const handlePageChange = (page: number) => {
  currentPage.value = page
  if (queryState.value === 'zyQuery') {
    lqInfoZyQuery()
  }
  if (queryState.value === 'zyGroupQuery') {
    lqInfoZyGroupQuery()
  }
}
const handleSizeChange = (size: number) => {
  pageSize.value = size
  if (queryState.value === 'zyQuery') {
    lqInfoZyQuery()
  }
  if (queryState.value === 'zyGroupQuery') {
    lqInfoZyGroupQuery()
  }
}

// goMyAspiration 跳转我的志愿页面
const router = useRouter()
const goMyAspiration = () => {
  router.push({ path: '/personalInfo', query: { tab: 'my-collections' } })
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
                <button v-for="(item, index) in schoolNatures" :key="index" @click="handleSchoolNatureClick(item.id)"
                  :class="[
                    'text-sm py-2 px-3 rounded-md border transition',
                    selectedSchoolNature === item.id
                      ? 'bg-blue-600 text-white border-blue-600'
                      : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                  ]">
                  {{ item.disp }}
                </button>
              </div>
            </div>
          </div>
          <!-- 院校省份（可多选）-->
          <div class="mt-6">
            <label class="block text-sm font-medium mb-2 text-gray-800">院校省份（可多选）</label>
            <div class="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-2">
              <button v-for="(item, index) in provinceList" :key="index" @click="handleProvinceClick(item.disp)" :class="[
                'text-sm py-2 px-3 rounded-md border transition',
                selectedProvince.includes(item.disp)
                  ? 'bg-blue-600 text-white border-blue-600'
                  : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
              ]">
                {{ item.disp }}
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
                  <button v-for="(item, index) in selectedMajorFeatureList" :key="index"
                    @click="handleMajorFeatureClick(item.id)" :class="[
                      'text-sm py-2 px-3 rounded-md border transition',
                      selectedMajorFeature === item.id
                        ? 'bg-blue-600 text-white border-blue-600'
                        : 'bg-white text-gray-700 border-gray-300 hover:border-blue-500',
                    ]">
                    {{ item.disp }}
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
              @click="handleBatchAdd">
              <span class="flex items-center space-x-2">
                <Icon class="text-lg" icon="material-symbols:add" />
                <span>批量填报</span>
              </span>
            </button>
            <button
              class="bg-gradient-to-r from-blue-600 to-purple-600 text-white px-6 py-2 rounded-lg hover:from-blue-500 hover:to-purple-500 transition"
              @click="goMyAspiration">
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
            @span-method="objectSpanMethod" stripe border size="small" class="custom-table" style="width: 100%">
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
            <el-table-column label="填报操作" width="80" align="center">
              <template #default="scope">
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
                :prev-text="'上一页'" :next-text="'下一页'" @size-change="handleSizeChange"
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

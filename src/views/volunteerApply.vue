<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { Icon } from '@iconify/vue'
import { ElTable, ElTableColumn, ElButton, ElPagination, ElMessage } from 'element-plus'
import * as api from '@/api/interfaceapi'

onMounted(() => {
  getPcList()
  getDisciplineCategoriesList()
  getSchoolNatures()
  getProvinceList()
  getMajorFeatureList()
  getMyChioesGroupQuery()
})

// 展开或收起
const isCollapsed = ref(false)

// 院校层次
const selectedSchoolLevel = ref('1')
const handleSchoolLevelClick = (level: string) => {
  selectedSchoolLevel.value = level
  selectedAdmissionBatch.value = ''
  selectedAdmissionType.value = ''
  getPcList()
  getDisciplineCategoriesList()
}

// 录取批次
const admissionBatch: any = ref([])
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
const admissionTypes: any = ref([])
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
const getSchoolNameOptions = async (value: any) => {
  if (value.length >= 3) {
    getSchoolNameLoading.value = true
    try {
      const res = await api.yxqueryBymcApi({
        token: window.localStorage.getItem('token') || '',
        yxmc: value || ''
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
  } else {
    schoolNameOptions.value = []
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
  if (nature === '0') {
    selectedAdmissionBatch.value = '0'
    selectedAdmissionType.value = ''
  }
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
  if (province === '0') {
    selectedProvince.value = ['0']
    return
  } else {
    const index = selectedProvince.value.indexOf('0')
    console.log('-------->', index)
    if (index > -1) {
      selectedProvince.value.splice(index, 1)
    }
  }
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
const getMajorNameOptions = async (value: any) => {
  if (value.length >= 2) {
    getMajorNameLoading.value = true
    try {
      const res = await api.zyqueryBymcApi({
        token: window.localStorage.getItem('token') || '',
        zymc: value || ''
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
  } else {
    majorNameOptions.value = []
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
const selectedMajorFeature: any = ref([])
const handleMajorFeatureClick = (feature: string) => {
  // 切换院校特色选中状态
  const index = selectedMajorFeature.value.indexOf(feature)
  if (index > -1) {
    selectedMajorFeature.value.splice(index, 1)
  } else {
    selectedMajorFeature.value.push(feature)
  }
  console.log(`选择了院校特色: ${selectedMajorFeature.value.join(', ')}`)
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
      subDisciplineList.value = res.data.data.Rs || []
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

// 录取范围 默认选择'稳一稳'
const selectedRiskLevel: any = ref(['4', '3', '2'])
const handleRiskLevelClick = (level: string) => {
  if (selectedRiskLevel.value.includes(level)) {
    selectedRiskLevel.value = selectedRiskLevel.value.filter((item: string) => item !== level)
  } else {
    selectedRiskLevel.value.push(level)
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
    genList: JSON.stringify({ Rs: [{ id: selectedSchoolNature.value, genType: 'yxxz' }, { id: selectedMajorFeature.value.join(','), genType: 'yxts' }, { id: selectedProvince.value.join(','), genType: 'prov' }] }),
    zydm: selectedMajor.value,
    lqdc: selectedRiskLevel.value.join(','),
    progressChong: riskThreshold.value,
    progressBao: safeThreshold.value,
    startrow: currentPage.value,
    pagesize: pageSize.value,
  }
  console.log('专业模式 - 志愿查询 -------->', JSON.stringify(data))
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
      lqbl: (row.bl / 100).toFixed(3),
    })
    if (res.data.code == 0) {
      ElMessage.success('填报成功')
      lqInfoZyQuery()
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
  const validRows = await selectedRows.value.filter((item: any) => item.chId == 1)
  if (validRows.length > 0) {
    ElMessage.warning('已经填报的专业，不能批量填报')
    return
  }
  try {
    const datas: any = ref([])
    await selectedRows.value.forEach((item: any) => {
      datas.value.push({
        zyid: item.zyid,
        lqdc: item.lqdc,
        lqbl: (item.bl / 100).toFixed(3),
      })
    })
    const data = {
      token: window.localStorage.getItem('token') || '',
      jsonStr: JSON.stringify({ Rs: datas.value }),
    }
    const res = await api.myChioesBatchAddApi(data)
    if (res.data.code == 0) {
      ElMessage.success('批量填报成功')
      lqInfoZyQuery()
    } else {
      ElMessage.error(res.data.message || '批量填报失败')
    }
  } catch (error) {
    console.log(error)
    ElMessage.error('批量填报失败')
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
    genList: JSON.stringify({ Rs: [{ id: selectedSchoolNature.value, genType: 'yxxz' }, { id: selectedMajorFeature.value.join(','), genType: 'yxts' }, { id: selectedProvince.value.join(','), genType: 'prov' }] }),
    zydm: selectedMajor.value,
    lqdc: selectedRiskLevel.value.join(','),
    progressChong: riskThreshold.value,
    progressBao: safeThreshold.value,
    startrow: currentPage.value,
    pagesize: pageSize.value,
  }
  console.log('专业组模式 - 志愿查询 -------->', JSON.stringify(data))
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

// 我的志愿 跳转我的志愿页面
const collectionDrawer = ref(false)
const goMyAspiration = () => {
  if (!selectedSchoolLevel.value) {
    ElMessage.warning('请选择院校层次')
    return
  }
  if (!selectedAdmissionBatch.value) {
    ElMessage.warning('请选择录取批次')
    return
  }
  collectionDrawer.value = true
  getMyChioesGroupQuery()
}

// 我的志愿 - 最外层
const myChioesGroupQueryState = ref('initQuery')
const myChioesGroupQueryList: any = ref([])
const getMyChioesGroupQuery = async () => {
  myChioesGroupQueryState.value = 'initQuery'
  try {
    const res: any = await api.myChioesGroupQueryApi({
      token: window.localStorage.getItem('token') || '',
      ccdm: selectedSchoolLevel.value,
      pcdm: selectedAdmissionBatch.value,
    })
    if (res.data.code === 0) {
      myChioesGroupQueryList.value = res.data.data.Rs || []
    } else {
      ElMessage.error(res.data.message || '查询失败')
    }
  } catch (error) {
    ElMessage.error('查询失败')
  }
}

// 专业模式 - 收藏
const zyHandleCollectList: any = ref([])
const zyHandleCollectItem: any = ref({})
const zyHandleCollect = async (row: any) => {
  myChioesGroupQueryState.value = 'zyQuery'
  zyHandleCollectItem.value = row
  try {
    const res = await api.zyChoicesQueryApi({
      token: window.localStorage.getItem('token') || '',
      chGroupId: row.chGroupId,
    })
    if (res.data.code == 0) {
      zyHandleCollectList.value = res.data.data.Rs || []
    } else {
      ElMessage.error(res.data.message || '收藏失败')
    }
  } catch (error) {
    ElMessage.error('收藏失败')
  }
}

// 专业模式 - 删除收藏
const zyHandleDelete = async (row: any) => {
  try {
    const res: any = await api.delChoiceApi({
      token: window.localStorage.getItem('token') || '',
      chId: row.chId,
    })
    if (res.data.code === 0) {
      ElMessage.success('删除成功')
      // 刷新收藏分组查询
      zyHandleCollect(zyHandleCollectItem.value)
    } else {
      ElMessage.error(res.data.message || '删除失败')
    }
  } catch (error) {
    ElMessage.error('删除失败')
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


</script>

<template>
  <div class="volunteer-apply-page">
    <main class="max-w-7xl mx-auto px-4 py-8">
      <section class="mb-10">
        <h2 class="text-2xl font-bold text-center mb-6">志愿填报查询</h2>
        <div class="bg-gray-50 rounded-2xl shadow-lg p-6 border border-gray-200">
          <div class="tagBox">
            <div class="tagTitle">院校层次：</div>
            <div class="tagContent">
              <div :class="selectedSchoolLevel === '1' ? 'primaryTag' : 'infoTag'" @click="handleSchoolLevelClick('1')">
                本科
              </div>
              <div :class="selectedSchoolLevel === '2' ? 'primaryTag' : 'infoTag'" @click="handleSchoolLevelClick('2')">
                专科
              </div>
            </div>
          </div>
          <div v-if="selectedSchoolLevel" class="tagBox">
            <div class="tagTitle">录取批次：</div>
            <div class="tagContent">
              <div :class="selectedAdmissionBatch === '0' ? 'primaryTag' : 'infoTag'"
                @click="handleAdmissionBatchClick('0')">
                不限
              </div>
              <div v-for="(item, index) in admissionBatch" :key="index"
                :class="selectedAdmissionBatch === item.pcdm ? 'primaryTag' : 'infoTag'"
                @click="handleAdmissionBatchClick(item.pcdm)">
                {{ item.pcmc }}
              </div>
            </div>
          </div>
          <div v-if="selectedAdmissionBatch && selectedAdmissionBatch != '0'" class="tagBox">
            <div class="tagTitle">录取类型：</div>
            <div class="tagContent">
              <div v-for="(item, index) in admissionTypes" :key="index"
                :class="selectedAdmissionType === item.tddw ? 'primaryTag' : 'infoTag'"
                @click="handleAdmissionTypeChange(item.tddw)">
                {{ item.tddwmc }}
              </div>
            </div>
          </div>
          <div class="tagBox">
            <div class="tagTitle">院校名称：</div>
            <el-select v-model="schoolName" filterable remote reserve-keyword placeholder="输入院校名称"
              :remote-method="getSchoolNameOptions" :loading="getSchoolNameLoading" @change="handleSchoolNameChange"
              class="select-tall38px" clearable style="margin-bottom: 10px; width: calc(50% - 90px);">
              <el-option v-for="(item, index) in schoolNameOptions" :key="index" :label="item.text" :value="item.id" />
            </el-select>
          </div>
          <div class="tagBox">
            <div class="tagTitle">院校性质：</div>
            <div class="tagContent">
              <div :class="selectedSchoolNature === '0' ? 'primaryTag' : 'infoTag'"
                @click="handleSchoolNatureClick('0')">
                不限
              </div>
              <div v-for="(item, index) in schoolNatures" :key="index"
                :class="selectedSchoolNature === item.id ? 'primaryTag' : 'infoTag'"
                @click="handleSchoolNatureClick(item.id)">
                {{ item.disp }}
              </div>
            </div>
          </div>
          <div v-if="!isCollapsed" class="tagBox">
            <div class="tagTitle">院校特色：</div>
            <div class="tagContent">
              <div v-for="(item, index) in selectedMajorFeatureList" :key="index"
                :class="selectedMajorFeature.includes(item.id) ? 'primaryTag' : 'infoTag'"
                @click="handleMajorFeatureClick(item.id)">
                {{ item.disp }}
              </div>
            </div>
          </div>
          <div v-if="!isCollapsed" class="tagBox">
            <div class="tagTitle">
              <p>院校省份：</p>
              <p>（可多选）</p>
            </div>
            <div class="tagContent">
              <div :class="selectedProvince.includes('0') ? 'primaryTag' : 'infoTag'" @click="handleProvinceClick('0')">
                全选
              </div>
              <div v-for="(item, index) in provinceList" :key="index"
                :class="selectedProvince.includes(item.id) ? 'primaryTag' : 'infoTag'"
                @click="handleProvinceClick(item.id)">
                {{ item.province }}
              </div>
            </div>
          </div>
          <!-- 专业名称 学科门类 一级学科 二级学科 -->
          <el-row v-if="!isCollapsed" :gutter="20">
            <el-col :span="6">
              <div class="tagTitle">专业名称：</div>
              <el-select v-model="majorName" filterable remote reserve-keyword placeholder="输入专业名称"
                :remote-method="getMajorNameOptions" :loading="getMajorNameLoading" @change="handleMajorNameChange"
                class="select-tall38px">
                <el-option v-for="(item, index) in majorNameOptions" :key="index" :label="item.text" :value="item.id" />
              </el-select>
            </el-col>
            <el-col :span="6">
              <div class="tagTitle">学科门类：</div>
              <el-select v-model="disciplineCategories" placeholder="请选择学科门类" class="select-tall38px"
                @change="disciplineCategoriesChange">
                <el-option v-for="(item, index) in disciplineCategoriesList" :key="index" :value="item.zydm"
                  :label="item.zymc" />
              </el-select>
            </el-col>
            <el-col :span="6">
              <div class="tagTitle">一级学科：</div>
              <el-select v-model="firstDiscipline" placeholder="请选择一级学科" class="select-tall38px"
                @change="firstDisciplineChange">
                <el-option v-for="(item, index) in firstDisciplineList" :key="index" :value="item.zydm"
                  :label="item.zymc" />
              </el-select>
            </el-col>
            <el-col :span="6">
              <div class="tagTitle">二级学科：</div>
              <el-select v-model="subDiscipline" placeholder="请选择二级学科" class="select-tall38px"
                @change="subDisciplineChange">
                <el-option v-for="(item, index) in subDisciplineList" :key="index" :value="item.zydm"
                  :label="item.zymc" />
              </el-select>
            </el-col>
          </el-row>
          <!-- 录取范围 -->
          <div v-if="!isCollapsed">
            <div class="flex items-center" style="margin: 20px 0;">
              <div class="tagTitle" style="margin-bottom: 0;">录取范围：</div>
              <el-tag :type="selectedRiskLevel.includes('4') ? 'danger' : 'info'"
                style="margin-right: 10px; cursor: pointer;" @click="handleRiskLevelClick('4')">冲一冲</el-tag>
              <el-tag :type="selectedRiskLevel.includes('3') ? 'warning' : 'info'"
                style="margin-right: 10px; cursor: pointer;" @click="handleRiskLevelClick('3')">稳一稳</el-tag>
              <el-tag :type="selectedRiskLevel.includes('2') ? 'success' : 'info'"
                style="margin-right: 10px; cursor: pointer;" @click="handleRiskLevelClick('2')">保一保</el-tag>
              <el-tag :type="selectedRiskLevel.includes('-2') ? 'primary' : 'info'"
                style="margin-right: 10px; cursor: pointer;" @click="handleRiskLevelClick('-2')">新增</el-tag>
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
          </div>
          <div class="zksqBox" @click="isCollapsed = !isCollapsed">
            <span v-if="isCollapsed">展开</span>
            <el-icon v-if="isCollapsed" color="#2563EB">
              <ArrowDownBold />
            </el-icon>
            <span v-if="!isCollapsed">收起</span>
            <el-icon v-if="!isCollapsed" color="#2563EB">
              <ArrowUpBold />
            </el-icon>
          </div>
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
      </section>
      <section v-if="tableData.length > 0">
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
          <el-table v-if="queryState === 'zyQuery'" v-loading="false" :data="tableData" @span-method="objectSpanMethod"
            @selection-change="handleSelectionChange" stripe border size="small" class="custom-table"
            style="width: 100%">
            <el-table-column type="selection" width="40" align="center"></el-table-column>
            <el-table-column prop="schoolName" label="招生院校" min-width="130" align="left">
              <template #default="scope">
                <div class="font-medium tableyxmc">
                  <span>{{ scope.row.yxmc }}</span>
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
                  <span v-if="scope.row.byly">保研率：{{ scope.row.byly }}</span>
                </div>
              </template>
            </el-table-column>
            <el-table-column label="招生专业" min-width="200" align="left">
              <template #default="scope">
                <div class="tablezy">
                  <div class="text-xs text-gray-500">计划人数：<span>{{ scope.row.jhrs }}</span>
                  </div>
                  <div class="text-xs text-gray-500">专业代号：<span>{{ scope.row.zydh }}</span>
                  </div>
                  <div class="text-xs text-gray-500">专业名称：<span>{{ scope.row.zymc }}</span>
                  </div>
                  <el-tooltip v-if="scope.row.jhb" popper-class="custom-tooltip" effect="dark" :content="scope.row.jhb"
                    placement="top">
                    <div class="text-xs text-gray-500">备注：<span class="beizhu">{{ scope.row.jhb }}</span></div>
                  </el-tooltip>
                  <div v-if="scope.row.xkkm" class="text-xs text-gray-500">选科：<span>{{ scope.row.xkkm }}</span></div>
                  <div class="text-xs text-gray-500">学制：<span>{{ scope.row.xzdm }}</span>
                  </div>
                  <div class="text-xs text-gray-500">学费：<span>{{ scope.row.sfbz }}</span>
                  </div>
                  <div class="text-xs text-gray-500">批次：<span>{{ scope.row.pcmc }}</span>
                  </div>
                  <div class="text-xs text-gray-500">投档单位：<span>{{ scope.row.tddwmc }}</span>
                  </div>
                </div>
              </template>
            </el-table-column>
            <el-table-column min-width="100" align="left">
              <template #header>
                {{ tableData[0].match1Year ?? '历年' }}
              </template>
              <template #default="scope">
                <div v-if="scope.row.minwc1 != 0 && scope.row.mincj1 != 0" class="tablezy">
                  <div class="text-xs text-gray-500">
                    成绩类型：<span>{{ scope.row.match1Type === 1 ? '精确' : scope.row.match1Type === 2 ? '近似' : '其他' }}</span>
                  </div>
                  <div class="text-xs text-gray-500">位次：<span>{{ scope.row.minwc1 }}</span></div>
                  <div class="text-xs text-gray-500">分数：<span>{{ scope.row.mincj1 }}</span></div>
                  <div class="text-xs text-gray-500" style="margin-bottom: 0;">录取人数：<span>{{ scope.row.lqrs1 }}</span>
                  </div>
                </div>
              </template>
            </el-table-column>
            <el-table-column min-width="100" align="left">
              <template #header>
                {{ tableData[0].match2Year ?? '历年' }}
              </template>
              <template #default="scope">
                <div v-if="scope.row.minwc2 != 0 && scope.row.mincj2 != 0" class="tablezy">
                  <div class="text-xs text-gray-500">
                    成绩类型：<span>{{ scope.row.match2Type === 1 ? '精确' : scope.row.match2Type === 2 ? '近似' : '其他' }}</span>
                  </div>
                  <div class="text-xs text-gray-500">位次：<span>{{ scope.row.minwc2 }}</span></div>
                  <div class="text-xs text-gray-500">分数：<span>{{ scope.row.mincj2 }}</span></div>
                  <div class="text-xs text-gray-500" style="margin-bottom: 0;">录取人数：<span>{{ scope.row.lqrs2 }}</span>
                  </div>
                </div>
              </template>
            </el-table-column>
            <el-table-column min-width="100" align="left">
              <template #header>
                {{ tableData[0].match3Year ?? '历年' }}
              </template>
              <template #default="scope">
                <div v-if="scope.row.minwc3 != 0 && scope.row.mincj3 != 0" class="tablezy">
                  <div class="text-xs text-gray-500">
                    成绩类型：<span>{{ scope.row.match3Type === 1 ? '精确' : scope.row.match3Type === 2 ? '近似' : '其他' }}</span>
                  </div>
                  <div class="text-xs text-gray-500">位次：<span>{{ scope.row.minwc3 }}</span></div>
                  <div class="text-xs text-gray-500">分数：<span>{{ scope.row.mincj3 }}</span></div>
                  <div class="text-xs text-gray-500" style="margin-bottom: 0;">录取人数：<span>{{ scope.row.lqrs3 }}</span>
                  </div>
                </div>
              </template>
            </el-table-column>
            <el-table-column prop="bl" label="录取比例" width="90" sortable align="center">
              <template #default="scope">
                <div class="text-center text-xs mt-1">
                  <span style="font-weight: bold; color: #000;">{{ scope.row.bl }}</span>%
                </div>
              </template>
            </el-table-column>
            <el-table-column label="操作" width="80" align="center">
              <template #default="scope">
                <el-button v-if="scope.row.chId == 0" text type="primary" size="small"
                  @click="zyHandleApply(scope.row)">
                  填报
                </el-button>
              </template>
            </el-table-column>
          </el-table>
          <!-- 专业组模式查询结果表格 -->
          <el-table v-if="queryState === 'zyGroupQuery'" v-loading="false" :data="tableData"
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
            <el-table-column prop="schoolName" label="招生院校" min-width="130" align="left">
              <template #default="scope">
                <div class="font-medium tableyxmc">
                  <span>{{ scope.row.yxmc }}</span>
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
                  <span v-if="scope.row.byly">保研率：{{ scope.row.byly }}</span>
                </div>
              </template>
            </el-table-column>
            <el-table-column label="招生专业" min-width="200" align="left">
              <template #default="scope">
                <div class="tablezy">
                  <div class="text-xs text-gray-500">计划人数：<span>{{ scope.row.jhrs }}</span>
                  </div>
                  <div class="text-xs text-gray-500">专业代号：<span>{{ scope.row.zydh }}</span>
                  </div>
                  <div class="text-xs text-gray-500">专业名称：<span>{{ scope.row.zymc }}</span>
                  </div>
                  <el-tooltip v-if="scope.row.jhb" popper-class="custom-tooltip" effect="dark" :content="scope.row.jhb"
                    placement="top">
                    <div class="text-xs text-gray-500">备注：<span class="beizhu">{{ scope.row.jhb }}</span></div>
                  </el-tooltip>
                  <div v-if="scope.row.xkkm" class="text-xs text-gray-500">选科：<span>{{ scope.row.xkkm }}</span></div>
                  <div class="text-xs text-gray-500">学制：<span>{{ scope.row.xzdm }}</span>
                  </div>
                  <div class="text-xs text-gray-500">学费：<span>{{ scope.row.sfbz }}</span>
                  </div>
                  <div class="text-xs text-gray-500">批次：<span>{{ scope.row.pcmc }}</span>
                  </div>
                  <div class="text-xs text-gray-500">投档单位：<span>{{ scope.row.tddwmc }}</span>
                  </div>
                </div>
              </template>
            </el-table-column>
            <el-table-column min-width="100" align="left">
              <template #header>
                {{ tableData[0].match1Year ?? '历年' }}
              </template>
              <template #default="scope">
                <div v-if="scope.row.minwc1 != 0 && scope.row.mincj1 != 0" class="tablezy">
                  <div class="text-xs text-gray-500">
                    成绩类型：<span>{{ scope.row.match1Type === 1 ? '精确' : scope.row.match1Type === 2 ? '近似' : '其他' }}</span>
                  </div>
                  <div class="text-xs text-gray-500">位次：<span>{{ scope.row.minwc1 }}</span></div>
                  <div class="text-xs text-gray-500">分数：<span>{{ scope.row.mincj1 }}</span></div>
                  <div class="text-xs text-gray-500" style="margin-bottom: 0;">录取人数：<span>{{ scope.row.lqrs1 }}</span>
                  </div>
                </div>
              </template>
            </el-table-column>
            <el-table-column min-width="100" align="left">
              <template #header>
                {{ tableData[0].match2Year ?? '历年' }}
              </template>
              <template #default="scope">
                <div v-if="scope.row.minwc2 != 0 && scope.row.mincj2 != 0" class="tablezy">
                  <div class="text-xs text-gray-500">
                    成绩类型：<span>{{ scope.row.match2Type === 1 ? '精确' : scope.row.match2Type === 2 ? '近似' : '其他' }}</span>
                  </div>
                  <div class="text-xs text-gray-500">位次：<span>{{ scope.row.minwc2 }}</span></div>
                  <div class="text-xs text-gray-500">分数：<span>{{ scope.row.mincj2 }}</span></div>
                  <div class="text-xs text-gray-500" style="margin-bottom: 0;">录取人数：<span>{{ scope.row.lqrs2 }}</span>
                  </div>
                </div>
              </template>
            </el-table-column>
            <el-table-column min-width="100" align="left">
              <template #header>
                {{ tableData[0].match3Year ?? '历年' }}
              </template>
              <template #default="scope">
                <div v-if="scope.row.minwc3 != 0 && scope.row.mincj3 != 0" class="tablezy">
                  <div class="text-xs text-gray-500">
                    成绩类型：<span>{{ scope.row.match3Type === 1 ? '精确' : scope.row.match3Type === 2 ? '近似' : '其他' }}</span>
                  </div>
                  <div class="text-xs text-gray-500">位次：<span>{{ scope.row.minwc3 }}</span></div>
                  <div class="text-xs text-gray-500">分数：<span>{{ scope.row.mincj3 }}</span></div>
                  <div class="text-xs text-gray-500" style="margin-bottom: 0;">录取人数：<span>{{ scope.row.lqrs3 }}</span>
                  </div>
                </div>
              </template>
            </el-table-column>
            <el-table-column prop="bl" label="录取比例" width="90" sortable align="center">
              <template #default="scope">
                <div class="text-center text-xs mt-1">
                  <span style="font-weight: bold; color: #000;">{{ scope.row.bl }}</span>%
                </div>
              </template>
            </el-table-column>
            <!-- <el-table-column label="填报操作" width="80" align="center">
              <template #default="scope">
                <el-button text type="warning" size="small" style="margin-left: 0 !important;"
                  @click="zyGroupHandleCollect(scope.row)">
                  收藏
                </el-button>
              </template>
            </el-table-column> -->
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
                :prev-text="'上一页'" :next-text="'下一页'" @size-change="handleSizeChange"
                @current-change="handlePageChange"></el-pagination>
            </div>
          </div>
        </div>
      </section>
      <!-- header-class="drawer-header" -->
      <el-drawer v-model="collectionDrawer" direction="rtl" :show-close="false" size="360" style="height: 100vh;">
        <template #header>
          <div
            class="bg-gradient-to-r from-blue-600 to-purple-600 text-white px-6 py-4 flex justify-between items-center sticky top-0 z-10">
            <h3 class="text-xl font-bold">我的志愿</h3>
            <el-icon size="24" @click="collectionDrawer = false" style="cursor: pointer;">
              <Close />
            </el-icon>
          </div>
        </template>
        <div v-if="myChioesGroupQueryList[0]?.chGroupId == 0" class="text-center py-12">
          <el-icon class="text-5xl text-gray-300 mb-4" size="50" color="rgb(107 114 128)">
            <MessageBox />
          </el-icon>
          <p class="text-gray-500 text-sm">还没有添加志愿，请点击表格中的"填报"按钮添加</p>
        </div>
        <div
          v-if="myChioesGroupQueryList?.length > 0 && myChioesGroupQueryList[0]?.chGroupId != 0 && myChioesGroupQueryState === 'initQuery'">
          <div v-for="(item, index) in myChioesGroupQueryList" :key="index" class="chGroupBox"
            @click="zyHandleCollect(item)">
            <div class="chGroupName">{{ item.chGroupName }}</div>
            <div class="text-xs text-gray-500 chGroupSub">
              已经收藏数量：<span>{{ item.addNum }}</span>
            </div>
            <div class="text-xs text-gray-500 chGroupSub">
              最大收藏数量：<span>{{ item.maxNum }}</span>
            </div>
            <el-icon color="#2563EB" class="chGroupIcon">
              <ArrowRightBold />
            </el-icon>
          </div>
        </div>
        <div v-if="myChioesGroupQueryState === 'zyQuery'">
          <div class="flex items-center" style="margin-bottom: 10px; color: #2563EB; cursor: pointer;"
            @click="goMyAspiration">
            <el-icon>
              <ArrowLeft />
            </el-icon>
            <span>返回</span>
          </div>
          <div v-for="(item, index) in zyHandleCollectList" :key="index" class="chGroupBox">
            <div class="chGroupName">
              <span>{{ item.yxmc }}</span>
              <span class="lqdcstr bg3">{{ item.yxdm }}</span>
            </div>
            <div class="text-xs text-gray-500 chGroupSub">
              <p style="width: 100%;">专业名称：<span>{{ item.zymc }}</span></p>
              <p>专业代号：<span>{{ item.zydh }}</span></p>
              <p>计划人数：<span>{{ item.jhrs }}</span></p>
            </div>
            <div class="text-xs text-gray-500 chGroupSub">
              <p v-if="item.bl">概率：<span>{{ item.bl }}%</span></p>
              <p v-if="item.lqdcstr.includes('稳')" class="lqdcstr bg2">{{ item.lqdcstr }}</p>
              <p v-else-if="item.lqdcstr.includes('冲')" class="lqdcstr bg1">{{ item.lqdcstr }}</p>
              <p v-else class="lqdcstr bg3">{{ item.lqdcstr }}</p>
            </div>
            <el-icon class="deleteIcon" color="#F56C6C" @click="zyHandleDelete(item)">
              <DeleteFilled />
            </el-icon>
          </div>
        </div>
      </el-drawer>
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

  .tableyxmc {
    margin-bottom: 10px;
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    font-size: 16px;
    color: #000;
    font-weight: bold;

    span:first-child {
      margin-right: 4px;
      line-height: 30px;
    }
  }

  .tablezy {
    display: flex;
    flex-wrap: wrap;

    div {
      display: flex;
      align-items: center;
      margin-bottom: 8px;
      margin-right: 16px;
      color: #646566;
      font-size: 12px;
      line-height: 14px;

      &:last-child {
        margin-right: 0;
      }

      span {
        font-size: 14px;
        line-height: 14px;
        color: #333;
      }

      .beizhu {
        display: inline-block;
        padding: 0 10px;
        width: 100px;
        font-size: 12px;
        height: 16px;
        line-height: 16px;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        background-color: #00000030;
        border-radius: 2px;

        &:hover {
          cursor: pointer;
        }
      }
    }
  }

  .lqdcstr {
    height: 20px;
    line-height: 20px;
    font-size: 12px;
    color: #fff;
    padding: 0 4px;
    border-radius: 4px;
  }

  .bg1 {
    background-color: #FA8E23;
  }

  .bg2 {
    background-color: #15C496;
  }

  .bg3 {
    background-color: #2563EB;
  }

  .tagBox {
    margin-bottom: 10px;
    display: flex;
    align-items: center;
  }

  .tagTitle {
    margin-bottom: 10px;
    margin-right: 20px;
    font-size: 14px;
    color: #646566;
  }

  .tagContent {
    width: calc(100% - 100px);
    display: flex;
    align-items: center;
    flex-wrap: wrap;

    .primaryTag {
      cursor: pointer;
      margin-bottom: 10px;
      margin-right: 8px;
      font-size: 14px;
      line-height: 30px;
      padding: 0 20px;
      color: #fff;
      background-color: #2563EB;
      border: 1px solid #2563EB;
      border-radius: 4px;
    }

    .infoTag {
      cursor: pointer;
      margin-bottom: 10px;
      margin-right: 8px;
      font-size: 14px;
      line-height: 30px;
      color: rgb(55 65 81);
      padding: 0 20px;
      background-color: #fff;
      border: 1px solid rgb(209 213 219 / var(--tw-border-opacity));
      border-radius: 4px;
    }
  }

  .zksqBox {
    cursor: pointer;
    margin: 20px auto;
    width: 100px;
    display: flex;
    align-items: center;
    justify-content: center;

    span {
      margin-right: 6px;
      color: #2563EB;
    }
  }

  .chGroupBox {
    cursor: pointer;
    position: relative;
    margin-bottom: 20px;
    background-color: #2563EB10;
    padding: 10px 40px 10px 10px;
    border-radius: 10px;

    .chGroupName {
      display: flex;
      flex-wrap: wrap;
      font-size: 16px;
      line-height: 20px;
      font-weight: 600;
      color: #333;
      margin-bottom: 6px;

      span {
        display: inline-block;
        margin-right: 10px;
        margin-bottom: 10px;
      }
    }

    .chGroupSub {
      display: flex;
      flex-wrap: wrap;
      font-size: 12px;
      line-height: 20px;
      color: #646566;

      p {
        margin-right: 10px;
        margin-bottom: 6px;
        line-height: 20px;
      }

      span {
        font-size: 14px;
        line-height: 20px;
        color: #2563EB;
      }
    }

    .chGroupIcon {
      position: absolute;
      top: 50%;
      right: 10px;
      transform: translateY(-50%);
    }

    .deleteIcon {
      cursor: pointer;
      position: absolute;
      top: 10px;
      right: 10px;
    }
  }
}
</style>

<style>
.drawer-header {
  border: 1px solid red;
  display: flex;
  justify-content: space-between;
  background-color: red;
}

.el-drawer__header {
  padding: 0 !important;
  margin-bottom: 0 !important;
}
</style>

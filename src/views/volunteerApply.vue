<script setup lang="ts">
import { nextTick, onMounted, ref, watch } from 'vue'
import { Icon } from '@iconify/vue'
import { ElTable, ElTableColumn, ElButton, ElPagination, ElMessage } from 'element-plus'
import * as api from '@/api/interfaceapi'
import selectProvince from '@/components/selectProvince.vue'


onMounted(() => {
  getPcList()
  if (localStorage.getItem('selectedAdmissionBatch')) {
    getTddwList()
  }
  getDisciplineCategoriesList()
  getSchoolNatures()
  getProvinceList()
  getMajorFeatureList()
})

// 1:所在省份专业模式 2:所在省份专业组模式
const zyType = JSON.parse(localStorage.getItem('userInfo') || '{}')?.zyType || '1'

// 展开或收起
const isCollapsed = ref(true)

// 院校层次
const selectedSchoolLevel = ref(localStorage.getItem('selectedSchoolLevel') || '1')
const handleSchoolLevelClick = (level: string) => {
  localStorage.setItem('selectedSchoolLevel', level)
  selectedSchoolLevel.value = level
  selectedAdmissionBatch.value = ''
  selectedAdmissionType.value = ''
  getPcList()
  getDisciplineCategoriesList()
}

// 录取批次
const admissionBatch: any = ref([])
const getPcList = async () => {
  const res: any = await api.pcListApi({
    ccdm: selectedSchoolLevel.value
  })
  if (res) {
    admissionBatch.value = res.data.Rs || []
  }
}
const selectedAdmissionBatch = ref(localStorage.getItem('selectedAdmissionBatch') || '')
const handleAdmissionBatchClick = (batch: string) => {
  if (selectedSchoolLevel.value === '') {
    ElMessage.error('请先选择院校层次')
    return
  }
  localStorage.setItem('selectedAdmissionBatch', batch)
  selectedAdmissionBatch.value = batch
  selectedAdmissionType.value = ''
  getTddwList()
}

// 录取类型
const admissionTypes: any = ref([])
const getTddwList = async () => {
  const res: any = await api.tddwListApi({
    ccdm: selectedSchoolLevel.value,
    pcdm: selectedAdmissionBatch.value
  })
  if (res) {
    admissionTypes.value = res.data.Rs || []
  }
}
const selectedAdmissionType = ref(localStorage.getItem('selectedAdmissionType') || '')
const handleAdmissionTypeChange = (value: string) => {
  if (selectedSchoolLevel.value === '' || selectedAdmissionBatch.value === '') {
    ElMessage.error('请先选择院校层次和录取批次')
    return
  }
  localStorage.setItem('selectedAdmissionType', value)
  selectedAdmissionType.value = value
}

// 院校名称
const schoolName = ref('')
const schoolNameOptions: any = ref([])
const getSchoolNameOptions = async (value: any) => {
  if (value.length >= 3) {
    const res: any = await api.yxqueryBymcApi({
      yxmc: value || ''
    })
    if (res) {
      schoolNameOptions.value = res.data.Rs || []
    }
  } else {
    schoolNameOptions.value = []
  }
}
const selectedSchool = ref('')
const handleSchoolNameChange = (value: string) => {
  selectedSchool.value = value
}

// 院校性质
const schoolNatures: any = ref([])
const getSchoolNatures = async () => {
  const res: any = await api.genListQueryApi({
    genType: 'yxxz'
  })
  if (res) {
    schoolNatures.value = res.data.Rs || []
  }
}
const selectedSchoolNature = ref(localStorage.getItem('selectedSchoolNature') || '')
const handleSchoolNatureClick = (nature: string) => {
  if (nature === '0') {
    selectedAdmissionBatch.value = '0'
    selectedAdmissionType.value = ''
  }
  localStorage.setItem('selectedSchoolNature', nature)
  selectedSchoolNature.value = nature
}

// 院校特色
const selectedMajorFeatureList = ref<any>([])
const getMajorFeatureList = async () => {
  const res: any = await api.genListQueryApi({
    genType: 'yxts'
  })
  if (res) {
    selectedMajorFeatureList.value = res.data.Rs || []
  }
}
const selectedMajorFeature: any = ref(localStorage.getItem('selectedMajorFeature')?.split(',') || [])
const handleMajorFeatureClick = (feature: string) => {
  // 切换院校特色选中状态
  const index = selectedMajorFeature.value.indexOf(feature)
  if (index > -1) {
    selectedMajorFeature.value.splice(index, 1)
  } else {
    selectedMajorFeature.value.push(feature)
  }
  localStorage.setItem('selectedMajorFeature', selectedMajorFeature.value.join(','))
}

// 院校省份
const provinceList = ref<any>([])
const getProvinceList = async () => {
  const res: any = await api.genListQueryApi({
    genType: 'prov'
  })
  if (res) {
    provinceList.value = res.data.Rs || []
  }
}
const selectedProvince: any = ref(localStorage.getItem('selectedProvince')?.split(',') || [])
const handleProvinceClick = (province: string) => {
  if (province === '') {
    selectedProvince.value = ['']
    return
  } else {
    const index = selectedProvince.value.indexOf('')
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
  localStorage.setItem('selectedProvince', selectedProvince.value.join(','))
}

// 专业名称
const yixuanzhuanye: any = ref([]) // 已选专业
const majorName = ref('')
const majorNameOptions: any = ref([])
const getMajorNameOptions = async (value: any) => {
  if (value.length >= 2) {
    const res: any = await api.zyqueryBymcApi({
      zymc: value || ''
    })
    if (res) {
      majorNameOptions.value = res.data.Rs || []
    }
  } else {
    majorNameOptions.value = []
  }
}
const selectedMajor = ref('')
const handleMajorNameChange = async (value: string) => {
  const obj = majorNameOptions.value.filter((item: any) => item.id === value)[0]
  yixuanzhuanye.value.push(obj)
  selectedMajor.value = value
  majorName.value = ''
}

// 学科门类
const disciplineCategoriesList: any = ref([])
const getDisciplineCategoriesList = async () => {
  const res: any = await api.xkmllistApi({
    ccdm: selectedSchoolLevel.value
  })
  if (res) {
    disciplineCategoriesList.value = res.data.Rs || []
  }
}
const disciplineCategories = ref('')
const disciplineCategoriesChange = (value: string) => {
  disciplineCategories.value = value
  firstDiscipline.value = ''
  firstDisciplineList.value = []
  subDiscipline.value = ''
  subDisciplineList.value = []
  getFirstDisciplineList()
}

// 一级学科
const firstDisciplineList: any = ref([])
const getFirstDisciplineList = async () => {
  const res: any = await api.yjxklistApi({
    xkml: disciplineCategories.value
  })
  if (res) {
    firstDisciplineList.value = res.data.Rs || []
    firstDisciplineList.value.forEach((item: any) => {
      if (firstDisciplineChecked.value.includes(item.zydm)) {
        item.checked = true
      } else {
        item.checked = false
      }
    })
  }
}
const firstDiscipline = ref('')
const firstDisciplineChange = (value: string) => {
  firstDiscipline.value = value
  subDiscipline.value = ''
  subDisciplineList.value = []
  getSubDisciplineList()
  nextTick(() => {
    subSelectRef.value.toggleMenu()
  })
}
const firstDisciplineChecked: any = ref([])
const firstDisciplineCheckClick = (item: any) => {
  const index = yixuanzhuanye.value.indexOf(item)
  if (index > -1) {
    yixuanzhuanye.value.splice(index, 1)
  } else {
    yixuanzhuanye.value.push(item)
  }
  const index2 = firstDisciplineChecked.value.indexOf(item.zydm)
  if (index2 > -1) {
    firstDisciplineChecked.value.splice(index2, 1)
  } else {
    firstDisciplineChecked.value.push(item.zydm)
  }
}

// 二级学科
const subDisciplineList: any = ref([])
const getSubDisciplineList = async () => {
  const res: any = await api.ejxklistApi({
    yjxk: firstDiscipline.value
  })
  if (res) {
    subDisciplineList.value = res.data.Rs || []
    subDisciplineList.value.forEach((item: any) => {
      if (subDisciplineChecked.value.includes(item.zydm)) {
        item.checked = true
      } else {
        item.checked = false
      }
    })
  }
}
const subSelectRef = ref()
const subDiscipline = ref('')
const subDisciplineChange = (value: string) => {
  subDiscipline.value = value
  console.log(`选择了二级学科: ${value}`)
  nextTick(() => {
    subSelectRef.value.blur()
  })
}
const subDisciplineChecked: any = ref([])
const subDisciplineCheckClick = (item: any) => {
  const index = yixuanzhuanye.value.indexOf(item)
  if (index > -1) {
    yixuanzhuanye.value.splice(index, 1)
  } else {
    yixuanzhuanye.value.push(item)
  }
  const index2 = subDisciplineChecked.value.indexOf(item.zydm)
  if (index2 > -1) {
    subDisciplineChecked.value.splice(index2, 1)
  } else {
    subDisciplineChecked.value.push(item.zydm)
  }
}

// 已选专业
const yixuanzhuanyeClick = async (index: any) => {
  const hasFirst: any = ref(null)
  await firstDisciplineChecked.value.forEach((item: any, index2: number) => {
    if (item === yixuanzhuanye.value[index].zydm) {
      hasFirst.value = index
    }
  })
  if (hasFirst.value !== null) {
    firstDisciplineChecked.value.splice(hasFirst.value, 1)
    getFirstDisciplineList()
  }
  const hasSub: any = ref(null)
  await subDisciplineChecked.value.forEach((item: any, index2: number) => {
    if (item === yixuanzhuanye.value[index].zydm) {
      hasSub.value = index
    }
  })
  if (hasSub.value !== null && firstDiscipline.value) {
    subDisciplineChecked.value.splice(hasSub.value, 1)
    getSubDisciplineList()
  }
  yixuanzhuanye.value.splice(index, 1)
}

// 录取范围 默认选择'稳一稳'
const selectedRiskLevel: any = ref(localStorage.getItem('selectedRiskLevel')?.split(',') || ['4', '3', '2'])
const handleRiskLevelClick = (level: string) => {
  if (selectedRiskLevel.value.includes(level)) {
    selectedRiskLevel.value = selectedRiskLevel.value.filter((item: string) => item !== level)
  } else {
    selectedRiskLevel.value.push(level)
  }
  localStorage.setItem('selectedRiskLevel', selectedRiskLevel.value.join(','))
}
// “冲” 风险阈值响应式变量
const riskThreshold = ref(Number(localStorage.getItem('riskThreshold') || '50'))
watch(riskThreshold, (newValue) => {
  localStorage.setItem('riskThreshold', newValue.toString())
})
// “保” 安全阈值响应式变量
const safeThreshold = ref(Number(localStorage.getItem('safeThreshold') || '50'))
watch(safeThreshold, (newValue) => {
  localStorage.setItem('safeThreshold', newValue.toString())
})

// 声明表格数据响应式变量
const currentPage = ref(1)
const pageSize = ref(10)
const total = ref(0)
const tableData: any = ref([])

// 专业模式 - 志愿查询
const lqInfoZyQuery = async () => {
  const zydmArray: any = ref([])
  await yixuanzhuanye.value.forEach((item: any) => {
    zydmArray.value.push(item.zydm || item.id)
  })
  const data = {
    ccdm: selectedSchoolLevel.value,
    pcdm: selectedAdmissionBatch.value,
    tddw: selectedAdmissionType.value,
    yxxz: selectedSchoolNature.value,
    yxid: selectedSchool.value || '',
    genList: JSON.stringify({ Rs: [{ id: selectedSchoolNature.value, genType: 'yxxz' }, { id: selectedMajorFeature.value.join(','), genType: 'yxts' }, { id: selectedProvince.value.join(','), genType: 'prov' }] }),
    zydm: zydmArray.value.join(','),
    lqdc: selectedRiskLevel.value.join(','),
    progressChong: riskThreshold.value,
    progressBao: safeThreshold.value,
    startrow: currentPage.value,
    pagesize: pageSize.value,
  }
  console.log('专业模式 - 志愿查询 -------->', JSON.stringify(data))
  const res: any = await api.lqInfoZyQueryApi(data)
  if (res) {
    tableData.value = res.data.Rs || []
    total.value = res.recordsTotal || 0
  }
}

// 专业模式 - 填报
const zyHandleApply = async (row: any) => {
  const res: any = await api.myChioesAddApi({
    zyId: row.zyid,
    lqdc: row.lqdc,
    lqbl: (row.bl / 100).toFixed(3),
  })
  if (res) {
    ElMessage.success('填报成功')
    lqInfoZyQuery()
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
  const datas: any = ref([])
  await selectedRows.value.forEach((item: any) => {
    datas.value.push({
      zyid: item.zyid,
      lqdc: item.lqdc,
      lqbl: (item.bl / 100).toFixed(3),
    })
  })
  const data = {
    jsonStr: JSON.stringify({ Rs: datas.value }),
  }
  const res: any = await api.myChioesBatchAddApi(data)
  if (res) {
    ElMessage.success('批量填报成功')
    lqInfoZyQuery()
  }
}

// 专业组模式志愿查询
const lqInfoZyGroupQuery = async () => {
  const zydmArray: any = ref([])
  await yixuanzhuanye.value.forEach((item: any) => {
    zydmArray.value.push(item.zydm || item.id)
  })
  const data = {
    ccdm: selectedSchoolLevel.value,
    pcdm: selectedAdmissionBatch.value,
    tddw: selectedAdmissionType.value,
    yxxz: selectedSchoolNature.value,
    yxid: selectedSchool.value || '',
    genList: JSON.stringify({ Rs: [{ id: selectedSchoolNature.value, genType: 'yxxz' }, { id: selectedMajorFeature.value.join(','), genType: 'yxts' }, { id: selectedProvince.value.join(','), genType: 'prov' }] }),
    zydm: zydmArray.value.join(','),
    lqdc: selectedRiskLevel.value.join(','),
    progressChong: riskThreshold.value,
    progressBao: safeThreshold.value,
    startrow: currentPage.value,
    pagesize: pageSize.value,
  }
  console.log('专业组模式 - 志愿查询 -------->', JSON.stringify(data))
  const res: any = await api.lqInfoZyGroupQueryApi(data)
  if (res) {
    tableData.value = res.data.Rs || []
    total.value = res.recordsTotal || 0
  }
}

// 专业组模式 - 填报
const zyGroupHandleApply = async (zyid: any, row: any) => {
  const res: any = await api.myChioesAddApi({
    zyId: zyid,
    lqdc: row.lqdc,
    lqbl: (row.bl / 100).toFixed(3),
  })
  if (res) {
    ElMessage.success('填报成功')
    lqInfoZyGroupQuery()
  }
}

// 处理分页变化
const handlePageChange = (page: number) => {
  currentPage.value = page
  if (zyType === '1') {
    lqInfoZyQuery()
  }
  if (zyType === '2') {
    lqInfoZyGroupQuery()
  }
}
const handleSizeChange = (size: number) => {
  pageSize.value = size
  if (zyType === '1') {
    lqInfoZyQuery()
  }
  if (zyType === '2') {
    lqInfoZyGroupQuery()
  }
}

// 我的志愿
const collectionDrawer = ref(false)
const goMyAspiration = () => {
  if (!selectedSchoolLevel.value) {
    ElMessage.warning('请选择院校层次')
    return
  }
  // if (!selectedAdmissionBatch.value) {
  //   ElMessage.warning('请选择录取批次')
  //   return
  // }
  collectionDrawer.value = true
  getMyChioesGroupQuery()
}

// 我的志愿 - 志愿分组查询
const myChioesGroupQueryInfo: any = ref({})
const getMyChioesGroupQuery = async () => {
  const res: any = await api.myChioesGroupQueryApi({
    ccdm: selectedSchoolLevel.value,
    pcdm: selectedAdmissionBatch.value,
  })
  if (res) {
    myChioesGroupQueryInfo.value = res.data?.Rs[0] || {}
    if (myChioesGroupQueryInfo.value?.chGroupId && myChioesGroupQueryInfo.value?.chGroupId != '0') {
      if (zyType === '1') {
        zyHandleCollect()
      }
      if (zyType === '2') {
        zyGroupHandleCollect()
      }
    }
  }
}

// 专业模式 - 收藏
const zyHandleCollectList: any = ref([])
const zyHandleCollect = async () => {
  const res: any = await api.zyChoicesQueryApi({
    chGroupId: myChioesGroupQueryInfo.value.chGroupId,
  })
  if (res) {
    zyHandleCollectList.value = res.data.Rs || []
  }
}

// 专业组模式 - 收藏
const zyGroupHandleCollect = async () => {
  const res: any = await api.zyGroupChoicesQueryApi({
    chGroupId: myChioesGroupQueryInfo.value.chGroupId,
  })
  if (res) {
    zyHandleCollectList.value = res.data.Rs || []
  }
}

// 专业模式 - 删除收藏
const zyHandleDelete = async (row: any) => {
  const res: any = await api.delChoiceApi({
    chId: row.chId,
  })
  if (res) {
    ElMessage.success('删除成功')
    // 刷新收藏分组查询
    getMyChioesGroupQuery()
  }
}

// 专业组模式 - 外层删除收藏
const zyGroupHandleDelete1 = async (row: any) => {
  const res: any = await api.delChoiceGroupApi({
    chZyGroupId: row.chZyGroupId,
  })
  if (res) {
    ElMessage.success('删除成功')
    // 刷新收藏分组查询
    getMyChioesGroupQuery()
  }
}
// 专业组模式 - 里层删除收藏
const zyGroupHandleDelete2 = async (row: any) => {
  const res: any = await api.delChoiceApi({
    chId: row.chId,
  })
  if (res) {
    ElMessage.success('删除成功')
    // 刷新收藏分组查询
    getMyChioesGroupQuery()
  }
}
// 折叠展开专业组志愿
const expandedRows: any = ref([])
function toggleExpand(row: any) {
  const index = expandedRows.value.indexOf(row.zyGroupId)
  if (index > -1) {
    expandedRows.value.splice(index, 1)
  } else {
    expandedRows.value.push(row.zyGroupId)
  }
}
const handleExpandChange = (row: any, expandedRows: any) => {
  console.log('展开行变化:', row, expandedRows)
}
</script>

<template>
  <div class="volunteer-apply-page">
    <component :is="selectProvince" />
    <main class="max-w-7xl mx-auto px-4 py-8">
      <!-- 查询条件 -->
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
              <div :class="selectedAdmissionBatch === '' ? 'primaryTag' : 'infoTag'"
                @click="handleAdmissionBatchClick('')">
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
              <div :class="selectedAdmissionType === '' ? 'primaryTag' : 'infoTag'"
                @click="handleAdmissionTypeChange('')">
                不限
              </div>
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
              :remote-method="getSchoolNameOptions" @change="handleSchoolNameChange" class="select-tall38px" clearable
              style="margin-bottom: 10px; width: calc(50% - 90px);">
              <el-option v-for="(item, index) in schoolNameOptions" :key="index" :label="item.text" :value="item.id" />
            </el-select>
          </div>
          <div class="tagBox">
            <div class="tagTitle">院校性质：</div>
            <div class="tagContent">
              <div :class="selectedSchoolNature === '' ? 'primaryTag' : 'infoTag'" @click="handleSchoolNatureClick('')">
                不限
              </div>
              <div v-for="(item, index) in schoolNatures" :key="index"
                :class="selectedSchoolNature === item.disp ? 'primaryTag' : 'infoTag'"
                @click="handleSchoolNatureClick(item.disp)">
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
              <div :class="selectedProvince.includes('') ? 'primaryTag' : 'infoTag'" @click="handleProvinceClick('')">
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
                :remote-method="getMajorNameOptions" @change="handleMajorNameChange" class="select-tall38px">
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
              <el-select v-model="firstDiscipline" placeholder="请选择一级学科" class="select-tall38px">
                <el-option v-for="(item, index) in firstDisciplineList" :key="index" :value="item.zydm"
                  :label="item.zymc">
                  <template #default>
                    <div style="display: flex; align-items: center; width: 100%;"
                      @click.stop="firstDisciplineChange(item.zydm)">
                      <el-checkbox v-model="item.checked" @click.stop="firstDisciplineCheckClick(item)"></el-checkbox>
                      <div style="margin-left: 5px;">{{ item.zymc }}</div>
                    </div>
                  </template>
                </el-option>
              </el-select>
            </el-col>
            <el-col :span="6">
              <div class="tagTitle">二级学科：</div>
              <el-select ref="subSelectRef" v-model="subDiscipline" placeholder="请选择二级学科" class="select-tall38px">
                <el-option v-for="(item, index) in subDisciplineList" :key="index" :value="item.zydm"
                  :label="item.zymc">
                  <template #default>
                    <div style="display: flex; align-items: center; width: 100%;"
                      @click.stop="subDisciplineChange(item.zydm)">
                      <el-checkbox v-model="item.checked" @click.stop="subDisciplineCheckClick(item)"></el-checkbox>
                      <div style="margin-left: 5px;">{{ item.zymc }}</div>
                    </div>
                  </template>
                </el-option>
              </el-select>
            </el-col>
          </el-row>
          <div v-if="yixuanzhuanye.length > 0" style="margin-top: 20px;">
            <div class="tagBox">
              <div class="tagTitle" style="margin-bottom: 0;">所选专业：</div>
              <div class="tagContent">
                <el-tag v-for="(item, index) in yixuanzhuanye" :key="index" type="primary" closable
                  style="margin: 5px 10px 5px 0; cursor: pointer;" @close="yixuanzhuanyeClick(index)">
                  {{ item.zymc || item.text }}
                </el-tag>
              </div>
            </div>
          </div>
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
                <input class="w-full" max="100" min="0" type="range" v-model="riskThreshold">
                <p class="text-xs text-slate-400 text-center">风险越高，录取可能性越低，建议作为前置志愿</p>
              </div>
              <div class="space-y-4">
                <div class="flex justify-between items-center">
                  <label class="text-sm font-semibold text-slate-700">“保” 安全阈值</label>
                  <span class="text-green-600 font-bold" id="val-bao">{{ safeThreshold }}%</span>
                </div>
                <input class="w-full" max="100" min="0" type="range" v-model="safeThreshold">
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
            <button v-if="zyType == '1'"
              class="w-full md:w-64 py-4 px-8 bg-blue-600 text-white rounded-2xl font-bold text-lg shadow-lg shadow-blue-200 hover:bg-blue-700 active:scale-95 transition-all flex items-center justify-center space-x-3"
              @click="lqInfoZyQuery">
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
            <button v-if="zyType == '2'"
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
              <span>立即开始智能检索</span>
            </button>
          </div>
        </div>
      </section>

      <!-- 结果信息 -->
      <section v-if="tableData.length > 0">
        <div class="flex justify-between items-center mb-6">
          <h2 class="text-2xl font-bold">结果信息</h2>
          <div class="flex items-center gap-3">
            <button v-if="zyType == '1'"
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
        <!-- 专业模式查询结果表格 -->
        <el-table v-if="zyType === '1'" v-loading="false" :data="tableData" @selection-change="handleSelectionChange"
          stripe border size="small" class="custom-table" style="width: 100%">
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
                {{ scope.row.sf211 === 1 ? ' 211高校 |' : '' }}
                {{ scope.row.sf985 === 1 ? ' 985高校' : '' }}
                <span v-if="scope.row.byly">保研率：{{ scope.row.byly }}</span>
                <span v-if="scope.row.byly && scope.row.yxts"> | </span>
                <span v-if="scope.row.yxts">{{ scope.row.yxts }}</span>
              </div>
            </template>
          </el-table-column>
          <el-table-column label="招生专业" min-width="200" align="left">
            <template #default="scope">
              <div class="tablezy" style="padding-top: 10px;">
                <div class="text-xs text-gray-500">专业名称：<span style="font-size: 16px; font-weight: bold;">{{
                  scope.row.zymc }}</span>
                </div>
                <div class="text-xs text-gray-500">专业代号：<span style="font-size: 16px; font-weight: bold;">{{
                  scope.row.zydh }}</span>
                </div>
                <div class="text-xs text-gray-500">计划人数：<span>{{ scope.row.jhrs }}</span>
                </div>
                <el-tooltip v-if="scope.row.JHBZ" popper-class="custom-tooltip" effect="dark" :content="scope.row.JHBZ"
                  placement="top">
                  <div class="text-xs text-gray-500">备注：<span class="beizhu">{{ scope.row.JHBZ }}</span></div>
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
              <el-button v-if="scope.row.chId == 0" text type="primary" size="small" @click="zyHandleApply(scope.row)">
                填报
              </el-button>
              <el-button v-else text type="danger" size="small">
                已填报
              </el-button>
            </template>
          </el-table-column>
        </el-table>
        <!-- 专业组模式查询结果表格 -->
        <el-table v-if="zyType === '2'" v-loading="false" :data="tableData" stripe
          :row-key="(row: any) => row.zyGroupId" :expand-row-keys="expandedRows" @expand-change="handleExpandChange"
          border size="small" id="custom-expand-table" style="width: 100%">
          <el-table-column type="expand" width="1" align="center">
            <template #default="{ row }">
              <el-table :data="row.zyRs" border :show-header="false">
                <el-table-column type="index" width="40" align="center">
                </el-table-column>
                <el-table-column label="专业" prop="zymc" min-width="200">
                  <template #default="scope">
                    <div class="font-medium tableyxmc">
                      <span>{{ scope.row.zymc }}</span><span v-if="scope.row.zydh">（{{ scope.row.zydh }}）</span>
                    </div>
                    <div v-if="scope.row.zyts" class="text-xs text-gray-500">{{ scope.row.zyts }}</div>
                    <el-tooltip v-if="scope.row.jhbz" popper-class="custom-tooltip" effect="dark"
                      :content="scope.row.jhbz" placement="top">
                      <div class="text-xs text-gray-500">备注：<span class="beizhu">{{ scope.row.jhbz }}</span></div>
                    </el-tooltip>
                  </template>
                </el-table-column>
                <el-table-column label="计划人数" min-width="100">
                  <template #default="scope">
                    <div style="display: flex; flex-direction: column; justify-content: center; align-items: center;">
                      <div class="text-xs text-gray-500"><span style="font-size: 20px; font-weight: 600; color: #000;">
                          {{ scope.row.jhrs }}</span>人
                      </div>
                      <div class="text-xs text-gray-500 mt-1">{{ scope.row.xkkm }}</div>
                      <div class="text-xs text-gray-500 mt-1">{{ scope.row.xzdm }}/{{ scope.row.sfbz }}</div>
                    </div>
                  </template>
                </el-table-column>
                <el-table-column label="match1Year" min-width="100">
                  <template #default="scope">
                    <div v-if="scope.row.minwc1 != 0 && scope.row.mincj1 != 0" class="tablezy">
                      <div class="text-xs text-gray-500"><span>{{ scope.row.match1Year }}</span>年</div>
                      <div class="text-xs text-gray-500">
                        成绩类型：<span>{{ scope.row.match1Type === 1 ? '精确' : scope.row.match1Type === 2 ? '近似' : '其他'
                          }}</span>
                      </div>
                      <div class="text-xs text-gray-500">位次：<span>{{ scope.row.minwc1 }}</span></div>
                      <div class="text-xs text-gray-500">分数：<span>{{ scope.row.mincj1 }}</span></div>
                      <div class="text-xs text-gray-500" style="margin-bottom: 0;">录取人数：<span>{{ scope.row.lqrs1
                      }}</span>
                      </div>
                    </div>
                  </template>
                </el-table-column>
                <el-table-column label="match2Year" min-width="100">
                  <template #default="scope">
                    <div v-if="scope.row.minwc2 != 0 && scope.row.mincj2 != 0" class="tablezy">
                      <div class="text-xs text-gray-500"><span>{{ scope.row.match2Year }}</span>年</div>
                      <div class="text-xs text-gray-500">
                        成绩类型：<span>{{ scope.row.match2Type === 1 ? '精确' : scope.row.match2Type === 2 ? '近似' : '其他'
                          }}</span>
                      </div>
                      <div class="text-xs text-gray-500">位次：<span>{{ scope.row.minwc2 }}</span></div>
                      <div class="text-xs text-gray-500">分数：<span>{{ scope.row.mincj2 }}</span></div>
                      <div class="text-xs text-gray-500" style="margin-bottom: 0;">录取人数：<span>{{ scope.row.lqrs2
                          }}</span>
                      </div>
                    </div>
                  </template>
                </el-table-column>
                <el-table-column label="match3Year" min-width="100">
                  <template #default="scope">
                    <div v-if="scope.row.minwc3 != 0 && scope.row.mincj3 != 0" class="tablezy">
                      <div class="text-xs text-gray-500"><span>{{ scope.row.match3Year }}</span>年</div>
                      <div class="text-xs text-gray-500">
                        成绩类型：<span>{{ scope.row.match3Type === 1 ? '精确' : scope.row.match3Type === 2 ? '近似' : '其他'
                          }}</span>
                      </div>
                      <div class="text-xs text-gray-500">位次：<span>{{ scope.row.minwc3 }}</span></div>
                      <div class="text-xs text-gray-500">分数：<span>{{ scope.row.mincj3 }}</span></div>
                      <div class="text-xs text-gray-500" style="margin-bottom: 0;">录取人数：<span>{{ scope.row.lqrs3
                      }}</span>
                      </div>
                    </div>
                  </template>
                </el-table-column>
                <el-table-column width="90">
                </el-table-column>
                <el-table-column label="操作" width="120" align="center">
                  <template #default="subScope">
                    <el-button v-if="subScope.row.chId == 0" text type="primary" size="small"
                      @click="zyGroupHandleApply(subScope.row.zyid, row)">
                      填报
                    </el-button>
                    <el-button v-else text type="danger" size="small">
                      已填报
                    </el-button>
                  </template>
                </el-table-column>
              </el-table>
            </template>
          </el-table-column>
          <el-table-column type="index" width="41" align="center" label="序号" />
          <el-table-column prop="schoolName" label="招生院校" min-width="200" align="left">
            <template #default="scope">
              <div class="font-medium tableyxmc">
                <span>{{ scope.row.yxmc }}（{{ scope.row.zyGroupDm }}）专业组</span>
                <span v-if="scope.row.lqdcstr.includes('稳')" class="lqdcstr bg2">{{ scope.row.lqdcstr }}</span>
                <span v-else-if="scope.row.lqdcstr.includes('冲')" class="lqdcstr bg1">{{ scope.row.lqdcstr }}</span>
                <span v-else class="lqdcstr bg3">{{ scope.row.lqdcstr }}</span>
              </div>
              <div class="text-xs text-gray-500">
                院校代码：<span style="font-weight: bold; color: #000;">{{ scope.row.yxdm }}</span> |
                {{ scope.row.provice }}/{{ scope.row.city }}
                {{ scope.row.sf211 === 1 ? ' 211高校 | ' : '' }}
                {{ scope.row.sf985 === 1 ? ' 985高校 | ' : '' }}
                <span v-if="scope.row.byly">保研率：{{ scope.row.byly }}</span>
                <span v-if="scope.row.byly && scope.row.yxts"> | </span>
                <span v-if="scope.row.yxts">{{ scope.row.yxts }}</span>
              </div>
            </template>
          </el-table-column>
          <el-table-column label="招生计划" min-width="100" align="left">
            <template #default="scope">
              <div style="display: flex; flex-direction: column; justify-content: center; align-items: center;">
                <div class="text-xs text-gray-500"><span style="font-size: 20px; font-weight: 600; color: #000;">
                    {{ scope.row.groupJhrs }}</span>人
                </div>
                <div class="text-xs text-gray-500" style="margin-top: 5px;">{{ scope.row.xkkm }}</div>
                <div class="text-xs text-gray-500" style="margin-top: 5px;">{{ scope.row.tddwmc }}</div>
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
          <el-table-column width="120" label="填报">
            <template #default="scope">
              <div style="display: flex; flex-direction: column; justify-content: center; align-items: center;"
                @click="toggleExpand(scope.row)">
                <el-tag type="primary">
                  <div style="cursor: pointer; display: flex; justify-content: center;align-items: center;">
                    <p style="margin-right: 5px;">专业 {{ scope.row.zyRs.length }}</p>
                    <el-icon>
                      <ArrowUp v-if="expandedRows.includes(scope.row.zyGroupId)" />
                      <ArrowDown v-else />
                    </el-icon>
                  </div>
                </el-tag>
                <div style="line-height: 30px;">已填({{ scope.row.chNum }})</div>
              </div>
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
              :prev-text="'上一页'" :next-text="'下一页'" @size-change="handleSizeChange"
              @current-change="handlePageChange"></el-pagination>
          </div>
        </div>
      </section>

      <!-- 我的志愿 -->
      <el-drawer v-model="collectionDrawer" direction="rtl" :show-close="false" size="360" style="height: 100vh;">
        <template #header>
          <div
            class="bg-gradient-to-r from-blue-600 to-purple-600 text-white px-6 py-4 flex justify-between items-center sticky top-0 z-10">
            <h4 class="text-l font-bold">
              {{ myChioesGroupQueryInfo.chGroupName || '我的志愿' }}（{{ myChioesGroupQueryInfo.addNum }}/{{
                myChioesGroupQueryInfo.maxNum
              }}）
            </h4>
            <el-icon size="24" @click="collectionDrawer = false" style="cursor: pointer;">
              <Close />
            </el-icon>
          </div>
        </template>
        <div v-if="myChioesGroupQueryInfo?.chGroupId == 0" class="text-center py-12">
          <el-icon class="text-5xl text-gray-300 mb-4" size="50" color="rgb(107 114 128)">
            <MessageBox />
          </el-icon>
          <p class="text-gray-500 text-sm">还没有添加志愿，请点击表格中的"填报"按钮添加</p>
        </div>
        <div v-if="zyHandleCollectList?.length > 0">
          <div v-if="zyType === '1'" v-for="(item, index) in zyHandleCollectList" :key="index" class="chGroupBox">
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
          <div v-if="zyType === '2'" v-for="(item, index) in zyHandleCollectList" :key="index" class="chGroupBox">
            <div class="chGroupName">
              <span>{{ item.yxmc }}</span>
              <span class="lqdcstr bg3">{{ item.yxdm }}</span>
            </div>
            <el-icon class="deleteIcon" color="#F56C6C" @click="zyGroupHandleDelete1(item)">
              <DeleteFilled />
            </el-icon>
            <div v-for="(item2, index) in item.zyRs" :key="index" style="position: relative; margin-top: 10px;">
              <div class="text-xs text-gray-500 chGroupSub">
                <p style="width: 100%;"><span>{{ item2.zymc }}</span></p>
                <p>专业代号：<span>{{ item2.zydh }}</span></p>
                <p>计划数：<span>{{ item2.jhrs }}</span></p>
              </div>
              <el-icon class="deleteIcon2" color="#F56C6C" @click="zyGroupHandleDelete2(item2)">
                <DeleteFilled />
              </el-icon>
            </div>
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
        width: 200px;
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
    padding: 10px;
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

    .deleteIcon2 {
      cursor: pointer;
      position: absolute;
      top: 0;
      right: 0;
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

#custom-expand-table .el-table__expand-column .cell {
  display: none;
}
</style>

<script setup lang="ts">
import axios from 'axios'
import Sortable, { type SortableEvent } from 'sortablejs'
import { nextTick, onMounted, ref } from 'vue'
import { dayjs, ElMessage } from 'element-plus'
import * as api from '@/api/interfaceapi'
import { baseURL } from '@/api/baseConfig'

// 防止重复提交
const timeout: any = ref(null)
function useDebounce(fn: any, wait?: number) {
  if (timeout.value !== null) {
    clearTimeout(timeout.value)
  }
  timeout.value = setTimeout(fn, wait || 1000)
}

// 初始化时根据路由参数设置选中的导航项
onMounted(() => {
  getMyuserInfoQuery()
})

// 选中的导航项 - 可选值：'basic-info', 'seeting-password', 'change-password', 'my-collections', 'my-scale'
const selectedNavItem = ref('basic-info')
const handleNavItemClick = (navItem: string) => {
  selectedNavItem.value = navItem
  if (navItem === 'my-collections') {
    getMyChioesGroupQuery()
  }
  if (navItem === 'my-scale') {
    getMyScalesQuery()
  }
  console.log(`选择了导航项: ${navItem}`)
}

// 个人信息
const personalInfo: any = ref<any>({})
const personalForm: any = ref({})
const getMyuserInfoQuery = async () => {
  const res: any = await api.myuserInfoQueryApi()
  if (res) {
    // res.data.phone = '13256605200'
    personalInfo.value = res.data || {}
    personalForm.value = JSON.parse(JSON.stringify(personalInfo.value))
    selectedSubjects.value = personalForm.value.xuanke?.split(',') || []
    if (personalForm.value.province) {
      getwctypeList()
      getYklmQuery()
    }
    if (personalInfo.value.ifDispUserInfo == '0') {
      handleNavItemClick('my-collections')
    }
    localStorage.setItem('userInfo', JSON.stringify(personalForm.value))
  }
}

// 所在省份
const handleProvinceChange = () => {
  getwctypeList()
  getYklmQuery()
}

// 选科信息
const selectedSubjects = ref<string[]>([])
const handleSubjectClick = (subject: string) => {
  if (personalForm.value.remainXuankeEditNum < 1) {
    return
  }
  const index = selectedSubjects.value.indexOf(subject)
  if (index > -1) {
    selectedSubjects.value.splice(index, 1)
  } else {
    // 3+1+2模式
    if (personalForm.value.xkMod == '2') {
      // 物理和历史二选一
      if (selectedSubjects.value.includes('A') && subject === 'D') {
        selectedSubjects.value.splice(selectedSubjects.value.indexOf('A'), 1)
      }
      if (selectedSubjects.value.includes('D') && subject === 'A') {
        selectedSubjects.value.splice(selectedSubjects.value.indexOf('D'), 1)
      }
      // 化学、生物、政治、地理四科中最多选择2科
      const bcefSubjects = ['B', 'C', 'E', 'F']
      const selectedBcefSubjects = selectedSubjects.value.filter(subject => bcefSubjects.includes(subject))
      if (bcefSubjects.includes(subject) && selectedBcefSubjects.length >= 2) {
        ElMessage.warning('化学、生物、政治、地理四科中最多选择2科')
        return
      }
    }
    if (selectedSubjects.value.length >= 3) {
      ElMessage.warning('最多选择3科')
      return
    }
    selectedSubjects.value.push(subject)
    // 3+1+2模式 物理和历史 change
    if (personalForm.value.xkMod == '2' && (selectedSubjects.value.includes('A') || selectedSubjects.value.includes('D')) && personalForm.value.wctype && personalForm.value.cj) {
      cjInput()
    }
  }
}

// 考试类别
const wctypeList: any = ref([])
const getwctypeList = async () => {
  const res: any = await api.WctypeQueryApi({
    province: personalForm.value.province || ''
  })
  if (res) {
    wctypeList.value = res.data || []
  }
}
const wctypeChange = () => {
  personalForm.value.yklm = ''
  if (personalForm.value.xkMod != '2' && personalForm.value.wctype && personalForm.value.wctype != '2' && personalForm.value.cj) {
    cjInput()
  }
}

// 详细类别
const subjectList = ref<any>([])
const getYklmQuery = async () => {
  const res: any = await api.yklmQueryApi({
    wctype: '2',
    province: personalForm.value.province || ''
  })
  if (res) {
    subjectList.value = res.data.Rs || []
  }
}
const handleYklmClick = () => {
  if (personalForm.value.xkMod != '2' && personalForm.value.wctype && personalForm.value.yklm && personalForm.value.cj) {
    cjInput()
  }
}

// 输入分数查询位次查询
const cjInput = async () => {
  const res: any = await api.wcQueryBycjApi({
    cj: personalForm.value.cj,
    wctype: personalForm.value.wctype,
    yklm: personalForm.value.yklm,
    // province: personalForm.value.province,
    kldm: personalForm.value.xkMod == 2 ? selectedSubjects.value.includes('A') ? '1' : '2' : ''
  })
  if (res) {
    personalForm.value.wc = res.data.wc || ''
  }
}

// 个人信息保存
const myUserInfoSaveBtn = async () => {
  if (!personalForm.value.phone) {
    ElMessage.warning('请输入手机号码')
    return
  }
  if (!/^(?:(?:\+|00)86)?1[3-9]\d{9}$/.test(personalForm.value.phone)) {
    ElMessage.warning('请输入正确的手机号码')
    return
  }
  if (!personalForm.value.userName) {
    ElMessage.warning('请输入姓名')
    return
  }
  if (!personalForm.value.sex) {
    ElMessage.warning('请选择性别')
    return
  }
  // if (!personalForm.value.province) {
  //   ElMessage.warning('请选择所在省份')
  //   return
  // }
  if (selectedSubjects.value.length === 0) {
    ElMessage.warning('请选择选科信息')
    return
  } else {
    personalForm.value.xkkm = selectedSubjects.value.join(',')
  }
  if (!personalForm.value.wctype) {
    ElMessage.warning('请选择考试类别')
    return
  }
  if (personalForm.value.wctype == 2) {
    if (!personalForm.value.yklm) {
      ElMessage.warning('请选择详细类别')
      return
    }
  }
  if (!personalForm.value.cj) {
    ElMessage.warning('请输入高考成绩')
    return
  }
  if (!personalForm.value.wc) {
    ElMessage.warning('请输入高考位次')
    return
  }
  if (personalForm.value.xkMod == '2') {
    if (!selectedSubjects.value.includes('A') && !selectedSubjects.value.includes('D')) {
      ElMessage.warning('选科信息中必须包含物理或历史')
      return
    }
  }
  const res: any = await api.myUserInfoSaveApi(personalForm.value)
  if (res) {
    localStorage.setItem('userInfo', JSON.stringify(personalForm.value))
    ElMessage.success('保存成功')
    window.location.reload()
  }
}

// 设置密码
const seetingpwdForm = ref({
  code: '',
  newPass: '',
  confirmPass: '',
})
const handlePasswordSubmit = async () => {
  if (!seetingpwdForm.value.code) {
    ElMessage.warning('请输入验证码')
    return
  }
  if (!seetingpwdForm.value.newPass) {
    ElMessage.warning('请输入新密码')
    return
  }
  if (!seetingpwdForm.value.confirmPass) {
    ElMessage.warning('请确认新密码')
    return
  }
  if (seetingpwdForm.value.newPass !== seetingpwdForm.value.confirmPass) {
    ElMessage.warning('两次输入的密码不一致')
    return
  }
  const res: any = await api.passResetApi({
    newPass: seetingpwdForm.value.newPass,
    vfCode: seetingpwdForm.value.code,
  })
  if (res) {
    ElMessage.success('密码设置成功')
    // 清空密码输入框
    seetingpwdForm.value.code = ''
    seetingpwdForm.value.newPass = ''
    seetingpwdForm.value.confirmPass = ''
  }
}

// 发送验证码
const sendCode = async () => {
  try {
    const res: any = await api.authcodeApi({
      phone: personalForm.value.phone,
      type: 1
    })
    ElMessage.success(`验证码已发送到 ${personalForm.value.phone}`)
    console.log('发送验证码 -------->', res)
    // if (res.data.code === 0) {
    //   ElMessage.success(`验证码已发送到 ${personalForm.value.phone}`)
    // } else {
    //   // ElMessage.error(res.data.message || '发送验证码失败')
    //   console.log('发送验证码失败 -------->', res.data.message || '发送验证码失败')
    // }
  } catch (error) {
    ElMessage.success(`验证码已发送到 ${personalForm.value.phone}`)
    console.log('发送验证码失败 -------->', error)
    // ElMessage.error('发送验证码失败')
  }
}

// 修改密码
const changePasswordForm = ref({
  oldPass: '',
  newPass: '',
  confirmPass: '',
})
const handleChangePasswordSubmit = async () => {
  if (!changePasswordForm.value.oldPass) {
    ElMessage.warning('请输入旧密码')
    return
  }
  if (!changePasswordForm.value.newPass) {
    ElMessage.warning('请输入新密码')
    return
  }
  if (!changePasswordForm.value.confirmPass) {
    ElMessage.warning('请确认新密码')
    return
  }
  if (changePasswordForm.value.newPass !== changePasswordForm.value.confirmPass) {
    ElMessage.warning('两次输入的密码不一致')
    return
  }
  const res: any = await api.passModiApi({
    oldPass: changePasswordForm.value.oldPass,
    newPass: changePasswordForm.value.newPass,
  })
  if (res) {
    ElMessage.success('密码修改成功')
    // 清空密码输入框
    changePasswordForm.value.oldPass = ''
    changePasswordForm.value.newPass = ''
    changePasswordForm.value.confirmPass = ''
  }
}

// 我的志愿单 - 志愿分组查询
const myChGroupSListId: any = ref('')
const myChioesGroupQueryList: any = ref([])
const getMyChioesGroupQuery = async () => {
  const res: any = await api.myChGroupSListApi({
  })
  if (res) {
    myChioesGroupQueryList.value = res.data.Rs || []
    if (myChGroupSListId.value == '' && myChioesGroupQueryList.value.length > 0) {
      myChGroupSListId.value = myChioesGroupQueryList.value[0].chGroupId || ''
    }
    if (personalForm.value.zyType == '1') {
      handleViewGroup1()
    }
    if (personalForm.value.zyType == '2') {
      handleViewGroup2()
    }
  }
}
// 根据zyType 切换查询
const handleViewGroup = async (id?: any) => {
  if (personalForm.value.zyType == '1') {
    handleViewGroup1(id)
  }
  if (personalForm.value.zyType == '2') {
    handleViewGroup2(id)
  }
}
// 专业模式志愿单查询
const tableData: any = ref([])
const tuozhuaiTableData: any = ref([])
const handleViewGroup1 = async (id?: any) => {
  if (id) {
    myChGroupSListId.value = id
  }
  const res: any = await api.zyChoicesQueryApi({
    chGroupId: myChGroupSListId.value,
  })
  if (res) {
    tableData.value = res.data.Rs || []
    tuozhuaiTableData.value = res.data.Rs || []
    await nextTick()
    initRowDrop()
  }
}

// 专业组模式 - 收藏
const handleViewGroup2 = async (id?: any) => {
  if (id) {
    myChGroupSListId.value = id
  }
  const res: any = await api.zyGroupChoicesQueryApi({
    chGroupId: myChGroupSListId.value,
  })
  if (res) {
    tableData.value = res.data.Rs || []
    tuozhuaiTableData.value = res.data.Rs || []
    await nextTick()
    initRowDrop()
  }
}
// 专业模式志 - 删除
const zyHandleDelete = async (row: any) => {
  const res: any = await api.delChoiceApi({
    chId: row.chId,
  })
  if (res) {
    ElMessage.success('删除成功')
    // 刷新志愿单分组查询
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

// 表格行拖拽
const sortableTableRef = ref()
let sortableInstance: Sortable | null = null

const destroyRowDrop = () => {
  sortableInstance?.destroy()
  sortableInstance = null
}

const reorderTableData = (oldIndex: number, newIndex: number) => {
  const newData = [...tableData.value]
  const [moved] = newData.splice(oldIndex, 1)
  newData.splice(newIndex, 0, moved)
  tableData.value = newData
  tuozhuaiTableData.value = newData
}

const initRowDrop = () => {
  destroyRowDrop()

  const tableEl = sortableTableRef.value?.$el as HTMLElement | undefined
  const tbody = tableEl?.querySelector('.el-table__body-wrapper tbody') as HTMLElement | null
  if (!tbody) return

  sortableInstance = Sortable.create(tbody, {
    animation: 150,
    draggable: 'tr.el-table__row',
    filter: '.el-table__expanded-row',
    onStart() {
      expandedRows.value = []
    },
    onEnd(evt: SortableEvent) {
      const { oldIndex, newIndex } = evt
      if (oldIndex == null || newIndex == null || oldIndex === newIndex) return

      destroyRowDrop()
      reorderTableData(oldIndex, newIndex)
      handleSaveSort()
      nextTick(() => initRowDrop())
    },
  })
}

// 专业模式志愿单保存排序
const handleSaveSort = async () => {
  const Rs = await tuozhuaiTableData.value.map((item: any, index: number) => ({
    id: item.chId || item.chZyGroupId,
    xh: index + 1,
  }))
  api.ZyChoiceSortApi({
    jsonStr: JSON.stringify({ Rs }),
  })
}

// 专业模式志愿单导出Excel
const zyExportExcel = async () => {
  const params = new FormData()
  params.append('token', window.localStorage.getItem('token') || '')
  params.append('chGroupId', myChGroupSListId.value)
  try {
    const response = await axios.post(`${baseURL}/?ctl=ajax&mod=zhiYuan&act=ZyChoiceExportExcel`, params, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token') || ''}`,
      }
    })
    // 触发浏览器下载
    const a = document.createElement('a')
    a.href = response.data.file
    a.download = response.data.filename || '我的志愿单.xlsx'
    a.style.display = 'none'
    document.body.appendChild(a)
    a.click()
    ElMessage.success('正在导出我的志愿单，请稍后...')
  } catch (error) {
    console.log('-------->', error)
    ElMessage.error('导出Excel失败')
  }
}

// 专业模式志愿单按录取比例自动排序
const choicesSortBylqbl = async () => {
  const res = await api.choicesSortBylqblApi({
    chGroupId: myChGroupSListId.value,
  })
  if (res) {
    ElMessage.success('按录取比例自动排序成功')
    getMyChioesGroupQuery()
    // // 专业模式
    // if(personalForm.zyType === '1') {
    //   getMyChioesGroupQuery()
    // }
    // // 专业组模式
    // if (personalForm.zyType === '2') {
    //   getMyChioesGroupQuery()
    // }
  }
}

// 我的测评
const scaleData: any = ref([])
const getMyScalesQuery = async () => {
  const res = await api.assListQueryApi()
  if (res) {
    scaleData.value = res.data.Rs || []
  }
}

const scaleRowClick = (row: any) => {
  window.open(`/#/aiAssessmentView?asId=${row.asId}`)
}
</script>

<template>
  <div class="personal-info-page">
    <main class="container mx-auto px-6 py-8 flex flex-col md:flex-row gap-8">
      <!-- 个人信息侧边导航 -->
      <aside class="w-full md:w-1/4">
        <div class="bg-white rounded-xl shadow-md p-6">
          <div class="flex items-center pb-6 border-b">
            <!-- <div class="w-20 h-20 rounded-full bg-gray-200 flex items-center justify-center">
              <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em"
                viewBox="0 0 32 32" data-icon="carbon:user-avatar"
                class="iconify text-4xl text-neutral iconify--carbon">
                <path fill="currentColor" d="M16 8a5 5 0 1 0 5 5a5 5 0 0 0-5-5m0 8a3 3 0 1 1 3-3a3.003 3.003 0 0 1-3 3">
                </path>
                <path fill="currentColor"
                  d="M16 2a14 14 0 1 0 14 14A14.016 14.016 0 0 0 16 2m-6 24.377V25a3.003 3.003 0 0 1 3-3h6a3.003 3.003 0 0 1 3 3v1.377a11.9 11.9 0 0 1-12 0m13.993-1.451A5 5 0 0 0 19 20h-6a5 5 0 0 0-4.992 4.926a12 12 0 1 1 15.985 0">
                </path>
              </svg>
            </div> -->
            <div class="ml-4">
              <h3 class="text-lg font-bold text-neutral">{{ personalInfo.userName || '' }}</h3>
              <p class="text-sm text-neutral-400">{{ personalInfo.province || '' }}</p>
            </div>
          </div>
          <nav class="mt-6 space-y-2">
            <a v-if="personalInfo.ifDispUserInfo != '0'" @click="handleNavItemClick('basic-info')" :class="[
              'flex items-center p-3 rounded-lg transition-colors cursor-pointer',
              selectedNavItem === 'basic-info'
                ? 'bg-primary bg-opacity-10 text-primary'
                : 'text-neutral hover:bg-gray-100',
            ]">
              <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em"
                viewBox="0 0 32 32" data-icon="carbon:user-profile" class="iconify mr-3 iconify--carbon">
                <path fill="currentColor"
                  d="M12 4a5 5 0 1 1-5 5a5 5 0 0 1 5-5m0-2a7 7 0 1 0 7 7a7 7 0 0 0-7-7m10 28h-2v-5a5 5 0 0 0-5-5H9a5 5 0 0 0-5 5v5H2v-5a7 7 0 0 1 7-7h6a7 7 0 0 1 7 7zm0-26h10v2H22zm0 5h10v2H22zm0 5h7v2h-7z">
                </path>
              </svg>
              <span class="font-medium">基本信息</span>
            </a>
            <a v-if="personalInfo.userType == 1 && personalInfo.ifDispUserInfo != '0'" @click="handleNavItemClick('seeting-password')" :class="[
              'flex items-center p-3 rounded-lg transition-colors cursor-pointer',
              selectedNavItem === 'seeting-password'
                ? 'bg-primary bg-opacity-10 text-primary'
                : 'text-neutral hover:bg-gray-100',
            ]">
              <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em"
                viewBox="0 0 32 32" data-icon="carbon:password" class="iconify mr-3 iconify--carbon">
                <path fill="currentColor"
                  d="M21 2a8.998 8.998 0 0 0-8.612 11.612L2 24v6h6l10.388-10.388A9 9 0 1 0 21 2m0 16a7 7 0 0 1-2.032-.302l-1.147-.348l-.847.847l-3.181 3.181L12.414 20L11 21.414l1.379 1.379l-1.586 1.586L9.414 23L8 24.414l1.379 1.379L7.172 28H4v-3.172l9.802-9.802l.848-.847l-.348-1.147A7 7 0 1 1 21 18">
                </path>
                <circle cx="22" cy="10" r="2" fill="currentColor"></circle>
              </svg>
              <span class="font-medium">设置密码</span>
            </a>
            <a v-if="personalInfo.userType == 2" @click="handleNavItemClick('change-password')" :class="[
              'flex items-center p-3 rounded-lg transition-colors cursor-pointer',
              selectedNavItem === 'change-password'
                ? 'bg-primary bg-opacity-10 text-primary'
                : 'text-neutral hover:bg-gray-100',
            ]">
              <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em"
                viewBox="0 0 32 32" data-icon="carbon:settings" class="iconify mr-3 iconify--carbon">
                <path fill="currentColor"
                  d="M27 16.76v-1.53l1.92-1.68A2 2 0 0 0 29.3 11l-2.36-4a2 2 0 0 0-1.73-1a2 2 0 0 0-.64.1l-2.43.82a11 11 0 0 0-1.31-.75l-.51-2.52a2 2 0 0 0-2-1.61h-4.68a2 2 0 0 0-2 1.61l-.51 2.52a11.5 11.5 0 0 0-1.32.75l-2.38-.86A2 2 0 0 0 6.79 6a2 2 0 0 0-1.73 1L2.7 11a2 2 0 0 0 .41 2.51L5 15.24v1.53l-1.89 1.68A2 2 0 0 0 2.7 21l2.36 4a2 2 0 0 0 1.73 1a2 2 0 0 0 .64-.1l2.43-.82a11 11 0 0 0 1.31.75l.51 2.52a2 2 0 0 0 2 1.61h4.72a2 2 0 0 0 2-1.61l.51-2.52a11.5 11.5 0 0 0 1.32-.75l2.42.82a2 2 0 0 0 .64.1a2 2 0 0 0 1.73-1l2.28-4a2 2 0 0 0-.41-2.51ZM25.21 24l-3.43-1.16a8.9 8.9 0 0 1-2.71 1.57L18.36 28h-4.72l-.71-3.55a9.4 9.4 0 0 1-2.7-1.57L6.79 24l-2.36-4l2.72-2.4a8.9 8.9 0 0 1 0-3.13L4.43 12l2.36-4l3.43 1.16a8.9 8.9 0 0 1 2.71-1.57L13.64 4h4.72l.71 3.55a9.4 9.4 0 0 1 2.7 1.57L25.21 8l2.36 4l-2.72 2.4a8.9 8.9 0 0 1 0 3.13L27.57 20Z">
                </path>
                <path fill="currentColor"
                  d="M16 22a6 6 0 1 1 6-6a5.94 5.94 0 0 1-6 6m0-10a3.91 3.91 0 0 0-4 4a3.91 3.91 0 0 0 4 4a3.91 3.91 0 0 0 4-4a3.91 3.91 0 0 0-4-4">
                </path>
              </svg>
              <span class="font-medium">修改密码</span>
            </a>
            <a @click="handleNavItemClick('my-collections')" :class="[
              'flex items-center p-3 rounded-lg transition-colors cursor-pointer',
              selectedNavItem === 'my-collections'
                ? 'bg-primary bg-opacity-10 text-primary'
                : 'text-neutral hover:bg-gray-100',
            ]">
              <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em"
                viewBox="0 0 32 32" data-icon="carbon:notification" class="iconify mr-3 iconify--carbon">
                <path fill="currentColor"
                  d="M28.707 19.293L26 16.586V13a10.014 10.014 0 0 0-9-9.95V1h-2v2.05A10.014 10.014 0 0 0 6 13v3.586l-2.707 2.707A1 1 0 0 0 3 20v3a1 1 0 0 0 1 1h7v.777a5.15 5.15 0 0 0 4.5 5.199A5.006 5.006 0 0 0 21 25v-1h7a1 1 0 0 0 1-1v-3a1 1 0 0 0-.293-.707M19 25a3 3 0 0 1-6 0v-1h6Zm8-3H5v-1.586l2.707-2.707A1 1 0 0 0 8 17v-4a8 8 0 0 1 16 0v4a1 1 0 0 0 .293.707L27 20.414Z">
                </path>
              </svg>
              <span class="font-medium">我的志愿单</span>
            </a>
            <a @click="handleNavItemClick('my-scale')" :class="[
              'flex items-center p-3 rounded-lg transition-colors cursor-pointer',
              selectedNavItem === 'my-scale'
                ? 'bg-primary bg-opacity-10 text-primary'
                : 'text-neutral hover:bg-gray-100',
            ]">
              <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em"
                viewBox="0 0 32 32" data-icon="carbon:notification" class="iconify mr-3 iconify--carbon">
                <path fill="currentColor"
                  d="M28.707 19.293L26 16.586V13a10.014 10.014 0 0 0-9-9.95V1h-2v2.05A10.014 10.014 0 0 0 6 13v3.586l-2.707 2.707A1 1 0 0 0 3 20v3a1 1 0 0 0 1 1h7v.777a5.15 5.15 0 0 0 4.5 5.199A5.006 5.006 0 0 0 21 25v-1h7a1 1 0 0 0 1-1v-3a1 1 0 0 0-.293-.707M19 25a3 3 0 0 1-6 0v-1h6Zm8-3H5v-1.586l2.707-2.707A1 1 0 0 0 8 17v-4a8 8 0 0 1 16 0v4a1 1 0 0 0 .293.707L27 20.414Z">
                </path>
              </svg>
              <span class="font-medium">我的测评</span>
            </a>
          </nav>
        </div>
      </aside>
      <!-- 个人信息表单 -->
      <div v-if="selectedNavItem === 'basic-info'" class="w-full md:w-3/4">
        <div class="bg-white rounded-xl shadow-md overflow-hidden">
          <!-- 表单标题区 -->
          <div class="gradient-border background-gradient p-6">
            <div class="flex items-center">
              <h1 class="text-2xl font-bold text-white">个人信息设置</h1>
            </div>
            <p class="text-white text-opacity-80 mt-2">
              请更新您的个人资料信息，确保志愿填报服务的准确性
            </p>
          </div>
          <!-- 表单内容区 -->
          <div class="p-6">
            <form id="profileForm">
              <!-- 个人信息表单 -->
              <div class="space-y-6">
                <div class="grid grid-cols-2 gap-6">
                  <!-- 手机号码 -->
                  <div>
                    <label class="block text-sm font-medium text-neutral mb-2">手机号码</label>
                    <el-input type="tel" v-model="personalForm.phone" placeholder="请输入手机号码"
                      :disabled="personalForm.ifEditPhone == 0" class="input-tall44px">
                      <template #suffix>
                        已验证
                      </template>
                    </el-input>
                    <p class="mt-2 text-sm text-neutral-400">用于接收志愿填报提醒和系统通知</p>
                  </div>
                  <!-- 姓名 -->
                  <div>
                    <label class="block text-sm font-medium text-neutral mb-2">姓名</label>
                    <el-input v-model="personalForm.userName" placeholder="请输入姓名" class="input-tall44px">
                      <template #suffix>
                        <el-icon class="el-input__icon">
                          <Edit />
                        </el-icon>
                      </template>
                    </el-input>
                    <p class="mt-2 text-sm text-neutral-400">系统中显示的名称</p>
                  </div>
                </div>
                <div class="grid grid-cols-2 gap-6">
                  <!-- 所在高中 -->
                  <div>
                    <label class="block text-sm font-medium text-neutral mb-2">所在高中</label>
                    <el-input v-model="personalForm.highSchool" placeholder="请输入所在高中" class="input-tall44px">
                    </el-input>
                  </div>
                  <!-- 性别 -->
                  <div>
                    <label class="block text-sm font-medium text-neutral mb-2">性别</label>
                    <el-radio-group v-model="personalForm.sex">
                      <el-radio value="1" size="large">男</el-radio>
                      <el-radio value="2" size="large">女</el-radio>
                    </el-radio-group>
                  </div>
                </div>
                <!-- 选科信息 -->
                <p class="mt-2 text-sm text-neutral-400">
                  您当前还剩余 {{ personalForm.remainEditNum }} 次修改分数、位次的机会; 高考后还会给您 {{ personalForm.remainEditNumAfter }} 次修改机会
                </p>
                <div v-if="personalForm.xkMod == '1'">
                  <label class="block text-sm font-medium text-neutral mb-3">选科信息</label>
                  <div class="flex flex-wrap gap-3">
                    <label @click.stop="handleSubjectClick('A')" :class="[
                      'subject-tag px-4 py-2 border-2 border-gray-300 rounded-full cursor-pointer transition duration-200 hover:border-primary hover:bg-blue-50',
                      selectedSubjects.includes('A')
                        ? 'active'
                        : '',
                    ]">
                      <span class="text-neutral font-medium">物理</span>
                    </label>
                    <label @click.stop="handleSubjectClick('B')" :class="[
                      'subject-tag px-4 py-2 border-2 border-gray-300 rounded-full cursor-pointer transition duration-200 hover:border-primary hover:bg-blue-50',
                      selectedSubjects.includes('B')
                        ? 'active'
                        : '',
                    ]">
                      <span class="text-neutral font-medium">化学</span>
                    </label>
                    <label @click.stop="handleSubjectClick('C')" :class="[
                      'subject-tag px-4 py-2 border-2 border-gray-300 rounded-full cursor-pointer transition duration-200 hover:border-primary hover:bg-blue-50',
                      selectedSubjects.includes('C')
                        ? 'active'
                        : '',
                    ]">
                      <span class="text-neutral font-medium">生物</span>
                    </label>
                    <label @click.stop="handleSubjectClick('F')" :class="[
                      'subject-tag px-4 py-2 border-2 border-gray-300 rounded-full cursor-pointer transition duration-200 hover:border-primary hover:bg-blue-50',
                      selectedSubjects.includes('F')
                        ? 'active'
                        : '',
                    ]">
                      <span class="text-neutral font-medium">政治</span>
                    </label>
                    <label @click.stop="handleSubjectClick('D')" :class="[
                      'subject-tag px-4 py-2 border-2 border-gray-300 rounded-full cursor-pointer transition duration-200 hover:border-primary hover:bg-blue-50',
                      selectedSubjects.includes('D')
                        ? 'active'
                        : '',
                    ]">
                      <span class="text-neutral font-medium">历史</span>
                    </label>
                    <label @click.stop="handleSubjectClick('E')" :class="[
                      'subject-tag px-4 py-2 border-2 border-gray-300 rounded-full cursor-pointer transition duration-200 hover:border-primary hover:bg-blue-50',
                      selectedSubjects.includes('E')
                        ? 'active'
                        : '',
                    ]">
                      <span class="text-neutral font-medium">地理</span>
                    </label>
                  </div>
                </div>
                <div v-if="personalForm.xkMod == '2'">
                  <label class="block text-sm font-medium text-neutral mb-3">选科信息（物理和历史二选一）</label>
                  <div class="flex flex-wrap gap-3">
                    <label @click.stop="handleSubjectClick('A')" :class="[
                      'subject-tag px-4 py-2 border-2 border-gray-300 rounded-full cursor-pointer transition duration-200 hover:border-primary hover:bg-blue-50',
                      selectedSubjects.includes('A')
                        ? 'active'
                        : '',
                    ]">
                      <span class="text-neutral font-medium">物理</span>
                    </label>
                    <label @click.stop="handleSubjectClick('D')" :class="[
                      'subject-tag px-4 py-2 border-2 border-gray-300 rounded-full cursor-pointer transition duration-200 hover:border-primary hover:bg-blue-50',
                      selectedSubjects.includes('D')
                        ? 'active'
                        : '',
                    ]">
                      <span class="text-neutral font-medium">历史</span>
                    </label>
                  </div>
                </div>
                <div v-if="personalForm.xkMod == '2'">
                  <label class="block text-sm font-medium text-neutral mb-3">选科信息（化学、生物、政治、地理四选二）</label>
                  <div class="flex flex-wrap gap-3">
                    <label @click.stop="handleSubjectClick('B')" :class="[
                      'subject-tag px-4 py-2 border-2 border-gray-300 rounded-full cursor-pointer transition duration-200 hover:border-primary hover:bg-blue-50',
                      selectedSubjects.includes('B')
                        ? 'active'
                        : '',
                    ]">
                      <span class="text-neutral font-medium">化学</span>
                    </label>
                    <label @click.stop="handleSubjectClick('C')" :class="[
                      'subject-tag px-4 py-2 border-2 border-gray-300 rounded-full cursor-pointer transition duration-200 hover:border-primary hover:bg-blue-50',
                      selectedSubjects.includes('C')
                        ? 'active'
                        : '',
                    ]">
                      <span class="text-neutral font-medium">生物</span>
                    </label>
                    <label @click.stop="handleSubjectClick('F')" :class="[
                      'subject-tag px-4 py-2 border-2 border-gray-300 rounded-full cursor-pointer transition duration-200 hover:border-primary hover:bg-blue-50',
                      selectedSubjects.includes('F')
                        ? 'active'
                        : '',
                    ]">
                      <span class="text-neutral font-medium">政治</span>
                    </label>
                    <label @click.stop="handleSubjectClick('E')" :class="[
                      'subject-tag px-4 py-2 border-2 border-gray-300 rounded-full cursor-pointer transition duration-200 hover:border-primary hover:bg-blue-50',
                      selectedSubjects.includes('E')
                        ? 'active'
                        : '',
                    ]">
                      <span class="text-neutral font-medium">地理</span>
                    </label>
                  </div>
                </div>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                  <div>
                    <label class="block text-sm font-medium text-neutral mb-2">考试类别</label>
                    <el-select v-model="personalForm.wctype" placeholder="请选择考试类别"
                      :disabled="personalForm.remainXuankeEditNum < 1" class="select-tall44px" @change="wctypeChange">
                      <el-option v-for="(item, index) in wctypeList" :key="index" :label="item.wctypestr"
                        :value="item.wctype">
                      </el-option>
                    </el-select>
                  </div>
                  <div v-if="personalForm.wctype == 2">
                    <label class="block text-sm font-medium text-neutral mb-2">详细类别</label>
                    <el-select v-model="personalForm.yklm" placeholder="请选择详细类别"
                      :disabled="personalForm.remainXuankeEditNum < 1" class="select-tall44px">
                      <el-option v-for="(item, index) in subjectList" :key="index" :label="item.yklmStr"
                        :value="item.yklm" @click="handleYklmClick">
                      </el-option>
                    </el-select>
                  </div>
                </div>

                <!-- 分数和位次 -->
                <div
                  v-if="personalForm.wctype && (personalForm.xkMod == '2' && (selectedSubjects?.includes('A') || selectedSubjects?.includes('D')) || personalForm.xkMod != '2')"
                  class="grid grid-cols-1 md:grid-cols-2 gap-6">
                  <!-- 高考分数 -->
                  <div>
                    <label class="block text-sm font-medium text-neutral mb-2">高考分数</label>
                    <el-input max="750" min="0" name="score" placeholder="请输入您的高考总分" v-model="personalForm.cj"
                      :disabled="personalForm.remainEditNum < 1" @input="useDebounce(cjInput)" class="input-tall44px" />
                    <p class="mt-2 text-sm text-neutral-400">总分范围：0-750分</p>
                  </div>
                  <!-- 位次 -->
                  <div>
                    <label class="block text-sm font-medium text-neutral mb-2">位次</label>
                    <el-input min="1" name="ranking" placeholder="请输入您的省内位次" v-model="personalForm.wc"
                      :disabled="personalForm.remainEditNum < 1" class="input-tall44px" />
                    <p class="mt-2 text-sm text-neutral-400">请输入省内排名位次，如果所在省的一分一段表是分阶段的，请在不同阶段按实际情况填写</p>
                  </div>
                </div>
              </div>
              <!-- 表单操作区 -->
              <div class="border-t mt-8 pt-8 flex justify-end space-x-4">
                <el-button type="primary" class="background-gradient hover:opacity-90 elbutton44px"
                  @click="myUserInfoSaveBtn">保存个人信息</el-button>
              </div>
            </form>
          </div>
        </div>
      </div>
      <!-- 设置密码 -->
      <div v-if="selectedNavItem === 'seeting-password'" class="w-full md:w-3/4">
        <div class="bg-white rounded-xl shadow-md overflow-hidden">
          <!-- 表单标题区 -->
          <div class="gradient-border background-gradient p-6">
            <div class="flex items-center">
              <h1 class="text-2xl font-bold text-white">设置密码</h1>
            </div>
            <p class="text-white text-opacity-80 mt-2">
              设置您的密码
            </p>
          </div>
          <!-- 密码设置表单 -->
          <div class="p-6">
            <el-form label-position="top">
              <el-form-item label="手机号码">
                <el-input v-model="personalForm.phone" type="tel" placeholder="请输入手机号码"
                  style="height: 48px; line-height: 48px;" disabled>
                  <template #prefix>
                    <el-icon class="el-input__icon">
                      <PhoneFilled />
                    </el-icon>
                  </template>
                </el-input>
              </el-form-item>
              <el-form-item label="验证码">
                <el-input v-model="seetingpwdForm.code" placeholder="请输入验证码" clearable
                  style="height: 48px; line-height: 48px;">
                  <template #prefix>
                    <el-icon class="el-input__icon">
                      <GoodsFilled />
                    </el-icon>
                  </template>
                  <template #append>
                    <el-button @click="sendCode">获取验证码</el-button>
                  </template>
                </el-input>
              </el-form-item>
              <el-form-item label="密码">
                <el-input v-model="seetingpwdForm.newPass" type="password" placeholder="请输入密码"
                  style="height: 48px; line-height: 48px;">
                  <template #prefix>
                    <el-icon class="el-input__icon">
                      <GoodsFilled />
                    </el-icon>
                  </template>
                </el-input>
              </el-form-item>
              <el-form-item label="确认密码">
                <el-input v-model="seetingpwdForm.confirmPass" type="password" placeholder="请确认密码"
                  style="height: 48px; line-height: 48px;">
                  <template #prefix>
                    <el-icon class="el-input__icon">
                      <GoodsFilled />
                    </el-icon>
                  </template>
                </el-input>
              </el-form-item>
            </el-form>
            <!-- 表单操作区 -->
            <div class="border-t mt-8 pt-8 flex justify-end space-x-4">
              <el-button type="primary" class="background-gradient hover:opacity-90 elbutton44px"
                @click="handlePasswordSubmit">保存密码</el-button>
            </div>
          </div>
        </div>
      </div>
      <!-- 修改密码 -->
      <div v-if="selectedNavItem === 'change-password'" class="w-full md:w-3/4">
        <div class="bg-white rounded-xl shadow-md overflow-hidden">
          <!-- 表单标题区 -->
          <div class="gradient-border background-gradient p-6">
            <div class="flex items-center">
              <h1 class="text-2xl font-bold text-white">修改密码</h1>
            </div>
            <p class="text-white text-opacity-80 mt-2">
              修改您的密码
            </p>
          </div>
          <!-- 密码设置表单 -->
          <div class="p-6">
            <el-form label-position="top">
              <el-form-item label="旧密码">
                <el-input v-model="changePasswordForm.oldPass" type="password" placeholder="请输入旧密码"
                  style="height: 48px; line-height: 48px;">
                  <template #prefix>
                    <el-icon class="el-input__icon">
                      <GoodsFilled />
                    </el-icon>
                  </template>
                </el-input>
              </el-form-item>
              <el-form-item label="新密码">
                <el-input v-model="changePasswordForm.newPass" type="password" placeholder="请输入新密码"
                  style="height: 48px; line-height: 48px;">
                  <template #prefix>
                    <el-icon class="el-input__icon">
                      <GoodsFilled />
                    </el-icon>
                  </template>
                </el-input>
              </el-form-item>
              <el-form-item label="确认密码">
                <el-input v-model="changePasswordForm.confirmPass" type="password" placeholder="请确认新密码"
                  style="height: 48px; line-height: 48px;">
                  <template #prefix>
                    <el-icon class="el-input__icon">
                      <GoodsFilled />
                    </el-icon>
                  </template>
                </el-input>
              </el-form-item>
            </el-form>
            <!-- 表单操作区 -->
            <div class="border-t mt-8 pt-8 flex justify-end space-x-4">
              <el-button type="primary" class="background-gradient hover:opacity-90 elbutton44px"
                @click="handleChangePasswordSubmit">保存密码</el-button>
            </div>
          </div>
        </div>
      </div>
      <!-- 我的志愿单 -->
      <div v-if="selectedNavItem === 'my-collections'" class="w-full md:w-3/4">
        <div class="bg-white rounded-xl shadow-md overflow-hidden">
          <!-- 表单标题区 -->
          <div class="gradient-border background-gradient p-6">
            <div class="flex items-center">
              <h1 class="text-2xl font-bold text-white">我的志愿单</h1>
            </div>
            <p class="text-white text-opacity-80 mt-2">
              查看您的志愿单
            </p>
          </div>
          <!-- 志愿单列表 -->
          <div class="p-6">
            <div class="flex align-center flex-wrap gap-4">
              <el-tag v-for="(item, index) in myChioesGroupQueryList" :key="index"
                :type="item.chGroupId == myChGroupSListId ? 'primary' : 'info'" @click="handleViewGroup(item.chGroupId)"
                style="cursor: pointer; font-size: 14px; height: 32px;">
                {{ item.chGroupName }}（{{ item.addNum }}/{{ item.maxNum }}）
              </el-tag>
              <el-button type="primary" @click="zyExportExcel">导出Excel</el-button>
              <el-button type="primary" @click="choicesSortBylqbl" style="margin-left: 0;">自动排序</el-button>
            </div>
            <div v-if="tableData?.length > 0" style="margin-top: 20px; width: 100%;">
              <el-table v-if="personalForm.zyType === '1'" ref="sortableTableRef" v-loading="false" :data="tableData"
                stripe border size="small" row-key="chId" class="custom-table" style="width: 100%">
                <el-table-column width="60" label="排序" align="center">
                  <template #default="scope">
                    <div style="font-size: 16px; font-weight: 700; color: #000;">
                      {{ scope.$index + 1 }}
                      <!-- {{ scope.row.xh }} -->
                    </div>
                  </template>
                </el-table-column>
                <el-table-column prop="yxmc" label="招生院校" min-width="130" align="left">
                  <template #default="scope">
                    <div class="font-medium tableyxmc">
                      <span style="font-size: 16px; font-weight: bold;">{{ scope.row.yxmc }}</span>
                      <span v-if="scope.row.lqdcstr.includes('稳')" class="lqdcstr bg2">{{ scope.row.lqdcstr }}</span>
                      <span v-else-if="scope.row.lqdcstr.includes('冲')" class="lqdcstr bg1">{{
                        scope.row.lqdcstr }}</span>
                      <span v-else class="lqdcstr bg3">{{ scope.row.lqdcstr }}</span>
                    </div>
                    <div class="text-xs text-gray-500">
                      {{ scope.row.provice }}/{{ scope.row.city }}
                      {{ scope.row.sylyx === 1 ? ' 一流大学 | ' : '' }}
                      {{ scope.row.sylxk === 1 ? '一流学科建设高校 | ' : '' }}
                      {{ scope.row.sf211 === 1 ? '211高校 |' : '' }}
                      {{ scope.row.sf985 === 1 ? '985高校' : '' }}
                      <span v-if="scope.row.byly">保研率：{{ scope.row.byly }}</span>
                      <span v-if="scope.row.yxjblxmc">{{ scope.row.yxjblxmc }}</span>
                    </div>
                  </template>
                </el-table-column>
                <el-table-column label="招生专业" min-width="200" align="left">
                  <template #default="scope">
                    <div class="tablezy" style="padding-top: 10px;">
                      <div class="text-xs text-gray-500">专业名称：<span style="font-weight: bold;">{{
                        scope.row.zymc }}</span>
                      </div>
                      <div class="text-xs text-gray-500">专业代号：<span style="font-weight: bold;">{{
                        scope.row.zydh }}</span>
                      </div>
                      <div class="text-xs text-gray-500">计划人数：<span>{{ scope.row.jhrs }}</span>
                      </div>
                      <el-tooltip v-if="scope.row.JHBZ" popper-class="custom-tooltip" effect="dark"
                        :content="scope.row.JHBZ" placement="top">
                        <div class="flex items-center text-xs text-gray-500">备注：<span class="beizhu">{{ scope.row.JHBZ
                            }}</span></div>
                      </el-tooltip>
                      <div v-if="scope.row.xkkm" class="text-xs text-gray-500">选科：<span>{{ scope.row.xkkm }}</span>
                      </div>
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
                <el-table-column min-width="90" align="left">
                  <template #header>
                    {{ tableData[0].match1Year ?? '历年' }}
                  </template>
                  <template #default="scope">
                    <div v-if="scope.row.minwc1 != 0 && scope.row.mincj1 != 0" class="tablezy">
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
                <el-table-column min-width="90" align="left">
                  <template #header>
                    {{ tableData[0].match2Year ?? '历年' }}
                  </template>
                  <template #default="scope">
                    <div v-if="scope.row.minwc2 != 0 && scope.row.mincj2 != 0" class="tablezy">
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
                <el-table-column min-width="90" align="left">
                  <template #header>
                    {{ tableData[0].match3Year ?? '历年' }}
                  </template>
                  <template #default="scope">
                    <div v-if="scope.row.minwc3 != 0 && scope.row.mincj3 != 0" class="tablezy">
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
                <el-table-column prop="bl" label="录取比例" width="90" sortable align="center">
                  <template #default="scope">
                    <div class="text-center text-xs mt-1">
                      <span v-if="scope.row.bl && scope.row.bl > 0 && scope.row.bl < 100" style="font-weight: bold; color: #000;">{{ scope.row.bl }}%</span>
                    </div>
                  </template>
                </el-table-column>
                <el-table-column width="80" align="center" fixed="right" label="操作">
                  <template #default="scope">
                    <el-button text type="danger" size="small" @click="zyHandleDelete(scope.row)">
                      删除
                    </el-button>
                  </template>
                </el-table-column>
              </el-table>
              <el-table v-if="personalForm.zyType === '2'" ref="sortableTableRef" v-loading="false" :data="tableData"
                stripe :row-key="(row: any) => row.zyGroupId" :expand-row-keys="expandedRows"
                @expand-change="handleExpandChange" border size="small" id="custom-expand-table" style="width: 100%">
                <el-table-column type="expand" width="1" align="center">
                  <template #default="{ row }">
                    <el-table :data="row.zyRs" border :show-header="false">
                      <!-- <el-table-column type="index" width="41" align="center">
                      </el-table-column> -->
                      <el-table-column width="61" label="排序" align="center">
                        <template #default="scope">
                          <div style="font-size: 16px; font-weight: 700; color: #000;">
                            {{ scope.$index + 1 }}
                            <!-- {{ scope.row.xh }} -->
                          </div>
                        </template>
                      </el-table-column>
                      <el-table-column label="专业" min-width="150">
                        <template #default="scope">
                          <div class="font-medium tableyxmc">
                            <p>
                              <span style="font-weight: normal;">专业名称：</span><span>{{ scope.row.zymc }}</span>
                              &nbsp;
                              <span style="font-weight: normal;">专业代号：</span><span>{{ scope.row.zydh }}</span>
                              &nbsp;
                              <span v-if="scope.row.lqdcstr.includes('稳')" class="lqdcstr bg2">{{ scope.row.lqdcstr }}</span>
                              <span v-else-if="scope.row.lqdcstr.includes('冲')" class="lqdcstr bg1">{{ scope.row.lqdcstr }}</span>
                              <span v-else class="lqdcstr bg3">{{ scope.row.lqdcstr }}</span>
                            </p>
                          </div>
                          <el-tooltip v-if="scope.row.jhbz" popper-class="custom-tooltip" effect="dark"
                            :content="scope.row.jhbz" placement="top">
                            <div class="text-xs text-gray-500">备注：<span class="beizhu">{{ scope.row.jhbz }}</span></div>
                          </el-tooltip>
                        </template>
                      </el-table-column>
                      <el-table-column label="计划人数" min-width="90">
                        <template #default="scope">
                          <div
                            style="display: flex; flex-direction: column; justify-content: center; align-items: center;">
                            <div class="text-xs text-gray-500"><span
                                style="font-size: 20px; font-weight: 600; color: #000;">
                                {{ scope.row.jhrs }}</span>人
                            </div>
                            <div class="text-xs text-gray-500 mt-1">{{ scope.row.xkkm }}</div>
                            <div class="text-xs text-gray-500 mt-1">{{ scope.row.xzdm }}/{{ scope.row.sfbz }}</div>
                          </div>
                        </template>
                      </el-table-column>
                      <el-table-column label="match1Year" min-width="90">
                        <template #default="scope">
                          <div v-if="scope.row.minwc1 != 0 && scope.row.mincj1 != 0" class="tablezy">
                            <!-- <div class="text-xs text-gray-500"><span>{{ scope.row.match1Year }}</span>年</div> -->
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
                      <el-table-column label="match2Year" min-width="90">
                        <template #default="scope">
                          <div v-if="scope.row.minwc2 != 0 && scope.row.mincj2 != 0" class="tablezy">
                            <!-- <div class="text-xs text-gray-500"><span>{{ scope.row.match2Year }}</span>年</div> -->
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
                      <el-table-column label="match3Year" min-width="90">
                        <template #default="scope">
                          <div v-if="scope.row.minwc3 != 0 && scope.row.mincj3 != 0" class="tablezy">
                            <!-- <div class="text-xs text-gray-500"><span>{{ scope.row.match3Year }}</span>年</div> -->
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
                      <el-table-column label="录取比例" width="100">
                        <template #default="scope">
                          <div class="text-center text-xs mt-1">
                            <span v-if="scope.row.bl && scope.row.bl > 0 && scope.row.bl < 100" style="font-weight: bold; color: #000;">{{ scope.row.bl }}%</span>
                          </div>
                        </template>
                      </el-table-column>
                      <el-table-column label="操作" width="70" align="center">
                        <template #default="subScope">
                          <el-button text type="danger" size="small" @click="zyGroupHandleDelete2(subScope.row)">
                            删除
                          </el-button>
                        </template>
                      </el-table-column>
                      <el-table-column label="操作" width="70" align="center">
                      </el-table-column>
                    </el-table>
                  </template>
                </el-table-column>
                <el-table-column width="60" label="排序" align="center">
                  <template #default="scope">
                    <div style="font-size: 16px; font-weight: 700; color: #000;">
                      {{ scope.$index + 1 }}
                      <!-- {{ scope.row.xh }} -->
                    </div>
                  </template>
                </el-table-column>
                <el-table-column label="招生院校" min-width="150">
                  <template #default="scope">
                    <div class="font-medium tableyxmc">
                      <span>{{ scope.row.yxmc }}（{{ scope.row.zyGroupDm }}）专业组</span>
                      <span v-if="scope.row.lqdcstr.includes('稳')" class="lqdcstr bg2">{{ scope.row.lqdcstr }}</span>
                      <span v-else-if="scope.row.lqdcstr.includes('冲')" class="lqdcstr bg1">{{ scope.row.lqdcstr
                        }}</span>
                      <span v-else class="lqdcstr bg3">{{ scope.row.lqdcstr }}</span>
                    </div>
                    <div class="text-xs text-gray-500">
                      院校代码：<span style="font-weight: bold; color: #000;">{{ scope.row.yxdm }}</span> |
                      {{ scope.row.provice }}/{{ scope.row.city }} |
                      {{ scope.row.sylyx === 1 ? ' 一流大学 | ' : '' }}
                      {{ scope.row.sylxk === 1 ? ' 一流学科建设高校 | ' : '' }}
                      {{ scope.row.sf211 === 1 ? ' 211高校 | ' : '' }}
                      {{ scope.row.sf985 === 1 ? ' 985高校 | ' : '' }}
                      <span v-if="scope.row.byly">保研率：{{ scope.row.byly }}</span>
                      <span v-if="scope.row.yxjblxmc">{{ scope.row.yxjblxmc }}</span>
                    </div>
                  </template>
                </el-table-column>
                <el-table-column label="招生计划" min-width="90">
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
                <el-table-column label="match1Year" min-width="90">
                  <template #header>
                    {{ tableData[0].match1Year ?? '历年' }}
                  </template>
                  <template #default="scope">
                    <div v-if="scope.row.minwc1 != 0 && scope.row.mincj1 != 0" class="tablezy">
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
                <el-table-column label="match2Year" min-width="90">
                  <template #header>
                    {{ tableData[0].match2Year ?? '历年' }}
                  </template>
                  <template #default="scope">
                    <div v-if="scope.row.minwc2 != 0 && scope.row.mincj2 != 0" class="tablezy">
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
                <el-table-column label="match3Year" min-width="90">
                  <template #header>
                    {{ tableData[0].match3Year ?? '历年' }}
                  </template>
                  <template #default="scope">
                    <div v-if="scope.row.minwc3 != 0 && scope.row.mincj3 != 0" class="tablezy">
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
                <el-table-column label="录取比例" width="100" sortable align="center">
                  <template #default="scope">
                    <div class="text-center text-xs mt-1">
                      <span v-if="scope.row.bl && scope.row.bl > 0 && scope.row.bl < 100" style="font-weight: bold; color: #000;">{{ scope.row.bl }}%</span>
                    </div>
                  </template>
                </el-table-column>
                <el-table-column label="操作" width="70" align="center">
                  <template #default="scope">
                    <el-button text type="danger" size="small" @click="zyGroupHandleDelete1(scope.row)">
                      删除
                    </el-button>
                  </template>
                </el-table-column>
                <el-table-column label="" width="70" align="center">
                  <template #default="scope">
                    <div style="display: flex; justify-content: center; align-items: center;"
                      @click="toggleExpand(scope.row)">
                      <el-button text type="primary">
                        <div v-if="!expandedRows.includes(scope.row.zyGroupId)"
                          style="cursor: pointer; display: flex; justify-content: center;align-items: center;">
                          展开
                          <el-icon>
                            <ArrowDown />
                          </el-icon>
                        </div>
                        <div v-else
                          style="cursor: pointer; display: flex; justify-content: center;align-items: center;">
                          收起
                          <el-icon>
                            <ArrowUp />
                          </el-icon>
                        </div>
                      </el-button>
                    </div>
                  </template>
                </el-table-column>
              </el-table>
            </div>
          </div>
        </div>
      </div>
      <div v-if="selectedNavItem === 'my-scale'" class="w-full md:w-3/4">
        <div class="bg-white rounded-xl shadow-md overflow-hidden">
          <!-- 表单标题区 -->
          <div class="gradient-border background-gradient p-6">
            <div class="flex items-center">
              <h1 class="text-2xl font-bold text-white">我的测评</h1>
            </div>
            <p class="text-white text-opacity-80 mt-2">
              查看您的测评结果
            </p>
          </div>
          <div class="p-6">
            <div class="flex align-center flex-wrap gap-4">
              <el-table :data="scaleData" v-loading="false" stripe border size="small" row-key="yxmc"
                class="custom-table" style="width: 100%" @row-click="scaleRowClick">
                <el-table-column prop="scaleName" label="测评名称" min-width="200">
                </el-table-column>
                <el-table-column label="测评时间" min-width="150">
                  <template #default="scope">
                    <div>
                      {{ dayjs(scope.row.completeTime).format('YYYY-MM-DD HH:mm:ss') }}
                    </div>
                  </template>
                </el-table-column>
              </el-table>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<style lang="scss" scoped>
.personal-info-page {
  max-width: 80vw;
  min-width: 1200px;
  min-height: calc(100vh - 428px);
  margin: 0 auto;
  background-color: #fff;
  box-shadow:
    0 10px 15px -3px rgb(0 0 0 / 0.1),
    0 4px 6px -4px rgb(0 0 0 / 0.1);
  border-top: 1px solid #e5e7eb;

  .gradient-border {
    background-color: rgba(0, 0, 0, 0);
    background-position-x: 0%;
    background-position-y: 0%;
    background-repeat: repeat;
    background-attachment: scroll;
    background-size: auto;
    background-origin: padding-box;
    background-clip: border-box;
  }

  .background-gradient {
    background-image: linear-gradient(to right, rgb(24, 144, 255), rgb(108, 92, 231));
  }

  .text-primary {
    color: rgb(24 144 255);
  }

  .bg-primary {
    background-color: rgb(24 144 255 / 0.1);
  }

  .active {
    background: linear-gradient(to right, #1890ff, #6c5ce7);
    background-color: rgba(0, 0, 0, 0);
    border-color: #1890ff !important;
    color: white;
  }
}

.tableyxmc {
  margin-bottom: 10px;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  // font-size: 16px;
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
    // display: flex;
    // align-items: center;
    margin-bottom: 8px;
    margin-right: 16px;
    color: #646566;
    font-size: 12px;
    line-height: 16px;

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
      width: 120px;
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
</style>


<style lang="scss">
.personal-info-page {
  .el-tag {
    border: 0;
  }

  .el-tag--primary {
    color: #fff;
    background-image: linear-gradient(to right, rgb(24, 144, 255), rgb(108, 92, 231));
  }

  .el-tag--info {
    color: rgb(55 65 81);
  }
}

#custom-expand-table .el-table__expand-column .cell {
  display: none;
}
</style>
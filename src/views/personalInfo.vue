<script setup lang="ts">
import { onMounted, ref } from 'vue'
import * as api from '@/api/interfaceapi'
import { ElMessage } from 'element-plus'
import { useRoute } from 'vue-router'
import {
  ArrowLeft,
} from '@element-plus/icons-vue'

const route = useRoute()
onMounted(() => {
  // 初始化时根据路由参数设置选中的导航项
  if (route.query.tab === 'my-collections') {
    selectedNavItem.value = route.query.tab as string
    getMyChioesGroupQuery()
  }
  genListQueryList()
  getMyuserInfoQuery()
})

// 选中的导航项 - 可选值：'basic-info', 'seeting-password', 'change-password', 'my-collections'
const selectedNavItem = ref('basic-info')
const handleNavItemClick = (navItem: string) => {
  selectedNavItem.value = navItem
  console.log(`选择了导航项: ${navItem}`)
  if (navItem === 'my-collections') {
    getMyChioesGroupQuery()
  }
  // 这里可以添加页面切换或内容加载逻辑
}

// 个人信息
const personalInfo: any = ref<any>({})
const personalForm: any = ref({})
const getMyuserInfoQuery = async () => {
  try {
    const res = await api.myuserInfoQueryApi({
      token: window.localStorage.getItem('token') || ''
    })
    if (res.data.code == 0) {
      personalInfo.value = res.data.data || {}
      personalForm.value = JSON.parse(JSON.stringify(personalInfo.value))
      selectedSubjects.value = personalForm.value.xuanke.split(',') || []
      if (personalForm.value.province) {
        getwctypeList()
        getYklmQuery()
      }
    } else {
      ElMessage.error(res.data.message || '获取个人信息失败')
    }
  } catch (error) {
    ElMessage.error('获取个人信息失败')
  }
}

// 所在省份
const handleProvinceChange = () => {
  getwctypeList()
  getYklmQuery()
}

// 获取省份列表
const provinceList = ref<any>([])
const genListQueryList = async () => {
  try {
    const res = await api.userProvQueryApi({
      token: window.localStorage.getItem('token') || '',
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

// 选科信息
const selectedSubjects = ref<string[]>([])
const handleSubjectClick = (subject: string) => {

  const index = selectedSubjects.value.indexOf(subject)
  if (index > -1) {
    selectedSubjects.value.splice(index, 1)
  } else {
    if (selectedSubjects.value.length >= 3) {
      ElMessage.warning('最多选择3科')
      return
    }
    selectedSubjects.value.push(subject)
  }
  console.log(`选科变化: 当前选中 ${selectedSubjects.value.join(',')}`)
}

// 考生类别查询
const wctypeList: any = ref([])
const getwctypeList = async () => {
  try {
    const res = await api.WctypeQueryApi({
      token: window.localStorage.getItem('token') || '',
      province: personalForm.value.province || ''
    })
    if (res.data.code == 0) {
      wctypeList.value = res.data.data || []
    } else {
      ElMessage.error(res.data.message || '获取考生类别列表失败')
    }
  } catch (error) {
    ElMessage.error('获取考生类别列表失败')
  }
}
const wctypeChange = () => {
  personalForm.value.yklm = ''
}

// 考试类别小类查询
const subjectList = ref<any>([])
const getYklmQuery = async () => {
  try {
    const res = await api.yklmQueryApi({
      token: window.localStorage.getItem('token') || '',
      wctype: '2',
      province: personalForm.value.province || ''
    })
    if (res.data.code == 0) {
      console.log(res);
      subjectList.value = res.data.data.Rs || []
    } else {
      ElMessage.error(res.data.message || '获取高考科目列表失败')
    }
  } catch (error) {
    ElMessage.error('获取高考科目列表失败')
  }
}

// 输入分数查询位次查询
const cjInput = async () => {
  try {
    const res = await api.wcQueryBycjApi({
      token: window.localStorage.getItem('token') || '',
      cj: personalForm.value.cj,
      wctype: personalForm.value.wctype,
      yklm: personalForm.value.yklm,
    })
    if (res.data.code == 0) {
      personalForm.value.wc = res.data.data.wc || ''
    } else {
      ElMessage.error(res.data.message || '查询失败')
    }
  } catch (error) {
    ElMessage.error('查询失败')
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
    ElMessage.warning('请输入昵称')
    return
  }
  if (!personalForm.value.sex) {
    ElMessage.warning('请选择性别')
    return
  }
  if (!personalForm.value.province) {
    ElMessage.warning('请选择所在省份')
    return
  }
  if (selectedSubjects.value.length === 0) {
    ElMessage.warning('请选择高考选科科目')
    return
  } else {
    personalForm.value.xkkm = selectedSubjects.value.join(',')
  }
  if (!personalForm.value.wctype) {
    ElMessage.warning('请选择考生类别')
    return
  }
  if (personalForm.value.wctype == 2) {
    if (!personalForm.value.yklm) {
      ElMessage.warning('请选择考试类别')
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
  if (personalForm.value.zyType == '2') {
    if (!selectedSubjects.value.includes('A') && !selectedSubjects.value.includes('D')) {
      ElMessage.warning('选科信息中必须包含物理或历史')
      return
    }
  }
  personalForm.value.token = window.localStorage.getItem('token') || ''
  try {
    const res = await api.myUserInfoSaveApi(personalForm.value)
    if (res.data.code == 0) {
      ElMessage.success('保存成功')
    } else {
      ElMessage.error(res.data.message || '保存失败')
    }
  } catch (error) {
    ElMessage.error('保存失败')
  }
}

// 设置密码
const seetingpwdForm = ref({
  phone: '',
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

  try {
    const res = await api.passResetApi({
      token: window.localStorage.getItem('token') || '',
      newPass: seetingpwdForm.value.newPass,
      vfCode: seetingpwdForm.value.code,
    })
    if (res.data.code == 0) {
      ElMessage.success('密码设置成功')
      // 清空密码输入框
      seetingpwdForm.value.phone = ''
      seetingpwdForm.value.code = ''
      seetingpwdForm.value.newPass = ''
      seetingpwdForm.value.confirmPass = ''
    } else {
      ElMessage.error(res.data.message || '密码设置失败')
    }
  } catch (error) {
    ElMessage.error('密码设置失败')
  }
}

// 发送验证码
const sendCode = async () => {
  if (!seetingpwdForm.value.phone) {
    ElMessage.warning('请输入手机号码')
    return
  }
  if (!/^(?:(?:\+|00)86)?1[3-9]\d{9}$/.test(seetingpwdForm.value.phone)) {
    ElMessage.warning('请输入正确的手机号码')
    return
  }
  try {
    const res: any = await api.authcodeApi({
      phone: seetingpwdForm.value.phone,
      type: 1
    })
    if (res.data.code === 0) {
      ElMessage.success(`验证码已发送到 ${seetingpwdForm.value.phone}`)
    } else {
      ElMessage.error(res.data.message || '发送验证码失败')
    }
  } catch (error) {
    ElMessage.error('发送验证码失败')
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
  try {
    const res: any = await api.passModiApi({
      token: window.localStorage.getItem('token') || '',
      oldPass: changePasswordForm.value.oldPass,
      newPass: changePasswordForm.value.newPass,
    })
    if (res.data.code === 0) {
      ElMessage.success('密码修改成功')
      // 清空密码输入框
      changePasswordForm.value.oldPass = ''
      changePasswordForm.value.newPass = ''
      changePasswordForm.value.confirmPass = ''
    } else {
      ElMessage.error(res.data.message || '密码修改失败')
    }
  } catch (error) {
    ElMessage.error('密码修改失败')
  }
}

// // 志愿分组查询
// // a.token:用户token，必选
// // b.ccdm  1 本科 2 专科 99全部
// export function myChioesGroupQueryApi(data: any) {
//   const params = new FormData()
//   Object.keys(data).forEach(key => {
//     params.append(key, data[key])
//   })
//   return axios.post(`${baseURL}/mod/zhiYuan/MyChoicesGroupQuery.ajax.php`, params)
// }
// 我的收藏 - 志愿分组查询
const myChioesGroupQueryState = ref('initQuery')
const ccdm = ref(99)
const myChioesGroupQueryList = ref([])
const myChioesGroupQueryLoading = ref(false)
const getMyChioesGroupQuery = async () => {
  try {
    myChioesGroupQueryLoading.value = true
    const res: any = await api.myChioesGroupQueryApi({
      token: window.localStorage.getItem('token') || '',
      ccdm: ccdm.value,
    })
    if (res.data.code === 0) {
      myChioesGroupQueryList.value = res.data.data || []
    } else {
      ElMessage.error(res.data.message || '查询失败')
    }
  } catch (error) {
    ElMessage.error('查询失败')
  } finally {
    myChioesGroupQueryLoading.value = false
  }
}
const zyHandleDelete = async (row: any) => {
  try {
    const res: any = await api.delChoiceApi({
      token: window.localStorage.getItem('token') || '',
      chId: row.chId,
    })
    if (res.data.code === 0) {
      ElMessage.success('删除成功')
      // 刷新收藏分组查询
      getMyChioesGroupQuery()
    } else {
      ElMessage.error(res.data.message || '删除失败')
    }
  } catch (error) {
    ElMessage.error('删除失败')
  }
}
// 专业模式收藏查询
const tableData: any = ref([])
const handleViewGroup1 = async (row: any) => {
  myChioesGroupQueryState.value = 'zyQuery'
  try {
    const res: any = await api.zyChoicesQueryApi({
      token: window.localStorage.getItem('token') || '',
      chGroupId: row.chGroupId,
    })
    if (res.data.code === 0) {
      tableData.value = res.data.data.Rs || []
    } else {
      ElMessage.error(res.data.message || '查询失败')
    }
  } catch (error) {
    ElMessage.error('查询失败')
  }
}
// 专业组模式收藏查询
const handleViewGroup2 = async (row: any) => {
  myChioesGroupQueryState.value = 'zyGroupQuery'
  try {
    const res: any = await api.zyGroupChoicesQueryApi({
      token: window.localStorage.getItem('token') || '',
      chGroupId: row.chGroupId,
    })
    if (res.data.code === 0) {
      tableData.value = res.data.data.Rs || []
    } else {
      ElMessage.error(res.data.message || '查询失败')
    }
  } catch (error) {
    ElMessage.error('查询失败')
  }
}
const zyGroupHandleDelete = async (row: any) => {
  try {
    const res: any = await api.delChoiceGroupApi({
      token: window.localStorage.getItem('token') || '',
      chZyGroupId: row.chZyGroupId,
    })
    if (res.data.code === 0) {
      ElMessage.success('删除成功')
      // 刷新收藏分组查询
      getMyChioesGroupQuery()
    } else {
      ElMessage.error(res.data.message || '删除失败')
    }
  } catch (error) {
    ElMessage.error('删除失败')
  }
}

// 合并表格
const objectSpanMethod = ({ row, rowIndex, columnIndex }: any) => {
  console.log('-------->', row, rowIndex, columnIndex)
}
</script>

<template>
  <div class="personal-info-page">
    <main class="container mx-auto px-6 py-8 flex flex-col md:flex-row gap-8">
      <!-- 个人信息侧边导航 -->
      <aside class="w-full md:w-1/4">
        <div class="bg-white rounded-xl shadow-md p-6">
          <div class="flex items-center pb-6 border-b">
            <div class="w-20 h-20 rounded-full bg-gray-200 flex items-center justify-center">
              <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em"
                viewBox="0 0 32 32" data-icon="carbon:user-avatar"
                class="iconify text-4xl text-neutral iconify--carbon">
                <path fill="currentColor" d="M16 8a5 5 0 1 0 5 5a5 5 0 0 0-5-5m0 8a3 3 0 1 1 3-3a3.003 3.003 0 0 1-3 3">
                </path>
                <path fill="currentColor"
                  d="M16 2a14 14 0 1 0 14 14A14.016 14.016 0 0 0 16 2m-6 24.377V25a3.003 3.003 0 0 1 3-3h6a3.003 3.003 0 0 1 3 3v1.377a11.9 11.9 0 0 1-12 0m13.993-1.451A5 5 0 0 0 19 20h-6a5 5 0 0 0-4.992 4.926a12 12 0 1 1 15.985 0">
                </path>
              </svg>
            </div>
            <div class="ml-4">
              <h3 class="text-lg font-bold text-neutral">{{ personalInfo.userName || '' }}</h3>
              <p class="text-sm text-neutral-400">{{ personalInfo.province || '' }}</p>
            </div>
          </div>
          <nav class="mt-6 space-y-2">
            <a @click="handleNavItemClick('basic-info')" :class="[
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
            <a @click="handleNavItemClick('seeting-password')" :class="[
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
            <a @click="handleNavItemClick('change-password')" :class="[
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
              <span class="font-medium">我的收藏</span>
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
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                  <!-- 手机号码 -->
                  <div>
                    <label class="block text-sm font-medium text-neutral mb-2">手机号码</label>
                    <el-input type="tel" v-model="personalForm.phone" placeholder="请输入手机号码"
                      :disabled="personalForm.ifEditPhone === 0" class="input-tall44px">
                      <template #suffix>
                        已验证
                      </template>
                    </el-input>
                    <p class="mt-2 text-sm text-neutral-400">用于接收志愿填报提醒和系统通知</p>
                  </div>
                  <!-- 昵称 -->
                  <div>
                    <label class="block text-sm font-medium text-neutral mb-2">昵称</label>
                    <el-input v-model="personalForm.userName" placeholder="请输入昵称" class="input-tall44px">
                      <template #suffix>
                        <el-icon class="el-input__icon">
                          <Edit />
                        </el-icon>
                      </template>
                    </el-input>
                    <p class="mt-2 text-sm text-neutral-400">系统中显示的名称</p>
                  </div>
                </div>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                  <!-- 性别 -->
                  <div>
                    <label class="block text-sm font-medium text-neutral mb-2">性别</label>
                    <el-radio-group v-model="personalForm.sex">
                      <el-radio value="1" size="large">男</el-radio>
                      <el-radio value="2" size="large">女</el-radio>
                    </el-radio-group>
                  </div>
                  <!-- 省份 -->
                  <div>
                    <label class="block text-sm font-medium text-neutral mb-2">所在省份</label>
                    <el-select v-model="personalForm.province" placeholder="请选择省份"
                      :disabled="personalForm.remainEditNum <= 0" class="select-tall44px"
                      @change="handleProvinceChange">
                      <el-option v-for="(item, index) in provinceList" :key="index" :label="item.province"
                        :value="item.province">
                      </el-option>
                    </el-select>
                  </div>
                </div>
                <!-- 选科信息 -->
                <div>
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
                <div v-if="personalForm.province" class="grid grid-cols-1 md:grid-cols-2 gap-6">
                  <div>
                    <label class="block text-sm font-medium text-neutral mb-2">高考选科科目</label>
                    <el-select v-model="personalForm.wctype" placeholder="请选择高考选科科目"
                      :disabled="personalForm.remainEditNum <= 0" class="select-tall44px" @change="wctypeChange">
                      <el-option v-for="(item, index) in wctypeList" :key="index" :label="item.wctypestr"
                        :value="item.wctype">
                      </el-option>
                    </el-select>
                  </div>
                  <div v-if="personalForm.wctype == 2">
                    <label class="block text-sm font-medium text-neutral mb-2">考试类别</label>
                    <el-select v-model="personalForm.yklm" placeholder="请选择考试类别"
                      :disabled="personalForm.remainEditNum <= 0" class="select-tall44px">
                      <el-option v-for="(item, index) in subjectList" :key="index" :label="item.yklmStr"
                        :value="item.yklm">
                      </el-option>
                    </el-select>
                  </div>
                </div>

                <!-- 分数和位次 -->
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                  <!-- 高考分数 -->
                  <div>
                    <label class="block text-sm font-medium text-neutral mb-2">高考分数</label>
                    <el-input-number max="750" min="0" name="score" placeholder="请输入您的高考总分" type="number"
                      v-model="personalForm.cj" :disabled="personalForm.remainEditNum <= 0" @input="cjInput"
                      class="input-tall44px" />
                    <p class="mt-2 text-sm text-neutral-400">总分范围：0-750分</p>
                  </div>
                  <!-- 位次 -->
                  <div>
                    <label class="block text-sm font-medium text-neutral mb-2">位次</label>
                    <el-input-number min="1" name="ranking" placeholder="请输入您的省内位次" type="number"
                      v-model="personalForm.wc" :disabled="personalForm.remainEditNum <= 0" class="input-tall44px" />
                    <p class="mt-2 text-sm text-neutral-400">请输入省内排名位次</p>
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
                <el-input v-model="seetingpwdForm.phone" type="tel" placeholder="请输入手机号码"
                  style="height: 48px; line-height: 48px;">
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
      <!-- 我的收藏 -->
      <div v-if="selectedNavItem === 'my-collections'" class="w-full md:w-3/4">
        <div class="bg-white rounded-xl shadow-md overflow-hidden">
          <!-- 表单标题区 -->
          <div class="gradient-border background-gradient p-6">
            <div class="flex items-center">
              <h1 class="text-2xl font-bold text-white">我的收藏</h1>
            </div>
            <p class="text-white text-opacity-80 mt-2">
              查看您的收藏
            </p>
          </div>
          <!-- 密码设置表单 -->
          <div class="p-6">
            <el-radio-group v-if="myChioesGroupQueryState === 'initQuery'" v-model="ccdm"
              @change="getMyChioesGroupQuery">
              <el-radio-button label="全部" :value="99" />
              <el-radio-button label="本科" :value="1" />
              <el-radio-button label="专科" :value="2" />
            </el-radio-group>
            <el-button v-if="myChioesGroupQueryState !== 'initQuery'" :icon="ArrowLeft"
              @click="myChioesGroupQueryState = 'initQuery'">
              返回
            </el-button>
            <el-table v-if="myChioesGroupQueryState === 'initQuery'" :loading="myChioesGroupQueryLoading"
              :data="myChioesGroupQueryList" border style="width: 100%; margin-top: 20px;">
              <el-table-column prop="chGroupName" label="我的收藏组名称" />
              <el-table-column prop="addNum" label="已经收藏数量" width="120" />
              <el-table-column prop="maxNum" label="最大收藏数量" width="120" />
              <el-table-column label="操作" width="130">
                <template #default="scope">
                  <el-button text type="primary" size="small" @click="handleViewGroup1(scope.row)">查看1</el-button>
                  <el-button text type="primary" size="small" @click="handleViewGroup2(scope.row)"
                    style="margin-left: 0 !important;">查看2</el-button>
                </template>
              </el-table-column>
            </el-table>
            <!-- 专业模式查询结果表格 -->
            <el-table v-if="myChioesGroupQueryState === 'zyQuery' && tableData.length > 0" v-loading="false"
              :data="tableData" @span-method="objectSpanMethod" stripe border size="small" class="custom-table"
              style="width: 100%; margin-top: 20px;">
              <!-- 选择列 -->
              <el-table-column type="selection" width="40" align="center"></el-table-column>
              <!-- 招生院校列 -->
              <el-table-column prop="schoolName" label="招生院校" min-width="180" align="left">
                <template #default="scope">
                  <div class="font-medium yxmc">
                    {{ scope.row.yxmc }}
                    <span v-if="scope.row.lqdcstr.includes('稳')" class="lqdcstr bg2">{{ scope.row.lqdcstr }}</span>
                    <span v-else-if="scope.row.lqdcstr.includes('冲')" class="lqdcstr bg1">{{ scope.row.lqdcstr
                    }}</span>
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
              <el-table-column label="操作" width="80" align="center" fixed="right">
                <template #default="scope">
                  <el-button text type="danger" size="small" @click="zyHandleDelete(scope.row)">
                    删除
                  </el-button>
                </template>
              </el-table-column>
            </el-table>
            <!-- 专业组模式查询结果表格 -->
            <el-table v-if="myChioesGroupQueryState === 'zyGroupQuery' && tableData.length > 0" v-loading="false"
              :data="tableData" @span-method="objectSpanMethod" stripe border size="small" class="custom-table"
              style="width: 100%; margin-top: 20px;">
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
                    <span v-else-if="scope.row.lqdcstr.includes('冲')" class="lqdcstr bg1">{{ scope.row.lqdcstr
                    }}</span>
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
              <el-table-column label="填报操作" width="80" align="center" fixed="right">
                <template #default="scope">
                  <el-button text type="danger" size="small" @click="zyGroupHandleDelete(scope.row)">
                    删除
                  </el-button>
                </template>
              </el-table-column>
            </el-table>
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
</style>

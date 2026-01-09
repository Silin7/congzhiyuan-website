<script setup lang="ts">
import { onMounted, ref } from 'vue'
import * as api from '@/api/interfaceapi'
import { ElMessage } from 'element-plus'

onMounted(() => {
  getMyuserInfoQuery()
})

const personalInfo = ref<any>({})
function getMyuserInfoQuery() {
  api.myuserInfoQueryApi({
    token: window.localStorage.getItem('token') || ''
  }).then(res => {
    personalInfo.value = res.data || {}
    selectedSubjects.value = personalInfo.value.xuankeStr.split(',') || []
  })
}

// 声明响应式变量
// 选中的导航项 - 可选值：'basic-info', 'seeting-password', 'change-password', 'my-collections'
const selectedNavItem = ref('basic-info')
const handleNavItemClick = (navItem: string) => {
  selectedNavItem.value = navItem
  console.log(`选择了导航项: ${navItem}`)
  // 这里可以添加页面切换或内容加载逻辑
}

// 选科信息
const selectedSubjects = ref<string[]>([])
const handleSubjectClick = (subject: string) => {
  // 切换科目选中状态
  const index = selectedSubjects.value.indexOf(subject)
  if (index > -1) {
    selectedSubjects.value.splice(index, 1)
  } else {
    selectedSubjects.value.push(subject)
  }
  console.log(`选科变化: 当前选中 ${selectedSubjects.value.join(', ')}`)
}

// 设置密码
const seetingpwdForm = ref({
  phone: '',
  code: '',
  newPass: '',
  confirmPass: '',
})
function handlePasswordSubmit() {
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

  api.passResetApi({
    token: window.localStorage.getItem('token') || '',
    newPass: seetingpwdForm.value.newPass,
    vfCode: seetingpwdForm.value.code,
  }).then(res => {
    console.log(res);
    ElMessage.success('密码设置成功')
    // 清空密码输入框
    seetingpwdForm.value.phone = ''
    seetingpwdForm.value.code = ''
    seetingpwdForm.value.newPass = ''
    seetingpwdForm.value.confirmPass = ''
  })
}

// 发送验证码
const sendCode = () => {
  if (!seetingpwdForm.value.phone) {
    ElMessage.warning('请输入手机号码')
    return
  }
  if (!/^(?:(?:\+|00)86)?1[3-9]\d{9}$/.test(seetingpwdForm.value.phone)) {
    ElMessage.warning('请输入正确的手机号码')
    return
  }
  api.authcodeApi({
    phone: seetingpwdForm.value.phone,
    type: 1
  }).then(res => {
    console.log(res)
    ElMessage.success(`验证码已发送到 ${seetingpwdForm.value.phone}`)
  })
}

const changePasswordForm = ref({
  oldPass: '',
  newPass: '',
  confirmPass: '',
})
function handleChangePasswordSubmit() {
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
  api.passModiApi({
    token: window.localStorage.getItem('token') || '',
    oldPass: changePasswordForm.value.oldPass,
    newPass: changePasswordForm.value.newPass,
  }).then(res => {
    console.log(res);
    ElMessage.success('密码修改成功')
    // 清空密码输入框
    changePasswordForm.value.oldPass = ''
    changePasswordForm.value.newPass = ''
    changePasswordForm.value.confirmPass = ''
  })
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
              <p class="text-sm text-neutral-400">山东(zw)</p>
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
                    <div class="relative">
                      <input
                        class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent transition"
                        name="mobile" pattern="1[0-9]{10}" :required="true" type="tel" value="13800138000(zw)" />
                      <div class="absolute top-1/2 transform -translate-y-1/2 right-4">
                        <span class="text-accent">已验证</span>
                      </div>
                    </div>
                    <p class="mt-2 text-sm text-neutral-400">用于接收志愿填报提醒和系统通知</p>
                  </div>
                  <!-- 昵称 -->
                  <div>
                    <label class="block text-sm font-medium text-neutral mb-2">昵称</label>
                    <div class="flex">
                      <input
                        class="flex-grow px-4 py-3 border border-gray-300 rounded-l-lg focus:ring-2 focus:ring-primary focus:border-transparent transition"
                        maxlength="16" name="nickname" :required="true" type="text"
                        :value="personalInfo.userName || ''" />
                      <button
                        class="px-4 bg-gray-100 border-y border-r border-gray-300 rounded-r-lg text-neutral-600 hover:bg-gray-200">
                        <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em"
                          viewBox="0 0 32 32" data-icon="carbon:edit" class="iconify iconify--carbon">
                          <path fill="currentColor"
                            d="M2 26h28v2H2zM25.4 9c.8-.8.8-2 0-2.8l-3.6-3.6c-.8-.8-2-.8-2.8 0l-15 15V24h6.4zm-5-5L24 7.6l-3 3L17.4 7zM6 22v-3.6l10-10l3.6 3.6l-10 10z">
                          </path>
                        </svg>
                      </button>
                    </div>
                    <p class="mt-2 text-sm text-neutral-400">系统中显示的名称</p>
                  </div>
                </div>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                  <!-- 性别 -->
                  <div>
                    <label class="block text-sm font-medium text-neutral mb-2">性别(zw)</label>
                    <div class="flex space-x-6">
                      <label class="flex items-center">
                        <input class="h-4 w-4 text-primary border-gray-300 focus:ring-primary" name="gender"
                          type="radio" value="male" />
                        <span class="ml-2 text-neutral">男</span>
                      </label>
                      <label class="flex items-center">
                        <input class="h-4 w-4 text-primary border-gray-300 focus:ring-primary" name="gender"
                          type="radio" value="female" />
                        <span class="ml-2 text-neutral">女</span>
                      </label>
                    </div>
                  </div>
                  <!-- 省份 -->
                  <div>
                    <label class="block text-sm font-medium text-neutral mb-2">所在省份</label>
                    <select
                      class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent transition"
                      name="province">
                      <option value="北京">北京</option>
                      <option value="天津">天津</option>
                      <option value="河北">河北</option>
                      <option value="山西">山西</option>
                      <option value="内蒙古">内蒙古</option>
                      <option value="辽宁">辽宁</option>
                      <option value="吉林">吉林</option>
                      <option value="黑龙江">黑龙江</option>
                      <option value="上海">上海</option>
                      <option value="江苏">江苏</option>
                      <option value="浙江">浙江</option>
                      <option value="安徽">安徽</option>
                      <option value="福建">福建</option>
                      <option value="江西">江西</option>
                      <option value="山东">山东</option>
                      <option value="河南">河南</option>
                      <option value="湖北">湖北</option>
                      <option value="湖南">湖南</option>
                      <option value="广东">广东</option>
                      <option value="广西">广西</option>
                      <option value="海南">海南</option>
                      <option value="重庆">重庆</option>
                      <option value="四川">四川</option>
                      <option value="贵州">贵州</option>
                      <option value="云南">云南</option>
                      <option value="西藏">西藏</option>
                      <option value="陕西">陕西</option>
                      <option value="甘肃">甘肃</option>
                      <option value="青海">青海</option>
                      <option value="宁夏">宁夏</option>
                      <option value="新疆">新疆</option>
                    </select>
                  </div>
                </div>
                <!-- 选科信息 -->
                <div>
                  <label class="block text-sm font-medium text-neutral mb-3">选科信息</label>
                  <div class="flex flex-wrap gap-3">
                    <label @click.stop="handleSubjectClick('物理')" :class="[
                      'subject-tag px-4 py-2 border-2 border-gray-300 rounded-full cursor-pointer transition duration-200 hover:border-primary hover:bg-blue-50',
                      selectedSubjects.includes('物理')
                        ? 'active'
                        : '',
                    ]">
                      <span class="text-neutral font-medium">物理</span>
                    </label>
                    <label @click.stop="handleSubjectClick('化学')" :class="[
                      'subject-tag px-4 py-2 border-2 border-gray-300 rounded-full cursor-pointer transition duration-200 hover:border-primary hover:bg-blue-50',
                      selectedSubjects.includes('化学')
                        ? 'active'
                        : '',
                    ]">
                      <span class="text-neutral font-medium">化学</span>
                    </label>
                    <label @click.stop="handleSubjectClick('生物')" :class="[
                      'subject-tag px-4 py-2 border-2 border-gray-300 rounded-full cursor-pointer transition duration-200 hover:border-primary hover:bg-blue-50',
                      selectedSubjects.includes('生物')
                        ? 'active'
                        : '',
                    ]">
                      <span class="text-neutral font-medium">生物</span>
                    </label>
                    <label @click.stop="handleSubjectClick('政治')" :class="[
                      'subject-tag px-4 py-2 border-2 border-gray-300 rounded-full cursor-pointer transition duration-200 hover:border-primary hover:bg-blue-50',
                      selectedSubjects.includes('政治')
                        ? 'active'
                        : '',
                    ]">
                      <span class="text-neutral font-medium">政治</span>
                    </label>
                    <label @click.stop="handleSubjectClick('历史')" :class="[
                      'subject-tag px-4 py-2 border-2 border-gray-300 rounded-full cursor-pointer transition duration-200 hover:border-primary hover:bg-blue-50',
                      selectedSubjects.includes('历史')
                        ? 'active'
                        : '',
                    ]">
                      <span class="text-neutral font-medium">历史</span>
                    </label>
                    <label @click.stop="handleSubjectClick('地理')" :class="[
                      'subject-tag px-4 py-2 border-2 border-gray-300 rounded-full cursor-pointer transition duration-200 hover:border-primary hover:bg-blue-50',
                      selectedSubjects.includes('地理')
                        ? 'active'
                        : '',
                    ]">
                      <span class="text-neutral font-medium">地理</span>
                    </label>
                  </div>
                  <p class="mt-2 text-sm text-neutral-400">请选择高考选科科目</p>
                </div>
                <!-- 分数和位次 -->
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                  <!-- 高考分数 -->
                  <div>
                    <label class="block text-sm font-medium text-neutral mb-2">高考分数</label>
                    <input
                      class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent transition"
                      max="750" min="0" name="score" placeholder="请输入您的高考总分" type="number"
                      :value="personalInfo.cj || ''" />
                    <p class="mt-2 text-sm text-neutral-400">总分范围：0-750分</p>
                  </div>
                  <!-- 位次 -->
                  <div>
                    <label class="block text-sm font-medium text-neutral mb-2">位次</label>
                    <input
                      class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent transition"
                      min="1" name="ranking" placeholder="请输入您的省内位次" type="number" :value="personalInfo.wc || ''" />
                    <p class="mt-2 text-sm text-neutral-400">请输入省内排名位次</p>
                  </div>
                </div>
              </div>
              <!-- 表单操作区 -->
              <div class="border-t mt-8 pt-8 flex justify-end space-x-4">
                <button class="px-8 py-3 border border-gray-300 rounded-lg text-neutral hover:bg-gray-50 transition"
                  type="button">
                  取消
                </button>
                <button
                  class="px-8 py-3 background-gradient bg-gradient-to-r from-primary to-secondary rounded-lg text-white font-medium hover:opacity-90 transition"
                  type="submit">
                  保存个人信息
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
      <!-- 设置密码 -->
      <div v-if="selectedNavItem === 'seeting-password'" class="w-full md:w-3/4">
        <div class="bg-white rounded-xl shadow-md overflow-hidden">
          <!-- 表单标题区 -->
          <div class="bg-gradient-to-r from-primary to-secondary px-6 py-4">
            <h2 class="text-2xl font-bold text-white">设置密码</h2>
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
              <button
                class="px-8 py-3 background-gradient bg-gradient-to-r from-primary to-secondary rounded-lg text-white font-medium hover:opacity-90 transition"
                type="submit" @click="handlePasswordSubmit">
                保存密码
              </button>
            </div>
          </div>
        </div>
      </div>
      <!-- 修改密码 -->
      <div v-if="selectedNavItem === 'change-password'" class="w-full md:w-3/4">
        <div class="bg-white rounded-xl shadow-md overflow-hidden">
          <!-- 表单标题区 -->
          <div class="bg-gradient-to-r from-primary to-secondary px-6 py-4">
            <h2 class="text-2xl font-bold text-white">修改密码</h2>
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
              <button
                class="px-8 py-3 background-gradient bg-gradient-to-r from-primary to-secondary rounded-lg text-white font-medium hover:opacity-90 transition"
                type="submit" @click="handleChangePasswordSubmit">
                保存密码
              </button>
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
</style>

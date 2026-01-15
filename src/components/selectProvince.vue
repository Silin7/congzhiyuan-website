<script setup lang="ts">
import router from "@/router"
import { onMounted, ref } from "vue"
import { ElMessage } from "element-plus"
import * as api from '@/api/interfaceapi'

onMounted(() => {
  zyTypeRule()
})

const userInfo: any = ref()
function zyTypeRule() {
  if (localStorage.getItem('userInfo')) {
    userInfo.value = JSON.parse(localStorage.getItem('userInfo') as string)
  } else {
    userInfo.value = false
  }
  if (!userInfo.value) {
    return
  }
  // zyType:  1所在省份专业模式 2  所在省份专业组模式 0 如果用户没有初始填写省份信息，不知道那个专业模式
  if (!userInfo.value.zyType || userInfo.value.zyType == '0' || userInfo.value.ifProvSave == '0') {
    genListQueryList()
  } else if (userInfo.value.ifUserActive == '0') {
    ElMessage.warning('请完善成绩信息')
    router.push({
      path: '/personalInfo',
    })
  }
}

// 获取省份列表
const showProvModal = ref(false)
const provinceList = ref<any>([])
const provinceSelected = ref('')
const genListQueryList = async () => {
  const res: any = await api.userProvQueryApi()
  if (res) {
    showProvModal.value = true
    provinceList.value = res.data.Rs || []
  }
}

// 保存省份
const myUserPorvSave = async () => {
  if (!provinceSelected.value) {
    ElMessage.warning('请选择省份')
    return
  }
  const res: any = await api.myUserPorvSaveApi({
    provId: provinceSelected.value
  })
  if (res) {
    showProvModal.value = false
    if (userInfo.value.ifUserActive == '0') {
      ElMessage.warning('请完善成绩信息')
      router.push({
        path: '/personalInfo',
      })
    } else {
      ElMessage.success('操作成功')
    }
  }
}
</script>

<template>
  <div>
    <!-- 选择省份弹窗 -->
    <el-dialog v-model="showProvModal" width="600" :show-close="false" :close-on-click-modal="false"
      :close-on-press-escape="false">
      <template #header>
        <h2 class="text-2xl font-bold text-gray-800">
          请先选择省份
        </h2>
      </template>
      <div class="flex flex-wrap gap-3 province-dialog">
        <label v-for="(item, index) in provinceList" :key="index" @click="provinceSelected = item.id" :class="[
          'subject-tag px-4 py-2 border-2 border-gray-300 rounded-full cursor-pointer transition duration-200 hover:border-primary hover:bg-blue-50',
          provinceSelected === item.id
            ? 'active'
            : '',
        ]">
          <span class="text-neutral font-medium">{{ item.province }}</span>
        </label>
      </div>
      <template #footer>
        <el-button type="primary" @click="myUserPorvSave">
          保存
        </el-button>
      </template>
    </el-dialog>
  </div>
</template>

<style lang="scss" scoped></style>
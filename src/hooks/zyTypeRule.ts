import router from "@/router"
import { ElMessage } from "element-plus"

function zyTypeRule() {
  const userInfo = JSON.parse(localStorage.getItem('userInfo') || '{}')
  if (userInfo?.zyType == '0') {
    router.push({
      path: '/personalInfo',
    })
    ElMessage.warning({
      message: '请先完善个人信息',
      type: 'warning',
    })
  }
}

export default zyTypeRule
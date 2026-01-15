import router from "@/router"
import { ElMessage } from "element-plus"

// zyType:  1所在省份专业模式 2  所在省份专业组模式 0 如果用户没有初始填写省份信息，不知道那个专业模式
function zyTypeRule() {
  const userInfo = JSON.parse(localStorage.getItem('userInfo') || '{}')
  if (userInfo?.zyType == '0' || userInfo?.zyType === null) {
    ElMessage.warning('请先完善个人信息')
    router.push({
      path: '/personalInfo',
    })
  } else if (userInfo?.ifUserActive == '0') {
    ElMessage.warning('请完善成绩信息')
    router.push({
      path: '/personalInfo',
    })
  }
}

export default zyTypeRule
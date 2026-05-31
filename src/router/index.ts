import { createRouter, createWebHashHistory , type RouteRecordRaw } from 'vue-router'
import useHeaderStore from '@/store/modules/header'
import { ElMessage } from 'element-plus'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'home',
    component: () => import('@/views/home.vue'),
    meta: {
      title: '系统首页',
      stcode: 'home',
      hashead: true,
      hasfoot: true,
    },
  },
  {
    path: '/volunteerApply',
    name: 'volunteerApply',
    component: () => import('@/views/volunteerApply.vue'),
    meta: {
      title: '志愿填报',
      stcode: 'volunteerApply',
      hashead: true,
      hasfoot: true,
    },
  },
  {
    path: '/schoolSearch',
    name: 'schoolSearch',
    component: () => import('@/views/schoolSearch.vue'),
    meta: {
      title: '院校查询',
      stcode: 'schoolSearch',
      hashead: true,
      hasfoot: true,
    },
  },
  {
    path: '/schoolDetail',
    name: 'schoolDetail',
    component: () => import('@/views/schoolDetail.vue'),
    meta: {
      title: '院校详情',
      stcode: 'schoolDetail',
      hashead: true,
      hasfoot: true,
    },
  },
  {
    path: '/majorAnalysis',
    name: 'majorAnalysis',
    component: () => import('@/views/majorAnalysis.vue'),
    meta: {
      title: '专业解析',
      stcode: 'majorAnalysis',
      hashead: true,
      hasfoot: true,
    },
  },
  {
    path: '/majorDetail',
    name: 'majorDetail',
    component: () => import('@/views/majorDetail.vue'),
    meta: {
      title: '专业解析',
      stcode: 'majorDetail',
      hashead: true,
      hasfoot: true,
    },
  },
  {
    path: '/aiAssessmentList',
    name: 'aiAssessmentList',
    component: () => import('@/views/aiAssessmentList.vue'),
    meta: {
      title: 'AI测评',
      stcode: 'aiAssessmentList',
      hashead: true,
      hasfoot: true,
    },
  },
  {
    path: '/aiAssessmentDetail',
    name: 'aiAssessmentDetail',
    component: () => import('@/views/aiAssessmentDetail.vue'),
    meta: {
      title: 'AI测评详情',
      stcode: 'aiAssessmentDetail',
      hashead: true,
      hasfoot: true,
    },
  },
  {
    path: '/aiAssessmentStart',
    name: 'aiAssessmentStart',
    component: () => import('@/views/aiAssessmentStart.vue'),
    meta: {
      title: 'AI测评开始',
      stcode: 'aiAssessmentStart',
      hashead: true,
      hasfoot: true,
    },
  },
  {
    path: '/aiAssessmentView',
    name: 'aiAssessmentView',
    component: () => import('@/views/aiAssessmentView.vue'),
    meta: {
      title: 'AI测评开始',
      stcode: 'aiAssessmentView',
      hashead: true,
      hasfoot: true,
    },
  },
  {
    path: '/personalInfo',
    name: 'personalInfo',
    component: () => import('@/views/personalInfo.vue'),
    meta: {
      title: '个人信息',
      stcode: 'personalInfo',
      hashead: true,
      hasfoot: true,
    },
  },
  {
    path: '/chargingInfomating',
    name: 'chargingInfomating',
    component: () => import('@/views/chargingInfomating.vue'),
    meta: {
      title: '升级VIP',
      stcode: 'chargingInfomating',
      hashead: true,
      hasfoot: true,
    },
  },
  {
    path: '/:pathMatch(.*)*',
    redirect: '/',
  }
]

const router = createRouter({
  history: createWebHashHistory (),
  routes,
})

router.beforeEach((to, from, next) => {
  // 根据路由元信息设置文档标题
  window.document.title = `聪志愿AI${to.meta.title ? '-' + to.meta.title : ''}`

  // if (useHeaderStore) {
  //   const headerStore = useHeaderStore()
  //   headerStore.setSelectedTab(to.meta.stcode as string)
  //   window.localStorage.setItem('selectedTab', to.meta.stcode as string)
  //   window.localStorage.setItem('selectedName', to.path as string)
  // }


  // const userInfo = JSON.parse(window.localStorage.getItem('userInfo') || '{}')
  // if (userInfo.zyType === '0') {
  //   ElMessage.warning('请先完善个人信息')
  //   router.push('/personalInfo')
  // }

  next()

})

export default router

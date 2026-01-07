import { createRouter, createWebHistory, type RouteRecordRaw } from 'vue-router'
import useHeaderStore from '@/store/modules/header'

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
    path: '/aiAssessment',
    name: 'aiAssessment',
    component: () => import('@/views/aiAssessment.vue'),
    meta: {
      title: 'AI测评',
      stcode: 'aiAssessment',
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
    path: '/:pathMatch(.*)*',
    redirect: '/',
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

router.beforeEach((to, from, next) => {
  // 根据路由元信息设置文档标题
  window.document.title = `聪志愿AI${to.meta.title ? '-' + to.meta.title : ''}`

  if (useHeaderStore) {
    const headerStore = useHeaderStore()
    headerStore.setSelectedTab(to.meta.stcode as string)
    window.localStorage.setItem('selectedTab', to.meta.stcode as string)
    window.localStorage.setItem('selectedName', to.path as string)
  }

  next()
})

export default router

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
  window.document.title = `科睿易晶官方网站${to.meta.title ? '-' + to.meta.title : ''}`

  if (useHeaderStore) {
    const headerStore = useHeaderStore()
    headerStore.setSelectedTab(to.meta.stcode as string)
    window.localStorage.setItem('selectedTab', to.meta.stcode as string)
    window.localStorage.setItem('selectedName', to.path as string)
  }

  next()
})

export default router

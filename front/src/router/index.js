import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ExamSettingsPage from '@/components/ExamSetup.vue';
import SubmittedInfoPage from '@/components/SubmittedInfoPage.vue';

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/',
    name: 'ExamSettingsPage',
    component: ExamSettingsPage,
  },
  {
    path: '/submitted',
    name: 'SubmittedInfoPage',
    component: SubmittedInfoPage,
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router

import { createRouter, createWebHistory } from 'vue-router'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  linkActiveClass: "active-link ",
  linkExactActiveClass: "text-grey-500",
  routes: [
    {
      path: "",
      redirect: "home",
      component: () => import('@/views/pages/IndexView.vue'),
      children: [
          {
            path: 'home',
            name: 'home',
            component: () => import('@/views/pages/HomeView.vue')
          },
          {
            path: '/items',
            name: 'items',
            component: () => import('@/views/pages/ItemsView.vue')
          },
      ]
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('@/views/LoginView.vue')
    },
  ]
})

export default router

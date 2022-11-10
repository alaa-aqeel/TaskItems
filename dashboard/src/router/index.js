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
      meta: {
        requiredAuth: true
      },
      children: [
          {
            path: 'home',
            name: 'home',
            component: () => import('@/views/pages/HomeView.vue'),
            meta: {
              requiredAuth: true
            },
          },
          {
            path: '/items',
            name: 'items',
            component: () => import('@/views/pages/ItemsView.vue'),
            meta: {
              requiredAuth: true
            },
          },
      ]
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('@/views/LoginView.vue'),
      meta: { guest: true },
    },
  ]
})

export default router

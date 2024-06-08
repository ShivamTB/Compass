import { RouteRecordRaw } from 'vue-router';

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    component: () => import('layouts/OuterLayout.vue'),
    children: [
      { path: '/', name: 'landing', component: () => import('pages/landing/LandingPage.vue') },
      { path: '/register', name: 'register', component: () => import('pages/register/RegisterPage.vue') },
      { path: '/login', name: 'login', component: () => import('pages/login/LoginPage.vue') },
    ],
  },
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '/dashboard', name: 'dashboard', component: () => import('pages/dashboard/DashboardPage.vue') },
      { path: '/profile', name: 'profile', component: () => import('pages/profile/ProfilePage.vue') },
    ],
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue'),
  },
];

export default routes;

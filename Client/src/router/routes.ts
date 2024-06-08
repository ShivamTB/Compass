import { RouteRecordRaw } from 'vue-router';

const routes: RouteRecordRaw[] = [
  {
    path: '/dashboard',
    component: () => import('layouts/MainLayout.vue'),
    children: [{ path: '', component: () => import('pages/IndexPage.vue') }],
  },
  {
    path: '/',
    component: () => import('layouts/OuterLayout.vue'),
    children: [
      { path: '/', name: 'landing', component: () => import('pages/landing/LandingPage.vue') },
      { path: 'register', name: 'register', component: () => import('pages/register/RegisterPage.vue') },
      { path: 'login', name: 'login', component: () => import('pages/login/LoginPage.vue') },
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

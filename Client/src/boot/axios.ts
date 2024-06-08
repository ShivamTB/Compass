import { boot } from 'quasar/wrappers';
import axios, { AxiosInstance } from 'axios';

declare module '@vue/runtime-core' {
  interface ComponentCustomProperties {
    $axios: AxiosInstance;
    $api: AxiosInstance;
  }
}

// Be careful when using SSR for cross-request state pollution
// due to creating a Singleton instance here;
// If any client changes this (global) instance, it might be a
// good idea to move this instance creation inside of the
// "export default () => {}" function below (which runs individually
// for each client)

const baseURL = process.env.VUE_API_URL ? process.env.VUE_API_URL : 'http://192.168.101.195:8000';

// Be careful when using SSR for cross-request state pollution
// due to creating a Singleton instance here;
// If any client changes this (global) instance, it might be a
// good idea to move this instance creation inside of the
// "export default () => {}" function below (which runs individually
// for each client)


const api = axios.create({
  xsrfCookieName: 'csrftoken',
  xsrfHeaderName: 'X-CSRFTOKEN',
  baseURL: baseURL,
  headers: {
    // 'Content-Type': 'application/json',
    // 'Access-Control-Allow-Origin': '*',
    // 'Access-Control-Allow-Methods': 'GET,PUT,POST,DELETE,PATCH,OPTIONS',
    // 'Access-Control-Allow-Headers': 'Content-Type, Authorization'


  },
});


api.interceptors.request.use(async (req: any) => {
  const { method } = req

  req.withCredentials = true
  if (method === 'post') {
    const token = await getCSRFToken()
    req.headers['X-CSRFToken'] = token
  }
  return req
})


const getCSRFToken = async () => {
  const response = await api.get('/csrf')
  const token = response.data.csrfToken
  localStorage.setItem('token', token)
  return token
}

api.interceptors.response.use((res: any) => {
  // const { method } = res
  // if (method === 'post') {
  //   const token = localStorage.getItem('token')
  //   res.body['csrfmiddlewaretoken'] = token
  // }
  return res
}, error => {
  if (error?.response?.status === 401) {
    localStorage.removeItem('token')
    window.location.href = '/login'
  }
  return Promise.reject(error)
})



export default boot(({ app }) => {
  // for use inside Vue files (Options API) through this.$axios and this.$api

  app.config.globalProperties.$axios = axios;
  // ^ ^ ^ this will allow you to use this.$axios (for Vue Options API form)
  //       so you won't necessarily have to import axios in each vue file

  app.config.globalProperties.$api = api;
  // ^ ^ ^ this will allow you to use this.$api (for Vue Options API form)
  //       so you can easily perform requests against your app's API
});

export { api };

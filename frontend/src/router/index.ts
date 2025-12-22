import { createRouter, createWebHistory } from 'vue-router'
import ProductsView from '@/views/ProductsView.vue'

const routes = [
  {
    path: '/',
    name: 'products',
    component: ProductsView,
  },
]

export default createRouter({
  history: createWebHistory(),
  routes,
})

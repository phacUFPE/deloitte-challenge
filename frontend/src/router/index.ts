import { createRouter, createWebHistory } from 'vue-router'
import ProductsView from '@/views/ProductsView.vue'

const routes = [
  {
    path: '/',
    name: 'products',
    component: ProductsView,
  },
  {
    path: '/items/:id',
    name: 'item-details',
    component: ProductsView,
    props: true,
  },
]

export default createRouter({
  history: createWebHistory(),
  routes,
})

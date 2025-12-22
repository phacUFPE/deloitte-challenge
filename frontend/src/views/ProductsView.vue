<script setup lang="ts">
import { ref, watch, onMounted, onBeforeUnmount } from 'vue'
import { useRoute, useRouter } from 'vue-router'

import { useFetch } from '@/composables/useFetch'
import ProductDialog from '@/components/ProductDialog.vue'
import ProductFilter from '@/components/ProductFilter.vue'
import SimpleProductCard from '@/components/SimpleProductCard.vue'
import type { Product } from '@/types/Product'
import type { ProductFilter as ProductFilterType } from '@/types/ProductFilter'
import type { PaginatedResponse } from '@/types/PaginatedResponse'

const route = useRoute()
const router = useRouter()

const products = ref<Product[]>([])
const selectedProduct = ref<Product | null>(null)
const dialogOpen = ref(false)
const next = ref<string | null>(null)

const filters = ref<ProductFilterType>({
  search: (route.query.search as string) || '',
  status: (route.query.status as string) || '',
})

const page = ref(route.query.page ? Number(route.query.page) : 1)

const url = ref('/products/')
const { data, loading, params } = useFetch<PaginatedResponse<Product>>(url)

const sentinel = ref<HTMLElement | null>(null)

function updateParams() {
  const allParams = { page: page.value, ...filters.value }

  params.value = Object.fromEntries(
    Object.entries(allParams).filter(([_, v]) => v !== '' && v != null)
  ) as Record<string, string>
}

watch(
  [filters, page],
  () => {
    const query = Object.fromEntries(
      Object.entries({
        page: page.value,
        search: filters.value.search,
        status: filters.value.status,
      }).filter(([_, v]) => v !== '' && v != null)
    )

    updateParams()

    router.replace({ query })
  },
  { deep: true }
)

watch(page, updateParams)

watch(data, (newData) => {
  if (!newData || !newData.results) return
  next.value = newData.next
  products.value.push(...newData.results)
})

function onFiltersUpdate(val: typeof filters.value) {
  products.value = []
  page.value = 1
  next.value = null
  filters.value = val
}

function openDialog(product: Product) {
  selectedProduct.value = product
  dialogOpen.value = true
  router.push(`/items/${product.id}`)
}

function closeDialog() {
  dialogOpen.value = false
  selectedProduct.value = null
  router.back()
}

let observer: IntersectionObserver | null = null

onMounted(() => {
  observer = new IntersectionObserver(
    ([entry]) => {
      if (entry?.isIntersecting && next.value && !loading.value) {
        page.value += 1
      }
    },
    {
      root: null,
      rootMargin: '100px',
      threshold: 0.1,
    }
  )

  if (sentinel.value) observer.observe(sentinel.value)
})

onBeforeUnmount(() => {
  if (observer && sentinel.value) {
    observer.unobserve(sentinel.value)
  }
})
</script>

<template>
  <v-container>
    <ProductFilter :initialFilters="filters" @update:filters="onFiltersUpdate" />

    <v-row class="justify-center">
      <h2 v-if="!products.length && !loading">No Products.</h2>
      <v-col v-for="product in products" :key="product.id" cols="12" md="4">
        <SimpleProductCard :product="product" @click="openDialog(product)" />
      </v-col>

      <v-col cols="12" md="4" v-for="n in 5" :key="n">
        <v-skeleton-loader v-if="loading" type="card" />
      </v-col>
    </v-row>

    <div ref="sentinel" style="height: 1px"></div>

    <ProductDialog
      v-if="selectedProduct"
      :open="dialogOpen"
      :product="selectedProduct"
      @close="closeDialog"
    />
  </v-container>
</template>

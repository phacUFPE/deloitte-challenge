<script setup lang="ts">
import { ref, watch, onMounted, onBeforeUnmount } from 'vue'
import { useRoute, useRouter } from 'vue-router'

import { useFetch } from '@/composables/useFetch'
import ProductFilter from '@/components/ProductFilter.vue'
import SimpleProductCard from '@/components/SimpleProductCard.vue'
import type { Product } from '@/types/Product'
import type { ProductFilter as ProductFilterType } from '@/types/ProductFilter'

const route = useRoute()
const router = useRouter()

const products = ref<Product[]>([])
const next = ref<string | null>(null)

const filters = ref<ProductFilterType>({
  search: (route.query.search as string) || '',
  status: (route.query.status as string) || '',
})

const page = ref(route.query.page ? Number(route.query.page) : 1)

const url = ref('/products/')
const { data, loading, error, params } = useFetch<PaginatedResponse<Product>>(url)

const sentinel = ref<HTMLElement | null>(null)

function updateParams() {
  const allParams = { page: page.value, ...filters.value }

  params.value = Object.fromEntries(
    Object.entries(allParams?.value || allParams).filter(([, v]) => v !== '' && v != null)
  )
}

watch(
  [filters, page],
  () => {
    console.log(filters.value)
    const query = Object.fromEntries(
      Object.entries({
        page: page.value,
        search: filters.value.search,
        status: filters.value.status,
      }).filter(([, v]) => v !== '' && v != null)
    )

    updateParams()

    router.replace({ query })
  },
  { deep: true }
)

watch(page, updateParams)

watch(data, (newData) => {
  if (!newData || !newData.results) return
  products.value.push(...newData.results)
  next.value = newData.next
})

function onFiltersUpdate(val: typeof filters.value) {
  products.value = []
  page.value = 1
  next.value = null
  filters.value = val
}

let observer: IntersectionObserver | null = null

onMounted(() => {
  observer = new IntersectionObserver(
    (entries) => {
      const entry = entries[0]
      if (entry.isIntersecting && next.value && !loading.value) {
        page.value += 1
      }
    },
    {
      root: null,
      rootMargin: '0px',
      threshold: 1.0,
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

    <v-row>
      <v-col v-for="product in products" :key="product.id" cols="12" md="4">
        <SimpleProductCard :product="product" />
      </v-col>

      <div v-if="loading">
      <v-col
        cols="12" md="4"
        v-for="n in 3"
        :key="n"
      >
        <v-skeleton-loader type="card" />
      </v-col>
      </div>
    </v-row>

    <div ref="sentinel" style="height: 1px"></div>
  </v-container>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue'
import type { ProductFilter } from '@/types/ProductFilter'

const props = withDefaults(
  defineProps<{
    initialFilters?: ProductFilter
  }>(),
  {
    initialFilters: () => ({}),
  }
)

const emit = defineEmits<{
  (e: 'update:filters', filters: Record<string, string>): void
}>()

const search = ref(props.initialFilters.search ?? '')
const status = ref(props.initialFilters.status ?? '')

function debounce<T extends (...args: string[]) => void>(fn: T, delay = 400) {
  let timer: number | undefined

  return (...args: Parameters<T>) => {
    clearTimeout(timer)
    timer = window.setTimeout(() => {
      fn(...args)
    }, delay)
  }
}

const emitFilters = () => {
  emit('update:filters', {
    search: search.value,
    status: status.value,
  })
}

const emitSearchDebounced = debounce(emitFilters, 500)

watch(
  () => props.initialFilters,
  (newFilters) => {
    if (!newFilters) return
    search.value = newFilters.search ?? ''
    status.value = newFilters.status ?? ''
  },
  { deep: true }
)

watch(search, () => {
  emitSearchDebounced()
})

watch([status], () => {
  emitFilters()
})
</script>

<template>
  <v-row class="mb-4 justify-center" dense>
    <v-col cols="12" md="3">
      <v-text-field v-model="search" label="Search" clearable />
    </v-col>

    <v-col cols="12" md="3">
      <v-select
        v-model="status"
        :items="['', 'ACTIVE', 'INACTIVE', 'BLOCKED']"
        label="Status"
        clearable
      />
    </v-col>
  </v-row>
</template>

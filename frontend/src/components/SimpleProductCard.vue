<script setup lang="ts">
import { computed, defineProps } from 'vue'
import type { Product } from '@/types/Product'

const props = defineProps<{
  product: Product
}>()

const description = computed(() => props.product.description || 'No description')
</script>

<template>
  <v-card height="200px">
    <v-card-title>{{ props.product.title }}</v-card-title>
    <v-card-text>
      {{ description }}
    </v-card-text>
  </v-card>
</template>

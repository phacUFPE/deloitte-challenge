<script setup lang="ts">
import type { Product } from '@/types/Product'

defineProps<{
  open: boolean
  product: Product
}>()

const emit = defineEmits<{
  (e: 'close'): void
}>()

function close() {
  emit('close')
}
</script>

<template>
  <Teleport to="body">
    <div v-if="open" class="overlay" @click.self="close">
      <div class="dialog">
        <header class="header">
          <v-btn variant="text" icon="mdi-star-outline" />
          <h2>{{ product.title }}</h2>
          <button class="close" @click="close">✕</button>
        </header>

        <section class="content">
          <p><strong>Status:</strong> {{ product.status }}</p>
          <p><strong>Date:</strong> {{ product.date }}</p>
          <p><strong>Description:</strong></p>
          <p class="description">{{ product.description }}</p>
        </section>

        <footer class="footer">
          <button class="btn" @click="close">Close</button>
        </footer>
      </div>
    </div>
  </Teleport>
</template>

<style scoped>
.overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.55);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 999;
}

.dialog {
  width: 100%;
  max-width: 520px;
  background: #fff;
  border-radius: 10px;
  padding: 1.25rem;
  animation: fadeIn 0.2s ease;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.close {
  background: none;
  border: none;
  font-size: 1.25rem;
  cursor: pointer;
}

.content p {
  margin: 0.5rem 0;
}

.description {
  color: #555;
}

.footer {
  display: flex;
  justify-content: flex-end;
  margin-top: 1rem;
}

.btn {
  padding: 0.5rem 1rem;
  border-radius: 6px;
  border: none;
  cursor: pointer;
  background: #2c7be5;
  color: white;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: scale(0.96);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}
</style>

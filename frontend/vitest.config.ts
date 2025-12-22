import { defineConfig } from 'vitest/config'
import vue from '@vitejs/plugin-vue'
import path from 'node:path'

export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'src'),

      '\\.(css|scss|sass)$': path.resolve(
        __dirname,
        'tests/__mocks__/styleMock.ts',
      ),
      'vuetify/styles': path.resolve(
        __dirname,
        'tests/__mocks__/styleMock.ts',
      ),
      'vuetify/lib/components': path.resolve(
        __dirname,
        'tests/__mocks__/styleMock.ts',
      ),
    },
  },
  test: {
    environment: 'jsdom',
    setupFiles: ['./tests/setup.ts'],
  },
})

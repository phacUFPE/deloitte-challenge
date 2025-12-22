import { type Ref, ref, watch } from 'vue'
import { AxiosError, type AxiosRequestConfig } from 'axios'

import http from '@/api/http'

export function useFetch<T>(
  initialUrl: Ref<string>,
  initialParams: Record<string, string> = {},
  config?: AxiosRequestConfig
) {
  const url = ref(initialUrl)
  const params = ref({ ...initialParams })

  const data = ref<T | null>(null)
  const loading = ref(false)
  const error = ref<string | null>(null)

  const fetchData = async (overrideParams?: Record<string, string>) => {
    loading.value = true
    error.value = null

    await new Promise((resolve) => setTimeout(resolve, 2000))

    try {
      const response = await http.get<T>(url.value, {
        ...config,
        params: overrideParams ? { ...params.value, ...overrideParams } : params.value,
      })
      data.value = response.data
      return response.data
    } catch (err: unknown) {
      if (err instanceof AxiosError) {
        error.value = err?.message ?? 'Unknown error'
      } else {
        error.value = 'Unknown Error'
      }
      console.error(err)
    } finally {
      loading.value = false
    }
  }

  watch([url, params], () => fetchData(), { immediate: true, deep: true })

  return {
    data,
    loading,
    error,
    url,
    params,
    fetchData,
  }
}

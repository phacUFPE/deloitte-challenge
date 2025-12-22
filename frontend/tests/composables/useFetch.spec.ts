import { describe, it, expect, vi } from "vitest"
import { useFetch } from "@/composables/useFetch"
import http from "@/api/http"
import { AxiosError } from 'axios'
import { flushPromises } from '@vue/test-utils'


vi.mock("@/api/http")

vi.spyOn(http, 'get').mockRejectedValue(
  new AxiosError('Network error')
)

describe("useFetch", () => {
  it("fetches data successfully", async () => {
    ;(http.get as any).mockResolvedValue({
      data: { results: [{ id: 1, title: "Product" }] },
    })

    const { fetchData, data, loading, error } =
      useFetch<{ results: any[] }>("/products")

    const result = await fetchData()

    expect(loading.value).toBe(false)
    expect(error.value).toBeNull()
    expect(data.value?.results.length).toBe(1)
    expect(result?.results[0].title).toBe("Product")
  })

  it("handles error", async () => {
    ;(http.get as any).mockRejectedValue(new Error("Network error"))

    const { fetchData, error } = useFetch("/products")

    await fetchData()
    await flushPromises()

    expect(error.value).toBeTruthy()
  })
})

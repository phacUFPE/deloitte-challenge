import { mount } from "@vue/test-utils"
import { describe, it, expect } from "vitest"
import SimpleProductCard from "@/components/SimpleProductCard.vue"

describe("SimpleProductCard", () => {
  it("renders product data", () => {
    const wrapper = mount(SimpleProductCard, {
      props: {
        product: {
          id: 1,
          title: "Test Product",
          description: "Nice product",
        },
      },
    })

    expect(wrapper.text()).toContain("Test Product")
    expect(wrapper.text()).toContain("Nice product")
  })

  it("renders fallback description", () => {
    const wrapper = mount(SimpleProductCard, {
      props: {
        product: {
          id: 1,
          title: "Test Product",
        },
      },
    })

    expect(wrapper.text()).toContain("No description")
  })
})

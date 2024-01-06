<template>
  <input
      :value="modelValue"
      @change="changeInptut"
      type="text"
      name=""
      id=""
      placeholder="Поиск..."
  >
</template>

<script>
export default {
  props: {
    modelValue: {
      type: String,
    }
  },
  methods: {
    changeInptut(event) {
      this.$emit('update:modelValue', event.target.value)
    }
  }
}
</script>

<style lang="scss" scoped>

</style>
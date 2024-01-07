<template>
  <input
      name=""
      @change="changeInptut"
      :value="modelValue"
      :placeholder="placeholder"
      :type="type"
  >
</template>

<script>
export default {
  props: {
    modelValue: {
      type: String,
    },
    type: {
      type: String,
      default: 'text'
    },
    placeholder: {
      type: String,
      default: "Ввод"
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
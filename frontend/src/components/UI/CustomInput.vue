<template>
  <input
      name=""
      class="input"
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
.input {
  padding: var(--p-standart);
  border: 1px solid var(--c-gray);
  border-radius: var(--br-standart);
}
</style>
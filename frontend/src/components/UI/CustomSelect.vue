<template>
  <select
      :value="modelValue"
      @change="changeOption"
  >
    <option disabled selected hidden value="">{{ label }}</option>
    <option
        v-for="option in options"
        :key="option.id"
        :value="option.value">
      {{ option.name }}
    </option>
  </select>
</template>

<script>
export default {
  props: {
    label: {
      type: String,
    },
    modelValue: {
      type: String,
      required: true
    },
    options: {
      type: Array,
      required: true,
      default: () => []
    }
  },
  methods: {
    changeOption(event) {
      this.$emit('update:modelValue', event.target.value);
    }
  }
}
</script>

<style lang="scss" scoped>

</style>
<template>
  <transition name="fade" appear>
    <select
        class="select"
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
  </transition>
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
.select {
  border: 1px solid var(--c-gray);
  background: var(--c-orange);
  font-family: var(--f-familySecond);
  font-size: var(--f-size-22);

  padding: var(--p-standart);

  cursor: pointer;

  box-shadow: var(--bS-standart);
  border-radius: var(--br-standart);
}
</style>
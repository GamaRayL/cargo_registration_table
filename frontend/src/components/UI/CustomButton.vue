<template>
  <button
      class="button"
      :type="type"
  >
    <slot></slot>
  </button>
</template>

<script>
export default {
  props: {
    type: {
      type: String,
      default: 'button'
    }
  }
}
</script>

<style lang="scss" scoped>
.button {
  display: flex;
  align-self: center;
  justify-self: center;
  cursor: pointer;
}
</style>
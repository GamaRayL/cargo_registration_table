<template>
  <button
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

</style>
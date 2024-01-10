<template>
  <button :class="['button', {'button_contained': contained}]" :type="type">
    <span v-if="contained" :class="{'button__label': contained}">
      <slot></slot>
    </span>
    <slot v-else></slot>
  </button>
</template>

<script>
export default {
  props: {
    type: {
      type: String,
      default: 'button'
    },
    contained: {
      type: Boolean
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

  &_contained {
    color: var(--c-orange);
    background: var(--c-dark);

    font-size: var(--f-size-22);
    font-weight: var(--f-weight-bold);
    font-family: var(--f-familySecond);

    border: none;
    box-shadow: var(--bS-standart);
    border-radius: var(--br-standart);

    padding: 0 4px;

    &:active .button__label {
      transform: scale(0.8);
    }
  }

  &__label {
    transition: ease-in-out .1s;
  }
}
</style>
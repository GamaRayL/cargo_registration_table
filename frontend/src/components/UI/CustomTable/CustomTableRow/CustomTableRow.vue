<template>
  <tr>
    <td
        class="table__data"
        v-for="[key, value] of filteredEntries"
        :key="key"
    >
      <input
          class="table__input"
          :value="value"
          ref="inputRef"
          @change="updateInput(key, $event.target.value)"
          type="text"
      >
    </td>
  </tr>
</template>

<script>


export default {
  props: {
    item: {
      type: Object,
      required: true
    },
  },
  methods: {
    updateInput(key, newValue) {
      this.$store.commit('entry/updateFieldValue', {id: this.item.id, key, newValue});
    }
  },
  computed: {
    filteredEntries() {
      return Object.entries(this.item).filter(([key]) => key !== 'id');
    },
  }
}
</script>

<style lang="scss" scoped>
.table {
  &__data {
    border: 1px solid var(--c-border);
  }

  &__input {
    border: 0;
    font-style: italic;

    padding: 2px;
    width: 100%;
  }
}
</style>

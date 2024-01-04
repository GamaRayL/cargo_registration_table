<template>
  <table class="table">
    <tr class="table__rowTitle">
      <th class="table__header">Дата</th>
      <th class="table__header">Время</th>
      <th class="table__header">Маркировка</th>
      <th class="table__header">Документ поступления</th>
      <th class="table__header">Поставщик</th>
      <th class="table__header">Заявлено</th>
      <th class="table__header">Принято</th>
      <th class="table__header">Расхождение</th>
      <th class="table__header">Считал</th>
      <th class="table__header">Водитель</th>
    </tr>
    <custom-table-row
        v-for="item in data"
        :item="item"
        :key="item.id"
    >
    </custom-table-row>
  </table>
</template>

<script>


import {CustomTableRow} from "@/components/UI/CustomTable/CustomTableRow";

export default {
  components: {CustomTableRow},
  props: {
    data: {
      type: Array,
      required: true
    }
  },
}
</script>

<style lang="scss" scoped>
.table {
  border-collapse: collapse;

  &__header {
    border: 1px solid var(--c-border);
    padding: 4px 14px;
    height: 36px;

    font-family: var(--f-family);
    font-weight: var(--f-weight-regular);
  }

  &__rowTitle {
    background-color: var(--с-bgColorTitle);
    font-size: var(--f-size-30);
  }
}
</style>
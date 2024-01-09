<template>
  <div class="wrapper">
    <button @click="changeSort()">Сброс сортировки</button>
    <table class="table">
      <tr class="table__rowTitle">
        <th
            class="table__header"
            v-for="item in sortOptions"
        >
          <div
              v-if="item.value !== 'left'"
              @click="changeSort(item.value)"
              style="cursor: pointer; padding: 4px 14px; width: 100%; display: block; margin: 0 2px"
          >
            {{ item.name }}
            <svg-sort-to-bottom v-if="sort === item.value" width="18" height="18"/>
            <svg-sort-to-top v-else width="18" height="18"/>
          </div>
          <div v-else>{{ item.name }}</div>
        </th>
      </tr>
      <custom-table-row
          v-for="item in shipments"
          :item="item"
          :key="item.id"
      >
        1
      </custom-table-row>
    </table>
  </div>
</template>

<script>

import {CustomTableRow} from "@/components/widgets/CustomTable/CustomTableRow/index.js";
import {mapActions, mapMutations, mapState} from "vuex";
import SvgSortToTop from "@/components/svg/SvgSortToTop.vue";
import SvgSortToBottom from "@/components/svg/SvgSortToBottom.vue";

export default {
  components: {SvgSortToBottom, SvgSortToTop, CustomTableRow},
  computed: {
    ...mapState('entry', {
      shipments: state => state.shipments,
      sortOptions: state => state.sortOptions,
      sort: state => state.sort
    })
  },
  methods: {
    ...mapMutations('entry', {
      setSort: 'setSort'
    }),
    ...mapActions('entry', ['fetchShipments']),
    changeSort(sort) {
      if (this.sort === sort) {
        this.setSort('-' + sort)
      } else {
        this.setSort(sort)
      }
    }
  },
  watch: {
    sort() {
      this.fetchShipments();
    }
  }
}
</script>

<style lang="scss" scoped>
.wrapper {
  min-height: 300px;
}

.table {
  border-collapse: collapse;

  &__header {
    user-select: none;

    border: 1px solid var(--c-gray);

    font-family: var(--f-familyTitle);
    font-weight: var(--f-weight-regular);
  }

  &__rowTitle {
    background-color: var(--с-orange);
    font-size: var(--f-size-30);
  }
}
</style>
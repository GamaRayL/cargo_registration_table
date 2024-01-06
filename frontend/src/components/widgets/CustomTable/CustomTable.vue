<template>
  <div class="wrapper">
    <table class="table">
      <tr class="table__rowTitle">
        <th
            class="table__header"
            v-for="item in sortOptions"
        >
          <label @click="changeSort(item.value)"
                 style="cursor: pointer; padding: 4px 14px; width: 100%; display: block; margin: 0 2px">{{ item.name }}
            <sort-from-top-to-bottom v-if="sort === item.value" width="18" height="18"/>
            <sort-from-bottom-to-top v-else width="18" height="18"/>
          </label>

        </th>
      </tr>
      <custom-table-row
          v-for="item in shipments"
          :item="item"
          :key="item.id"
      >
      </custom-table-row>
    </table>
  </div>
</template>

<script>

import {CustomTableRow} from "@/components/widgets/CustomTable/CustomTableRow/index.js";
import {mapActions, mapMutations, mapState} from "vuex";
import SortFromBottomToTop from "@/components/svg/sortFromBottomToTop.vue";
import SortFromTopToBottom from "@/components/svg/sortFromTopToBottom.vue";

export default {
  components: {SortFromTopToBottom, SortFromBottomToTop, CustomTableRow},
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
    ...mapActions('entry', {
      fetchShipments: 'fetchShipments',
    }),
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
    background-color: var(--с-bgColorTitle);
    font-size: var(--f-size-30);
  }
}
</style>
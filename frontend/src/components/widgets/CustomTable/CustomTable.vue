<template>
  <div class="wrapper">
    <button @click="changeSort()">Сброс сортировки</button>
    <table class="table">
      <tr class="table__row-title">
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
      <transition-group name="fade-table">
        <custom-table-row
            class="table__row"
            v-for="item in shipments"
            :item="item"
            :key="item.id"
            v-if="shipments.length > 0"
        />
        <tr v-else>
          <td style="padding: 4px 12px;" v-for="i in 10">---------------------------------------</td>
        </tr>
      </transition-group>
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

    font-family: var(--f-familySecond);
    font-weight: var(--f-weight-regular);
  }

  &__row {
    transition: all .6s;
  }

  &__row-title {
    background: var(--c-orange);
    font-size: var(--f-size-30);
  }
}

.fade-table-enter, .fade-table-leave-to {
  opacity: 0;
  transform: translateY(5px);
}

.fade-table-leave-active {
  position: absolute;
}
</style>
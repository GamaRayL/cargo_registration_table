<template>
  <div class="wrapper">
    <div class="table">
      <div class="table__row-title">
        <div
            class="table__header"
            v-for="item in sortOptions"
        >
          <div
              v-if="item.value !== 'left'"
              @click="changeSort({sort: item.value})"
              style="cursor: pointer; gap: 4px; justify-content: center; padding: 4px 14px; width: 100%; display: flex; margin: 0 2px; align-items: center"
          >
            <span>{{ item.name }}</span>
            <svg-sort-to-bottom v-if="sort === item.value" width="18" height="18"/>
            <svg-sort-to-top v-else width="18" height="18"/>
          </div>
          <div v-else>{{ item.name }}</div>
        </div>
      </div>
      <transition-group name="fade-table">
        <custom-table-row
            class="table__row"
            v-for="item in shipments"
            :item="item"
            :key="item.id"
            v-if="shipments.length > 0"
        />
      </transition-group>
    </div>
  </div>
</template>

<script>

import {CustomTableRow} from "@/components/widgets/CustomTable/CustomTableRow";
import {mapActions, mapMutations, mapState} from "vuex";
import SvgSortToTop from "@/components/svg/SvgSortToTop";
import SvgSortToBottom from "@/components/svg/SvgSortToBottom";

export default {
  components: {SvgSortToBottom, SvgSortToTop, CustomTableRow},
  computed: {
    ...mapState('shipment', {
      shipments: 'shipments', sortOptions: 'sortOptions', sort: 'sort'
    })
  },
  methods: {
    ...mapMutations('shipment', {
      setSort: 'setSort'
    }),
    ...mapActions('shipment', {
      fetchShipments: 'fetchShipments',
      changeSort: 'changeSort'
    }),
  },
  watch: {
    sort() {
      this.fetchShipments();
    }
  }
}
</script>

<style lang="scss" scoped>
@import "@/assets/styles/mixins";

.wrapper {
  min-height: 300px;
  position: relative;
}

.table {
  width: 100%;

  &__header {
    @include flex-center;
    user-select: none;

    border: 1px solid var(--c-gray);

    font-family: var(--f-familySecond);
    font-weight: var(--f-weight-regular);
  }

  &__row {
    @include grid-10;

    transition: all .4s;
  }

  &__row-title {
    @include grid-10;

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
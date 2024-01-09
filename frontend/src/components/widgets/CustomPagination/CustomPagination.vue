<template>
  <div
      class="pagination"
  >
    <div
        class="pagination__item"
        v-for="item in totalPages"
        @click="changePage(item)"
        :class="{'pagination__item_current':
            page === item
        }"
    >
      {{ item }}
    </div>
  </div>
</template>

<script>
import {mapActions, mapMutations, mapState} from "vuex";

export default {
  computed: {
    ...mapState('shipment', {
      isShipmentsLoading: 'isShipmentsLoading',
      totalPages: 'totalPages',
      page: 'page',
    })
  },
  methods: {
    ...mapMutations('shipment', {
      setPage: 'setPage',
    }),
    ...mapActions('shipment', ['fetchShipments']),
    changePage(currentPage) {
      if (currentPage !== this.page) {
        this.setPage(currentPage);
      }
    },
    savePageToLocalStorage() {
      localStorage.setItem('currentPage', this.page);
    },
  },
  mounted() {
    const currentPage = localStorage.getItem('currentPage');
    const parsedPage = parseInt(currentPage);
    parsedPage && this.setPage(parsedPage);
    this.fetchShipments();
  },
  watch: {
    page() {
      this.savePageToLocalStorage();
      this.fetchShipments();
    }
  }
}
</script>

<style lang="scss" scoped>
.pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 5px;

  padding: 10px 0;

  &__item {
    cursor: pointer;
    padding: 4px 10px;
    font-size: var(--f-size-18);
    font-weight: 600;
    transition: ease-in-out .2s;
    font-family: var(--f-familyMain);

    &:hover {
      color: orange;
    }

    &_current {
      border: 2px solid orange;
      border-radius: 4px;

      &:hover {
        color: inherit;
      }
    }
  }
}
</style>
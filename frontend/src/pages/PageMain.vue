<template>
  <div style="display: grid;">
    <custom-toolbar></custom-toolbar>
    <transition-group name="fade-table-pagination">
      <template v-if="shipments.length > 0">
        <custom-table></custom-table>
        <custom-pagination></custom-pagination>
      </template>
    </transition-group>
  </div>
</template>

<script>

import CustomTable from "@/components/widgets/CustomTable/CustomTable";
import CustomPagination from "@/components/widgets/CustomPagination/CustomPagination";
import CustomToolbar from "@/components/widgets/CustomToolbar";
import {mapState} from "vuex";

export default {
  components: {CustomToolbar, CustomPagination, CustomTable},
  computed: {
    ...mapState('shipment', {
      shipments: 'shipments'
    })
  }
}
</script>

<style lang="scss" scoped>
.fade-table-pagination-enter-active {
  transition: ease-in-out .4s;
}

.fade-table-pagination-leave-active {
  transition: ease-in-out .2s;
}

.fade-table-pagination-enter-from,
.fade-table-pagination-leave-to {
  transform: translateY(-20px);
  opacity: 0;
}
</style>
<template>
  <div style="display: grid;">
    <custom-toolbar></custom-toolbar>
    <custom-table></custom-table>
    <custom-pagination></custom-pagination>
  </div>
</template>

<script>

import CustomTable from "@/components/widgets/CustomTable/CustomTable.vue";
import CustomPagination from "@/components/widgets/CustomPagination/CustomPagination.vue";
import CustomToolbar from "@/components/widgets/CustomToolbar/index.js";

export default {
  components: {CustomToolbar, CustomPagination, CustomTable},
}
</script>

<style lang="scss" scoped>

</style>
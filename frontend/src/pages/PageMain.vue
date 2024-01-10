<template>
  <div style="display: grid;">
    <custom-toolbar></custom-toolbar>
    <custom-table></custom-table>
    <custom-pagination></custom-pagination>
  </div>
</template>

<script>

import CustomPagination from "@/components/widgets/CustomPagination";
import CustomToolbar from "@/components/widgets/CustomToolbar";
import CustomTable from "@/components/widgets/CustomTable";

export default {
  components: {CustomToolbar, CustomPagination, CustomTable},
}
</script>

<style lang="scss" scoped>
</style>
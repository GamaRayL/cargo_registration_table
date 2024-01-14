<template>
  <div class="page-main">
    <custom-toolbar></custom-toolbar>
    <custom-table></custom-table>
    <custom-pagination></custom-pagination>
  </div>
</template>

<script>

import CustomTable from '@/components/widgets/CustomTable';
import CustomToolbar from '@/components/widgets/CustomToolbar';
import CustomPagination from '@/components/widgets/CustomPagination';

export default {
  components: {CustomToolbar, CustomPagination, CustomTable},
};
</script>

<style lang="scss" scoped>
.page-main {
  display: grid;
}
</style>
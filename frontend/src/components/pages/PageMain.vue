<template>
  <custom-table
      :data="arrivalRegistrations"
  >
  </custom-table>
</template>

<script>

import CustomTable from "@/components/UI/CustomTable/CustomTable.vue";
import {mapState} from "vuex";

export default {
  components: {CustomTable},
  computed: {
    ...mapState({
      arrivalRegistrations: state => state.entry.arrivalRegistrations
    })
  }
}
</script>

<style lang="scss" scoped>

</style>
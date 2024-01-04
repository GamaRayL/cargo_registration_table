<template>
  <custom-table
      :data="shipments"
  >
  </custom-table>
</template>

<script>

import CustomTable from "@/components/UI/CustomTable/CustomTable.vue";
import {mapActions, mapState} from "vuex";

export default {
  components: {CustomTable},
  computed: {
    ...mapState({
      shipments: state => state.entry.shipments
    })
  },
  methods: {
    ...mapActions({
      fetchShipments: 'entry/fetchShipments'
    })
  },
  mounted() {
    this.fetchShipments()
  },
}
</script>

<style lang="scss" scoped>

</style>
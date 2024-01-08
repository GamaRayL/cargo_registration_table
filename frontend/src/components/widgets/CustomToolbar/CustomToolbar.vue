<template>
  <div class="toolbar">
    <form class="form" @submit.prevent="fetchData">
      <custom-select
          name="property-select"
          label="Выберите колонку"
          v-model="localFilterProperty"
          :options="sortOptionsWithoutLeft"
      />
      <custom-select
          name="statement-select"
          label="Выберите условие"
          v-model="localFilterStatement"
          :options="statementByColumn"
          v-if="localFilterProperty && statementByColumn.length > 0"
      />
      <custom-input
          name="value-select"
          v-model="localFilterValue"
          v-if="localFilterStatement"
      />
      <custom-button @submit.prevent="fetchData" type="submit">Получить</custom-button>
      <custom-button @click.prevent="resetData">Сброс</custom-button>
    </form>
    <custom-button @click="createShipment">
      <svg-add height="20" width="20"/>
    </custom-button>
  </div>
</template>

<script>
import CustomSelect from "@/components/UI/CustomSelect";
import CustomInput from "@/components/UI/CustomInput";
import CustomButton from "@/components/UI/CustomButton";
import {mapActions, mapGetters, mapMutations, mapState} from "vuex";
import SvgAdd from "@/components/svg/SvgAdd.vue";

export default {
  components: {SvgAdd, CustomButton, CustomInput, CustomSelect},
  data() {
    return {
      localFilterProperty: "",
      localFilterStatement: "",
      localFilterValue: "",
    };
  },
  computed: {
    ...mapState('entry', ['sortOptions', 'filterStatement', 'filterValue', 'filterProperty']),
    ...mapGetters('entry', {
      statementByColumn: 'statementByColumn',
      sortOptionsWithoutLeft: 'sortOptionsWithoutLeft'
    }),
  },
  methods: {
    ...mapMutations('entry', ['setFilterStatement', 'setFilterValue', 'setFilterProperty']),
    ...mapActions('entry', ['fetchShipments', 'createShipment']),
    fetchData() {
      this.setFilterProperty(this.localFilterProperty);
      this.setFilterStatement(this.localFilterStatement);
      this.setFilterValue(this.localFilterValue);
      this.fetchShipments();
    },
    resetData() {
      this.setFilterProperty('');
      this.setFilterStatement('');
      this.setFilterValue('');
      this.localFilterProperty = '';
      this.localFilterStatement = '';
      this.localFilterValue = '';
      this.fetchShipments();
    }
  },
  mounted() {
    this.localFilterProperty = this.filterProperty;
    this.localFilterStatement = this.filterStatement;
    this.localFilterValue = this.filterValue;
  },
  watch: {
    localFilterProperty() {
      this.setFilterProperty(this.localFilterProperty);
    }
  }
}
</script>

<style lang="scss" scoped>
.toolbar {
  margin-bottom: 10px;
}

.form {
  display: flex;
  gap: 4px;
}
</style>
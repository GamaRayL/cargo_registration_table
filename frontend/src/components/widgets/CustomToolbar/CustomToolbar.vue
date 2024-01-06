<template>
  <div>
    <form action="" @submit.prevent="handleSubmit">
      <custom-select
          name="property-select"
          label="Выберите колонку"
          v-model="localFilterProperty"
          :options="sortOptions"
      />
      <custom-select
          name="statement-select"
          label="Выберите условие"
          v-model="localFilterStatement"
          :options="statements"
      />
      <custom-input name="value-select" v-model="localFilterValue"></custom-input>
      <custom-button @submit.prevent="handleSubmit" type="submit">Получить</custom-button>
      <custom-button @submit.prevent="handleReset" type="submit">Сброс</custom-button>
    </form>
  </div>
</template>

<script>
import CustomSelect from "@/components/UI/CustomSelect";
import CustomInput from "@/components/UI/CustomInput.vue";
import CustomButton from "@/components/UI/CustomButton.vue";
import {mapActions, mapGetters, mapMutations, mapState} from "vuex";

export default {
  components: {CustomButton, CustomInput, CustomSelect},
  data() {
    return {
      localFilterProperty: '',
      localFilterStatement: '',
      localFilterValue: ''
    };
  },
  computed: {
    ...mapState('entry', {
      sortOptions: state => state.sortOptions,
      filterStatement: state => state.filterStatement,
      filterValue: state => state.filterValue,
      filterProperty: state => state.filterProperty,
      statements: state => state.statements
    }),
    ...mapGetters('entry', {
      // statementByColumn: "statementByColumn"
    })
  },
  methods: {
    ...mapMutations('entry', {
      setFilterStatement: 'setFilterStatement',
      setFilterValue: 'setFilterValue',
      setFilterProperty: 'setFilterProperty'
    }),
    ...mapActions('entry', {
      fetchShipments: 'fetchShipments'
    }),
    handleSubmit() {
      this.setFilterProperty(this.localFilterProperty);
      this.setFilterStatement(this.localFilterStatement);
      this.setFilterValue(this.localFilterValue);
      this.fetchShipments();
      // this.localFilterProperty = '';
      // this.localFilterStatement = '';
      // this.localFilterValue = '';
    },
    handleReset() {
      this.setFilterProperty('');
      this.setFilterStatement('');
      this.setFilterValue('');
      this.fetchShipments();
    }
  }
}
</script>

<style lang="scss" scoped>

</style>
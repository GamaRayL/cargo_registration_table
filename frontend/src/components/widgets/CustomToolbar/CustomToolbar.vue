<template>
  <div class="toolbar">
    <form class="form" @submit.prevent="handleGetData">
      <custom-select
          name="property-select"
          label="Выберите колонку"
          v-model="localFilterProperty"
          :options="sortOptionsWithoutLeft"
      />
      <transition name="fade-toolbar">
        <custom-select
            name="statement-select"
            label="Выберите условие"
            :options="statementByColumn"
            v-model="localFilterStatement"
            v-if="localFilterProperty !== ''"
        />
      </transition>
      <transition name="fade-toolbar">
        <custom-input
            v-focus
            name="value-select"
            class="form__input"
            v-model="localFilterValue"
            v-if="localFilterStatement !== ''"
        />
      </transition>
      <div class="buttons-group">
        <transition name="fade-toolbar">
          <custom-button
              contained
              type="submit"
              @submit.prevent="handleGetData"
              v-if="localFilterStatement !== ''"
          >
            Получить
          </custom-button>
        </transition>
        <transition name="fade-toolbar">
          <custom-button
              contained
              @click.prevent="handleResetData"
              v-if="localFilterProperty && statementByColumn.length > 0"
          >
            Сбросить
          </custom-button>
        </transition>
      </div>
    </form>
  </div>
</template>

<script>

import SvgAdd from "@/components/svg/SvgAdd";
import CustomInput from "@/components/UI/CustomInput";
import CustomSelect from "@/components/UI/CustomSelect";
import CustomButton from "@/components/UI/CustomButton";
import {mapActions, mapGetters, mapMutations, mapState} from "vuex";

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
    ...mapState('shipment', ['sortOptions', 'filterStatement', 'filterValue', 'filterProperty']),
    ...mapGetters('shipment', {
      statementByColumn: 'statementByColumn',
      sortOptionsWithoutLeft: 'sortOptionsWithoutLeft'
    }),
  },
  methods: {
    ...mapMutations('shipment', ['setFilterStatement', 'setFilterValue', 'setFilterProperty', 'setSort']),
    ...mapActions('shipment', ['fetchShipments', 'createShipment']),
    handleGetData() {
      this.setFilterProperty(this.localFilterProperty);
      this.setFilterStatement(this.localFilterStatement);
      this.setFilterValue(this.localFilterValue);
      if (this.filterValue) {
        this.filterValue && this.fetchShipments();
      }
    },
    handleResetData() {
      this.setFilterProperty('');
      this.setFilterStatement('');
      this.setFilterValue('');
      this.localFilterProperty = '';
      this.localFilterStatement = '';
      this.localFilterValue = '';
      this.fetchShipments();
    },
  },
  mounted() {
    this.localFilterProperty = this.filterProperty;
    this.localFilterStatement = this.filterStatement;
    this.localFilterValue = this.filterValue;
  },
  watch: {
    localFilterProperty() {
      this.setFilterProperty(this.localFilterProperty);
    },
  }
}
</script>

<style lang="scss" scoped>
@import "@/assets/styles/mixins";

.toolbar {
  margin-bottom: 4px;
}

.buttons-group {
  display: flex;
  gap: 4px;
}

.form {
  display: flex;
  margin-bottom: 4px;
  gap: 4px;

  &__input {
    box-shadow: var(--bS-standart);
  }
}

.fade-toolbar-enter-active {
  transition: all .4s ease;
}

.fade-toolbar-leave-active {
  transition: all .1s cubic-bezier(1.0, 0.5, 0.8, 1.0);
}

.fade-toolbar-enter-from,
.fade-toolbar-leave-to {
  transform: translateX(-10px);
  opacity: 0;
}
</style>
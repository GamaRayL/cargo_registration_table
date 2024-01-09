<template>
  <div class="toolbar">
    <form class="form" @submit.prevent="fetchData">
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
            v-model="localFilterStatement"
            :options="statementByColumn"
            v-if="localFilterProperty !== ''"
        />
      </transition>
      <transition name="fade-toolbar">
        <custom-input
            class="form__input"
            name="value-select"
            v-model="localFilterValue"
            v-if="localFilterStatement !== ''"
        />
      </transition>
      <div
          style="display: flex; gap: 4px;"
      >
        <transition name="fade-toolbar">
          <custom-button
              class="form__button"
              @submit.prevent="fetchData"
              type="submit"
              v-if="localFilterStatement !== ''"
          >
            <span class="button__text">Получить</span>
          </custom-button>
        </transition>
        <transition name="fade-toolbar">
          <custom-button
              class="form__button"
              @click.prevent="resetData"
              v-if="localFilterProperty && statementByColumn.length > 0"
          >
            <span class="button__text">Сбросить</span>
          </custom-button>
        </transition>
      </div>
    </form>
    <custom-button @click="createShipment">
      <svg-add height="20" width="20"/>
    </custom-button>
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
      if (this.filterValue) {
        this.filterValue && this.fetchShipments();
      }
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
    },
  }
}
</script>

<style lang="scss" scoped>
.toolbar {
  margin-bottom: 10px;
}

.button__text {
  transition: ease-in-out .1s;
}

.form {
  display: flex;
  gap: 4px;

  &__button {
    background: #363636;
    color: var(--c-orange);
    font-weight: var(--f-weight-bold);
    font-size: var(--f-size-22);
    font-family: var(--f-familySecond);
    border: none;
    border-radius: var(--br-standart);
    padding: 0 4px;
    box-shadow: var(--bS-standart);

    &:active .button__text {
      transform: scale(0.8);
    }
  }

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
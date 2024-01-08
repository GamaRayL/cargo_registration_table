<template>
  <tr
      class="table__row"
      @mouseover="isShow = !isShow"
      @mouseout="isShow = !isShow"
  >
    <td
        class="table__data"
        :key="key" v-for="[key, value] of filteredEntries"
    >
      <input
          class="table__input"
          :value="value"
          ref="inputRef"
          @input="updateInput(key, $event.target.value)"
          :name="key"
          :type="getTypeForInput(key)"
          :disabled="key === 'left'"
      >
    </td>
    <custom-button
        :class="[
            'button_delete-row',
            {'button_hide': !isShow}
            ]"
        @click="handleDeleteClick(item['id'])"
    >
      <svg-button-delete width="16" height="16"/>
    </custom-button>
  </tr>
</template>

<script>


import CustomInput from "@/components/UI/CustomInput.vue";
import {mapActions} from "vuex";
import CustomButton from "@/components/UI/CustomButton.vue";
import SvgButtonDelete from "@/components/svg/SvgDelete.vue";

export default {
  components: {SvgButtonDelete, CustomButton, CustomInput},
  data() {
    return {
      isShow: false,
    }
  },
  props: {
    item: {
      type: Object,
      required: true
    }
  },
  methods: {
    ...mapActions('entry', ["updateShipment", "deleteShipment"]),
    updateInput(key, newValue) {
      const data = {
        [key]: newValue
      }
      this.updateShipment({id: this.item.id, data});

      console.log(Object.keys(this.item).map(i => i))
    },
    handleDeleteClick(id) {
      this.deleteShipment({id: id})
    },
    getTypeForInput(key) {
      if (key === 'date') {
        return 'date';
      } else if (key === 'time') {
        return 'time';
      } else if (['label', 'document', 'vendor', 'counted', 'driver'].includes(key)) {
        return 'text';
      } else if (['declared', 'accepted'].includes(key)) {
        return 'number';
      } else {
        return 'text'
      }
    },
  },
  computed: {
    filteredEntries() {
      return Object.entries(this.item).filter(([key]) => key !== 'id');
    },
  }
}

</script>

<style lang="scss" scoped>
.table {
  &__data {
    border: 1px solid var(--c-gray);
  }

  &__input {
    border: 0;

    padding: 0 2px;
    width: 100%;
  }
}

.button {
  &_delete-row {
    transition: ease-in-out .1s;
  }


  &_delete-row:active {
    transform: translateX(-4px);
  }

  &_hide {
    visibility: hidden;
  }
}
</style>

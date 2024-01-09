<template>
  <tr
      class="row"
      @mouseover="isShow = !isShow"
      @mouseout="isShow = !isShow"
  >
    <td
        class="row__data"
        :key="key" v-for="[key, value] of filteredEntries"
    >
      <input
          class="row__input"
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


import CustomInput from "@/components/UI/CustomInput";
import {mapActions} from "vuex";
import CustomButton from "@/components/UI/CustomButton";
import SvgButtonDelete from "@/components/svg/SvgDelete";

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
.row {
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
    background: none;
    border: none;
  }


  &_delete-row:active {
    transform: translateX(-4px);
  }

  &_hide {
    visibility: hidden;
  }
}
</style>

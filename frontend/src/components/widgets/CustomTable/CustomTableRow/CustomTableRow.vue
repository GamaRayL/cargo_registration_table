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
          @change="updateInput(key, $event.target.value)"
          :name="key"
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
import SvgButtonDelete from "@/components/svg/SvgButtonDelete.vue";
// updateShipment
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
    // ...mapMutations('entry', ['updateFieldValue']),
    updateInput(key, newValue) {
      const data = {
        [key]: newValue
      }
      this.updateShipment({id: this.item.id, data});
      // console.log(this.item.id)
      // this.updateFieldValue({id: this.item.id, key, newValue})
      // this.$store.commit('entry/updateFieldValue', {id: this.item.id, key, newValue});
    },
    handleDeleteClick(id) {
      this.deleteShipment({id: id})
    }
  },
  computed: {
    filteredEntries() {
      return Object.entries(this.item).filter(([key]) => key !== 'id');
    },
    // typeIdentify() {
    //   console.log(this.item.label)
    //   // if (typeof (this.item.key) === 'string') {
    //   //   return 'text'
    //   // } else if (typeof (this.item.value) === 'number') {
    //   //   return 'number'
    //   // }
    //   // return this.item.value
    // }
  },
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

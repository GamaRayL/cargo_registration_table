import {createStore} from 'vuex'
import {shipmentStore} from "@/store/shipmentStore.js";
import createPersistedState from "vuex-persistedstate";


export default createStore({
    modules: {
        shipment: shipmentStore
    },
    plugins: [
        createPersistedState({
            storage: window.sessionStorage
        })
    ]
})

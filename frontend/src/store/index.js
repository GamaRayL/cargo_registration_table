import {createStore} from 'vuex'
import {entryStore} from "@/store/entryStore.js";
import createPersistedState from "vuex-persistedstate";


export default createStore({
    modules: {
        entry: entryStore
    },
    plugins: [
        createPersistedState({
            storage: window.sessionStorage
        })
    ]
})

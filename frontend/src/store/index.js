import {createStore} from 'vuex'
import {entryStore} from "@/store/entryStore.js";

export default createStore({
    modules: {
        entry: entryStore
    }
})

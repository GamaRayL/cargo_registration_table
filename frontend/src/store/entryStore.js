import axios from "axios";
import {API_URL} from "@/constants/index.js";

export const entryStore = {
    state: () => ({
        shipments: [],
        isShipmentsLoading: false,
        searchQuery: '',
        selectedSort: '',
        // page: 1,
        // limit: 10,
        // totalPages: 0,
        // sortOptions: [
        //     {value: 'id', name: 'По id'},
        //     {value: 'title', name: 'По названию'},
        //     {value: 'body', name: 'По содержанию'}
        // ]
    }),
    getters: {},
    mutations: {
        setLoading(state, bool) {
            state.isShipmentsLoading = bool
        },
        setShipments(state, shipments) {
            state.shipments = shipments
        },
        // updateFieldValue(state, {id, key, newValue}) {
        //     const foundItem = state.shipments.find(registration => registration.id === id);
        //     if (foundItem) foundItem[key] = newValue;
        // }
    },
    actions: {
        async fetchShipments({state, commit}) {
            try {
                commit('setLoading', true);
                const response = await axios.get(`${API_URL}/shipments/`);
                commit('setShipments', response.data);
                console.log(response.data)
            } catch (e) {
                console.log(e)
            } finally {
                commit('setLoading', false)
            }
        }
    },
    // actions: {
    //     async fetchPosts({state, commit}) {
    //         try {
    //             commit('setLoading', true);
    //             const response = await axios.get('https://jsonplaceholder.typicode.com/posts', {
    //                 params: {
    //                     _page: state.page,
    //                     _limit: state.limit,
    //                 }
    //             });
    //             commit('setTotalPages', Math.ceil(response.headers['x-total-count'] / state.limit));
    //             commit('setPosts', response.data);
    //         } catch (e) {
    //             alert(`Ошибка ${e}`)
    //         } finally {
    //             commit('setLoading', false);
    //         }
    //     }
    // },
    namespaced: true
}
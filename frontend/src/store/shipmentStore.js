import axios from "axios";
import {API_URL, SORT_OPTIONS} from "@/constants";


export const shipmentStore = {
    state: () => ({
        shipments: [],
        isShipmentsLoading: false,
        searchQuery: '',
        selectedSort: '',
        page: 1,
        limit: 10,
        totalPages: 0,
        sort: '',
        sortOptions: SORT_OPTIONS,
        filterStatement: '',
        filterProperty: '',
        filterValue: '',
    }),
    getters: {
        statementByColumn(state) {
            if (state.filterProperty) {
                const option = state.sortOptions.filter(i => i.value === state.filterProperty);
                return option && option[0].statement.list;
            }
            return [];
        },
        sortOptionsWithoutLeft(state) {
            return state.sortOptions.filter(i => i.value !== 'left')
        }
    },
    mutations: {
        setLoading(state, bool) {
            state.isShipmentsLoading = bool
        },
        setShipments(state, shipments) {
            state.shipments = shipments
        },
        setTotalPages(state, totalPages) {
            state.totalPages = totalPages
        },
        setPage(state, newPage) {
            state.page = newPage
        },
        setSort(state, sort) {
            state.sort = sort
        },
        setFilterStatement(state, filterStatement) {
            state.filterStatement = filterStatement;
        },
        setFilterValue(state, filterValue) {
            state.filterValue = filterValue;
        },
        setFilterProperty(state, filterProperty) {
            state.filterProperty = filterProperty;
        },
        // updateFieldValue(state, {id, key, newValue}) {
        //     const foundItem = state.shipments.find(registration => registration.id === id);
        //     console.log(foundItem)
        //     if (foundItem) foundItem[key] = newValue;
        // }
    },
    actions: {
        async createShipment({dispatch}) {
            try {
                await axios.post(`${API_URL}/shipments/create/`);
                dispatch('fetchShipments');
            } catch (error) {
                console.log('Ошибка создания строки отгрузки:', error)
            }
        },
        async deleteShipment({state, commit, dispatch}, {id}) {
            try {
                await axios.delete(`${API_URL}/shipments/delete/${id}/`);
                dispatch('fetchShipments');
            } catch (error) {
                console.error('Ошибка удаления строки отгрузки:', error);
            }
        },
        async updateShipment({state, commit, dispatch}, {id, data}) {
            try {
                await axios.patch(`${API_URL}/shipments/update/${id}/`, data);
                dispatch('fetchShipments');
            } catch (error) {
                console.error('Ошибка изменения значения:', error);
            }
        },
        async fetchShipments({state, commit}) {
            try {
                commit('setLoading', true);

                const params = {
                    page: state.page,
                    limit: state.limit,
                    ordering: state.sort,
                }


                if (state.filterStatement) {
                    params[state.filterProperty + state.filterStatement] = state.filterValue
                }

                const response = await axios.get(`${API_URL}/shipments/`, {params});
                const data = response.data

                commit('setTotalPages', Math.ceil(data.count / state.limit))
                commit('setShipments', data.results);
            } catch (error) {
                console.log(error)
            } finally {
                commit('setLoading', false)
            }
        },
    },
    namespaced: true
}
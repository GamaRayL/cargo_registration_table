import axios from "axios";
import {API_URL, SORT_OPTIONS, STATEMENTS} from "@/constants";


export const entryStore = {
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
        statements: STATEMENTS,
        // filterOptions: FILTER_OPTIONS
    }),
    getters: {
        // statementByColumn(state) {
        //     const option = state.sortOptions.filter(i => i.value === state.filterProperty);
        //     return option && option.statement;
        // }
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
        }
        // updateFieldValue(state, {id, key, newValue}) {
        //     const foundItem = state.shipments.find(registration => registration.id === id);
        //     if (foundItem) foundItem[key] = newValue;
        // }
    },
    actions: {
        async fetchShipments({state, commit}) {
            try {
                commit('setLoading', true);

                const params = {
                    page: state.page,
                    limit: state.limit,
                    ordering: state.sort,
                }

                params[state.filterProperty + state.filterStatement] = state.filterValue
                const response = await axios.get(`${API_URL}/shipments/`, {params});
                const data = response.data

                commit('setTotalPages', Math.ceil(data.count / state.limit))
                commit('setShipments', data.results);
            } catch (e) {
                console.log(e)
            } finally {
                commit('setLoading', false)
            }
        },
    },
    namespaced: true
}
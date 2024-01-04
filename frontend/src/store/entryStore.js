export const entryStore = {
    state: {
        arrivalRegistrations: [
            {
                id: 1,
                date: '27.12.2023',
                time: '15:00',
                marking: '27082',
                document: '0000-015606,0000-016056, 0000-016150',
                vendor: 'Мерлион',
                declared: 79,
                accepted: 79,
                discrepancy: 0,
                counted: 'Рандом',
                driver: 'Газель ТК'
            },
        ]
    },
    getters: {},
    mutations: {
        updateFieldValue(state, {id, key, newValue}) {
            const foundItem = state.arrivalRegistrations.find(registration => registration.id === id);
            if (foundItem) foundItem[key] = newValue;
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
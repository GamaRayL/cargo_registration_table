export const API_URL = 'http://localhost:8000/'
export const SORT_OPTIONS = [
    {id: 1, value: 'date', name: 'Дата'},
    {id: 2, value: 'time', name: 'Время'},
    {id: 3, value: 'label', name: 'Маркировка'},
    {id: 4, value: 'document', name: 'Документ'},
    {id: 5, value: 'vendor', name: 'Поставщик'},
    {id: 6, value: 'declared', name: 'Заявлено'},
    {id: 7, value: 'accepted', name: 'Принято'},
    {id: 8, value: 'left', name: 'Осталось'},
    {id: 9, value: 'counted', name: 'Считал'},
    {id: 10, value: 'driver', name: 'Водитель'},
]


export const STATEMENTS = [
    {id: 1, value: '', name: 'Равно'},
    {id: 2, value: '__ct', name: 'Содержит'},
    {id: 3, value: '__lt', name: 'Меньше'},
    {id: 4, value: '__gt', name: 'Больше'}
]
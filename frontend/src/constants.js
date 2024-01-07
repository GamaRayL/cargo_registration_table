export const API_URL = 'http://localhost:8000'

export const STATEMENTS = [
    {
        id: 1, list: [{id: 1, value: '', name: 'Равно'},
            {id: 2, value: '__ct', name: 'Содержит'},
            {id: 3, value: '__lt', name: 'Меньше'},
            {id: 4, value: '__gt', name: 'Больше'}]
    },
    {
        id: 2, list: [{id: 1, value: '', name: 'Равно'},
            {id: 2, value: '__ct', name: 'Содержит'},]
    },
]

export const SORT_OPTIONS = [
    {id: 1, value: 'date', name: 'Дата', format: 'date', statement: STATEMENTS[0]},
    {id: 2, value: 'time', name: 'Время', format: 'time', statement: STATEMENTS[0]},
    {id: 3, value: 'label', name: 'Маркировка', format: "text", statement: STATEMENTS[1]},
    {id: 4, value: 'document', name: 'Документ', format: "text", statement: STATEMENTS[1]},
    {id: 5, value: 'vendor', name: 'Поставщик', format: "text", statement: STATEMENTS[1]},
    {id: 6, value: 'declared', name: 'Заявлено', format: "number", statement: STATEMENTS[0]},
    {id: 7, value: 'accepted', name: 'Принято', statement: STATEMENTS[0]},
    {id: 8, value: 'left', name: 'Осталось'},
    {id: 9, value: 'counted', name: 'Считал', format: "text", statement: STATEMENTS[1]},
    {id: 10, value: 'driver', name: 'Водитель', format: "text", statement: STATEMENTS[1]},
]



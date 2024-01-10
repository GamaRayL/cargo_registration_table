import {createRouter, createWebHistory} from "vue-router";
import PageMain from "@/pages/PageMain";


const routes = [
    {
        path: '/',
        component: PageMain
    }
]

const router = createRouter({
    routes,
    history: createWebHistory(import.meta.env.BASE_URL)
})

export default router;
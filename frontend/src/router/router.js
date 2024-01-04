import {createRouter, createWebHistory} from "vue-router";
import PageMain from "@/components/pages/PageMain.vue";


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
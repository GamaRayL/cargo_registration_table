import directives from "@/directives";
import router from "@/router/router";
import "@/assets/styles/global.scss"
import {createApp} from 'vue';
import store from "@/store";
import App from "./App";

const app = createApp(App)
directives.forEach(directive => {
    app.directive(directive.name, directive)
})

app
    .use(router)
    .use(store)
    .mount('#app')

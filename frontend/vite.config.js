import {defineConfig} from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path'


// https://vitejs.dev/config/
export default defineConfig({
    plugins: [vue()],
    server: {
        watch: {
            usePolling: true
        },
        host: true,
        strictPort: true,
        port: 5173
    },
    resolve: {
        alias: {
            '@': path.resolve(__dirname, './src'),
            '@styles': path.resolve(__dirname, './src/assets/styles'),
        },
        extensions: ['.js', '.json', '.vue', '.scss', '.sass'],
    }
})

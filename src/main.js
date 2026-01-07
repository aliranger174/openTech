import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import App from './App.vue'
import Home from './pages/Home.vue'
import News from './pages/News.vue'
import Tutorials from './pages/Tutorials.vue'
import Books from './pages/Books.vue'
import Projects from './pages/Projects.vue'

const routes = [
  { path: '/', component: Home },
  { path: '/news', component: News },
  { path: '/tutorials', component: Tutorials },
  { path: '/books', component: Books },
  { path: '/projects', component: Projects }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

const app = createApp(App)
app.use(router)
app.mount('#app')

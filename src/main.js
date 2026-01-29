import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import App from './App.vue'
import Home from './pages/Home.vue'
import News from './pages/News.vue'
import NewsDetail from './pages/NewsDetail.vue'
import Tutorials from './pages/Tutorials.vue'
import TutorialDetail from './pages/TutorialDetail.vue'
import Books from './pages/Books.vue'
import BookDetail from './pages/BookDetail.vue'
import Projects from './pages/Projects.vue'
import ProjectDetail from './pages/ProjectDetail.vue'

const routes = [
  { path: '/', component: Home },
  { path: '/news', component: News },
  { path: '/news/:id', component: NewsDetail },
  { path: '/tutorials', component: Tutorials },
  { path: '/tutorials/:id', component: TutorialDetail },
  { path: '/books', component: Books },
  { path: '/books/:id', component: BookDetail },
  { path: '/projects', component: Projects },
  { path: '/projects/:id', component: ProjectDetail }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

const app = createApp(App)
app.use(router)
app.mount('#app')

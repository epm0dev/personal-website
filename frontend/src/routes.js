import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from './views/Home'
import Projects from './views/Projects'
import ProjectDetail from "./views/ProjectDetail";
import Blog from './views/Blog'
import Feed from './views/Feed'
import Contact from './views/Contact'

Vue.use(VueRouter)

export default new VueRouter({
    mode: 'history',
    base: '/',
    routes: [
        {
            path: '/',
            name: 'home',
            component: Home,
        },
        {
            path: '/projects',
            name: 'projects',
            component: Projects,
        },
        {
            path: '/projects/:id',
            name: 'project-detail',
            component: ProjectDetail
        },
        {
            path: '/blog',
            name: 'blog',
            component: Blog,
        },
        {
            path: '/feed',
            name: 'feed',
            component: Feed,
        },
        {
            path: '/contact',
            name: 'contact',
            component: Contact,
        }
    ]
})
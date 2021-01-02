import Vue from 'vue'
import Vuex from 'vuex'
import {getAPI} from './axios-api'

Vue.use(Vuex)

const getBlogPosts = (page, posts, resolve, reject) => {
    getAPI.get('/blog/?page=' + page)
        .then(response => {
            const retrievedPosts = posts.concat({page: page, posts: response.data.results})
            if (response.data.next !== null) {
                getBlogPosts(page + 1, retrievedPosts, resolve, reject)
            } else {
                resolve(retrievedPosts)
            }
        })
        .catch(err => {
            reject(err)
        })
}

export default new Vuex.Store({
    state: {
        accessToken: null,
        refreshToken: null,
        projects: {
            featured: [],
            general: [],
            archived: []
        },
        project: {},
        blogPosts: []
    },
    mutations: {
        updateStorage(state, {access, refresh}) {
            state.accessToken = access
            state.refreshToken = refresh
        },
        destroyToken(state) {
            state.accessToken = null
            state.refreshToken = null
        },
        setProjectCategory(state, {category, projects}) {
            state.projects[category] = projects
        },
        setCurrentProject(state, {project}) {
            state.project = project
        },
        setBlogPosts(state, {posts}) {
            state.blogPosts = posts
        }
    },
    getters: {
        loggedIn(state) {
            return state.accessToken != null
        }
    },
    actions: {
        userLogout(context) {
            if (context.getters.loggedIn) {
                context.commit('destroyToken')
            }
        },
        userLogin(context, usercredentials) {
            return new Promise((resolve, reject) => {
                getAPI.post('/token/', {
                    username: usercredentials.username,
                    password: usercredentials.password
                })
                    .then(response => {
                        context.commit('updateStorage', {access: response.data.access, refresh: response.data.refresh})
                        resolve()
                    })
                    .catch(err => {
                        reject(err)
                    })
            })
        },
        loadProjects(context) {
            return new Promise((resolve, reject) => {
                getAPI.get('/projects/?category=featured'/*, {headers: {Authorization: `Bearer ${this.state.accessToken}`}}*/)
                    .then(response => {
                        context.commit('setProjectCategory', {category: 'featured', projects: response.data.results})
                        resolve()
                    }).catch(err => {
                    reject(err)
                })
                getAPI.get('/projects/?category=general'/*, {headers: {Authorization: `Bearer ${this.state.accessToken}`}}*/)
                    .then(response => {
                        context.commit('setProjectCategory', {category: 'general', projects: response.data.results})
                        resolve()
                    }).catch(err => {
                    reject(err)
                })
                getAPI.get('/projects/?category=archived'/*, {headers: {Authorization: `Bearer ${this.state.accessToken}`}}*/)
                    .then(response => {
                        context.commit('setProjectCategory', {category: 'archived', projects: response.data.results})
                        resolve()
                    }).catch(err => {
                    reject(err)
                })
            })
        },
        loadProject(context, payload) {
            return new Promise((resolve, reject) => {
                getAPI.get('/projects/' + payload.id,/* {headers: {Authorization: `Bearer ${this.state.accessToken}`}}*/)
                    .then(response => {
                        context.commit('setCurrentProject', {project: response.data})
                        resolve()
                    }).catch(err => {
                    reject(err)
                })
            })
        },
        loadBlogPosts(context) {
            return new Promise((resolve, reject) => {
                getBlogPosts(1, [], resolve, reject)
            })
                .then(response => {
                    context.commit('setBlogPosts', {
                        posts: response
                    })
                })
        }
    }
})
import Vue from 'vue'
import Vuex from 'vuex'
import {getAPI} from './axios-api'

Vue.use(Vuex)

const getProjects = (category, page, projects, resolve, reject) => {
    getAPI.get('/projects/?category=' + category + '&page=' + page)
        .then(response => {
            const retrievedProjects = projects.concat(response.data.results)
            if (response.data.next != null) {
                getProjects(category, page + 1, retrievedProjects, resolve, reject)
            } else {
                resolve(retrievedProjects)
            }
        })
        .catch(err => {
            reject(err)
        })
}

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

const getFeedActivity = (page, posts, resolve, reject) => {
    getAPI.get('/feed/?page=' + page)
        .then(response => {
            const retrievedActivity = posts.concat({page: page, activity: response.data.results})
            if (response.data.next !== null) {
                getFeedActivity(page + 1, retrievedActivity, resolve, reject)
            } else {
                resolve(retrievedActivity)
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
        blogPosts: [],
        numBlogPostPages: 0,
        feedActivity: [],
        numFeedActivityPages: 0,
        resume: {}
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
        },
        setNumBlogPostPages(state) {
            state.numBlogPostPages = state.blogPosts.length
        },
        setFeedActivity(state, {activity}) {
            state.feedActivity = activity
        },
        setNumFeedActivityPages(state) {
            state.numFeedActivityPages = state.feedActivity.length
        },
        setResume(state, {resume}) {
            state.resume = resume
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
        userLogin(context, userCredentials) {
            return new Promise((resolve, reject) => {
                getAPI.post('/token/', {
                    username: userCredentials.username,
                    password: userCredentials.password
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
        loadFeaturedProjects(context) {
            return new Promise((resolve, reject) => {
                getProjects('featured', 1, [], resolve, reject)
            })
                .then(response => {
                    context.commit('setProjectCategory', {category: 'featured', projects: response})
                })
        },
        loadGeneralProjects(context) {
            return new Promise((resolve, reject) => {
                getProjects('general', 1, [], resolve, reject)
            })
                .then(response => {
                    context.commit('setProjectCategory', {category: 'general', projects: response})
                })
        },
        loadArchivedProjects(context) {
            return new Promise((resolve, reject) => {
                getProjects('archived', 1, [], resolve, reject)
            })
                .then(response => {
                    context.commit('setProjectCategory', {category: 'archived', projects: response})
                })
        },
        loadProject(context, payload) {
            return new Promise((resolve, reject) => {
                getAPI.get('/projects/' + payload.id)
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
                    context.commit('setNumBlogPostPages')
                })
        },
        loadFeedActivity(context) {
            return new Promise((resolve, reject) => {
                getFeedActivity(1, [], resolve, reject)
            })
                .then(response => {
                    context.commit('setFeedActivity', {
                        activity: response
                    })
                    context.commit('setNumFeedActivityPages')
                })
        },
        loadResume(context) {
            return new Promise((resolve, reject) => {
                getAPI.get('/resume/latest/')
                    .then(response => {
                        var data = response.data;
                        data.summary = data.sections.filter(function (el) {
                            return el.heading.toLowerCase() === 'summary'
                        })[0].content;
                        data.sections = data.sections.filter(function (el) {
                            return el.heading.toLowerCase() !== 'summary'
                        })

                        context.commit('setResume', {resume: data})
                        resolve()
                    })
                    .catch(err => {
                        reject(err)
                    })
            })
        }
    }
})
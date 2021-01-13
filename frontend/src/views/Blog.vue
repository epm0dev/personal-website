<template>
    <div>
        <NavBar></NavBar>
        <div v-cloak class="container" v-if="blogPosts[0].posts.length !== 0">
            <h1 class="text-center mt-3 mb-0">Blog</h1>
            <div class="container-fluid">
                <hr class="mb-0">
                <BlogPostPage :class="{'d-none': currentPage !== postPage.page}" v-for="postPage in blogPosts"
                              :key="postPage.page" :blogPage="postPage"></BlogPostPage>
                <hr>
                <nav class="d-flex justify-content-center">
                    <ul class="pagination">
                        <li @click="prevPage" class="page-item" :class="{disabled: currentPage === 1}">
                            <a class="page-link" href="#">Previous</a>
                        </li>
                        <li @click="setPage(postPage.page)" :class="{active: currentPage === postPage.page}"
                            v-for="postPage in blogPosts" :key="postPage.page" class="page-item">
                            <a class="page-link" href="#">{{ postPage.page }}</a>
                        </li>
                        <li @click="nextPage" class="page-item" :class="{disabled: currentPage === numBlogPostPages}">
                            <a class="page-link" href="#">Next</a>
                        </li>
                    </ul>
                </nav>
            </div>
        </div>
        <div v-else class="container mt-5">
            <h5 class="text-center">It looks like there's nothing here, or the page's content failed to load properly. Please try again later.</h5>
        </div>
    </div>
</template>

<script>
import NavBar from '../components/NavBar'
import BlogPostPage from "../components/BlogPostPage";
import {mapState} from 'vuex'

export default {
    name: "Blog",
    components: {
        NavBar,
        BlogPostPage
    },
    data() {
        return {
            currentPage: 1
        }
    },
    computed: mapState(['blogPosts', 'numBlogPostPages']),
    methods: {
        prevPage() {
            if (this.currentPage !== 1) {
                this.currentPage--;
            }
        },
        nextPage() {
            if (this.currentPage !== this.numBlogPostPages) {
                this.currentPage++;
            }
        },
        setPage(page) {
            this.currentPage = page;
        }
    },
    created() {
        this.$store.dispatch('loadBlogPosts')
    }
}
</script>

<style scoped>

</style>
<template>
    <div>
        <NavBar></NavBar>
        <div class="container">
            <h1 class="text-center mt-3 mb-0">Blog</h1>
            <div class="container-fluid">
                <hr class="mb-0">
                <BlogPostPage v-for="postPage in blogPosts" :key="postPage.page" :blogPage="postPage"></BlogPostPage>
                <hr>
                <nav>
                    <ul class="pagination">
                        <li class="page-item"><a class="page-link" href="#">Previous</a></li>
                        <li class="page-item"><a class="page-link" href="#">1</a></li>
                        <li class="page-item"><a class="page-link" href="#">2</a></li>
                        <li class="page-item"><a class="page-link" href="#">3</a></li>
                        <li class="page-item"><a class="page-link" href="#">Next</a></li>
                    </ul>
                </nav>
            </div>
        </div>
    </div>
</template>

<script>
import NavBar from '../components/NavBar'
import BlogPostPage from "@/components/BlogPostPage";
import {mapState} from 'vuex'

export default {
    name: "Blog",
    components: {
        NavBar,
        BlogPostPage
    },
    computed: mapState(['blogPosts']),
    created() {
        this.$store.dispatch('loadBlogPosts')
    }
}
</script>

<style scoped>

</style>
<template>
<div>
    <BlogPost v-for="post in blogPage.posts" :key="post.pk" :post="post"></BlogPost>
</div>
</template>

<script>
import BlogPost from "@/components/BlogPost";

export default {
    name: "BlogPostPage",
    components: {
        BlogPost
    },
    props: {
        blogPage: {required: true, type: Object}
    }
}
</script>

<style scoped>

</style>
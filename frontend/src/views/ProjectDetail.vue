<template>
    <div>
        <NavBar></NavBar>
        <div v-cloak class="container">
            <div class="d-flex align-content-center justify-content-end">
                <router-link id="projectsPageLink" class="nav-link active p-0 mt-1 me-2" :to="{ name: 'projects' }">&lt;&lt;
                    Return to Projects
                </router-link>
            </div>
            <h1>{{ project.title }}</h1>
            <div>
                <small class="text-muted">Created {{ project.date_created }} at {{ project.time_created }}</small>
            </div>
            <div>
                <small class="text-muted">Last updated {{ project.date_changed }} at {{ project.time_changed }}</small>
            </div>
            <hr>
            <p class="lead">{{ project.description }}</p>
            <p v-for="(paragraph, index) in descriptionFormatted" :key="index">{{paragraph}}</p>
            <div v-if="project.posts.length > 0">
                <hr>
                <h5 class="ms-1">Related Blog Posts</h5>
                <BlogPost v-for="post in project.posts" :key="post.pk" :post="post" class="px-0"></BlogPost>
            </div>
        </div>
    </div>
</template>

<script>
import NavBar from "@/components/NavBar";
import BlogPost from "@/components/BlogPost";
import {mapState} from "vuex";

export default {
    name: "ProjectDetail",
    components: {
        NavBar,
        BlogPost
    },
    computed: {
        ...mapState(['project']),
        descriptionFormatted () {
            let description = this.project.description_verbose
            return description.split('\r\n')
        }
    },
    created() {
        this.$store.dispatch('loadProject', {id: this.$route.params.id})
    }
}
</script>

<style scoped>
#projectsPageLink {
    color: black;
    opacity: 55%;
    transition: opacity 0.15s linear;
}

#projectsPageLink:hover {
    opacity: 85%;
}
</style>
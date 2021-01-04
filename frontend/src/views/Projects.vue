<template>
    <div>
        <NavBar></NavBar>
        <div class="container">
            <h1 class="text-center mt-3 mb-0">My Projects</h1>
            <ProjectsCategory category="Featured" :projects="projects.featured"></ProjectsCategory>
            <ProjectsCategory :projects="projects.general"></ProjectsCategory>
            <ProjectsCategory category="Archived" :projects="projects.archived"></ProjectsCategory>
        </div>
    </div>
</template>

<script>
import NavBar from '../components/NavBar'
import {mapState} from 'vuex'
import ProjectsCategory from "@/components/ProjectsCategory";

export default {
    name: "Projects",
    components: {
        NavBar,
        ProjectsCategory
    },
    computed: mapState(['projects']),
    created() {
        this.$store.dispatch('loadProjects')
    }
}
</script>

<style scoped>

</style>
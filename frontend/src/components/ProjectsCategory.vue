<template>
<div v-if="projects.length > 0">
    <div class="row">
        <div class="col-auto" v-if="category">
            <h2 class="my-2">{{category}}</h2>
        </div>
        <div class="col d-flex align-items-center">
            <hr class="flex-fill mt-4" v-if="category">
            <hr class="flex-fill" v-if="!category">
        </div>
    </div>
    <div class="container-fluid">
        <div class="row">
            <div class="col-12 col-sm-6 col-lg-4 col-xxl-3 mb-3" v-for="project in projects" :key="project.url">
                <ProjectCard class="h-100" :project="project"></ProjectCard>
            </div>
        </div>
    </div>
</div>
</template>

<script>
import ProjectCard from "@/components/ProjectCard";

export default {
    name: "ProjectsCategory",
    components: {
        ProjectCard
    },
    props: {
        category: {required: false, type: String},
        projects: {required: true, type: Array}
    }
}
</script>

<style scoped>

</style>
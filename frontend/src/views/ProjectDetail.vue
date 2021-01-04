<template>
    <div>
        <NavBar></NavBar>
        <div class="container mt-3">
            <h1>{{project.title}}</h1>
            <div>
                <small class="text-muted">Created {{project.date_created}} at {{project.time_created}}</small>
            </div>
            <div>
                <small class="text-muted">Last updated {{project.date_changed}} at {{project.time_changed}}</small>
            </div>
            <hr>
            <p class="lead">{{project.description}}</p>
            <p>{{project.description_verbose}}</p>
        </div>
    </div>
</template>

<script>
import NavBar from "@/components/NavBar";
import {mapState} from "vuex";

export default {
    name: "ProjectDetail",
    components: {
        NavBar
    },
    computed: mapState(['project']),
    created() {
        this.$store.dispatch('loadProject', { id: this.$route.params.id })
    }
}
</script>

<style scoped>

</style>
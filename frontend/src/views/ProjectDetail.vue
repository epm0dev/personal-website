<template>
    <div>
        <NavBar></NavBar>
        <div class="container">
            <h1>{{project.title}}</h1>
            <div>
                <small class="text-muted">This project was created {{project.datetime_created}}</small>
            </div>
            <div>
                <small class="text-muted">This project was last updated {{project.datetime_changed}}</small>
            </div>
            <hr>
            <p>{{project.description}}</p>
            <hr>
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
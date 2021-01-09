<template>
    <div>
        <NavBar></NavBar>
        <div class="container">
            <div class="container-fluid pt-4">
                <div class="card">
                    <div class="card-header bg-primary text-light">
                        <h2 class="mb-0">About Me</h2>
                    </div>
                    <div class="card-body">
                        <div class="row">
                            <div class="col-12 col-md-4">
                                <div class="d-flex justify-content-center">
                                    <img src="../../public/portrait.png" class="img-fluid rounded-circle py-2 px-md-4"
                                         alt="portrait">
                                </div>
                                <h3 class="text-center m-0">Ethan Mancini</h3>
                                <hr class="d-md-none">
                            </div>
                            <div class="col-12 col-md-8">
                                <div class="d-flex flex-column justify-content-center h-100">
                                    <p class="lead fs-2 m-0 p-2 py-0 py-md-2">
                                        {{ resume.summary }}
                                    </p>
                                </div>
                            </div>
                        </div>
                        <hr>
                        <div class="row">
                            <div class="col-12">
                                <ResumeAccordion :resume="resume"></ResumeAccordion>
                            </div>
                        </div>
                    </div>
                    <div class="card-footer d-flex justify-content-center">
                        <a target="_blank" href="https://github.com/epm0dev">
                            <i class="fab fa-github-square fa-3x"></i>
                        </a>
                        <a target="_blank" href="https://www.linkedin.com/in/epm0dev/">
                            <i class="fab fa-linkedin fa-3x"></i>
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import NavBar from '../components/NavBar'
import ResumeAccordion from "../components/ResumeAccordion";
import {mapState} from 'vuex'

export default {
    name: "Home",
    components: {
        NavBar,
        ResumeAccordion
    },
    computed: mapState(['resume']),
    created() {
        this.$store.dispatch('loadResume')
    }
}
</script>

<style scoped>
a {
    color: black;
    opacity: 75%;
    margin: 0 0.5rem;
    transition: all 0.15s linear;
}

a:hover {
    opacity: 55%;
}
</style>
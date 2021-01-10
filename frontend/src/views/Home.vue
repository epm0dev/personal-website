<template>
    <div>
        <NavBar></NavBar>
        <div class="container">
            <div class="container-fluid pt-4 pb-4">
                <div class="card border border-2">
                    <div class="card-header bg-primary text-light">
                        <h2 class="mb-0">About Me</h2>
                    </div>
                    <div class="card-body pt-2">
                        <div class="row">
                            <div class="col-12 col-md-4">
                                <div class="row">
                                    <div class="col-2 col-lg-4 px-0">
                                        <img src="../../public/portrait.png"
                                             class="img-fluid rounded-circle ml-3"
                                             alt="portrait">
                                    </div>
                                    <div class="col-10 col-lg-8 pt-4 pt-lg-0">
                                        <h3 class="text-start text-lg-center m-0 align-text-bottom h-100">Ethan Mancini</h3>
                                    </div>
                                </div>
                            </div>
                            <div class="col-12">
                                <hr class="d-md-none my-2">
                            </div>
                            <div class="col-12 col-md-8">
                                <div class="d-flex flex-column justify-content-center h-100">
                                    <p class="lead fs-5 fs-md-4 fs-lg-3 m-0 p-2 py-0 py-md-2">
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
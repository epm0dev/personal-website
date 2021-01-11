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
                                <div class="row px-2">
                                    <div class="col-10 col-md-12 d-flex align-items-center d-md-none">
                                        <h3 class="text-start m-0">Ethan Mancini</h3>
                                    </div>
                                    <div class="col-2 col-md-12">
                                        <img src="../../public/portrait.png"
                                             class="img-fluid rounded-circle p-md-2 px-xl-4"
                                             alt="portrait">
                                    </div>
                                    <div class="col-12 d-none d-md-flex align-items-center justify-content-center">
                                        <h3 class="mb-0">Ethan Mancini</h3>
                                    </div>
                                </div>
                            </div>
                            <div class="col-12 d-md-none">
                                <hr class="my-2">
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
                            <div class="col-12 mt-3">
                                <a class="resumeDownload bg-dark" href="http://localhost:8000/api/resume/latest/download/"
                                   download>
                                    <button type="button" class="btn btn-primary w-100">
                                        <i class="fas fa-download me-1"></i>
                                        Download Resume
                                    </button>
                                </a>
                            </div>
                        </div>
                    </div>
                    <div class="card-footer d-flex justify-content-center">
                        <a class="socialLink" target="_blank" href="https://github.com/epm0dev">
                            <i class="fab fa-github-square fa-2x"></i>
                        </a>
                        <a class="socialLink" target="_blank" href="https://www.linkedin.com/in/epm0dev/">
                            <i class="fab fa-linkedin fa-2x"></i>
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
.socialLink {
    color: black;
    opacity: 55%;
    margin: 0 0.25rem;
    transition: all 0.15s linear;
}

.socialLink:hover {
    opacity: 75%;
}

.resumeDownload {
 text-decoration: none;
}
</style>
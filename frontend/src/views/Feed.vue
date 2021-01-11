<template>
    <div>
        <NavBar></NavBar>
        <div v-cloak class="container">
            <h1 class="text-center mt-3 mb-0">Feed</h1>
            <div class="container">
                <hr class="mb-0">
                <ActivityPage :class="{'d-none': currentPage !== activityPage.page}"
                              v-for="activityPage in feedActivity"
                              :key="activityPage.page" :activityPage="activityPage"></ActivityPage>
                <hr>
                <nav class="d-flex justify-content-center">
                    <ul class="pagination">
                        <li @click="prevPage" class="page-item" :class="{disabled: currentPage === 1}">
                            <a class="page-link" href="#">Previous</a>
                        </li>
                        <li @click="setPage(activityPage.page)" :class="{active: currentPage === activityPage.page}"
                            v-for="activityPage in feedActivity" :key="activityPage.page" class="page-item">
                            <a class="page-link" href="#">{{ activityPage.page }}</a>
                        </li>
                        <li @click="nextPage" class="page-item"
                            :class="{disabled: currentPage === numFeedActivityPages}">
                            <a class="page-link" href="#">Next</a>
                        </li>
                    </ul>
                </nav>
            </div>
        </div>
    </div>
</template>

<script>
import NavBar from '../components/NavBar'
import ActivityPage from "../components/ActivityPage";
import {mapState} from 'vuex'

export default {
    name: "Feed",
    components: {
        NavBar,
        ActivityPage
    },
    data() {
        return {
            currentPage: 1
        }
    },
    computed: mapState(['feedActivity', 'numFeedActivityPages']),
    methods: {
        prevPage() {
            if (this.currentPage !== 1) {
                this.currentPage--;
            }
        },
        nextPage() {
            if (this.currentPage !== this.numFeedActivityPages) {
                this.currentPage++;
            }
        },
        setPage(page) {
            this.currentPage = page;
        }
    },
    created() {
        this.$store.dispatch('loadFeedActivity')
    }
}
</script>

<style scoped>

</style>
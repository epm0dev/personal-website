<template>
<div>
    <Activity v-for="activity in activityPage.activity" :key="activity.pk" :activity="activity"></Activity>
</div>
</template>

<script>
import Activity from "./Activity";

export default {
    name: "ActivityPage",
    components: {
        Activity
    },
    props: {
        activityPage: {required: true, type: Object}
    }
}
</script>

<style scoped>

</style>
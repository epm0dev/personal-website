<template>
    <div class="container px-2 mt-3">
        <div class="card shadow-sm">
            <div class="card-body">
                <h5>{{ activity.text }}</h5>
                <div>
                    <small class="text-muted">Created {{ activity.date_created }} at {{ activity.time_created }}</small>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "Activity",
    props: {
        activity: {required: true, type: Object}
    }
}
</script>

<style scoped>

</style>
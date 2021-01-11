<template>
    <div class="container mt-3" :class="{'px-2': this.$router.currentRoute.fullPath.startsWith('/blog/')}">
        <div class="card shadow-sm">
            <div class="card-body">
                <h3>{{ post.title }}</h3>
                <h5 class="card-subtitle text-muted mb-2">{{ post.subtitle }}</h5>
                <p class="card-text">{{ post.contents }}</p>
                <div>
                    <small class="text-muted">Created {{post.date_changed}} at {{post.time_changed}}</small>
                </div>
                <div>
                    <small class="text-muted">Last updated {{post.date_changed}} at {{post.time_changed}}</small>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'BlogPost',
    props: {
        post: {required: true, type: Object}
    }
}
</script>

<style scoped>

</style>
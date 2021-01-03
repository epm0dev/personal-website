<template>
    <div class="container px-2 mt-3">
        <div class="card">
            <div class="card-body">
                <h3>{{ post.title }}</h3>
                <h5 class="card-subtitle text-muted mb-2">{{ post.subtitle }}</h5>
                <p class="card-text">{{ post.contents }}</p>
                <div>
                    <small class="text-muted">This post was created {{ post.datetime_created }}</small>
                </div>
                <div>
                    <small class="text-muted">This post was last updated {{ post.datetime_changed }}</small>
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
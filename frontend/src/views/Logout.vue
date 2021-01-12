<template>
    <div v-cloak>
        <h1 class="mt-5 text-center">Logging out...</h1>
    </div>
</template>

<script>
export default {
    created() {
        this.$store.dispatch('userLogout')
            .then(() => {
                this.$router.push({name: 'login'})
            })
    }
}
</script>

<style scoped>
</style>
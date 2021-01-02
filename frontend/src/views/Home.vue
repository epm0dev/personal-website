<template>
    <div>
        <NavBar></NavBar>
    </div>
</template>

<script>
import NavBar from '../components/NavBar'

export default {
    name: "Home",
    components: {
        NavBar
    },
    created() {
        /*
        this.$store.dispatch('userLogin', {
            username: 'admin',
            password: 'admin'
        })
         */
    }
}
</script>

<style scoped>

</style>
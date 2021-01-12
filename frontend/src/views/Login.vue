<template>
    <div>
        <NavBar></NavBar>
        <div v-cloak class="container-lg mt-3 px-5">
            <div class="mx-5 px-5">
                <h1 class="text-center">Please Sign In</h1>
                <hr>
                <p v-if="incorrectAuth" class="text-warning">Incorrect username or password entered - please try
                    again</p>
                <form v-on:submit.prevent="login">
                    <div class="row mt-3">
                        <div class="form-group col">
                            <label for="user" class="form-label">Username</label>
                            <input type="text" name="username" id="user" v-model="username" class="form-control">
                        </div>
                    </div>
                    <div class="row mt-3">
                        <div class="form-group col">
                            <label for="pass" class="form-label">Password</label>
                            <input type="password" name="password" id="pass" v-model="password" class="form-control">
                        </div>
                    </div>
                    <div class="row mt-3">
                        <div class="col form-group">
                            <div class="d-grid gap-2">
                                <button class="btn btn-lg btn-primary mb-2 form-control" type="submit">Login</button>
                            </div>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import NavBar from "../components/NavBar";

export default {
    name: 'Login',
    components: {NavBar},
    data() {
        return {
            username: '',
            password: '',
            incorrectAuth: false
        }
    },
    methods: {
        login() {
            this.$store.dispatch('userLogin', {
                username: this.username,
                password: this.password
            })
                .then(() => {
                    this.$router.push({name: 'admin'})
                })
                .catch(err => {
                    console.log(err)
                    this.incorrectAuth = true
                })
        }
    }
}
</script>

<style scoped>
</style>
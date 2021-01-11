<template>
    <div>
        <NavBar></NavBar>
        <div class="container mt-3">
            <div v-if="!formSubmitted">
                <h1 class="text-center">Contact Me</h1>
                <hr class="mx-1">
                <form @submit.prevent="submitForm" class="mx-1">
                    <div class="row mt-3">
                        <div class="col form-group">
                            <label for="first-name" class="mb-2">First Name</label>
                            <input v-model="first_name" id="first-name" type="text" class="form-control" required
                                   maxlength="50"
                                   placeholder="John">
                        </div>
                        <div class="col form-group">
                            <label for="last-name" class="mb-2">Last Name</label>
                            <input v-model="last_name" id="last-name" type="text" class="form-control" required
                                   maxlength="50"
                                   placeholder="Doe">
                        </div>
                        <div class="col-1 form-group">
                            <label for="middle-initial" class="mb-2">M.I.</label>
                            <input v-model="middle_initial" id="middle-initial" type="text" class="form-control"
                                   maxlength="1" placeholder="P">
                        </div>
                    </div>
                    <div class="row mt-3">
                        <div class="col form-group">
                            <label for="email" class="mb-2">Email</label>
                            <input v-model="email_address" id="email" type="email" class="form-control" required
                                   placeholder="email@example.com">
                        </div>
                        <div class="col form-group">
                            <label for="phone" class="mb-2">Phone Number</label>
                            <input v-model="phone_number" id="phone" type="tel" class="form-control"
                                   pattern="[0-9]{3}-[0-9]{3}-[0-9]{4}"
                                   placeholder="123-456-7890">
                        </div>
                    </div>
                    <div class="row mt-3">
                        <div class="col form-group">
                            <label for="message" class="mb-2">Message</label>
                            <textarea v-model="message" id="message" class="form-control" required spellcheck="true"
                                      maxlength="5000"
                                      placeholder="Enter the contents of your message, up to 5000 characters."></textarea>
                        </div>
                    </div>
                    <div class="row mt-3">
                        <div class="col form-group">
                            <div class="d-grid gap-2">
                                <button type="submit" class="btn btn-lg btn-primary mb-2">Submit</button>
                            </div>
                        </div>
                    </div>
                </form>
            </div>
            <div v-if="formSubmitted" class="px-5">
                <h1>Contact Form Submitted</h1>
                <hr>
                <p class="lead">Thanks for reaching out! I will get in contact with you as soon as possible!</p>
                <div class="d-grid gap-2">
                    <button @click="resetForm" class="btn btn-secondary">Close</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import NavBar from '../components/NavBar'
import {getAPI} from "@/axios-api";

export default {
    name: "Contact",
    components: {
        NavBar
    },
    data() {
        return {
            first_name: '',
            last_name: '',
            middle_initial: '',
            email_address: '',
            phone_number: '',
            message: '',
            formSubmitted: false
        }
    },
    methods: {
        submitForm() {
            return new Promise((resolve, reject) => {
                getAPI.post('/contact/', {
                    first_name: this.first_name,
                    last_name: this.last_name,
                    middle_initial: this.middle_initial,
                    email_address: this.email_address,
                    phone_number: this.phone_number,
                    message: this.message
                })
                    .then(response => {
                        console.log(response)
                        this.formSubmitted = true
                        resolve()
                    })
                    .catch(err => {
                        reject(err)
                    })
            })
        },
        resetForm() {
            this.first_name = ''
            this.last_name = ''
            this.middle_initial = ''
            this.email_address = ''
            this.phone_number = ''
            this.message = ''
            this.formSubmitted = false
        }
    }
}
</script>

<style scoped>

</style>
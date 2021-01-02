<template>
    <div>
        <NavBar></NavBar>
        <div class="container mt-3">
            <h1 class="text-center">Contact Me</h1>
            <form>
                <div class="row mt-3">
                    <div class="col form-group">
                        <label for="first-name" class="mb-2">First Name</label>
                        <input id="first-name" type="text" class="form-control" required placeholder="John">
                    </div>
                    <div class="col form-group">
                        <label for="last-name" class="mb-2">Last Name</label>
                        <input id="last-name" type="text" class="form-control" required placeholder="Doe">
                    </div>
                    <div class="col-1 form-group">
                        <label for="middle-initial" class="mb-2">M.I.</label>
                        <input id="middle-initial" type="text" class="form-control" maxlength="1" placeholder="P">
                    </div>
                </div>
                <div class="row mt-3">
                    <div class="col form-group">
                        <label for="email" class="mb-2">Email</label>
                        <input id="email" type="email" class="form-control" required placeholder="email@example.com">
                    </div>
                    <div class="col form-group">
                        <label for="phone" class="mb-2">Phone Number</label>
                        <input id="phone" type="tel" class="form-control" pattern="[0-9]{3}-[0-9]{3}-[0-9]{4}"
                               placeholder="123-456-7890">
                    </div>
                </div>
                <div class="row mt-3">
                    <div class="col form-group">
                        <label for="message" class="mb-2">Message</label>
                        <textarea id="message" class="form-control" required spellcheck="true"
                                  placeholder="Enter the contents of your message"></textarea>
                    </div>
                </div>
                <div class="row mt-3">
                    <div class="col form-group">
                        <div class="d-grid gap-2 px-5">
                            <button type="submit" class="btn btn-lg btn-primary mb-2">Submit</button>
                        </div>
                    </div>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
import NavBar from '../components/NavBar'

export default {
    name: "Contact",
    components: {
        NavBar
    },
}
</script>

<style scoped>

</style>
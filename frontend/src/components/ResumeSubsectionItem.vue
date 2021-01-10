<template>
<div>
    <div>
        <strong>{{subsection.heading}}</strong>
    </div>
    <div v-if="subsection.subtext">
        <em>{{subsection.subtext}}</em>
    </div>
    <div>
        <ul class="mb-0">
            <li v-for="p in subsection.paragraphs" :key="p">{{p}}</li>
        </ul>
    </div>
</div>
</template>

<script>
export default {
    name: "ResumeSubsectionItem",
    props: {
        subsection: {required: true, type: Object}
    }
}
</script>

<style scoped>

</style>
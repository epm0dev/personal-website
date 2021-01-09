<template>
    <div class="accordion" id="resumeAccordion">
        <ResumeSectionItem v-for="section in resume.sections" :key="section.pk" :section="section"></ResumeSectionItem>
    </div>
</template>

<script>
import ResumeSectionItem from "@/components/ResumeSectionItem";

export default {
    name: "ResumeAccordion",
    components: {
        ResumeSectionItem
    },
    props: {
        resume: {required: true, type: Object}
    }
}
</script>

<style scoped>

</style>
<template>
    <div class="accordion-item">
        <h2 class="accordion-header" :id="headerId">
            <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse"
                    :data-bs-target="contentIdHash" aria-expanded="true"
                    :aria-controls="contentId">
                {{ section.heading }}
            </button>
        </h2>
        <div :id="contentId" class="accordion-collapse collapse" :aria-labelledby="headerId"
             data-bs-parent="#resumeAccordion">
            <div class="accordion-body pb-0">
                <div v-if="section.subsections.length !== 0">
                    <ResumeSubsectionItem v-for="subsection in section.subsections" :key="subsection.pk"
                                          :subsection="subsection"></ResumeSubsectionItem>
                </div>
                <div v-if="section.subsections.length === 0">
                    <ul class="mb-0 pb-3">
                        <li v-for="p in section.paragraphs" :key="p">{{ p }}</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import ResumeSubsectionItem from "@/components/ResumeSubsectionItem";

export default {
    name: "ResumeSectionItem",
    components: {
        ResumeSubsectionItem
    },
    props: {
        section: {required: true, type: Object}
    },
    computed: {
        headerId() {
            return 'header' + this.section.pk
        },
        contentId() {
            return 'content' + this.section.pk
        },
        contentIdHash() {
            return '#content' + this.section.pk
        }
    }
}
</script>

<style scoped>

</style>
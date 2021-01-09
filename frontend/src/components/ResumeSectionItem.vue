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
            <div class="accordion-body">
                {{section.content}}
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "ResumeSectionItem",
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
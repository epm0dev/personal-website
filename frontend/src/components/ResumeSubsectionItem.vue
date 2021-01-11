<template>
<div class="pb-3">
    <div>
        <strong>{{subsection.heading}}</strong>
    </div>
    <div v-if="subsection.subtext">
        <em>{{subsection.subtext}}</em>
    </div>
    <div>
        <ul class="mb-0">
            <li v-for="(p, index) in formattedParagraphs" :key="index">{{p.it}}
                <ul v-if="p.nested">
                    <li v-for="(n, index) in p.nested" :key="index">
                        {{n}}
                    </li>
                </ul>
            </li>
        </ul>
    </div>
</div>
</template>

<script>
export default {
    name: "ResumeSubsectionItem",
    props: {
        subsection: {required: true, type: Object}
    },
    computed: {
        formattedParagraphs () {
            let pars = []
            let i = 0;
            let len = this.subsection.paragraphs.length;
            while (i < len) {
                if (i + 1 < len && Array.isArray(this.subsection.paragraphs[i + 1])) {
                    pars.push({
                        it: this.subsection.paragraphs[i],
                        nested: this.subsection.paragraphs[i + 1]
                    });
                    i++;
                } else {
                    pars.push({
                        it: this.subsection.paragraphs[i],
                        nested: null
                    });
                }
                i++;
            }
            return pars;
        }
    }
}
</script>

<style scoped>

</style>
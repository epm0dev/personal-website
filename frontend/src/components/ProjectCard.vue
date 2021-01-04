<template>
<div class="card">
    <div class="card-header bg-primary bg-gradient text-light">
        <h3 class="mb-0">{{project.title}}</h3>
    </div>
    <div v-if="!isArchived" class="card-header text-center" :class="phaseColor">
        <h5 class="mb-0">{{project.phase}}</h5>
    </div>
    <div class="card-body">
        <div>
            <span class="badge rounded-pill bg-primary bg-gradient mx-1" v-for="keyword in project.keywords" :key="keyword.pk">{{ keyword.word }}</span>
        </div>
        <div :class="{'mt-3': project.keywords.length > 0}">
            {{project.description}}
        </div>
    </div>
    <div class="card-footer text-muted text-end">
        <router-link :to="{ name: 'project-detail', params: { id: project.pk } }">
            Read More <i class="fas fa-external-link-alt"></i>
        </router-link>
    </div>
</div>
</template>

<script>
export default {
name: "ProjectCard",
    props: {
        project: {required: true, type: Object}
    },
    computed: {
        isArchived () {
            return this.project.category === 'Archived'
        },
        phaseColor () {
            return {
                'bg-info': this.project.phase === 'Design',
                'bg-warning': this.project.phase === 'Implementation',
                'bg-success': this.project.phase === 'Integration',
                'bg-secondary': this.project.phase === 'Maintenance',
                'text-light': this.project.phase === 'Integration' || this.project.phase === 'Maintenance'
            }
        }
    }
}
</script>

<style scoped>

</style>
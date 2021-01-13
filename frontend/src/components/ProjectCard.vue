<template>
    <div class="card transition shadow-sm" @mouseover="hover = true" @mouseleave="hover = false" :class="{hovered: hover}">
        <div class="card-header bg-primary text-light">
            <h3 class="mb-0">{{ project.title }}</h3>
        </div>
        <div v-if="!isArchived" class="card-header text-center py-1" :class="phaseColor">
            <h5 class="mb-0">{{ project.phase }}</h5>
        </div>
        <div class="card-body p-2">
            <div class="row g-1 justify-content-center">
                <div class="col-auto" v-for="keyword in project.keywords"
                     :key="keyword.pk">
                    <span class="badge rounded-pill bg-secondary">{{ keyword.word }}</span>
                </div>
            </div>
            <div :class="{'mt-2': project.keywords.length > 0}" class="px-1 pb-1">
                {{ project.description }}
            </div>
        </div>
        <div class="card-footer text-muted text-end">
            <router-link id="readMore" :to="{ name: 'project-detail', params: { id: project.pk } }">
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
    data() {
        return {
            hover: false
        }
    },
    computed: {
        isArchived() {
            return this.project.category === 'Archived'
        },
        phaseColor() {
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
.transition {
    transition: all 0.15s ease;
}

.hovered {
    transform: scale(1.1);
}

#readMore {
    color: black;
    opacity: 75%;
    transition: all 0.15s linear;
    text-decoration: none;
}

#readMore:hover {
    opacity: 55%;
}
</style>
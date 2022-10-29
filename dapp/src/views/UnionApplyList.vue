<template>
        <div class="flex flex-row h-full">
        <AppNav :union_id="union_id" :app_name="'apply'"/>
        <div class="w-full flex-grow">
          <div v-for="(apply, idx) in applys">
                <div>{{apply.desc}}</div>
                <div><button @click="approve(idx)">OK</button></div>
            </div>
        </div>
    </div>
</template>
<script>
import { unionapply_find, unionapply_patch } from '../daoverse_apis'
import AppNav  from '../components/AppNav'


export default {
    name: 'UnionApplyList',
    components: {
            AppNav
    },
    data() {
        return {
            union_id: '',
            applys: [],
            dailog: false,
            dailog_data: null,
            apply_content: ''
        }
    },
    mounted() {
        this.union_id = this.$route.params.union_id;
        unionapply_find({ union: this.union_id}, {})
            .then(res => {
                console.log(res.data)
                this.applys = res.data;
            })
    },
    methods: {
        approve(idx) {
            console.log(idx)
            let apply = this.applys[idx];

            unionapply_patch(apply.id, {}, {certified:1})
                .then(res=>{
                    console.log(res)
                })
        }
    }
}
</script>
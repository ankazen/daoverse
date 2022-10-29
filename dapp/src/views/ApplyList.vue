<template>
    <div class="about w-full">
        <div class="p-2" v-for="apply in applys">
            <div>{{apply.desc}}</div>
            <div><button @click="certify(apply)">OK</button></div>
        </div>
    </div>
</template>
<script type="text/javascript">
import { apply_find, apply_patch } from '../daoverse_apis'
export default {
    props: ['union'],
    data() {
        return {
            applys: []
        }
    },
    mounted() {
        apply_find({}, {})
            .then(res => {
                this.applys = res.data;
            })
    },
    methods: {
        certify(apply) {
            apply_patch(apply.id, {}, { certified: 1 })
                .then(res => {
                    console.log(res);
                })
                .catch(res=>{
                  console.log(res)
                })
        }
    }
}
</script>
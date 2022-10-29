<template>
    <div class="flex flex-row h-full">
        <div class="bg-green-400 w-80 flex-none h-full">
            <div class="h-60 p-2 bg-green-300 m-4 round"></div>
            <div class="flex flex-row">
                <div v-for="(uu, idx) in unionusers" class="w-20 h-20 bg-green-200 m-4">
                {{uu.union.name}}
            </div>
            </div>
            
        </div>
        <div class="w-full">
            <div class="h-12 bg-green-100 w-full">
            </div>
            <div v-for="(union, idx) in unions" class="w-full bg-white p-2">
                <div class="w-full">
                    <div class="flex flex-row hover:bg-green-100 p-2">
                        <div class="w-24 h-24 bg-green-200 flex-none">{{union.name}}</div>
                        <div class="flex-grow"></div>
                        <div class="flex-none w-24" ><button class="px-4 py-2 bg-green-300" @click="showDailog(union)">Apply</button></div>
                        <div class="flex-none w-24" ><button class="px-4 py-2 bg-green-300" @click="selectUnion(union)">View</button></div>
                    </div>
                </div>
            </div>
        </div>
        <div class="bg-black w-full h-full top-0 left-0 fixed content-center flex opacity-80" v-show="dailog">
            <div class="p-4 w-3/6 h-3/6 m-auto bg-white flex flex-col opacity-100">
                <textarea class="p-2 h-5/6 w-full outline-green" v-model="apply_content"></textarea>
                <div>
                    <button class="px-4 py-1.5 w-20 rounded bg-green-400" @click="createApply()">Apply</button>
                    <button class="px-4 py-1.5 w-20 rounded bg-green-400" @click="closeDailog()">X</button>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
// @ is an alias to /src
import { union_find, unionapply_create, unionuser_find } from '../daoverse_apis'

export default {
    name: 'HomeView',
    components: {},
    data() {
        return {
            unions: [{ name: 'A', link: '/union/A' }],
            unionusers: [],
            dailog: false,
            apply_content: '',
            dailog_data: null,
        }
    },
    mounted() {
        union_find({}, {})
            .then(res => {
                this.unions = res.data;
            })
        unionuser_find({}, {})
            .then(res => {
                this.unionusers = res.data;
            })
    },
    methods: {
        selectUnion(union) {
            this.$router.push({name:'union', params:{union_id:union.id}})
        },
        createApply() {
          unionapply_create({}, {union: this.dailog_data.id, desc: this.apply_content})
            .then(res=>{
                console.log(res);
                this.dailog = false;
                this.dailog_data = null;
            })
        },
        showDailog(union) {
            this.dailog_data = union;
            this.dailog = true;
        },
        closeDailog() {
            this.dailog = false
        }
    }
}
</script>
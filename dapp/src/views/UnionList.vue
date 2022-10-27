<template>
    <div class="p-4">
        <div v-for="item in unions" class="w-full">
            <div class="flex flex-row">
                <div class="m-4 bg-green-400 w-24 h-24 rounded flex-none">{{item.name}}</div>
                <div class="flex-grow"></div>
            </div>
            <div class="flex-none"><button class="bg-green-700 text-white px-4 py-2 rounded" @click="showDailog(item)">Apply</button></div>
            <hr class="w-full mt-4">
        </div>
        <div class="bg-black w-full h-full top-0 left-0 fixed content-center flex opacity-80" v-show="dailog">
            <div class="p-4 w-3/6 h-3/6 m-auto bg-white flex flex-col opacity-100">
                <textarea class="p-2 h-5/6 w-full outline-green" v-model="apply_content"></textarea>
                <div>
                    <button class="px-4 py-1.5 w-20 rounded bg-green-400" @click="createApply()">Apply</button>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import { union_find, apply_create} from '../daoverse_apis'

export default {
    name: 'HomeList',
    components: {},
    data() {
        return {
            unions: [{ name: 'A', link: '/union/A' }],
            dailog: false,
            dailog_data: null,
            apply_content: ''
        }
    },
    mounted() {
        union_find({}, {})
            .then(res => {
                this.unions = res.data;
            })
    },
    methods: {
        selectUnion(union) {
            this.union = union;
            console.log(this.union);
            console.log(this.unions)
            console.log(union)
        },
        selectContract(contract) {
            console.log(contract)
        },
        createApply() {
          apply_create({}, {union: this.dailog_data.id, desc: this.apply_content})
            .then(res=>{
                console.log(res);
                this.dailog = false;
                this.dailog_data = null;
            })
        },
        showDailog(union) {
            this.dailog_data = union;
            this.dailog = true;
        }
    }
}
</script>
<template>
    <div class="flex flex-row h-full">
        <AppNav :union_id="union_id" :app_name="app_id" />
        <div class="w-full flex-grow p-4">
            <div class="w-full ">
                <textarea v-model="file_summary" class="w-full h-40 text-sm"></textarea>
            </div>
            <hr class="p-4">
            <div class="w-full">
                <textarea v-model="abi" class="w-full h-40 text-sm"></textarea>
            </div>
            <hr class="p-4">
            <div class="w-full">
                {{address}}
            </div>
            <hr>
        </div>
    </div>
</template>
<script>
import { unoincontract_findOne } from '../daoverse_apis'
import AppNav from '../components/AppNav'
import { emitter } from '../global.js'
import { ethers } from 'ethers';

export default {
    components: {
        AppNav
    },
    data() {
        return {
            union_id: '',
            app_id: '',
            app:{},
            file_summary: '',
            address:'',
            contract: '',
            interface:null,
            abi: ''
        }
    },
    mounted() {
        console.log(this.$route)
        this.union_id = this.$route.params.union_id;
        this.app_id = this.$route.params.app_id;
        unoincontract_findOne(this.app_id, {}, {})
            .then(res => {
                console.log(res.data)
                this.app = res.data;
                this.file_summary = res.data.contract.file_summary;
                this.interface = JSON.parse(res.data.abi_content);
                this.address = res.data.address
                this.abi = this.interface.abi.join('\n');
                console.log(this.interface.abi)
                const provider = new ethers.providers.Web3Provider(window.ethereum)
                this.contract = new ethers.Contract(this.address, this.interface.abi, provider);
                console.log(this.contract)
            })
    },
    methods: {
    }
}
</script>
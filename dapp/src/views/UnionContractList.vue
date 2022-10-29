<template>
    <div class="flex flex-row h-full">
        <AppNav :union_id="union_id" :app_name="'contract'" />
        <div class="w-full flex-grow">
            <div v-for="(contract, idx) in contracts" class="p-4">
                <div class="text-left text-lg">{{contract.name}}</div>
                <div class="w-full h-40 hover:bg-green-100 m-2"><textarea class="w-full h-full p-2 hover:bg-green-100" v-model="contract.file_summary"></textarea></div>
                <div class="p-4"><button @click="installApp(idx)" class="px-4 py-2 rounded-sm bg-green-400 text-white showdom">Install</button></div>
                <hr>
            </div>
        </div>
        <div class="bg-black w-full h-full top-0 left-0 fixed content-center flex opacity-80" v-show="dailog">
            <div class="p-4 w-5/6 h-5/6 m-auto bg-white flex flex-col opacity-100">
                <div class="content-center">
                    <textarea v-model="contract.file_summary" class="h-40 w-full"></textarea>
                    <div class="flex flex-row">
                        <div class="relative flex-1">
                            <button @click="versions_show =!versions_show" class="bg-green-400">{{version}}</button><br>
                            <ul v-show="versions_show" class="absolute bg-white top-0 left-0 shadow-lg">
                                <li v-for="version in versions" @click="selectVersion(version)">{{version}}</li>
                            </ul>
                        </div>
                        <div class="flex-1"><button class="px-4 py-1.5 w-20 rounded bg-green-400" @click="Compile()">{{state}}</button></div>
                    </div>
                    <textarea v-model="compile_result.contracts.interface" class="w-full h-40"></textarea>
                </div>
                <div class="right-0 top-0">
                    <button class="px-4 py-1.5 w-20 rounded bg-green-400" @click="closeDailog()">X</button>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import { contract_find } from '../daoverse_apis'
import AppNav from '../components/AppNav'
import {emitter} from '../global.js'

export default {
    components: {
        AppNav
    },
    data() {
        return {
            union_id: '',
            contracts: [],
            dailog: false,
            contract: { file_summary: '' },
            dailog_content: '',
            versions: [],
            version: '',
            versions_show: false,
            state: 'Compile',
            compile_result: {contracts:{interface:''}}
        }
    },
    mounted() {
        this.union_id = this.$route.params.union_id;
        contract_find({}, {})
            .then(res => {
                console.log(res.data)
                this.contracts = res.data;
            })
        let _this = this;
        BrowserSolc.getVersions(function(soljsonSources, soljsonReleases) {
            for (let key in soljsonReleases) {
                _this.versions.push(soljsonReleases[key])
                _this.version = soljsonReleases[key]
            }
        });

    },
    methods: {
        installApp(idx) {
            this.dailog = true
            this.contract = this.contracts[idx]
            console.log(this.contract)
        },
        closeDailog() {
            this.dailog = false;
            this.dailog_data = '';
        },
        selectVersion(version) {
            this.version = version;
            this.versions_show = false
        },
        Compile() {
            console.log(this.version)
            this.state = 'Downloading'
            let _this = this
            BrowserSolc.loadVersion(this.version, function(compiler) {
                _this.state = 'Compiling'
                // console.log(this.contract)
                emitter.emit('Complie', {compiler: compiler, contract: _this.contract})
            });

            emitter.on('ComplieDone', result=>{
                console.log(result);
            });
            
        },
    }
}
</script>
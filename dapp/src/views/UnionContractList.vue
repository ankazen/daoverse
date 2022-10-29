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
            <div class="p-4 w-5/6 m-auto bg-white flex flex-col opacity-100">
                <div>
                    <textarea v-model="contract.file_summary" class="h-40 w-full"></textarea>
                    <div class="flex flex-row">
                        <div class="relative flex-1">
                            <button @click="versions_show =!versions_show" class="bg-green-400 px-4 py-1">{{version}}</button><br>
                            <ul v-show="versions_show" class="absolute bg-white top-0 left-0 shadow-lg">
                                <li v-for="version in versions" @click="selectVersion(version)">{{version}}</li>
                            </ul>
                        </div>
                        <div class="flex-1"><button class="px-4 py-1.5 w-30 rounded bg-green-400" @click="Compile()" :class="{'bg-gray-400':(state==='ComplieDone')}">{{state}}</button></div>
                    </div>
                </div>
                <div v-show="state==='ComplieDone'">
                    <hr class="p-2">
                    <textarea v-model="interfaces" class="w-full h-40"></textarea>
                    <div class="flex flex-row">
                        <div class="relative flex-1">
                            <button @click="networks_show =!networks_show" class="bg-green-400  px-4 py-1">{{network}}</button><br>
                            <ul v-show="networks_show" class="absolute bg-white top-0 left-0 shadow-lg">
                                <li v-for="network in networks" @click="selectNetwork(network)">{{network}}</li>
                            </ul>
                        </div>
                        <div class="flex-1"><button class="px-4 py-1.5 w-30 rounded bg-green-400" @click="deploy()" :class="{'bg-gray-400':(state==='DeployDone')}">{{state_deploy}}</button></div>
                    </div>
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
import { emitter } from '../global.js'
import { ContractFactory } from 'ethers';

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
            compile_result: { },
            interfaces: '',
            state_deploy: 'Deploy',
            networks: ['window.web3'],
            networks_show: false
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
        this.network = this.networks[0]

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
            this.state = 'Compile'
            console.log(this.state)
        },
        selectVersion(version) {
            this.version = version;
            this.versions_show = false
        },
        Compile() {
            console.log(this.version)
            this.state = 'Downloading'
            this.interfaces = ''
            // this.ComplieDone = false
            let _this = this
            BrowserSolc.loadVersion(this.version, function(compiler) {
                _this.state = 'Compiling'
                // console.log(this.contract)
                emitter.emit('Complie', { compiler: compiler, contract: _this.contract })
            });

            emitter.on('ComplieDone', result => {
                console.log(result);
                _this.state = 'ComplieDone'
                _this.compile_result = result
                for (let c in result.contracts) {
                    console.log(c)
                    _this.interfaces = result.contracts[c].interface
                }
            });

        },
        async deploy() {
            let abis = []

            for (let key in this.compile_result.contracts) {
                    // abis.push(this.compile_result.contracts[c].interface)
                    const provider = new ethers.providers.Web3Provider(window.ethereum)

                    await provider.send("eth_requestAccounts", []);
                    let signer = provider.getSigner();

                    let contract = this.compile_result.contracts[key]
                    let abi = contract['interface']
                    let bytecode = contract['bytecode']
                    let factory = new ContractFactory(abi, bytecode, signer)
                    console.log(factory)
                    const Contract = await factory.deploy();
                    console.log(Contract)
                    await Contract.deployTransaction.wait()
                    console.log(Contract)
                }

            // let abi = this.compile_result
            // let bytecode = data.bytecode
            // let signer = data.signer
            // let network = data.network

            // contract = await factory.deploy("ricmoo.eth", 42);
            // await contract.deployTransaction.wait()

            // console.log(contract)
            // emitter.emit('DeployDone', contract.address)
        }
    }
}
</script>
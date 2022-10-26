<template>
  <div class="about h-full">
    <h1>Welcome</h1>
    <button @click="connect">connect</button>
  </div>
</template>

<script type="text/javascript">
  import {userdata} from '../global'
  import { ethers } from "ethers";

  export default {
    methods: {
        async connect(i) {
            const provider = new ethers.providers.Web3Provider(window.ethereum)
            await provider.send("eth_requestAccounts", []);
            this.signer = provider.getSigner();
            console.log(this.signer);
            userdata.address = await this.signer.getAddress()
            this.$router.push({name:'home'})
        }
    }
}
</script>

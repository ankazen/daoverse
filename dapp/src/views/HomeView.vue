<template>
    <div class="flex flex-row h-full">
        <div class="h-full w-80 bg-green-400">
            <div><button @click="this.$router.push({name:'unions'})">+</button></div>
            <div class="flex flex-row p-4">
              <div v-for="item in unions" :class="(unoin===item? 'bg-green-200 w-20 h-20':'w-20 h-20')" @click="selectUnion(item)">{{item.name}}</div>
            </div>
        </div>
        <div class="flex-grow flex flex-row">
            <div class="w-60 bg-green-200">
                <div><button @click="this.$router.push({name:'contracts'})">+</button></div>
                <div v-for="contract in contracts">{{contract.name}}</div>
            </div>
            <div class="w-full"></div>
        </div>
    </div>
</template>
<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

export default {
    name: 'HomeView',
    components: {
        HelloWorld
    },
    data() {
        return {
            unions: [{ name: 'A', link: '/union/A' }],
            contracts: [{ name: 'dddd' }],
            union: 'A',
            contract: ''
        }
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
      }
    }
}
</script>
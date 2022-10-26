<template>
    <router-view />
<!--     <div class="flex flex-row h-full">
        <div class="h-full bg-green-400 w-96">
            <div class="round-lg w-48 h-48 m-auto">
                <img src="https://ts1.cn.mm.bing.net/th/id/R-C.d62e15da88951c4b61fb4703ce25d4e8?rik=VTsMAZtlbHyQxg&riu=http%3a%2f%2fstore.mdcgate.com%2fmarket%2fassets%2fimage%2ficon_user_default.png&ehk=u1%2fGzy4%2fUVv2WFKpvV9T1tJc8cJNN%2bb5I1n8rKl46Dw%3d&risl=&pid=ImgRaw&r=0">
            </div>
            <div class="w-full flex p-4" v-for="item in items">
                <div class="w-20 h-20 p-2 bg-white" @click="selectUnion(item)">
                    {{item.name}}
                </div>
            </div>
        </div>
        <div class="flex-grow">
            
        </div>
    </div> -->
</template>
<script type="text/javascript">
export default {
    data() {
        return {
            items: [{ name: 'A', link: '/union/A' }],
        }
    },
    // `mounted` 是生命周期钩子，之后我们会讲到
    mounted() {
    },
    methods: {
        selectUnion(i) {
            console.log(i)
            console.log(this.global)
            this.$router.push({ path: '/union/' + i.name, query: {} })
        }
    }
}
</script>
<style>
#app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    height: 100%;
}

nav {
    padding: 30px;
}

nav a {
    font-weight: bold;
    color: #2c3e50;
}

nav a.router-link-exact-active {
    color: #42b983;
}

html,
body {
    height: 100%;
}
</style>
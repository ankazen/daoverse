<template>
    <div class="h-full bg-green-400 w-80">
        <div class="h-60 p-2 bg-green-300 m-4 round" @click="goback()"></div>
        <div v-for="app in apps" class="ml-4 hover:bg-green-200 p-2 text-green-900" :class="{'bg-white': (app_name==app.name||app_name==app.id), 'text-red': (app_name==app.name||app_name==app.id)}"  @click="selectApp(app)">{{app.name}}</div>
    </div>
</template>
<script>
import { unoincontract_find } from '../daoverse_apis'
export default {
    name: 'AppNav',
    props: {
        union_id: String,
        app_name: String
    },
    data() {
        return {
            apps: [],
            dailog: false,
            dailog_data: null
        }
    },
    mounted() {
        console.log(this.union_id, this.app_name, this.apps)
        unoincontract_find({ union_id: this.union_id }, {})
            .then(res => {
              console.log(3, res.data)
                let apps = [{name:'apply'}]

                apps = apps.concat(res.data)
                console.log(apps)
                apps.push({name:'contract'})
                this.apps = apps;
                console.log(this.union_id, this.app_name, this.apps)
            })
    },
    methods: {
        selectApp(app) {
            if (app.name==='contract') {
              this.$router.push({name:'union_contract', params:{union_id: this.union_id}})
              return;
            }
            if (app.name==='apply') {
              this.$router.push({name:'union_apply', params:{union_id: this.union_id}})
              return;
            }
            this.$router.push({ name: 'union_app', params: { union_id: this.union_id, app_id: app.id} })
        },
        createContract() {
            contract_create({}, { union: this.dailog_data.id, desc: this.apply_content })
                .then(res => {
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
        },
        goback() {
          this.$router.push({name:'union', params:{union_id: this.union_id}})
        }
    }
}
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
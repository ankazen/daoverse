<template>
    <div class="flex flex-row h-full">
        <AppNav :union_id="union_id" :app_name="0" />
        <div class="w-full flex-grow">
          ddd
        </div>
    </div>
</template>
<script type="text/javascript">
import { unoincontract_find } from '../daoverse_apis'
import AppNav  from '../components/AppNav'

export default {
    name: 'UnionView',
    components: {
      AppNav
    },
    data() {
        return {
            union_id: '',
            apps: [],
            dailog: false,
            dailog_data: null,
        }
    },
    mounted() {
        console.log(this.$route.params)
        this.union_id = this.$route.params.union_id;
    },
    methods: {
        selectApp(app) {
            this.$router.push({ name: 'union', params: { name: union.name } })
        },
        createApply() {
            unionapply_create({}, { union: this.dailog_data.id, desc: this.apply_content })
                .then(res => {
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
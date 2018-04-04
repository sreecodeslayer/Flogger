// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'
import 'font-awesome/css/font-awesome.min.css'
import axios from 'axios'
import VueAxios from 'vue-axios'
import VueMoment from 'vue-moment'
import { SemipolarSpinner } from 'epic-spinners'

axios.defaults.headers.post['Content-Type'] = 'application/json'
axios.defaults.baseURL = process.env.BASE_URL
Vue.use(Vuetify)
Vue.use(VueMoment)
Vue.use(VueAxios, axios)

Vue.component('v-spinner', SemipolarSpinner)

Vue.config.productionTip = false

Vue.filter('humanizeTime', function (value) {
  return Vue.moment(value).fromNow()
})

Vue.filter('calendarTime', function (value) {
  return Vue.moment(value).calendar()
})

/* eslint-disable no-new */
document.addEventListener('DOMContentLoaded', () => {
  new Vue({
    el: '#app',
    router,
    components: { App },
    template: '<App/>'
  })
})

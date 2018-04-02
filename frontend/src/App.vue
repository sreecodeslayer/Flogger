<template>
  <v-app>
    <v-navigation-drawer
    persistent class="white darken-4"
    :mini-variant="miniVariant"
    :clipped="clipped"
    v-model="drawer"
    mini-variant-width="100"
    width="450"
    enable-resize-watcher
    fixed
    app
    >
    <v-toolbar flat light class="transparent">
      <v-container>
        <v-layout row wrap align-center>
          <v-flex xs12 sm12 md12 lg12>
            <div class="text-xs-center">

              <v-avatar
              :tile="false"

              :size="miniVariant ? 50 : 250"
              class="grey lighten-4"
              style="cursor:pointer"
              >
              <img v-on:click="miniVariant = !miniVariant" class="elevation-7" src="https://randomuser.me/api/portraits/men/9.jpg" alt="avatar">
            </v-avatar>
            <div id="details" v-if="!miniVariant">
              <div class="headline">Sreenadh <span style="font-weight:bold">TC</span></div>
              <div class="subheading text-xs-center grey--text pt-1 pb-3">Product Engineer | Hashwave Technologies</div>
            </div>
          </div>
          </v-flex>
          <v-divider></v-divider>
          <v-layout justify-space-between v-if="!miniVariant">

            <v-btn flat icon href="#"><v-icon mini>fa-dashboard</v-icon></v-btn>
            <v-btn flat icon href="#"><v-icon mini>fa-twitter-square</v-icon></v-btn>
            <v-btn flat icon href="#"><v-icon mini>fa-github</v-icon></v-btn>
            <v-btn flat icon href="#"><v-icon mini>fa-facebook</v-icon></v-btn>
          </v-layout>
          <v-layout row wrap align-center v-if="miniVariant">
            <v-flex xs12 sm12 md12 lg12 class="text-xs-center">
              <v-btn icon href="#"><v-icon medium>fa-at</v-icon></v-btn>
            </v-flex>
            <v-flex xs12 sm12 md12 lg12 class="text-xs-center">
              <v-btn icon href="#"><v-icon medium>fa-twitter</v-icon></v-btn>
            </v-flex>
            <v-flex xs12 sm12 md12 lg12 class="text-xs-center">
              <v-btn icon href="#"><v-icon medium>fa-github</v-icon></v-btn>
            </v-flex>
            <v-flex xs12 sm12 md12 lg12 class="text-xs-center">
              <v-btn icon href="#"><v-icon medium>fa-facebook</v-icon></v-btn>
            </v-flex>
          </v-layout>
      </v-layout>
    </v-container>
  </v-toolbar>
</v-navigation-drawer>
<v-content>
  <router-view/>
</v-content>
<v-footer :fixed="fixed" app>
  <span>&copy; 2017</span>
</v-footer>
</v-app>
</template>

<script>
export default {
  data () {
    return {
      clipped: false,
      drawer: true,
      fixed: false,
      items: [{
        icon: 'bubble_chart',
        title: 'Inspire'
      }],
      miniVariant: true,
      right: true,
      rightDrawer: false,
      title: 'Vuetify.js'
    }
  },
  name: 'App'
}
</script>

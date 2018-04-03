<template>
  <v-app>
    <v-navigation-drawer
    persistent class="white darken-4"
    :mini-variant="miniVariant"
    :clipped="clipped"
    v-model="drawer"
    mini-variant-width="150"
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

              :size="miniVariant ? 90 : 250"
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
          <v-divider dark></v-divider>
        </v-flex>
        <v-layout justify-space-between v-if="!miniVariant">

          <v-btn flat icon href="#"><v-icon size="1.5rem">fa-at</v-icon></v-btn>
          <v-btn flat icon href="#"><v-icon size="1.5rem">fa-twitter-square</v-icon></v-btn>
          <v-btn flat icon href="#"><v-icon size="1.5rem">fa-github</v-icon></v-btn>
          <v-btn flat icon href="#"><v-icon size="1.5rem">fa-facebook</v-icon></v-btn>
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
      <v-divider dark></v-divider>
    </v-container>
  </v-toolbar>
</v-navigation-drawer>
<v-content>
  <router-view/>
</v-content>
<v-footer color="teal darken-2" app>

         <!--  <v-fab-transition>
            <v-btn color="red" dark small absolute top right fab>
              <v-icon>expand_more</v-icon>
            </v-btn>
          </v-fab-transition> -->
  <v-layout row wrap align-center>
    <v-flex xs10 sm10 md11 lg11>
      <div class="white--text ml-3 text-xs-center">
        Made with
        <v-icon mini class="white--text">favorite</v-icon> by Sreenadh TC
      </div>
    </v-flex>
    <v-flex xs2 sm2 md1 lg1>
        <v-btn icon flat :href="'https://github.com/sreecodeslayer/Flogger'">
          <v-icon class="white--text" style="cursor:pointer;" medium>fa-github</v-icon>
        </v-btn>
    </v-flex>
  </v-layout>
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
      miniVariant: true,
      title: 'Sreenadh TC - Flogger'
    }
  },
  name: 'App'
}
</script>

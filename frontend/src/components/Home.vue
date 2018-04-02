<template>
  <v-container fluid>
    <v-slide-y-transition mode="out-in">
      <v-layout row wrap>
        <v-flex xs9 sm9 md9 lg9>
          <v-layout row wrap>
            <v-flex xs12 v-for="post in posts" :key="post.id">
              <v-card class="my-3" hover>
                <v-card-media class="white--text" height="150px" :src="'http://via.placeholder.com/150x50'">
                  <v-container fill-height fluid>
                    <v-layout fill-height>
                      <v-flex xs12 align-end felxbox>
                        <span class="headline">{{post.title}}</span>
                      </v-flex>
                    </v-layout>
                  </v-container>
                </v-card-media>
                <v-card-title>
                  <div>
                    <span class="grey--text">{{post.created_on}}</span><br>
                  </div>
                </v-card-title>
                <v-card-text>
                  {{post.meta}}
                </v-card-text>
                <v-card-actions>
                 <v-btn icon class="red--text">
                  <v-icon mini>fa-heart</v-icon>
                </v-btn>
                <v-btn icon class="blue--text">
                  <v-icon mini>fa-share</v-icon>
                </v-btn>
                <v-spacer></v-spacer>
                <v-btn small flat class="teal--text" :href="post.url">Read</v-btn>
              </v-card-actions>
            </v-card>
          </v-flex>
        </v-layout>
      </v-flex>
    </v-layout>
  </v-slide-y-transition>
</v-container>
</template>
<script>
export default {
  name: 'Home',
  data () {
    return {
      posts: []
    }
  },
  methods: {
    getPosts () {

    }
  }
}
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>

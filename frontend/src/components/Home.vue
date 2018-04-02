<template>
  <v-container fluid>
    <v-slide-y-transition mode="out-in">
      <v-layout row wrap>
        <v-flex xs9 sm9 md9 lg9 offset-md1 offset-lg2>
          <v-layout row wrap>
            <v-flex xs12 v-for="post in posts" :key="post.id">
              <v-card class="my-3" hover>
                <v-parallax :src="post.cover_img" height="450">
                  <v-card-media class="white--text" height="450">
                    <v-container fill-height fluid>
                      <v-layout fill-height>
                        <v-flex xs12 align-end felxbox>
                            <span class="headline">{{post.title}}</span>
                        </v-flex>
                      </v-layout>
                    </v-container>
                  </v-card-media>
                </v-parallax>
                <v-card-title>
                  <div>
                    <span class="grey--text">{{post.created_on.$date | humanizeTime}}</span><br>
                  </div>
                </v-card-title>
                <v-card-text>
                  {{post.caption}}
                </v-card-text>
                <v-card-actions>
                 <v-btn icon class="red--text">
                  <v-icon mini>fa-heart</v-icon>
                </v-btn>
                <v-btn icon class="blue--text">
                  <v-icon mini>fa-share</v-icon>
                </v-btn>
                <v-spacer></v-spacer>
                <v-btn small flat class="teal--text" :href="'/posts/'+post._id.$oid">Read</v-btn>
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
      var url = 'http://127.0.0.1:8000/api/posts'
      this.$http.get(url).then((response) => {
        this.posts = response.data.posts.items
      })
    }
  },
  created () {
    this.getPosts()
  }
}
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>

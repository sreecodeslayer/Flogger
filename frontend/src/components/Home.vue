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
                <v-bottom-sheet v-model="shareSheet">
                  <v-btn slot="activator" icon class="blue--text" @click.native="postToShare = post">
                    <v-icon mini>fa-share</v-icon>
                  </v-btn>
                  <v-list>
                    <v-subheader>Share post via</v-subheader>
                    <v-list-tile color="indigo darken-1" @click="shareSheet = false;sharePost()">
                      <v-list-tile-avatar>
                        <v-icon medium color="indigo darken-1">fa-facebook</v-icon>
                      </v-list-tile-avatar>
                      <v-list-tile-content>Facebook</v-list-tile-content>
                    </v-list-tile>
                    <v-list-tile color="blue lighten-2" @click="shareSheet = false;sharePost()">
                      <v-list-tile-avatar>
                        <v-icon medium color="blue lighten-2">fa-twitter</v-icon>
                      </v-list-tile-avatar>
                      <v-list-tile-content>Twitter</v-list-tile-content>
                    </v-list-tile>
                    <v-list-tile color="teal darken-3" @click="shareSheet = false;sharePost()">
                      <v-list-tile-avatar>
                        <v-icon medium color="teal darken-3">fa-whatsapp</v-icon>
                      </v-list-tile-avatar>
                      <v-list-tile-content>WhatsApp</v-list-tile-content>
                    </v-list-tile>
                    <v-list-tile color="lime darken-3" @click="shareSheet = false;sharePost()">
                      <v-list-tile-avatar>
                        <v-icon medium color="lime darken-3">fa-copy</v-icon>
                      </v-list-tile-avatar>
                      <v-list-tile-content>Clipboard</v-list-tile-content>
                    </v-list-tile>
                  </v-list>
                </v-bottom-sheet>
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
      posts: [],
      shareSheet: false,
      postToShare: null
    }
  },
  methods: {
    getPosts () {
      var url = 'http://127.0.0.1:8000/api/posts'
      this.$http.get(url).then((response) => {
        this.posts = response.data.posts.items
      })
    },
    sharePost () {
      console.log(this.postToShare)
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

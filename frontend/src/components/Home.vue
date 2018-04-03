<template>
  <v-container fluid>
    <v-slide-y-transition mode="out-in">
      <v-layout row wrap>
        <v-flex xs10 sm10 md10 lg10 offset-lg2>
          <div v-if="loaded">
            <v-layout row wrap>
              <v-toolbar>
                <!-- <v-toolbar-side-icon></v-toolbar-side-icon> -->
                <v-toolbar-title></v-toolbar-title>
                <v-text-field 
                append-icon="search" 
                hide-details 
                single-line
                v-model="query"></v-text-field>
              <!-- <v-btn icon flat>
                <v-icon medium>search</v-icon>
              </v-btn> -->
            </v-toolbar>
          </v-layout>
            <v-layout row wrap v-if="loaded">
              <v-flex xs12 v-for="post in posts" :key="post.id" v-cloak>
                <v-card class="my-3" hover>
                  <v-parallax :src="post.cover_img" v-ripple height="450">
                    <v-card-media class="white--text" v-ripple height="450">
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
                      <v-tooltip bottom>
                        <span slot="activator" class="grey--text">{{post.created_on.$date | humanizeTime}}</span>
                        <span>{{post.created_on.$date | calendarTime}}</span>
                      </v-tooltip>
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
                  <v-btn small flat class="teal--text" :href="'#/posts/'+post._id.$oid">Read</v-btn>
                </v-card-actions>
              </v-card>
            </v-flex>
          </v-layout>
          <v-layout row wrap align-center v-if="posts.length > 0">
            <v-flex xs12>
              <div class="text-xs-center" v-cloak>
                <v-pagination 
                :length="totalPages"
                value="page"
                v-model="page"
                ></v-pagination>
              </div>
            </v-flex>
          </v-layout>
        </div>
        <!-- <v-layout row wrap align-center v-else> -->
          <div class="topcorner-loader" v-else>
            <v-spinner :animation-duration="2000"
            :size="50"
            color="#ff1d5e"
            ></v-spinner>
          </div>
          <!-- </v-layout> -->
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
      postToShare: null,
      loaded: false,
      page: 1,
      perPage: 10,
      totalPages: 0,
      query: null
    }
  },
  watch: {
    page (newIndex) {
      this.page = newIndex
      this.getPosts()
    },
    query (q) {
      if (q.length >= 5) {
        this.getPosts(q)
      }
    }
  },
  methods: {
    getPosts (q = '') {
      this.loaded = false
      console.log(q)
      var url = '/api/posts?page=' + this.page + '&per_page=' + this.perPage + '&q=' + q

      this.$http.get(url).then(
        (response) => {
          var posts = response.data.posts
          this.totalPages = parseInt(posts.total / posts.per_page)
          this.posts = response.data.posts.items
          this.loaded = true
        },
        (err) => {
          console.log(err)
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


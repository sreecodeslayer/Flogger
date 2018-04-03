<template>
	<v-container fluid>
		<v-slide-y-transition mode="out-in">
			<div v-if="loaded" class="article">
        <v-layout row wrap>
          <v-flex xs10 offset-xs2>
            <h1 class="display-2 teal--text darken-2" >{{post.title}}</h1>
            <br>
            <v-layout row wrap>
              <v-flex xs10>
                <div class="subheading">{{post.caption}}</div>
              </v-flex>
              <v-flex xs2  class="teal--text darken-2" v-ripple>
                <span class="caption">
                  <v-icon color="teal darken-2" mini flat>fa-calendar</v-icon>
                  {{ post.created_on.$date | calendarTime }}
                </span>
              </v-flex>
            </v-layout>
            <v-divider></v-divider>
            <br>
          </v-flex>
          <v-flex xs10 offset-xs2 v-html="post.content">
          </v-flex>
        </v-layout>
      </div>
      <div class="topcorner-loader" v-else>
        <v-spinner :animation-duration="2000"
        :size="50"
        color="#ff1d5e"
        ></v-spinner>
      </div>

    </v-slide-y-transition>
  </v-container>
</template>
<script>
export default {
  name: 'Post',
  data () {
    return {
      post: {
        id: this.$route.params.id
      },
      loaded: false

    }
  },
  methods: {
    getPost () {
      var url = 'http://localhost:8000/api/posts/' + this.post.id
      this.$http.get(url).then(
        (response) => {
          this.post = response.data.post
          this.loaded = true
        },
        (err) => {
          var errData = err.response
          this.$router.push('/oops/' + errData.status)
        }
        )
    }
  },
  created () {
    this.getPost()
  }
}
</script>

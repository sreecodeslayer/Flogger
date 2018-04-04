<template>
	<v-container fluid>
		<v-slide-y-transition mode="out-in">
			<div v-if="loaded" class="article">
        <v-layout row wrap>
          <v-flex xs10 offset-xs2>
            <h1 class="teal--text darken-2" :class="$vuetify.breakpoint.xs ? 'title':'display-1'">{{post.title}}</h1>
            <br>
            <v-layout row wrap>
              <v-flex sm9 md9 lg10>
                <div :class="$vuetify.breakpoint.xs ? 'caption':'subheading'">{{post.caption}}</div>
              </v-flex>
              <v-flex sm3 md3 lg2 class="primary--text darken-4" v-ripple>
                <span :class="$vuetify.breakpoint.xs ? '':'caption'">
                  <v-icon color="primary darken-2" mini flat>fa-calendar</v-icon>
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
        :size="$vuetify.breakpoint.xs ? 100 : 65"
        color="#ff1d5e"
        ></v-spinner>
      </div>

    </v-slide-y-transition>
  </v-container>
</template>
<script>
export default {
  name: 'Post',
  metaInfo () {
    return {
      title: this.title,
      titleTemplate: '%s | Flogger'
    }
  },
  data () {
    return {
      post: {
        id: this.$route.params.id
      },
      loaded: false,
      title: 'Loading ...'

    }
  },
  methods: {
    getPost () {
      var url = '/posts/' + this.post.id
      this.$http.get(url).then(
        (response) => {
          this.post = response.data.post
          this.title = this.post.title
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

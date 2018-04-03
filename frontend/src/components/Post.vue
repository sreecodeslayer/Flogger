<template>
	<v-container fluid>
		<v-slide-y-transition mode="out-in">
			<v-layout row wrap v-if="loaded">
        <v-flex xs10 offset-xs2 class="article" v-html="post.content">
        </v-flex>
			</v-layout>
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
        (response) => {

        }
        )
    }
  },
  created () {
    this.getPost()
  }
}
</script>

<template>
	<v-container fluid>
		<v-slide-y-transition mode="out-in">
			<v-layout row wrap align-center>
				<v-flex xs12>
					<div v-if="errCode == 404" class="teal--text darken-2 text-xs-center">
						<v-icon size="400px" color="teal darken-2">sentiment_neutral</v-icon>
						<v-spacer></v-spacer>
						<span class="subheading">Hmm, I am sorry, I couldn't quite get what you asked for!</span>
					</div>
					<div v-if="errCode == 500" class="primary--text darken-2 text-xs-center">
						<v-icon size="400px" color="primary darken-2">sentiment_very_dissatisfied</v-icon>
						<v-spacer></v-spacer>
						<span class="subheading">I am a noob! Something terrible struck me!</span>
					</div>
				</v-flex>
			</v-layout>
		</v-slide-y-transition>
	</v-container>
</template>
<script>
export default {
  name: 'HttpError',
  data () {
    return {
      errCode: this.$route.params.errCode
    }
  }
}
</script>
<script setup>
import CommunityCards from "./CommunityCards.vue";
import Player from "./Player.vue";

// min 2 players
const playerCount = 12;
</script>

<template>
  <div class="flex flex-row">
    <div class="bg-green-900 rounded-full w-80 h-80 relative left-40 -z-10">
      <Player v-if="playerCount >= 9" class="absolute top-2 left-6"></Player>
      <Player
        v-if="playerCount >= 3"
        class="absolute bottom-32 -left-8"
      ></Player>
      <Player
        v-if="playerCount >= 12"
        class="absolute bottom-2 left-6"
      ></Player>
    </div>
    <div
      class="bg-green-900 w-80 h-80 flex flex-col justify-center items-center relative"
    >
      <Player v-if="playerCount >= 5" class="absolute -top-8 -left-2"></Player>
      <Player v-if="playerCount >= 2" class="absolute -top-8"></Player>
      <Player v-if="playerCount >= 7" class="absolute -top-8 right-0"></Player>
      <CommunityCards></CommunityCards>
      <Player
        v-if="playerCount >= 8"
        class="absolute -bottom-8 -left-2"
      ></Player>
      <Player v-if="playerCount >= 1" class="absolute -bottom-8"></Player>
      <Player
        v-if="playerCount >= 6"
        class="absolute -bottom-8 right-0"
      ></Player>
    </div>
    <div class="bg-green-900 rounded-full w-80 h-80 relative right-40 -z-10">
      <Player v-if="playerCount >= 11" class="absolute top-2 right-6"></Player>
      <Player
        v-if="playerCount >= 4"
        class="absolute bottom-32 -right-8"
      ></Player>
      <Player
        v-if="playerCount >= 10"
        class="absolute bottom-2 right-6"
      ></Player>
    </div>
  </div>
</template>

<style scoped></style>

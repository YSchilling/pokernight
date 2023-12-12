<script setup>
import { ref } from 'vue';

const state = ref(null);
async function fetchCreate() {
    try {
        await fetch('http://127.0.0.1:8000/game/create', { method: "POST" });
    } catch (error) {
        console.error(error);
    }
}
async function fetchJoin() {
    try {
        await fetch('http://127.0.0.1:8000/player/join?name=Player', { method: "POST" });
    } catch (error) {
        console.error(error);
    }
}
async function fetchStart() {
    try {
        await fetch('http://127.0.0.1:8000/game/start', { method: "POST" });
    } catch (error) {
        console.error(error);
    }
}
async function fetchState() {
    try {
        const response = await fetch('http://127.0.0.1:8000/game/state');
        state.value = JSON.parse(await response.json());
    } catch (error) {
        console.error(error);
    }

}
</script>
<template>
    <div class="flex flex-col">
        <button class="border" @click="fetchCreate()">Create</button>
        <button class="border" @click="fetchJoin()">Join</button>
        <button class="border" @click="fetchStart()">Start</button>
        <button class="border" @click="fetchState()">Reload</button>
        <ol v-if="state">
            <li v-for="player in state.players">{{ player.name }}</li>
        </ol>
    </div>
</template>
<style scoped></style>
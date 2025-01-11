<template>
  <div class="container mx-auto p-4">
    <NuxtLink to="/" class="text-blue-500 hover:text-blue-700 mb-4 block">
      ← Back to Home
    </NuxtLink>
    
    <div v-if="content" class="mt-4">
      <h1 class="text-2xl font-bold mb-2">{{ content.title }}</h1>
      <p class="text-gray-600 mb-4">Category: {{ content.category }}</p>
      <div class="prose">
        {{ content.content }}
      </div>
    </div>
  </div>
</template>

<script setup>
const route = useRoute()
const { data: content } = await useFetch(
  `http://localhost:8000/api/content/${route.params.id}`
)
</script> 
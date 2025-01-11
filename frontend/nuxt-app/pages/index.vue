<template>
    <div class="container mx-auto p-4">
      <h1 class="text-2xl font-bold mb-4">Content Navigator</h1>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div v-for="item in content" :key="item.id" 
             class="border p-4 rounded-lg hover:shadow-lg transition-shadow">
          <h2 class="text-xl font-semibold">{{ item.title }}</h2>
          <p class="text-gray-600">Category: {{ item.category }}</p>
          <NuxtLink :to="`/content/${item.id}`" 
                    class="text-blue-500 hover:text-blue-700">
            Read more
          </NuxtLink>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  const { data: content } = await useFetch('http://localhost:8000/api/content')
  </script>
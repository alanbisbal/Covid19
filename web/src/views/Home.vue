<template>
  <div
    class="d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 bg-white border-bottom shadow-sm"
  >
    <index />
  </div>
</template>

<script>
import index from '@/components/Home/index.vue';

export default {
  name: 'App',
  components: {
    index,
  },
};
</script>

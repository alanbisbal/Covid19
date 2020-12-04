<template>
  <div class="content">
    <p>User ID: {{ result.userId }}</p>
    <p>Title: {{ result.title }}</p>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data: () => ({
    result: null
  }),
  created() {
    axios.get("https://jsonplaceholder.typicode.com/todos/1").then((result) => {
      this.result = result.data;
    })
  }
};
</script>

<style scoped lang="scss">
</style>

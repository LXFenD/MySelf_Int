<template>
  <div class="detail-left">
    <Detail_l_top></Detail_l_top>
    <Detail_l_Content></Detail_l_Content>
    <Detail_l_Settings></Detail_l_Settings>
  </div>
</template>

<script>
  import Detail_l_top from '../../blog/blog-write/detail-left-top'
  import Detail_l_Content from '../../blog/blog-write/detail-left-content'
  import Detail_l_Settings from '../../blog/blog-write/detail-left-settings'
  export default {
    name: "blog-write-left",
    components:{
      Detail_l_top,
      Detail_l_Content,
      Detail_l_Settings
    }
  }
</script>

<style scoped>
  .detail-left {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    background: #fff;
  }


</style>

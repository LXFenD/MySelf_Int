<template>
    <div class="detail-left-top">
      <h4><span class="glyphicon glyphicon-text-width"></span>写博客</h4>
      <p><span class="glyphicon glyphicon-list-alt"></span>
        <router-link to="/blog/">博客主页</router-link>
      </p>
    </div>
</template>

<script>
    export default {
        name: "detail-left-top"
    }
</script>

<style scoped>
.detail-left .detail-left-top {
    width: 100%;
    border-bottom: 1px solid #ccc;

  }

  .detail-left-top h4 {
    width: 100%;
    text-align: center;
    background: crimson;
    height: 50px;
    line-height: 50px;
    cursor: pointer;
  }

.detail-left-top span {
    padding-right: 10px;
  }

  .detail-left-top p {
    text-align: center;
    height: 45px;
    color: #888;
    line-height: 45px;
  }

   .detail-left-top p:hover {
    background: crimson;
    color: #fff;
  }

   .detail-left-top p:hover a {
    color: #fff;
  }

  .detail-left-top p > a {
    text-decoration: none;
    color: #888;
    font-size: 15px;
  }
</style>

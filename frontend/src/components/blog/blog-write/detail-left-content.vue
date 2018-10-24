<template>
    <div class="detail-left-content">
        <p class="p-title">内容</p>
        <ul class="ul-content">
          <li>博客管理</li>
          <li>评论管理</li>
          <li>分类管理</li>
        </ul>
    </div>
</template>

<script>
    export default {
        name: "detail-left-content"
    }
</script>

<style scoped>
  .p-title{
    color: #ccc;
    margin-left: 10px;
  }
    .detail-left-content{
      width: 100%;
      color: #999;
      margin-top: 10px;
      font-size: 16px;
      border-bottom: 1px solid #ccc;
    }

  .detail-left-content .ul-content{
    width: 100%;
      padding: 0;
      list-style-type: none;
  }
   .detail-left-content .ul-content li{
     width: 100%;
     padding: 10px 0;
     text-align: center;
     cursor: pointer;
     height: 50px;
     line-height: 30px;
     box-sizing: border-box;
   }
  .detail-left-content .ul-content li:hover{
    background: crimson;
    color: #fff;
  }
</style>

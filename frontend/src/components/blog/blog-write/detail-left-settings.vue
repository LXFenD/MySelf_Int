<template>
    <div class="detail-left-settings">
        <p class="p-title">设置</p>
        <ul class="ul-content">
          <li>博客设置</li>
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
    .detail-left-settings{
      width: 100%;
      color: #999;
      margin-top: 10px;
      font-size: 16px;
    }

  .detail-left-settings .ul-content{
    width: 100%;
      padding: 0;
      list-style-type: none;
  }
   .detail-left-settings .ul-content li{
     width: 100%;
     padding: 10px 0;
     text-align: center;
     height: 50px;
     line-height: 30px;
     box-sizing: border-box;
     cursor: pointer;
   }
  .detail-left-settings .ul-content li:hover{
    background: crimson;
    color: #fff;
  }
</style>

<template>
    <div class="footer">
      <div class="footer-cont">
        <p>且歌且行且从容，鲜衣怒马少年时 <span class="fa fa-github"></span></p>
      </div>
    </div>
</template>

<script>
    export default {
        name: "BG_Footer"
    }
</script>

<style scoped>
    .footer{
      width: 100%;
      height: 70px;
      background: #303d4a;
      border-top: 3px solid goldenrod;
    }
  .footer-cont{
    margin: 0 auto;
    width: 100%;
    height: 100%;
    line-height: 70px;
    text-align: center;
  }
  .footer-cont p {
    margin: 0;
    padding: 0;
  }
  span{
    font-size: 18px;
    color: white;
    padding: 10px;
    cursor: pointer;
  }
</style>

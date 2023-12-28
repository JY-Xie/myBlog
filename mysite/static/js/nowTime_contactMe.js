    // 获取当前时间
    function getCurrentTime() {
      var date = new Date();
      var hours = String(date.getHours()).padStart(2, '0');
      var minutes = String(date.getMinutes()).padStart(2, '0');
      var seconds = String(date.getSeconds()).padStart(2, '0');
      return hours + ":" + minutes + ":" + seconds;
    }

    // 更新页面上的当前时间
    function updateCurrentTime() {
      var currentTimeElement = document.getElementById("current-time");
      if (currentTimeElement) {
        currentTimeElement.textContent = getCurrentTime();
      }
    }

    // 每秒钟更新一次当前时间
    setInterval(updateCurrentTime, 1000);

    // 获取弹窗
    var modal = document.getElementById('myModal');

    // 打开弹窗的按钮对象
    var btn = document.getElementById("myBtn");

    // 获取 <span> 元素，用于关闭弹窗
    var span = document.querySelector('.close');

    // 点击按钮打开弹窗
    btn.onclick = function() {
        modal.style.display = "block";
    }

    // 点击 <span> (x), 关闭弹窗
    span.onclick = function() {
        modal.style.display = "none";
    }

    // 在用户点击其他地方时，关闭弹窗
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }
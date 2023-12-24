
setRating = function (rating) {
    var stars = document.querySelectorAll('.product-details .rate a');

    for (var i = 0; i < stars.length; i++) {
        if (i < rating) {
            stars[i].classList.add('active');
        } else {
            stars[i].classList.remove('active');
        }
    }
}

// function updateOption() {
//     var dropdown = document.getElementById("batteryDropdown");
//     var selectedOption = dropdown.querySelector("select").value;
//     document.querySelector(".option").innerText = " (" + selectedOption + " mAh)";
// }

var rentNowButton = document.getElementById('rentNowButton');

// console.log(rentNowButton);
// 添加点击事件处理函数
rentNowButton.addEventListener('click', function () {
    var confirmation = confirm('确定要执行操作吗？');
    if (confirmation) {
        window.location.href = '../profile';
    } else {
        console.log('用户取消了操作');
    }
});
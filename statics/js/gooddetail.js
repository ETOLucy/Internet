
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
        
        // 获取商品当前价格的元素
        var priceElement = document.querySelector('.current');

        // 提取价格信息（假设价格是以人民币￥为前缀的数字）
        var currentPrice = parseFloat(priceElement.innerText.replace('￥', ''));

        // 获取用户选择的商品信息
        var selectedProduct = {
            productId: "{{drone.id}}",
            property1: document.querySelector('#batteryDropdown1 select').value,
            property2: document.querySelector('#batteryDropdown2 select').value,
            property3: document.querySelector('#batteryDropdown3 select').value,
            
            price: currentPrice,
            // 其他商品信息...
        };

        // 发送数据到后端
        fetch('../../submit_order/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken'),
            },
            body: JSON.stringify(selectedProduct),
        })
            .then(response => response.json())
            .then(data => {
                console.log('Success:', data);
                // 在成功的回调中执行跳转或其他操作
                window.location.href = '../profile';
            })
            .catch((error) => {
                console.error('Error:', error);
            });
        // window.location.href = '../profile';
    } else {
        console.log('用户取消了操作');
    }
});


    // 获取 CSRF token 的函数，可以根据你的实际情况进行调整
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
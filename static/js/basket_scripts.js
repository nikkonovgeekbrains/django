window.onload = function () {
    $('.basket_list').on('click', 'input[type="number"]', function () {
        let target_href = event.target;

        $.ajax({
            url: "/basket/edit/" + target_href.name + "/" + target_href.value + "/",

            success: function (data) {
                $('.basket_list').html(data.result);
                console.log('ajax done');
            },
        });

        event.preventDefault();
    });
}
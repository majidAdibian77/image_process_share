function change_black_white() {
    $.ajax({
        type: "GET",
        url: '/change_black_white',
        data: {
            "general_image_url": $('#show_image').attr('name'),
            "new_image_url": $('#show_image').attr('src')
        },
        dataType: "json",
        success: function (data) {
            $("#show_image").attr("src", data["newImage_url"]);
        },
        failure: function (data) {
            alert('There is a problem!!!');
        }
    });
}

function reset_image() {
    var general_url_image = $('#show_image').attr('name');
    var new_url_image = $('#show_image').attr('src');

    if (general_url_image != new_url_image) {
        $.ajax({
            type: "GET",
            url: '/reset_image',
            data: {
                "image_url": new_url_image
            },
            dataType: "json",
            success: function (data) {
                $("#show_image").attr("src", data["newImage_url"]);
                $("#show_image").attr("width", data["height"]);
                $("#show_image").attr("height", data["width"]);
            },
            failure: function (data) {
                alert('There is a problem!!!');
            }
        });
    }
}

function change_size() {
    var width_image = $('#width_image');
    var height_image = $('#height_image');
    var width = width_image.val();
    var height = height_image.val();
    if (width < 200) {
        width_image.css('background', 'red');
        width_image.val(200);
        width = 200;
    }
    else if (width > 500) {
        width_image.css('background', 'red');
        width_image.val(400);
        width = 400;
    }
    if (height < 300) {
        height_image.css('background', 'red');
        height_image.val(300);
        height = 300;
    }
    else if (height > 600) {
        height_image.css('background', 'red');
        height_image.val(500);
        height = 500;
    }
    $.ajax({
        type: "GET",
        url: '/change_size_of_image',
        data: {
            "image_url": $('#show_image').attr('name'),
            "width": width,
            "height": height,
        },
        dataType: "json",
        success: function (data) {
            $("#show_image").attr("src", data["newImage_url"]);
            $('#show_image').attr('width', width);
            $('#show_image').attr('height', height);
        },
        failure: function (data) {
            alert('There is a problem!!!');
        }
    });
}

function change_contract() {
    $.ajax({
        type: "GET",
        url: '/change_contract_image',
        data: {
            "image_url": $('#show_image').attr('name'),
            "factor": $('#contract_range').val(),
        },
        dataType: "json",
        success: function (data) {
            $("#show_image").attr("src", data["newImage_url"]);
        },
        failure: function (data) {
            alert('There is a problem!!!');
        }
    });
}

function add_comment_button(postPk) {
    $.ajax({
        type: "GET",
        url: '/user_add_comment',
        data: {
            "comment_text": $('#user-comment-' + postPk).val(),
            "post_pk": postPk,
        },
        dataType: "json",
        success: function (data) {
            location.href = data["url"];
        },
        failure: function () {
            alert('There is a problem!!!');
        }
    });
}

function follow() {
    $.ajax({
        type: "GET",
        url: '/follow',
        data: {
            "user_pk": $('#follow-button').attr("name")
        },
        dataType: "json",
        success: function (data) {
            location.href = data["url"];
        },
        failure: function () {
            alert('There is a problem!!!');
        }
    });
}


function unfollow() {
    $.ajax({
        type: "GET",
        url: '/unfollow',
        data: {
            "user_pk": $('#follow-button').attr("name")
        },
        dataType: "json",
        success: function (data) {
            location.href = data["url"];
        },
        failure: function () {
            alert('There is a problem!!!');
        }
    });
}

function approve_comment(comment_pk) {
    $.ajax({
        type: "GET",
        url: '/approve_comment',
        data: {
            "comment_pk": comment_pk,
            // "user_pk": $('#approve-comment-' + comment_pk).attr("name")
        },
        dataType: "json",
        success: function (data) {
            location.href = data["url"];
        },
        failure: function () {
            alert('There is a problem!!!');
        }
    });
}

function delete_comment(comment_pk) {
    $.ajax({
        type: "GET",
        url: '/delete_comment',
        data: {
            "comment_pk": comment_pk,
            // "user_pk": $('#approve-comment-' + comment_pk).attr("name")
        },
        dataType: "json",
        success: function (data) {
            location.href = data["url"];
        },
        failure: function () {
            alert('There is a problem!!!');
        }
    });
}

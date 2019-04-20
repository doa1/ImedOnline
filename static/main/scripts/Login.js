/*A jquery file to handle user login; force execution only after page contents have loaded
* */
$(document).ready(function() {

        $('#loginBtn').click(function (ev) {
            ev.preventDefault();
            var form = $('form#loginForm');
            var formData = form.serializeArray(); // returns an array of the form fields
            var data = {};
            // to deserialize form data to extract every field by name and value and store as a new array
            // trying my luck with the es6
            $.each(formData,(key,field)=>{
                data[field.name] =field.value;
            });
            // get the api login endpoint and the redirect url

            var endpoint = $(this).data('auth');
            var redirect_url = $(this).data('redirect');
            console.log(endpoint);
            // did the user enter all the fields!!!
            if(data.username === "" || data.password === ""){
                console.log("This must be crazy, we want these data");
                $("#login-errors").toggleClass("invisible visible");
                $("#login-errors").html("<div class=\"alert alert-danger alert-dismissible fade show\" role=\"alert\">\n" +
                    "<strong>Error!!</strong>  Please enter the username and password\n" +
                    "<button type=\"button\" class=\"close\" data-dismiss=\"alert\" aria-label=\"Close\">\n" +
                    "    <span aria-hidden=\"true\">&times;</span>\n" +
                    "    </button>\n" +
                    "</div>")
            }else {
                // get ready to send this data, but for some reasons django was rejecting the csrf sent via ajax form,
                // so we need to set up the xhr headers
                var token =  $('input[name="csrfmiddlewaretoken"]').val();

                console.log('token',token);
                function csrfSafeMethod(method) {
                    // these HTTP methods do not require CSRF protection
                    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
                }
                $.ajaxSetup({
                    beforeSend: function(xhr, settings) {
                        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                            xhr.setRequestHeader("X-CSRFToken", token);
                        }
                    }
                });
                $.ajax({
                    url: endpoint,
                    data: JSON.stringify(data),
                    method: "POST",
                    //headers:{'X-CSRFToken': token},
                    contentType:'application/json', // telling the server to receive this data in json format not the default django-form queryset
                    success:function (response) {
                        console.log(response.auth_error);
                        if(!response.user_exists){
                            console.log("We didnt find this account. signup!!");
                            $("#login-errors").toggleClass("invisible visible");
                            $("#login-errors").html("<div class=\"alert alert-danger alert-dismissible fade show\" role=\"alert\">\n" +
                            "<strong>Error!!</strong>  We could not find this account. Please signup!!\n" +
                            "<button type=\"button\" class=\"close\" data-dismiss=\"alert\" aria-label=\"Close\">\n" +
                            "    <span aria-hidden=\"true\">&times;</span>\n" +
                            "    </button>\n" +
                            "</div>");
                        }
                        //check for incorrect login details errrro
                        else if(response.auth_error){
                            $("#login-errors").toggleClass("invisible visible");
                            $("#login-errors").html("<div class=\"alert alert-danger alert-dismissible fade show\" role=\"alert\">\n" +
                            "<strong>Error!!</strong> Incorrect Password !!\n" +
                            "<button type=\"button\" class=\"close\" data-dismiss=\"alert\" aria-label=\"Close\">\n" +
                            "    <span aria-hidden=\"true\">&times;</span>\n" +
                            "    </button>\n" +
                            "</div>");

                        }
                        else if (response.success_login) {
                            console.log("you are in. Get Some coffee!!");
                            window.location.href=redirect_url;

                        }

                    },
                    error: function (errors) {
                        console.log(errors);
                            $("#login-errors").toggleClass("invisible visible");
                            $("#login-errors").html("<div class=\"alert alert-danger alert-dismissible fade show\" role=\"alert\">\n" +
                            "<strong>Ooops!!</strong> There was an error processing this request. Please try again!!\n" +
                            "<button type=\"button\" class=\"close\" data-dismiss=\"alert\" aria-label=\"Close\">\n" +
                            "    <span aria-hidden=\"true\">&times;</span>\n" +
                            "    </button>\n" +
                            "</div>");
                    }
                })
            }


        });
    }
);
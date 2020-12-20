jQuery(function ($) {

    'use strict';
    var user_name = '';
    var invite_user_array = [];
    var is_location = false;
   
// ----------------------------------------------------------------
   


    (function() {
       function get_tickets()
       {
           var data = $(".search_filter").serialize();
            $.ajax({
                url: "/ticket/get_tickets",
                method: 'get',
                type: 'json',
                data: data,
                success: function(response) 
                {
                    $(".ticket_list").html("");
                    if(response.results.length > 0)
                    {
                        var data = response.results;                        
                        for (var i = 0; i < data.length; i++) {
                            data[i];
                            var html = `
                                <tr>
                                    <td>
                                        <input type="checkbox" name="">
                                    </td>
                                    <td>
                                        ${data[i].date_of_incident}
                                    </td>
                                    <td>
                                        ${data[i].contact_name}
                                    </td>
                                    <td>
                                        ${data[i].contact_number}
                                    </td>
                                    <td>
                                        ${data[i].insurer}
                                    </td>
                                    <td>
                                        ${data[i].ticket_type}
                                    </td>
                                    <td>
                                        ${data[i].ticket_status}
                                    </td>
                                    <td>
                                        ${data[i].vehicle_reg_num}
                                    </td>
                                    <td>
                                        ${data[i].vehicle_manufacturer}
                                    </td>
                                    <td>
                                        ${data[i].vehicle_model}
                                    </td>
                                    <td>
                                        ${data[i].assigned_to}
                                    </td>
                                    <td>
                                        ${data[i].tow_from}
                                    </td>
                                    <td>
                                        ${data[i].tow_to_workshop}
                                    </td>
                                    <td>
                                        ${data[i].tow_to_address}
                                    </td>
                                    <td width="70">                                       
                                        <a class="btn_transparent btn_edit_ticket text-green mr-2" href="/ticket/edit/${data[i].id}" data-id="${data[i].id}">
                                            <i class="far fa-edit"></i>
                                        </a>
                                        <button type="buttom" class="btn_transparent btn_delete_ticket text-red" data-id="${data[i].id}">
                                            <i class="far fa-trash-alt"></i>
                                        </button>
                                    </td>
                                </tr>
                            `;
                            $(".ticket_list").append(html);
                        }
                        

                    }
                    else
                    {
                        var html = `
                                <tr>
                                    <td class="text-center" colspan="15">
                                        <p>There is no any ticket yet.</p>
                                    </td>                                   
                                </tr>
                            `;
                            $(".ticket_list").append(html);
                    }
                }
            });
       }

        function get_location_response(params) {
            $.ajax({
                url: "/ticket/get_location_response",
                method: 'get',
                type: 'json',
                success: function(response) 
                {
                    console.log(response);
                }
            });
       }
       $(document).on('click','.btn_create_ticket',function()
       {            
            var checkvalid = true;       
            $(".required").each(function(){
                if($(this).val() == "")
                {                        
                    $(this).addClass('alertborder');
                    checkvalid = false;
                }
            });
            if($("input[name='which']").val()=="0")
            {
                if($("input[name='locationID']").val()=="")
                {
                    checkvalid = false;
                    swal({
                        title: "Something wrong!",                                                                                
                        type: "error",
                        text: "You did not send link, please click 'Send Link' button.",
                    }).then(function() {
                        
                    });
                }
            }
            if(checkvalid)
            {
                var data = $("#form_ticket").serialize();
                $.ajax({
                    url: "/ticket/store",
                    method: 'post',
                    type: 'json',
                    data: data,
                    success: function(response) 
                    {
                        if(response.results)
                        {
                            swal({
                                title: "Successfully stored!",                                                                                
                                type: "success"
                            }).then(function() {
                                location.reload()
                            });
                        }
                        else
                        {
                            swal({
                                title: "Something wrong!",                                                                                
                                type: "error"
                            }).then(function() {
                                location.reload()
                            });
                        }
                    }
                });
            }
        });

        $(document).on('click','.btn_delete_ticket',function(){
            var id = $(this).data('id');

            $.ajax({
                url: "/ticket/delete",
                method: 'GET',
                type: 'json',
                data: {id:id},
                success: function(response) 
                {
                    if(response.results)
                    {
                        swal({
                            title: "Successfully removed!",                                                                                
                            type: "success"
                        }).then(function() {
                            location.reload()
                        });
                    }
                    else
                    {
                        swal({
                            title: "Something wrong!",                                                                                
                            type: "error",
                            text: "Please try again",
                        }).then(function() {
                            location.reload()
                        });
                    }          
                }
            });
        });
        
        
        $(document).on('click','.btn_get_location',function(){
            var checkvalid = true;
            if($("input[name='locationID']").val()=="")
            {
                checkvalid = false;
                swal({
                    title: "Something wrong!",                                                                                
                    type: "error",
                    text: "You did not send link, please click 'Send Link' button.",
                }).then(function() {
                    
                });
            }
            if(checkvalid)
            {
                $("#loading").css('display','flex');
                $.ajax({
                    url: "/ticket/get_location",
                    method: 'GET',
                    type: 'json',
                    data: {id:$("input[name='locationID']").val()},
                    success: function(response) 
                    {
                        $("#loading").css('display','none');
                        if(response.allow == "1")
                        {
                            if(response.location == "")
                            {                            
                                swal({
                                    title: "No address",                                                                                
                                    type: "error"
                                }).then(function() {
                                    
                                });
                            }
                            else
                            {
                                $("input[name='tow_from']").val(response.location);
                            }
                        } 
                        else
                        {
                            swal({
                                title: "Not allow to get location!",                                                                                
                                type: "error"
                            }).then(function() {
                                $("input[name='tow_from']").focus();
                            });
                        }                                 
                    }
                });
            }
        });
        $(document).on('click','.btn_send_link',function(){
            var is_check = true;
            if($("input[name='contact_number']").val()=="")
            {
                $("input[name='contact_number']").addClass('alertborder');
                is_check = false;
            }    
            if($("input[name='vehicle_reg_num']").val()=="")
            {
                $("input[name='vehicle_reg_num']").addClass('alertborder');
                is_check = false;
            }         
            if(is_check)
            {
                $.ajax({
                    url: "/ticket/send_link",
                    method: 'GET',
                    type: 'json',
                    data: {num:$("input[name='contact_number']").val()},
                    success: function(response) 
                    {
                        if(response.results)
                        {
                            var id = response.id;
                            $("input[name='locationID']").val(id);
                            swal({
                                title: "Successfully sent!",                                                                                
                                type: "success"
                            }).then(function() {
                                
                            });
                        }
                        else
                        {
                            swal({
                                title: "Something wrong!",                                                                                
                                type: "error",
                                text: "Please try again",
                            }).then(function() {
                                location.reload()
                            });
                        }          
                    }
                });
            }   
            else
            {
                return false;
            }      
        });
        $(document).on('click','.alertborder',function(){
            $(this).removeClass('alertborder');
        });
        $(document).on('click','.btn_filter_clear',function(){
            location.reload();
        });
        $(document).on('click','.btn_filter',function(){
            get_tickets();
        });
        $(document).ready(function(){
            get_tickets(); 
            get_location_response();
           
        });        
    }());

 

  
   
});


    


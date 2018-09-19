function checkCode() {
            var code = $('#code').val();
            var r = /^[0-9]+/;
            var a = r.test(code);
            if (a=false){
                $('#codespan').html('只能为数字');

                return false;
            }
            var csrf = $('input[name="csrfmiddlewaretoken"]').val();
            var data = {'code':code,'csrfmiddlewaretoken':csrf};
            if(code.length==0){
                $('#codespan').html('*');


            }else{
                $.post('/mark/exist/',data,function(result){
                    r = result.flag;

                if(r){
                        $('#codespan').html('√');

                }else{
                        $('#codespan').html('该学生编号不存在');

                    }
                })

            }
        }
function checkName() {
            var name = $('#name').val();
            var r = /^[0-9]+/;
            var a = r.test(name);
            if (a){
                $('#namespan').html('只能为汉字');
                return false;
            }
            var csrf = $('input[name="csrfmiddlewaretoken"]').val();
            var data = {'name':name,'csrfmiddlewaretoken':csrf};
            if(name.length==0){
                $('#namespan').html('*');

            }else{
                $.post('/mark/exist1/',data,function(result){
                    r = result.flag;

                if(r){
                        $('#namespan').html('√');

                    }else{
                        $('#namespan').html('学生姓名与学生编号不存在');

                    }
                })
            }
        }


function clss() {
    var name = $('#cls').val();
    var csrf = $('input[name="csrfmiddlewaretoken"]').val();
    var data = {'name':name,'csrfmiddlewaretoken':csrf};
    if(name.length==0){
        $('#clsspan').html('*');

    }else{
        $.post('/mark/exist2/',data,function(result){
            r = result.flag;

        if(r){
                $('#clsspan').html('√');

            }else{
                $('#clsspan').html('班级不存在');

            }
        })
    }
}


// function clssSelect() {
//     var a = $('#dd').val();
//     console.log(a);
//     var con = $('.aa').val();
//     console.log(con);
//     var csrf = $('input[name="csrfmiddlewaretoken"]').val();
//     if(con.length==0){
//         $('#sspan').html('*');
//         return false;
//     }
//     // if (a='1'){
//     //     console.log(1);
//     //     $('#sspan').html('只能为数字');
//     //     return false;
//     // }else if(a='2'){
//     //     console.log(2);
//     //     $('#sspan').html('只能为汉字');
//     //     return false;
//     // }
//     var data = {'con':con,'a':a,'csrfmiddlewaretoken':csrf};
//     $.post('/mark/exist3/',data,function(result){
//         r = result.codes;
//         console.log(r);
//         $('#ad').html(result)
//     })
//
// }




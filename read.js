
function readThread(board, key) {
    var reader = new XMLHttpRequest();
    reader.open("GET", "../../../../" + board + "/dat/" + key + ".dat", false);
    reader.send();
    var data = reader.responseText;
    alert(data);
    var a = data.split("\n");
    var resCount = 0;
    var threadTitle = "";
    var strs = "";
    for (var i = 0; i < a.length; i++) {
        var codes = a[i].split("<>");
        if (resCount == 0) {
            threadTitle = data[4];
        }
        var isMailEmpty = false;
        resCount++;
        var htmls = "<dt><a name=\"resCount\">" + resCount + "</a> :";
        if (a[1] == "") {
            htmls += '<font color="green">';
            isMailEmpty = true;
        } else {
            htmls += '<a href="mailto:' + a[1] + '">';
        }
        htmls += "<b>"+a[0]+"</b>";
        if (isMailEmpty) {
            htmls += "</font>";
        } else {
            htmls += "</a>";
        }
        htmls += ":" + a[2] + "</dt>\r\n";
        htmls += " <dd> " + a[3] + "<br><br></dd>\r\n";
        strs += htmls;
    }
    var returns = Array(threadTitle, strs);
    return returns;
}
function executeReadThread(threadUrl) {
    
    var para = analysisParameter(threadUrl.substr(1, 100));
    
    var data = readThread(para[0], para[1]);
    var bodys = document.getElementById('bodys');
    bodys.innerHTML = "<section id=\"bodys\">"+data[1]+"</section>";
    var tiles = document.getElementById('title');
    tiles.textContent = data[0];
    document.title = data[0];
}

function analysisParameter(param) {
    alert(param);
    return param.split("/");
}

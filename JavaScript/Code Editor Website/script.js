function run(){
    let htmlCode = document.getElementById("html-code").value;
    let cssCode = document.getElementById("css-code").value;
    let jsCode = document.getElementById("js-code").value;
    let output = document.getElementById("output");

    output.contentDocument.body.innerHTML = htmlCode + "<style>"+cssCode+"</style>";
    output.contentWindow.eval(jsCode);
}



/*
LOGIC: iframe works to create a seperate document of its own similar to a webpage document. We take value of html code and it renders an dispaly on the output.
For CSS we put it inside style tags to get it rendered into  proper css.
*/

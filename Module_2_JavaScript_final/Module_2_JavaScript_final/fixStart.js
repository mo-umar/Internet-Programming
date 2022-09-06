// fixStart
function fixStart(str){
    const firstChar = str[0];
    var result = firstChar;
    for(let i=1; i<str.length; i++) {
        if(str[i]==firstChar) {
            result += '*';
        }
        else {
            result += str[i];
        }
    }
    return result;
}
document.getElementById("fix_start").onclick = function(){
    const input = document.getElementById("fix_start_input");
    const result = document.getElementById("fix_start_result");
    result.value = fixStart(input.value);
    result.innerHTML = result.value;
}
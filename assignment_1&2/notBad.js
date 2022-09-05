// notBad
function notBad(str){
    const lower = str.toLowerCase()
    let not = lower.indexOf('not');
    let bad = lower.indexOf('bad');
    if(not > bad || not==-1 || bad==-1){
        return str;
    }
    return str.substring(0,not) + "good" + str.substring(bad+3);
}
document.getElementById("notBad").onclick = function(){
    const input = document.getElementById("notBadInput");
    const result = document.getElementById("notBadAnswer");
    result.value = notBad(input.value);
    result.innerHTML = result.value;
}
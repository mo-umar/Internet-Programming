// Square Number
function squareNumber(num){
    return Math.pow(num,2);
}
document.getElementById("square").onclick = function(){
    const sq_num = document.getElementById("squareNum");
    const sum = document.getElementById("answer");
    sum.value = squareNumber(sq_num.value);
    sum.innerHTML = sum.value;
}
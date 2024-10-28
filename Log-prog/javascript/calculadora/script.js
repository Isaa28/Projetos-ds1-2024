function exibir(){
    let n1 = parseFloat(document.getElementById("n1").value);
    let n2 = parseFloat(document.getElementById("n2").value);
    let op = document.getElementById("op").value;
    let res = ""

    if(op == "soma"){
        res = n1 + n2
    } else if(op == "subtracao"){
        res = n1 - n2
    } else if(op == "multiplicacao"){
        res = n1 * n2
    } else{
        res = n1 / n2
    }

    document.getElementById("res").innerHTML = res;
}
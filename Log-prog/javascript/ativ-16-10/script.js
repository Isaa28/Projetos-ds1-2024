function imc(){
    let peso= document.getElementById("peso").value;
    let altura= document.getElementById("altura").value;
    let res= (peso/altura**2).toFixed(2)
    document.getElementById("res").innerHTML= res
    let clas = ""

    if(res < 18.5) {
        clas = 'Abaixo do peso.'
    } else if(res < 25) {
        clas = 'Peso normal'
    } else if(res < 30) {
        clas = 'Acima do peso'
    } else if(res < 35) {
        clas = 'Obesidade grau I'
    } else if(res < 41) {
        clas = 'Obesidade grau II' 
    } else {
        clas = 'Obesidade grau III'
    }

    document.getElementById("vl").innerHTML= clas
}
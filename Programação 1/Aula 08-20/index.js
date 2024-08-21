texto.textContent = 'o nome deve ter mais de 5 caracteres'
nome.onkeyup = function(){
    if (nome.value.length <= 5){
        texto.textContent = 'nome invalido'
        nome.style.backgroundColor = 'red'
    }else{
        texto.textContent = 'nome ok.' 
        nome.style.backgroundColor = 'li'
    }
}
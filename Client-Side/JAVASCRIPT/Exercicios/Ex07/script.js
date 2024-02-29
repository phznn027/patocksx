var div = document.querySelector('.box')
div.style.backgroundColor = 'green'
div.style.width = '250px'
div.style.height = '200px'
div.style.margin = '10%'
div.style.marginLeft = '40%'

div.style.color = 'white'
div.style.textAlign = 'center'
div.style.fontSize = '25px'
div.style.paddingTop = '110px'
div.style.fontFamily = 'Arial'

div.addEventListener('click', clicar)
div.addEventListener()


function clicar(){
    div.style.backgroundColor = 'red'
    div.innerHTML = 'Voce Apertou'
}

function hover() {
    div.style.backgroundColor = 'yellow'
}

function hoverout() {
    div.style.backgroundColor = 'green'
}


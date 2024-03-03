document.querySelector('.botao').addEventListener('click', cadastrarnoti)

function cadastrarnoti() {
    document.getElementsByTagName('h1')[0].style.display = 'none'
    document.getElementsByTagName('main')[0].style.width = '0px'.style.height = '0px'
    document.querySelector('#container').style.display = 'block'
}


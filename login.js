
const emailInput = document.getElementById('username');
const passwordInput = document.getElementById('password')

emailInput.addEventListener('input', ()  => validarInput(emailInput));

passwordInput.addEventListener('input',() => validarInput(passwordInput));

emailInput.addEventListener('blur', () => resetearInput(emailInput));

passwordInput.addEventListener('blur',() => resetearInput(passwordInput))
validarInput = (input) => {
    if (input.value.length > 0) {
       input.style.borderBottom = '2px solid #07c1ce';
    }
}

function resetearInput(input) {
    
        input.style.borderBottom = ''; 
        
    
}
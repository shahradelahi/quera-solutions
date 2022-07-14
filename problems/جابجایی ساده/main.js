// vars
const square = document.querySelector('#square')

let flag = 0

// funcs

// handlers
const handle_window_keydown = (e) => {
	const keyCode = e.keyCode


	if(e.shiftKey && keyCode == 39){
		square.style.left = `${parseInt(window.getComputedStyle(square).getPropertyValue('left')) + 10}px` 
		return
	} else if(e.shiftKey && keyCode == 37){
		square.style.left = `${parseInt(window.getComputedStyle(square).getPropertyValue('left')) - 10}px` 
		return
	} else if(e.shiftKey && keyCode == 38){
		square.style.top = `${parseInt(window.getComputedStyle(square).getPropertyValue('top')) - 10}px` 
		return
	} else if(e.shiftKey && keyCode == 40){
		square.style.top = `${parseInt(window.getComputedStyle(square).getPropertyValue('top')) + 10}px` 
		return
	} 



	if(flag != 0) return

	


	// if(keyCode ==)
	
	if(keyCode == 39)
		square.style.left = `${parseInt(window.getComputedStyle(square).getPropertyValue('left')) + 1}px` 

	else if (keyCode == 37)
		square.style.left = `${parseInt(window.getComputedStyle(square).getPropertyValue('left')) - 1}px` 

	else if (keyCode == 38)
		square.style.top = `${parseInt(window.getComputedStyle(square).getPropertyValue('top')) - 1}px` 
	
	else if (keyCode == 40)
		square.style.top = `${parseInt(window.getComputedStyle(square).getPropertyValue('top')) + 1}px` 



	++flag
}

const handle_window_keyup = () => {
	flag = 0
}

window.addEventListener('keydown', handle_window_keydown)
window.addEventListener('keyup', handle_window_keyup)
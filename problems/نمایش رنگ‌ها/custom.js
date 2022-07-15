console.log("runnig");

const colorInput = document.querySelector("#color_input");
const colorPreview = document.querySelector("#color_preview");

const validColor = /^#([0-9A-F]{3}){1,2}$/i.test("#ABC");

let color;

function isValidHex(color) {
    if(!color || typeof color !== 'string') return false;

    // Validate hex values
    if(color.substring(0, 1) === '#') color = color.substring(1);

    switch(color.length) {
      case 3: return /^[0-9A-F]{3}$/i.test(color);
      case 6: return /^[0-9A-F]{6}$/i.test(color);
      case 8: return /^[0-9A-F]{8}$/i.test(color);
      default: return false;
    }

    return false;
  }

const handleColorPreview = () => {
  color = colorInput.value;
  console.log(color);
  if (isValidHex(color)) {
    colorPreview.style.background = `#${color}`;
  } else {
    colorPreview.style.background = 'black';
  }
};

colorInput.addEventListener("input", handleColorPreview);

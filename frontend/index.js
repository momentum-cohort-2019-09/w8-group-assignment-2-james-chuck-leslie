import './prism.css';
import './prism.js';
import './index.scss';

const codebox = document.getElementById('codebox')

codebox.addEventListener("keydown", (e) => {
    let { keyCode } = e;
    let { value, selectionStart, selectionEnd } = codebox;

    if (keyCode === 9) {  // TAB = 9
      e.preventDefault();
      codebox.value = value.slice(0, selectionStart) + "    " + value.slice(selectionEnd);
      codebox.setSelectionRange(selectionStart+4, selectionStart+4)
    }
});
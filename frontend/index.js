import './prism.css';
import './prism.js';
import './index.scss';
import './codemirror-5.49.2/lib/codemirror.css';
import './codemirror-5.49.2/lib/codemirror.js';
import './codemirror-5.49.2/mode/clike/clike.js';
import './codemirror-5.49.2/mode/css/css.js';
import './codemirror-5.49.2/mode/javascript/javascript.js';
import './codemirror-5.49.2/mode/python/python.js';
import './codemirror-5.49.2/theme/tomorrow-night-eighties.css';
import './codemirror-5.49.2/mode/sass/sass.js';
import './codemirror-5.49.2/mode/markdown/markdown.js';

const codebox = document.getElementById('codebox');

var myCodeMirror = CodeMirror.fromTextArea(codebox, 'tomorrow-night-eighties');

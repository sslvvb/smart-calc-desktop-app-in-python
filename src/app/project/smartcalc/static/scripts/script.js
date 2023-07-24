function appendValue(value, event) {
    event.preventDefault();
    document.getElementById('expression').value += value;
}

function clearExpression(event) {
    event.preventDefault();
    document.getElementById('expression').value = '';
}

function calculateExpression(event) {
    if (document.getElementById('expression').value == '' ||
        document.getElementById('x_num').value == '') {
        event.preventDefault();
    } else {
        document.getElementById('expression').value = document.getElementById('expression').value.replace(/,/g, '.');
        const form = document.getElementById('calculator-form');
        form.action = '/';
        form.method = 'POST';
        form.submit();
    }
}

function graphExpression(event) {
    const xMin = parseFloat(document.getElementById('x_min').value);
    const xMax = parseFloat(document.getElementById('x_max').value);
    const yMin = parseFloat(document.getElementById('y_min').value);
    const yMax = parseFloat(document.getElementById('y_max').value);
    if (document.getElementById('expression').value != '' &&
        document.getElementById('x_num').value != '' &&
        document.getElementById('x_min').value != '' &&
        document.getElementById('x_max').value != '' &&
        document.getElementById('y_min').value != '' &&
        document.getElementById('y_max').value != '' &&
        xMin < xMax && yMin < yMax && xMin != xMax && yMin != yMax) {
        document.getElementById('expression').value = document.getElementById('expression').value.replace(/,/g, '.');
        const form = document.getElementById('calculator-form');
        form.action = 'graph/';
        form.method = 'POST';
        form.submit();
    } else {
        event.preventDefault();
    }
}

function selectHistory() {
    const selectElement = document.querySelector('select[name="history"]');
    const selectedOption = selectElement.options[selectElement.selectedIndex].value;
    const splitLines = selectedOption.split('=');
    document.querySelector('.expression-input').value = splitLines[0].trim();
    document.querySelector('.x-input').value = splitLines[2].trim();
}

// TODO: разные формы для этого мб ?
function submitForm(action, method) {
  const form = document.getElementById('calculator-form');
  form.action = action;
  form.method = method;
  form.submit();
}

function cleanHistorySubmit() {
  submitForm('clean_history/', 'POST');
}

function backgroundSubmit() {
  submitForm('background/', 'POST');
}

function colorSubmit() {
  submitForm('main_color/', 'POST');
}

function fontSubmit() {
  submitForm('font_size/', 'POST');
}

// TODO: для внутренних мб другой гугл стиль ?
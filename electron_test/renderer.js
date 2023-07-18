// const { ipcRenderer } = require('electron');

// const reverseButton = document.getElementById('reverseButton');
// const textInput = document.getElementById('textInput');
// const reversedText = document.getElementById('reversedText');

// reverseButton.addEventListener('click', () => {
//     console.log('addEventListener click.'); //
//     const text = textInput.value;
//     ipcRenderer.send('reverse-text', text); // используется для отправки текста на бэкэнд
// });

// // Бэкэнд выполнит реверсирование текста и отправит измененный текст обратно на фронтэнд. // где это происходит ?

// // Фронтенд прослушивает событие 'reversed-text' с помощью ipcRenderer.on и обновляет содержимое
// // элемента reversedText полученным реверсированным текстом.
// ipcRenderer.on('reversed-text', (event, reversed) => {
//     console.log('ipcRenderer on reversed-text'); //
//     reversedText.textContent = reversed;
// });

test = 'Hello'
async function makePostRequest(test) {
    axios.post('http://127.0.0.1:5000/test', test)
        .then(function (response) {
            console.log("It says: ", response.data);
        })
        .catch(function (error) {
            console.log(error);
        });
}

import './style.css';
import {sum} from './math';

const div_sum = document.querySelector('.sum');
div_sum.innerHTML = 'Test Webpack<br>';
div_sum.innerHTML += 'sum = ' + sum(10, 20);


// Получение данных с JSON сервера
const btn = document.querySelector('.btn');
const div_jsonData = document.querySelector('.jsonData');

function getJson() {
  fetch('http://localhost:3000/posts/')
    .then(response => response.json())
    .then(json => {
        div_jsonData.innerHTML = '';
        for (let item of json.values()) {
            console.log(item);
            div_jsonData.innerHTML += '<br>';
            for (let elem in item) {
                console.log(elem, '=', item[elem]);
                const newString = `<b>${elem} = ${item[elem]}</b><br>`;
                div_jsonData.innerHTML += newString;
            }
        }
    })
    .catch(() => window.alert(`Нет связи с json-server! Запустите сервер командой:\n json-server --watch database.json`));
}
btn.addEventListener('click', getJson);

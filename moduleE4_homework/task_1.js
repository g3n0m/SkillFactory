// Написать, функцию, которая принимает в качестве аргумента объект и выводит в консоль все ключи и значения только собственных свойств. Данная функция не должна возвращать значение.

const object = {'': 1, green: 2, yellow: 3, dark: 4};

const printObj = (i) => {
  for (let key in i) {
    if (i.hasOwnProperty(key)) {
        console.log(key);
    }
  }
}

printObj(obj);
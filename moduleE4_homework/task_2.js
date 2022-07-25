// Написать функцию, которая принимает в качестве аргументов строку и объект, а затем проверяет есть ли у переданного объекта свойство с данным именем. Функция должна возвращать true или false.

const object = {'': 1, green: 2, yellow: 3, dark: 4};
let string = "dark";

const string_in_object = (a, b) => {
  for (let key in a) {
    if (key == b) {
        return true;
    }
  }
  return false;
}

let result = string_in_object(object, string);
console.log(result);
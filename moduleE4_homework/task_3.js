// Написать функцию, которая создает пустой объект, но без прототипа.

function createObject () {
    return Object.create(null);
  }
  
  const object = createObject();
  console.log(object);
  console.log(Object.getPrototypeOf(object));
/*Реализовать следующее консольное приложение подобно примеру, который разбирался в видео. Реализуйте его на прототипах.
Определить иерархию электроприборов. Включить некоторые в розетку. Посчитать потребляемую мощность. 
Таких приборов должно быть, как минимум, два (например, настольная лампа и компьютер). Выбрав прибор, подумайте, какими свойствами он обладает.
План:
1. Определить родительскую функцию с методами, которые включают/выключают прибор из розетки.
2. Создать делегирующую связь [[Prototype]] для двух конкретных приборов.
3. У каждого из приборов должны быть собственные свойства и, желательно, методы, отличные от родительских методов.
4. Создать экземпляры каждого прибора.
5. Вывести в консоль и посмотреть результаты работы, гордиться собой. :)*/

function Devices(name) {
    this.voltage = 220;
    this.deviceOn = false // devices on default - OFF
  }
  Devices.prototype.deviceSwitch = function(deviceSwitch) { // device ON or OFF func
    if (deviceSwitch === 'on') {
      this.deviceOn = true;
    } else {
      this.deviceOn = false;
    }
  }
  Devices.prototype.powerConsumption = function(time) { // Counting of power consumption, transfer to kWh
    let сonsumption = this.devicePower * time * 0.01;
    console.log(`Device ${this.name} while working ${time} (hour) spent ${сonsumption} kWh`);
  }
    
  function Light(name, amperage, luminous) { // subclass, lighting
    this.name = name;
    this.luminous = luminous;
    this.amperage = amperage;
    this.devicePower = Math.round(this.voltage * amperage)
  }
  Light.prototype = new Devices() // subclass delegating relationship
  Light.prototype.getInfo = function() { // all device parameters console output
    console.log(`Lighting parametrs ${this.name}`);
    for (const key in this) {
      if (typeof this[key] !== "function") { 
        console.log(`${key}: ${this[key]}`);
      }
    }
    console.log('\n');
  }
  
  function Computers(name, amperage, size) { // subclass, computers
    this.name = name;
    this.size = size + " inch";
    this.amperage = amperage;
    this.devicePower = Math.round(this.voltage * amperage)
  }
  Computers.prototype = new Devices(); 
  Computers.prototype.getInfo = function() {
    console.log(`Computer parameters ${this.name}`);
    for (const key in this) {
      if (typeof this[key] !== "function") {
        console.log(`${key}: ${this[key]}`);
      }
    }
    console.log('\n');
  }
  
  const chandelier = new Light('Chandelier', 0.1, 500); // Name, current (A), light power (lum)
  const daskTop = new Computers('Dasktop computer', 0.6, 21); // Name, current (A), screen diagonal (inch)
  
  chandelier.getInfo(); // Lighting device parameters output 
  daskTop.getInfo(); // Dasktop device parameters output
  
  chandelier.deviceSwitch('on'); // ON or OFF this device
  chandelier.getInfo(); // Lighting device parameters output again
  
  chandelier.powerConsumption(4); // Calculate total amount of electricity consumed per N hours.
  daskTop.powerConsumption(4);
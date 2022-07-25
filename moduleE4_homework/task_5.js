/*Переписать консольное приложение из предыдущего юнита на классы.
Общие требования:
Имена классов, свойств и методов должны быть информативными;
Соблюдать best practices;
Использовать синтаксис ES6.*/

class Devices {
    constructor(name) {
      this.name = name;
      this.voltage = 220;
      this.deviceOn = false;
    }
    deviceSwitch(deviceSwitch) {
      if (deviceSwitch === 'on') {
        this.deviceOn = true;
      } else {
        this.deviceOn = false;
      }
    }
    powerConsumption(time) {
      let сonsumption = this.devicePower * time * 0.01;
      console.log(`Device ${this.name} while working ${time} (hour) spent ${сonsumption} kWh`);      
    }
  }
  
  class Light extends Devices {
    constructor(name, amperage, luminous, voltage, deviceOn) {
      super(voltage, deviceOn);
      this.name = name;
      this.luminous = luminous;
      this.amperage = amperage;
      this.devicePower = Math.round(this.voltage * amperage);
    }
    getInfo() {
      console.log(`Lighting parametrs ${this.name}`);      
      for (let key in this) {
        if (typeof this[key] !== "function") {
          console.log(`${key}: ${this[key]}`);
        }
      }
      console.log('\n');
    }
  
  }
  
  class Computers extends Devices {
    constructor(name, amperage, size, voltage, deviceOn) {
      super(voltage, deviceOn);
      this.name = name;
      this.size = size + " inch";
      this.amperage = amperage;
      this.devicePower = Math.round(this.voltage * amperage);
    }
    getInfo() {
      console.log(`Computer parameters ${this.name}`);
      for (const key in this) {
        if (typeof this[key] !== "function") {
          console.log(`${key}: ${this[key]}`);
        }
      }
      console.log('\n');
    }
  }
    
  const chandelier = new Light('Chandelier', 0.1, 500); // Name, current (A), light power (lum)
  const daskTop = new Computers('Dasktop computer', 0.6, 21); // Name, current (A), screen diagonal (inch)
  
  chandelier.getInfo(); // Lighting device parameters output 
  daskTop.getInfo(); // Dasktop device parameters output
  
  chandelier.deviceSwitch('on'); // ON or OFF this device
  chandelier.getInfo(); // Lighting device parameters output again
  
  chandelier.powerConsumption(4);  // Calculate total amount of electricity consumed per N hours.
  daskTop.powerConsumption(4);

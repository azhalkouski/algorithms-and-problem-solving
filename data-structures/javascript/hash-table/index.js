 class HashTable {
  constructor(size) {
    this.table = new Array(size);
    this.size = size;
  }

  hash(key) {
    // this implementation of a hashing function results in name collisions
    // it produces the same index for different keys
    // example: `name` and `mane` are given the same hash
    // ! which results in lose of data
    let total = 0;
    for (let i = 0; i < key.length; i++) {
      total += key.charCodeAt(i);
    }
    return total % this.size;
  }

  set(key, value) {
    const index = this.hash(key);
    this.table[index] = value;
  }

  get(key) {
    const index = this.hash(key);
    return this.table[index];
  }

  remove(key) {
    const index = this.hash(key);
    this.table[index] = undefined;
  }

  display() {
    console.log("display::start");
    for (let i = 0; i < this.size; i++) {
      if (this.table[i]) {
        console.log(i, this.table[i]);
      }
    }
    console.log("display::end");
    }
 }

 const table = new HashTable(50);

 table.set("name", "Bruce");
 table.set("age", 25);
 table.display();

 console.log(table.get("name"));

 table.remove("name");
 table.display();
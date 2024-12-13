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
    // we can still use this hashing function but we need to change the way we
    // set and get key-value pairs
    // setter and getter, and remove() with name collisions are suffixed with _DEPRECATED
    let total = 0;
    for (let i = 0; i < key.length; i++) {
      total += key.charCodeAt(i);
    }
    return total % this.size;
  }

  set_DEPRECATED(key, value) {
    const index = this.hash(key);
    this.table[index] = value;
  }

  get_DEPRECATED(key) {
    const index = this.hash(key);
    return this.table[index];
  }

  remove_DEPRECATED(key) {
    const index = this.hash(key);
    this.table[index] = undefined;
  }

  set(key, value) {
    const index = this.hash(key);
    // instead of storing a value at a distinc index in the table (array) we will
    // store an array of arrays, where every inner array is an array holding key and
    // value - [[key, value], [key, value]]
    // bucket is a reference to that outer array
    // the name `bucket` is a common naming convention
    const bucket = this.table[index];
    if (!bucket) {
      this.table[index] = [[key, value]];
    } else {
      const sameKeyItem = bucket.find(item => item[0] === key);
      if (sameKeyItem) {
        sameKeyItem[1] = value;
      } else {
        bucket.push([key, value]);
      }
    }
  }

  get(key) {
    const index = this.hash(key);
    const bucket = this.table[index];

    if (bucket) {
      const sameKeyItem = bucket.find(item => item[0] === key);
      if (sameKeyItem) {
        return sameKeyItem[1];
      }
    }

    return undefined;
  }

  remove(key) {
    const index = this.hash(key);
    const bucket = this.table[index];

    if (bucket) {
      const sameKeyItem = bucket.find(item => item[0] === key);
      if (sameKeyItem) {
        bucket.splice(bucket.indexOf(sameKeyItem), 1);
      }
    }
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

 table.set("mane", "Clark");
 table.display();

 // overwrite Bruce with Diana
 table.set("name", "Diana");
 table.display();

 table.remove("name");
 table.display();
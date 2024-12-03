class MySQLService {
  boolean saveOrder(Order order) {
    // ...
  }
}


class MongoDBService { // an update
  boolean saveOrder(Order order) {
    // ...
  }
}


class OrderService {
  MySQLService dbService;

  // we are passing MySQLService through the OrderService constructor,
  // instead of calling MySQLService constructor inside OrderService.
  // This is called INVERSION OF CONTROL (IoC), and it helps us remove
  // a strong dependency between both classes.
  public OrderService(MySQLService dbService) { // change here
    this.dbService = dbService;
  }

  void processOrder(Order order) {
    // do things to the order, then save it:
    this.dbService.saveOrder(order);
  }
}


class App {
  void newOrder() {
    OrderService service = new OrderService(new MySQLService()); // change here
    // get new order, process it and store it...
    service.processOrder(order);
  }
}
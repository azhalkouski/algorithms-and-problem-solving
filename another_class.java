interface DBService {
  boolean saveOrder(Order order);
}


class MySQLService implements DBService{
  boolean saveOrder(Order order) {
    // Do SQL stuff...
  }
}


class MongoDBService implements DBService{
  boolean saveOrder(Order order) {
    // Do Mongo stuff...
  }
}

// Remote Procedure Call (RPC)
class RemoteDBService implements DBService{
  HttpClient httpClinet;

  boolean saveOrder(Order order) {
    // create http request from order
    // ...
    HttpResponse<String> = httpClient.post(
      HttpRequest request = HttpRequest.newBuilder().uri(
        URI.create("https://pizzaplace.com/api/saveOrder"))
           .header("Content-Type", "application/json")
           .POST(orderRequest)
           .build()
      );
  }
}


class OrderService {
  DBService dbService;

  // INVERSION OF CONTROL
  // instead of new MySQLService() or new MongoDBService() here, we just
  // define what interface must be used and then passing an implementation
  // through
  public OrderService(DBService dbService) {
    this.dbService = dbService;
  }

  void processOrder(Order order) {
    // do things to the order, then save it:
    this.dbService.saveOrder(order);
  }
}


class App {
  void newOrder() {
    // Use one implementation...
    // the concrete implementation is passed to the constructor of OrderService
    // this is a pattern known as DEPENDENCY INJECTION
    OrderService service1 = new OrderService(new MySQLService());
    // or the other
    OrderService service2 = new OrderService(new MongoDBService());
    OrderService serviceRPC = new OrderService(new RemoteDBService());
    service1.processOrder(order);
    service2.processOrder(order);
    serviceRPC.processOrder(order);
  }
}
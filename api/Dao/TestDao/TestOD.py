import logging

from Model.OrderModel import NewOrderModel
from OrderDao import OrderDao


class test_order_dao:
  def main(*args):
    logging.getLogger().setLevel(args[0])
    ##### TEST OrderDAO ######
    #in console mi aspetto 5 info, il primo ritorna il dizionario contenente tutti i record della tabella, il secondo contiene il dizionario con il record con ID=1, il terzo è il record da inserire in tabella, il quarto è il record che vado ad aggiornare e il quinto mi ritorna la conferma del DELETE del record con ID=2
    total = 0
    counter = 0

    try:
      total += 1
      OrderDao.getAllOrders()
      counter += 1
    except(RuntimeError, TypeError, NameError)  as e:
      logging.error("OrderDao getAllOrders not passed")
      logging.exception(e)

    try:
      total += 1
      commessaCreate = NewOrderModel(description="txt", id_customer="123e4567-e89b-12d3-a456-426614174000", id_business="124e4567-e85b-1fd3-a456-426614474000", startDate= "2022-07-19", endDate= "2022-08-19")
      uuidOrder = OrderDao.createOrder(commessaCreate)
      logging.debug("OrderDao createOrder:" + str(uuidOrder))
      counter += 1
    except(RuntimeError, TypeError, NameError) as e:
      logging.error("OrderDao createOrder not passed")
      logging.exception(e)

    try:
      total += 1
      order = OrderDao.getOrderByID(str(uuidOrder))
      counter += 1
    except(RuntimeError, TypeError, NameError)  as e:
      logging.error("OrderDao getOrderByID not passed")
      logging.exception(e)
      
      
    # GETORDERBYEMPLOYEE
    try:
        total += 1
        OrderDao.getOrderByEmplyee('e55917e1-0e9f-40b2-92ae-c880328aa110')
        counter += 1
    except(RuntimeError, TypeError, NameError) as e:
        logging.error("EmployeeDao getEmployeesByAccount not passed")
        logging.exception(e)

    try:
      total += 1
      order.description = "modificato"
      OrderDao.updateOrderById(order)
      counter += 1
    except(RuntimeError, TypeError, NameError)  as e:
      logging.error("OrderDao updateOrderById not passed")
      logging.exception(e)

    try:
      total += 1
      OrderDao.deleteOrderByID(str(uuidOrder))
      counter += 1
    except(RuntimeError, TypeError, NameError)  as e:
      logging.error("OrderDao deleteOrderByID not passed")
      logging.exception(e)

    logging.warning("Test OrderDao, completati con successo %d / %d", counter, total)
    return dict(totals = total, counters = counter)
 
 
if __name__ == "__main__":
   test_order_dao.main()

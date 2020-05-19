class ShoppingCar:
    def __init__(self, user):
        self._user = user
        self._shoppingCar = list()
        self._offProduct = list()
    def addProduct(self, name, price, num):
        product = dict()
        product["name"] = name
        product["price"] = price
        product["num"] = num
        self._shoppingCar.append(product)
    
    def removeProduct(self, name, price, num):
        for index, product in enumerate(self._shoppingCar):
            if product["name"] == name and product["price"] == price:
                product["num"] -= num
                if product["num"] == 0:
                    del self._shoppingCar[index]
                return
    
    def getUser(self):
        return self._user
    
    def getProduct(self):
        name_list = list()
        for product in self._shoppingCar:
            name_list.append(product["name"])
        return name_list
    
    def getCost(self):
        total = 0
        for product in self._shoppingCar:
            total += self._calculateOff(product["name"], product["price"], product["num"], 0, False)
        return total
    
    def getOff(self):
        return self._offProduct
    
    def _calculateOff(self, name, price, num, total, isOff):
        if num >= 2:
            isOff = True
            total += price + round(price * 0.8)
            return self._calculateOff(name, price, num - 2, total, isOff) 
        elif num == 1:
            total += price
            return self._calculateOff(name, price, num - 1, total, isOff) 
        else:
            if isOff:
                self._offProduct.append(name)
            return total

obj = ShoppingCar("mushding")
obj.addProduct("巧克力", 50, 1)
obj.addProduct("咖啡豆", 120, 5)
obj.addProduct("咖啡豆", 120, 1)
obj.addProduct("草莓果醬", 70, 5)
#obj.removeProduct("咖啡豆", 120, 2)
print(obj._shoppingCar)
print(obj.getUser(), "的購物車裡面有", obj.getProduct(), "總共", obj.getCost(), "元 其中", obj.getOff(), "享有第二件八件的優惠")